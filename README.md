# Rock, Paper, Scissors!

#### Video Demo: https://youtu.be/E9BBdk1hzco?si=Lg7yr2kCiQUo9WuX

## Description
This is an interactive game: Rock, Paper, Scissors! It provides 2 types of modes- tournament and endless. The user competes with the computer and the score is displayed at the end.

## Project Structure
- project.py : Contains the main logic of the program
- test_project.py : Contains the unit tests of the functions
- requirements.txt : Contains the libraries which need to be installed
- README.md : Contains the overview of the program

## Libraries
- **RANDOM** : The random library in Python is used for generating random numbers and for performing random selections. It's part of Python's standard library, so no installation is needed—just import it with import random.
- **ART** : The art library in Python is used to create ASCII art and text-based art.
- **EMOJI** : The emoji library in Python allows you to use and display emojis in your code.
- **TERMCOLOR** : The termcolor library in Python is used to add colored text output to command-line applications.
- **PYTEST** : The pytest library is a popular testing framework for Python that simplifies writing and running tests, especially useful for unit and functional testing.

These can be installed by running the following command in the terminal:

`pip install -r requirements.txt`

## Usage

![command to run program](<1.png>)

![welcome](<2.png>)

### **<ins>Tournament mode:**

![tournament mode](<3.png>)

### **<ins>Endless mode:**

![endless mode](<4.png>)

## Functioning

**Rules:**

- Rock vs Paper → Rock Wins
- Paper vs Scissors → Scissors Wins
- Scissors vs Rock → Rock Wins

The program consists of 5 functions in total:

**def main():** The function asks the user to choose between 2 modes - tournament and endless.

**Tournament mode:**

The program shows the manual, according to which:
- `1` = Rock
- `2` = Paper
- `3` = Scissors

It then asks for the number of rounds that the user would like to play. The user and computer scores are stored in pscore and cscore respectively. At the end of the specificed rounds, the program discloses the winner, and in case of a draw, it outputs that, along with a thank you message.

**Endless mode:**

The program shows the manual, according to which:
- `1` = Rock
- `2` = Paper
- `3` = Scissors
- `4` = End Game

The game begins and every time the program displays who won - the player or the computer, or if it's a draw.

The program uses ascii art and colors, making the game visually attractive.

**def player_tournament_input(playert):** The function checks if the player input for tournament mode is an integer or not and if it's between 1 and 3, inclusive.

**def player_endless_input(playere):** The function checks if the player input for endless mode is an integer or not and if it's between 1 and 4, inclusive.

**def rounds_input(rounds):** The function checks if the player input for the number of rounds is a positive integer or not.

**def computer_input(comp):** The functions checks if the computer input is an integer between 1 and 3, inclusive, or not.

## TO-DO
Install the necessary libraries as listed above.


> [!CAUTION]
> Enter the specified numbers only as per the requirements.

## Author
Anvi Singh Parihar


