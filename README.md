# Trivia Flash Card Game

Welcome to `Trivia Flash`, a terminal-based trivia game where you can test your knowledge in various categories and difficulty levels!

## Overview

This project is a Python-based trivia game that allows users to play with a deck of trivia cards fetched from an external API. Players can choose their preferred category and difficulty level before starting the game.

The original project concept is from the Turing School of Software & Design's Mod 1 'Flash Card' project (originally designed for Ruby), and while I utilized the interaction pattern for the first two iterations, I deviated greatly once I reached iteration 3, by implementing a third party API to generate dynamic and varied questions for players.

## Features

- Choose from multiple categories such as music, history, science, and geography.
- Select difficulty levels: easy, medium, or hard.
- Answer trivia questions and receive feedback on correctness.
- Track your performance with percentage correctness and category-wise scores.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/trivia-flash.git
   ```

2. Install the required dependencies:

   ```bash
   pip install requests  # If not already installed
   ```

3. Run the game:

   ```bash
   python main.py
   ```

4. Follow the on-screen instructions to play the game!

## Game Flow

1. Start the game by choosing to play (`y`) or exit (`n`).
2. Set your preferred category and difficulty level or leave them blank.
3. Answer trivia questions displayed one by one.
4. Receive feedback on your answers and track your performance.
5. Continue playing until you complete the deck of cards.

## Project Structure
```
- main.py         # Contains the main logic and user interaction flow.
- lib/             # Directory containing the game classes
    - card.py 
    - deck.py 
    - round.py
    - turn.py
- tests/           # Directory containing the PyTest game class test and class method tests 
    - card_test.py
    - deck_test.py
    - round_test.py
    - turn_test.py
- README.md       # This file providing information about the project.
- .gitignore      # Ignores the pycache from running the test cases.
```
## Technologies Used

- Python
- PyTest
- Requests library for API communication

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

## Credits

- Trivia API: [https://the-trivia-api.com](https://the-trivia-api.com)
- Turing Mod 1 FlashCards Project: [https://backend.turing.edu/module1/projects/flashcards/index](https://backend.turing.edu/module1/projects/flashcards/index)

## Contact

If you have any questions or feedback, feel free to reach out to me:

- Email: ethan.vangorkom@gmail.com
- LinkedIn: https://www.linkedin.com/in/evangorkom/
- GitHub: https://github.com/EVanGorkom

Thank you for visiting my repository!