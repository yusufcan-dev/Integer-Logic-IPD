import axelrod as axl
from axelrod.action import Action

C, D = Action.C, Action.D

# Kognitif 3.0'ı Axelrod standartlarında bir bota dönüştürüyoruz
class Kognitif3(axl.Player):
    name = "Kognitif 3.0"

    def __init__(self):
        super().__init__()
        # 4 durum için hafıza defteri. C = Paylaş, D = İhanet
        self.hafiza = {
            (C, C): {'hamle': C, 'aktif': False, 'puan': 0, 'tur': 0},
            (C, D): {'hamle': D, 'aktif': False, 'puan': 0, 'tur': 0},
            (D, C): {'hamle': D, 'aktif': False, 'puan': 0, 'tur': 0},
            (D, D): {'hamle': C, 'aktif': False, 'puan': 0, 'tur': 0},
        }

    def strategy(self, opponent: axl.Player) -> Action:
        # İlk tur körüz, barışçıl (C) başlarız
        if len(self.history) == 0:
            return C
        
        # Önceki turun verilerini çek
        bizim_son = self.history[-1]
        rakip_son = opponent.history[-1]
        
        # Puanlama sistemi
        puan = 0
        if bizim_son == C and rakip_son == C: puan = 3
        elif bizim_son == C and rakip_son == D: puan = 0
        elif bizim_son == D and rakip_son == C: puan = 5
        elif bizim_son == D and rakip_son == D: puan = 1

        # Arka plandaki tüm aktif sayaçları güncelle (Kelebek Etkisi)
        for durum in self.hafiza:
            if self.hafiza[durum]['aktif']:
                self.hafiza[durum]['puan'] += puan
                self.hafiza[durum]['tur'] += 1

        # İçinde bulunduğumuz durumu tespit et ve yargı anını başlat
        mevcut_durum = (bizim_son, rakip_son)
        kayit = self.hafiza[mevcut_durum]

        if kayit['aktif']:
            toplam = kayit['puan']
            gecen = kayit['tur']
            
            # Bölmesiz O(1) Eşik Optimizasyonumuz
            if (toplam * 2) < (gecen * 5):
                # Strateji zarar ettirdi, tersine çevir!
                kayit['hamle'] = D if kayit['hamle'] == C else C
            
            # Döngü bitti, sayacı sıfırla
            kayit['puan'] = 0
            kayit['tur'] = 0
        else:
            # Döngü ilk defa başlıyor
            kayit['aktif'] = True
            kayit['puan'] = 0
            kayit['tur'] = 0

        return kayit['hamle']

# ==========================================
# ARENA KURULUMU VE TURNUVA
# ==========================================

oyuncular = [
    Kognitif3(),
    
    # 1. BARIŞÇIL VE İYİ NİYETLİLER (Koyunlar ve Koruyucular)
    axl.Cooperator(),             # Saf Enayi
    axl.TitForTat(),              # Klasik Ayna
    axl.TitFor2Tats(),            # Sabırlı Ayna (2 hatada vurur)
    axl.Appeaser(),               # Yatıştırıcı
    axl.Forgiver(),               # Affedici (Zamanla kinini unutur)
    axl.FirmButFair(),            # Sert ama Adil (Sadece haksızlığa vurur)
    axl.WinStayLoseShift(),       # Pavlov (Kazanıyorsa sistemi bozmaz)
    axl.TwoTitsForTat(),          # Agresif Ayna
    
    # 2. KİNDAR VE İNTİKAMCILAR (Adalet Sağlayıcılar)
    axl.Grudger(),                # Saf Kindar (Tek hatada çizer)
    axl.SoftGrudger(),            # Yumuşak Kindar (Cezalandırıp zeytin dalı uzatır)
    axl.FoolMeOnce(),             # Akıllı Kindar (İkinci hatada çizer)
    axl.ForgetfulGrudger(),       # Unutkan Kindar
    axl.OppositeGrudger(),        # Ters Kindar
    
    # 3. SÖMÜRÜCÜ VE SİNSİLER (Kurtlar ve Parazitler)
    axl.Defector(),               # Acımasız
    axl.Bully(),                  # Zorba
    axl.SuspiciousTitForTat(),    # Kötü Niyetli Ayna (İhanetle başlar)
    axl.SneakyTitForTat(),        # Sinsi Ayna (Fırsat buldukça ihanet dener)
    axl.BackStabber(),            # Sırtından Bıçaklayan
    axl.DoubleCrosser(),          # İkili Oynayan
    axl.WorseAndWorse(),          # Çürüyen Bot (Sürekli daha çok ihanet eder)
    axl.AntiTitForTat(),          # Ters Ayna (Tam bir parazit)
    
    # 4. ANALİTİK VE KEŞİFCİLER (Mühendisler ve Kaos)
    axl.Adaptive(),               # Adaptif (Sürekli kâr hesabı yapar)
    axl.Calculator(),             # Hesap Makinesi
    axl.GoByMajority(),           # Çoğunlukçu
    axl.HardGoByMajority(),       # Katı Çoğunlukçu
    axl.Prober(),                 # Keşifçi (Rakibi analiz eder)
    axl.Prober2(),                # Keşifçi 2
    axl.Prober3(),                # Keşifçi 3
    axl.HardProber(),             # Katı Keşifçi
    axl.Alternator(),             # Sarkaç (Düzenli gürültü)
    axl.CyclerCCD(),              # P-P-İ Ritimcisi
    axl.CyclerDDC(),              # İ-İ-P Ritimcisi
    axl.Random()                  # Tam Kaos
]

print("Turnuva basliyor... 1000 tur, amansiz mucadele.")
turnuva = axl.Tournament(players=oyuncular, turns=1000, repetitions=1)
sonuclar = turnuva.play()

# Detaylı ve puanlı skorbordu yazdır
print("\n--- DETAYLI SKORBORD (Puan Farklariyla) ---")
for sira, index in enumerate(sonuclar.ranking):
    isim = oyuncular[index].name
    # repetitions=1 olduğu için [0] ile turnuva toplamını çekiyoruz
    toplam_puan = sonuclar.scores[index][0]
    
    # Konsolda hizalı ve şık durması için biçimlendirme yapıyoruz
    print(f"{sira + 1:02d}. {isim:<25} | Puan: {toplam_puan}")