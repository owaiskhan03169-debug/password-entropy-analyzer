# Password Entropy Analyzer

A simple tool to evaluate password strength using entropy calculation.
It provides an estimated crack time and basic feedback through both a web interface and a Python CLI.

---

## Features

* Calculates password entropy based on length and character set
* Estimates brute-force crack time (assumed ~100 billion guesses/sec)
* Detects use of:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Symbols
* Web version with terminal-style UI
* Python CLI version

---

## How It Works

Entropy is calculated as:

Entropy = Length × log₂(Character Pool Size)

Higher entropy generally means a stronger password.

---

## Project Structure

index.html
Password-Strength.py
README.md

---

## Usage

### Web

Open `index.html` in a browser and enter a password.

### Python

Run:

python Password-Strength.py

---

## Notes

* Crack time is an estimate and not exact
* This project is for learning purposes

---

## Author

Owais Khan
