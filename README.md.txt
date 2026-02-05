# Twitch Mobile Web Automation

## Overview
This project contains an automated UI test framework built with Python, Pytest, and Selenium.
The tests run using the Google Chrome mobile emulator to validate core user journeys on Twitch.

## Tech Stack
- Python
- Pytest
- Selenium
- Chrome Mobile Emulator

## Test Scenario
1. Open Twitch
2. Tap the search icon
3. Search for "StarCraft II"
4. Scroll down twice
5. Select a streamer

## How to Run
```bash
pip install -r requirements.txt
pytest
