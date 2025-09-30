# Waybar Plugin: pISSStream Waybar

A custom plugin for [Waybar](https://github.com/AlexanderThaller/waybar), the highly customizable status bar for Wayland. 

This plugin provides a "constant stream" to the state of the urine tank on the International Space Station. All these other platforms have it, why not Waybar! (I was bored and curious) 

## Installation

### Prerequisites

- [Waybar](https://github.com/AlexanderThaller/waybar) installed
- The current icon is unicode from Noto Emoji but could be anything you like

### Easiest Installation

1. Download the 



## Configuration

Add the following section to your `~/.config/waybar/config` under the `custom` module:

```jsonc
"custom/your-plugin": {
    "exec": "~/.config/waybar/plugins/your-plugin.py",
    "interval": 60,
    "return-type": "json"
}
```

**Config options:**
- `interval`: [Description of what this controls]
- [Other config options]

### Example Configuration

```jsonc
"custom/your-plugin": {
    "exec": "~/.config/waybar/plugins/your-plugin.py",
    "interval": 30,
    "format": "{}"
}
```

## Usage

Once configured, reload Waybar to see your plugin in action:

```bash
killall waybar && waybar
```

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an [issue](https://github.com/yourusername/your-plugin/issues) or submit a pull request.

## License

[MIT](LICENSE)  
Copyright (c) [year] [yourusername]

## Acknowledgements

- [Waybar](https://github.com/AlexanderThaller/waybar) for providing a powerful platform for customization
- [Any other libraries, resources, or contributors]

---

*This is a template README. Please update with your plugin’s actual details, installation steps, and configuration options!*
