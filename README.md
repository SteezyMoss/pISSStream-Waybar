# Waybar Plugin: pISSStream Waybar

A custom plugin for [Waybar](https://github.com/AlexanderThaller/waybar), the highly customizable status bar for Wayland. 

This plugin provides a "constant stream" to the state of the urine tank on the International Space Station. All these other platforms have it, why not Waybar! (I was bored and curious) 

This is a super simple plugin that connects to the lightstreamer client and returns a value. If you wanted, you could change the subscription item value to any of the other Symbols on https://demos.lightstreamer.com/ISSLive/

## Prerequisites

- [Waybar](https://github.com/AlexanderThaller/waybar) installed
- The current icon is unicode from Noto Emoji but could be anything you like

## Installation

The easiest way to install would be to clone the repo, and then simply move the executable within the dist/ folder to your preferred directory for exectuables. Then follow the steps in the configuration section. The rest of the files can be deleted, only the executable is required. 

## Configuration

Add the following snippet to your Waybar config.jsonc file. You will also need to add `custom/pISSStream` to modules-left, modules-center, or modules-right at the top of the config. Consult the waybar docs if you need more information on adding modules/plugins.

```jsonc
"custom/pISSStream": {
    "exec": "/path/to/your/executable/directory", 
    "interval": 5,
    "return-type": "json",
    "format": "🚽{text}", 
    "tooltip": true
  },
```

**Config options:**
- `interval`: How often you would like Waybar to call for a refresh. Set to 5 seconds per default. 
- `format`: This is where you can change the icon, just don't remove `{text}`
- `tooltip`: If you don't want anything to appear when you mouse over, remove this.

## CSS Configuration

Add the following snippet to your Waybar style.css file.

```CSS
#custom-pISSStream {
  color: #ffffff;
  padding: 0 5px;
}
```

## Usage

Once configured, reload Waybar to see your plugin in action!

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an [issue](https://github.com/SteezyMoss/pISSStream-Waybar/issues) or submit a pull request.

## License

MIT License

## Acknowledgements

- [Waybar](https://github.com/AlexanderThaller/waybar) for providing a powerful platform for customization
- [Lightstreamer Client Library](https://github.com/Lightstreamer/Lightstreamer-lib-client-haxe)  for making this very accessible
- Those who come before me that provided inspiration for this little project; [Jaennaet](https://github.com/Jaennaet/pISSStream), [LeLocTai](https://github.com/LeLocTai/pISSStreamUnity), and [Stovoy](https://github.com/Stovoy/pISSStreamGodot).
- Pyinstaller!


