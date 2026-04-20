---
title: How to show and hide menubar
description: Show or hide the GridJs menubar at startup with the toolbar display settings, and use the built-in menubar toggle button while the spreadsheet is running.
keywords: menubar, showToolbar, showPartToolbar, showFileName, menu-display-hide, menu-display-show, Banner, Menubar
type: docs
weight: 1
url: /python-net/aspose-cells-gridjs/user-guide/how-to-show-and-hide-menubar/
aliases:
- /python-net/aspose-cells-gridjs/user-guide/how-to-show-and-hide-menubar/
---

## Introduction

GridJs builds the menubar through the `Banner` component. The inspected sheet constructor creates `new Banner(data, view.width, !showToolbar, showPartToolbar, showFileName, this, local)` and also creates the toolbar with the same `!showToolbar` value. The default settings set `showToolbar` to `true`, so the menubar is shown by default.

The inspected code does not expose a separate `showMenubar` option. Initial visibility is controlled by `showToolbar` and `showPartToolbar`, and runtime visibility is controlled by the toolbar `MenuDisplay` item, whose tag is `menu-display-hide`.

## How to use

1. Show the menubar at startup by creating the spreadsheet with `showToolbar: true`, or by omitting `showToolbar` because the default value is `true`.

```js
const xs = x_spreadsheet('#gridjs-demo-uid', {
  showToolbar: true,
});
```

2. Hide the full toolbar and menubar at startup by setting `showToolbar: false` and leaving `showPartToolbar` as `false`.

```js
const xs = x_spreadsheet('#gridjs-demo-uid', {
  showToolbar: false,
  showPartToolbar: false,
});
```

3. Use a partial toolbar without the menubar by setting `showToolbar: false` and `showPartToolbar: true`.

```js
const xs = x_spreadsheet('#gridjs-demo-uid', {
  showToolbar: false,
  showPartToolbar: true,
});
```

4. Hide the file-name area while keeping the menubar path available by setting `showFileName: false`.

```js
const xs = x_spreadsheet('#gridjs-demo-uid', {
  showToolbar: true,
  showFileName: false,
});
```

5. While the full toolbar is visible, click the built-in menubar display icon. The inspected toolbar creates a `MenuDisplay` item with tag `menu-display-hide`. When this item is clicked, the sheet change handler checks the current state:

   - If the state is `up`, GridJs calls `setDown()`, hides the banner menubar with `this.menubar.hide()`, and renders the table.
   - If the state is `down`, GridJs calls `setUp()`, shows the banner menubar with `this.menubar.show()`, and renders the table.

6. The menubar includes localized top-level menu groups for file, edit, insert, text, and comment operations. These groups are built from `t("menubar.menuFile")`, `t("menubar.menuEdit")`, `t("menubar.menuInsert")`, `t("menubar.menuText")`, and `t("menubar.menuComment")`.

## JavaScript API

Configure initial menubar visibility through the spreadsheet options used by the inspected implementation.

```js
// Default visible menubar path.
const visible = x_spreadsheet('#gridjs-demo-uid', {
  showToolbar: true,
});

// Hide full toolbar and menubar at startup.
const hidden = x_spreadsheet('#gridjs-demo-uid', {
  showToolbar: false,
  showPartToolbar: false,
});

// Keep only the partial toolbar path; the Menubar component is hidden.
const partial = x_spreadsheet('#gridjs-demo-uid', {
  showToolbar: false,
  showPartToolbar: true,
});
```

The inspected code does not expose a public JavaScript method named `showMenubar`, `hideMenubar`, or `setMenubarVisible`. Runtime show and hide behavior is implemented by the internal toolbar item `MenuDisplay`, which emits the `menu-display-hide` change type.

### Relevant functions
| Function / Location | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `defaultSettings` (`core/data_proxy.js`) | Sets `showToolbar: true`, `showPartToolbar: false`, and `showFileName: true`. | None | Settings object |
| `Sheet(targetEl, data, xs)` (`component/sheet.js`) | Reads `showToolbar`, `showFileName`, and `showPartToolbar`, then creates `Banner` and `Toolbar` with `!showToolbar` as the hide flag. | `targetEl`, `data`, `xs` | `Sheet` instance |
| `Banner(data, widthFn, isHide, showPartToolbar, showFileName, sheet, local)` (`component/banner.js`) | Creates the icon bar, file-name bar, and `Menubar`. If `isHide && !showPartToolbar`, it hides the banner wrapper and marks `notShow`. If `showFileName` is false, it hides the file-name bar. | `data`, `widthFn`, `isHide`, `showPartToolbar`, `showFileName`, `sheet`, `local` | `Banner` instance |
| `Menubar(data, widthFn, isHide, showPartToolbar, local)` (`component/menubar.js`) | Builds menubar dropdown groups when `isHide` is false. If `isHide` is true, it hides the menubar element. | `data`, `widthFn`, `isHide`, `showPartToolbar`, `local` | `Menubar` instance |
| `Toolbar(data, widthFn, isHide, showPartToolbar)` (`component/toolbar/index.js`) | Creates the toolbar and always adds a `MenuDisplay` item to the toolbar element when the toolbar path is rendered. | `data`, `widthFn`, `isHide`, `showPartToolbar` | `Toolbar` instance |
| `MenuDisplay` (`component/toolbar/menuDisplay.js`) | Starts with state `up`; `setDown()` changes the icon to `menu-display-show` and state to `down`; `setUp()` changes the icon to `menu-display-hide` and state to `up`. | None | `MenuDisplay` instance |
| `toolbarChange(type, value)` branch for `menu-display-hide` (`component/sheet.js`) | Toggles the banner menubar. It hides when the menu display state is `up`, shows when the state is `down`, and calls `this.table.render()` after each change. | `type`, `value` | `void` |
| `menubarStatus()` (`index.js`) | Returns `toolbar.menuDisplay.state === 'up'` when a sheet exists, otherwise returns `true`. | None | `boolean` |
| `viewHeight()` (`core/data_proxy.js`) | Subtracts menubar height only when `showToolbar` is true and `menubarStatus()` returns true. | None | `number` |

The inspected `index.d.ts` file declares `showToolbar`, `showContextmenu`, and `showFileName`, but it does not declare `showPartToolbar`.

## Common Questions

Q: Is the menubar shown by default?
A: Yes. The inspected default settings set `showToolbar` to `true`, and the sheet passes `!showToolbar` as the menubar hide flag.

Q: Is there a separate `showMenubar` option?
A: No. No `showMenubar` option was found in the inspected source.

Q: What hides the menubar at startup?
A: Setting `showToolbar: false` passes `isHide: true` into `Banner`, `Menubar`, and `Toolbar`. With `showPartToolbar: false`, the banner wrapper and toolbar are hidden.

Q: Can users hide and show the menubar after the spreadsheet is created?
A: Yes, through the built-in toolbar display icon. The inspected code handles its `menu-display-hide` change type and toggles `this.menubar.hide()` or `this.menubar.show()`.

Q: Does `showFileName: false` hide the menubar?
A: No. The inspected `Banner` code hides the file-name bar when `showFileName` is false. Menubar visibility still follows the `showToolbar` and runtime menu display state paths.
