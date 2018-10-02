# Create Border GIMP Plugin

Python GIMP plugin which creates border for selected layer.

## Getting Started

Install this plugin, open GIMP project and select layer with image. Open in main menu Filters->Decor->Create border...
Choose parameters and push Ok button.

![Screenshot](https://github.com/4ster/gimp-create-border-plugin/blob/master/docs/screenshot.png)

### Examples

![Automation](https://github.com/4ster/gimp-create-border-plugin/blob/master/docs/automation.png)

![Mario](https://github.com/4ster/gimp-create-border-plugin/blob/master/docs/mario.png)

### Prerequisites

This plugin tested with GIMP 2.10

### Installing

Copy create_border.py to GIMP plugins folder and restart GIMP. Make script executable if you use *nix-based system:
```
sudo chmod +x ~/.config/GIMP/2.10/plug-ins/create_border.py
```

You may bind shortcut for this action: main menu Edit->Keyboard Shortcuts. Search Create border plugin, click on cell and push your shortcut keys.

![Shortcut](https://github.com/4ster/gimp-create-border-plugin/blob/master/docs/shortcut.png)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details