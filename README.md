# Waybar Plugin: pISSStream Waybar

A custom plugin for [Waybar](https://github.com/AlexanderThaller/waybar), the highly customizable status bar for Wayland. 

This plugin provides a "constant stream" to the state of the urine tank on the International Space Station. All these other platforms have it, why not Waybar! (I was bored and curious) 

This is a super simple plugin that connects to the lightstreamer client and returns a value. If you wanted, you could change the subscription item value to any of the other Symbols on https://demos.lightstreamer.com/ISSLive/

## Prerequisites

- [Waybar](https://github.com/AlexanderThaller/waybar) installed
- The current icon is unicode from Noto Emoji but could be anything you like

<<<<<<< HEAD
## Installation

The easiest way to install would be to clone the repo, and then simply move the executable within the dist/ folder to your preferred directory for exectuables. Then follow the steps in the configuration section.
=======
### Manual Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SteezyMoss/pISSStream-Waybar.git
   ```

 
2. **[If compilation is needed] Build the plugin:**
   ```bash
   make
   ```

3. **Copy or symlink the plugin to your Waybar scripts/plugins directory:**
   ```bash
   cp your-plugin.py ~/.config/waybar/plugins/
   # Or
   ln -s /path/to/your-plugin.py ~/.config/waybar/plugins/
   ```
>>>>>>> ce4f54c (readme and requirements update)

## Configuration

Add the following section to your Waybar config.jsonc file. You will also need to add `custom/pISSStream` to modules-left, modules-center, or modules-right at the top of the config. Consult the waybar docs if you need more information on adding modules/plugins.

```jsonc
"custom/your-plugin": {
    "exec": "~/.config/waybar/plugins/your-plugin.py",
    "interval": 60,
    "return-type": "json"
}
```

**Config options:**
- `interval`: How often you would like Waybar to call for a refresh. Set to 5 seconds per default. 
- [Other config options]

## CSS Configuration

```css
"custom/your-plugin": {
    "exec": "~/.config/waybar/plugins/your-plugin.py",
    "interval": 30,
    "format": "{}"
}
```

## Usage

Once configured, reload Waybar to see your plugin in action!

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

