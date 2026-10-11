```markdown
# Kognitif 3.0: Computationally-Optimized Strategy for the Iterated Prisoner's Dilemma

Kognitif 3.0 is a game theory algorithm developed for Iterated Prisoner's Dilemma (IPD) tournaments.

Unlike traditional rule-based and complex-memory bots (e.g., Tit-for-Tat, Grim Trigger), this project makes autonomous decisions by measuring profitability in the system through a "pure mathematical threshold that does not strain the processor." It proved its evolutionary stability (ESS) by securing **1st place** in 1000-round tests conducted within a massive ecosystem containing over 35 AI, Markov chain, and chaos bots in the Axelrod library.

## Core Algorithm and Computational Efficiency

The greatest strength of Kognitif 3.0 is that its decision-making mechanism relies on a highly lightweight and efficient mathematical model, completely stripped of complex calculations.

In game theory state analysis, it is typically necessary to divide the total score by the number of rounds played (Average Score) to compare it against a threshold `(Total Score / Turns >= 2.5)`. However, in software architecture, division operations and the use of floating-point numbers are computationally more expensive for the system compared to simple integer operations.

Kognitif 3.0 overcomes this problem by transforming the logic into a pure integer multiplication equation:

```python
# Kognitif 3.0 O(1) Comparator Logic
if (total_score * 2) >= (turns * 5):
    # Strategy yields above a 2.5 average, maintain the current move (C or D).
else:
    # Strategy caused a loss, autonomously REVERSE the move!

```

Thanks to this simple `O(1)` **Comparator** logic, the bot does not bloat memory while reading the system, keeps CPU cycles to an absolute minimum, and instantly tolerates noise (parasitic defections) in the game.

## The Butterfly Effect and "Cyclic" Q-Learning

The bot independently tracks the 4 fundamental states in the game (`C-C`, `C-D`, `D-C`, `D-D`) as 4 separate "Ledgers".

1. **Cycle Initiation:** When the bot encounters a state (e.g., C-C), it makes its move and activates the counter for that specific state.
2. **Cumulative Observation:** Even if different states intervene as the game continues, earned points and elapsed turns continue to be added to the active counter's ledger. This measures the long-term *Butterfly Effect* created by the move.
3. **The Judgment:** When the game returns to the exact same state (`C-C`), the cycle closes. The bot runs the formula. If the system is profitable, it does nothing; if unprofitable, it reverses the move (C becomes D, D becomes C), resets the cycle, and starts a new test.

## 35-Bot Axelrod Arena Performance

Kognitif 3.0 was tested in a balanced ecosystem of 35 distinct algorithms, including literature heavyweights like "Fool Me Once", "Soft Grudger", "Random", "Prober", and "Tit For Tat".

**Tournament Parameters:**

* **Game:** Iterated Prisoner's Dilemma (T=5, R=3, P=1, S=0)
* **Rounds:** 1000 Rounds (per matchup)
* **Opponents:** 35 different algorithms
* **Environment:** Axelrod Python Library

**Test Results (Top 5):**

| Rank | Bot Name | Total Score | Strategy Class |
| --- | --- | --- | --- |
| **1.** | **Kognitif 3.0** | **97,503** | **Mathematical / Autonomous** |
| 2. | Fool Me Once | 94,962 | Rule-Based / Limited Forgiver |
| 3. | Soft Grudger | 91,615 | Sequence-Based / Punisher |
| 4. | Grudger | 91,008 | Pure Punisher |
| 5. | BackStabber | 90,866 | Sneaky / Exploiter |

*(Secured 1st place with a ~2,500 point lead over its closest rival and a ~6,000 point lead over 3rd place, proving true evolutionary stability.)*

## How to Run

To test the project, the [Axelrod library](https://github.com/Axelrod-Python/Axelrod) must be installed.

```bash
pip install axelrod

```

Run your Python file to observe Kognitif 3.0's performance in the arena and the simulation results live.

```bash
python oyun_teorisi.py

```

## Developer's Note

Instead of imitating psychological patterns or complex IF/ELSE blocks, this algorithm was developed to solve game theory purely on the level of rationality and computational efficiency. "Don't trust feelings, only trust the score in the ledger."

```

```
