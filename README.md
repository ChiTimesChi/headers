# headers

Generate perfect code headers every time.

## Setup

```sh
$ pip install -r requirements.txt
```

## Usage

```sh
$ python3 headers.py this is quite a pretty good looking box
```

```solidity
    /*▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜*\
    ▏*▌               THIS IS QUITE A PRETTY GOOD LOOKING BOX                ▐*▕
    \*▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟*/
```

It will also copy the header to your clipboard automatically.

### With VSCode

- Set your global `tasks.json` like so to add the command as task.
  > Change `~/VSCodeProjects/headers/headers.py` to the actual path to the script.

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Generate Header",
      "type": "shell",
      "command": "python3 ~/VSCodeProjects/headers/headers.py ${input:header}",
      "presentation": {
        "reveal": "never"
      }
    }
  ],
  "inputs": [
    {
      "id": "header",
      "description": "Header",
      "type": "promptString"
    }
  ]
}
```

- To really speed-up your workflow, you can even add a keybind for the task in `keybindings.json`:
  > Feel free to use `"cmd+<...>"`, if you happen to own one of these fancy Mac computers.

```json
[
  {
    "key": "ctrl+alt+h",
    "command": "workbench.action.tasks.runTask",
    "args": "Generate Header"
  }
]
```

## Credits

Inspired (just a bit more than straight up copypasta fork) by transmissions11's [`headers`](https://github.com/transmissions11/headers),
which was in turn inspired by virtualjpeg's [`blocky`](https://github.com/virtualjpeg/blocky).
