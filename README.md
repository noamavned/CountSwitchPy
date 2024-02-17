# CountSwitchPy

## Overview
This Python script is designed to control LED and fan devices based on keypress events using the `keyboard` library.

The system toggles the LED and fan states in response to a specific keypress sequence.

## Dependencies
- [keyboard](https://github.com/boppreh/keyboard): A Python library to detect and process keyboard events.

## Usage
1. Install the required library using the following command:
   ```pip install keyboard```
2. Run the script: app.py
3. Use the key "1" to trigger the control sequence.

## Configuration
- `delay`: Adjust this variable to set the delay time for the control sequence.
- `led`: Represents the state of the LED (1 for ON, 0 for OFF).
- `fan`: Represents the state of the fan (1 for ON, 0 for OFF).

## Control Sequence
1. Press and release "1" to toggle the LED state.
2. Press and release "1" again within the specified delay to toggle the fan state.
3. The script uses a sequence of keypresses to control both LED and fan states.

## Author
[Noam Avned](https://github.com/noamavned)

## License
This project is licensed under the [GNU General Public License (GPL) Version 2](LICENSE).
