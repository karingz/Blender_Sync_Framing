# Blender Sync Framing Toggle Addon

A Blender addon that synchronizes viewport framing with the Outliner's locate feature, making it easier to navigate and focus on objects in your scene.

## Description

The **Sync Framing Toggle** addon enhances Blender's workflow by automatically synchronizing the viewport framing with the Outliner's locate function. When enabled, pressing the frame key will not only frame the selected object in the 3D viewport but also locate and highlight it in the Outliner simultaneously.

## Features

- **Sync Framing Toggle**: Enable or disable synchronization between viewport framing and Outliner locate
- **Smart Frame Operator**: Intelligently frames objects based on the sync setting
- **UI Integration**: Adds a toggle option directly in the Outliner filter menu
- **Keyboard Shortcut**: Remaps the numpad period (`.`) key to use the smart framing feature
- **Multi-window Support**: Works across all open Blender windows and layouts
- **Persistent Settings**: Sync framing preference is saved per scene

## Installation

1. Download the `sync_locate_addon.py` file
2. Open Blender
3. Go to `Edit` > `Preferences` > `Add-ons`
4. Click `Install...` button
5. Navigate to and select the `sync_locate_addon.py` file
6. Enable the addon by checking the checkbox next to "Interface: Sync Framing Toggle"

## Usage

### Toggle Sync Framing

1. Open the Outliner panel
2. Click on the filter icon (funnel) in the Outliner header
3. At the bottom of the filter menu, you'll find the "Sync Framing" checkbox
4. Check or uncheck to enable/disable the sync framing feature

### Frame Selected Object

- **With Sync Enabled**: Press `Numpad Period (.)` to frame the selected object in both the 3D viewport and locate it in the Outliner
- **With Sync Disabled**: Press `Numpad Period (.)` to frame the selected object only in the 3D viewport (standard Blender behavior)

## Requirements

- **Blender Version**: 4.5.0 or higher
- **Category**: Interface

## How It Works

The addon provides two main operators:

1. **Sync Locate** (`view3d.sync_locate`): Frames the active object in all 3D viewports and locates it in all Outliner panels across all windows
2. **Smart Frame** (`view3d.smart_frame`): Checks if sync framing is enabled and calls either the sync locate operator or the standard view selected operator

The addon automatically initializes the sync framing setting to `True` for all scenes when a file is loaded.

## Technical Details

- **Operator ID**: `view3d.sync_locate`, `view3d.smart_frame`
- **Property**: `Scene.sync_framing_enabled` (Boolean)
- **Keymap**: Numpad Period in 3D View space
- **UI Hook**: Appended to `OUTLINER_PT_filter` panel

## Author

**Jerome Kim**

## Version
1.0.0

