---
title: How to Customize Menus and Toolbars in GridJs  
type: docs
weight: 250
url: /java/aspose-cells-gridjs/how-to-customize-menus/
description: This article describes how to customize menus and toolbars in GridJs.
keywords: GridJs, customize menus, menus, customize
aliases:
  - /java/aspose-cells-gridjs/customize-menus/
  - /java/aspose-cells-gridjs/customize-ui/
  - /java/aspose-cells-gridjs/customize-toolbar/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## About Customize Menus and Toolbar Buttons
We don't provide useful APIs directly.  
However, we can write some JavaScript functions based on the DOM structure to achieve it.

## Customize Menubar
For example, to keep the File menu only, assume the div id of GridJs is `"gridjs-divid"`:

```javascript
// get menubar parent DOM
const menubar = document.querySelector("#gridjs-divid > div > div:nth-child(1) > div > div.x-spreadsheet-banner-info-s > div.x-spreadsheet-toolbar.x-spreadsheet-menubar");
var childs = menubar.childNodes;

for (var i = childs.length - 1; i >= 0; i--) {
  // keep File menu only
  if (childs[i].childNodes[0].childNodes[0].textContent !== "File") {
    menubar.removeChild(childs[i]);
  }
}
```

After calling this function  

![todo:the screen for customize menubar](gridjs_customize_menubar.png)

## Customize Items in Menubar
For example, to keep the **"Download As XLSX"** menu item in the File menu only, assume the div id of GridJs is `"gridjs-divid"`:

```javascript
// get menubar parent DOM
const menubar = document.querySelector("#gridjs-divid > div > div:nth-child(1) > div > div.x-spreadsheet-banner-info-s > div.x-spreadsheet-toolbar.x-spreadsheet-menubar");
var childs = menubar.childNodes;

// keep the first one → File menu only
for (var i = childs.length - 1; i >= 0; i--) {
  // find the File menu
  if (childs[i].childNodes[0].childNodes[0].textContent === "File") {
    var dropdownparent = childs[i].childNodes[0].childNodes[1];
    var menuitems = dropdownparent.childNodes;
    for (var ii = menuitems.length - 1; ii >= 0; ii--) {
      // remove other menu items that are not "Download As XLSX"
      if (menuitems[ii].textContent !== "Download As XLSX") {
        dropdownparent.removeChild(menuitems[ii]);
      }
    }
  }
}
```

After calling this function  

![todo:the screen for customize menubar item](gridjs_customize_menu.png)

## Customize Toolbar Items
For example, to keep the Zoom button only, assume the div id of GridJs is `"gridjs-divid"`:

```javascript
// get toolbar parent DOM
const toolbar = document.querySelector("#gridjs-divid > div > div.x-spreadsheet-toolbar > div.x-spreadsheet-toolbar-btns");
var childs = toolbar.childNodes;

for (var i = childs.length - 1; i >= 0; i--) {
  // keep Zoom button only
  if (childs[i].getAttribute("data-tooltip") !== "Zoom") {
    toolbar.removeChild(childs[i]);
  }
}
```

After calling this function  

![todo:the screen for customize toolbar](gridjs_customize_toolbar.png)

## Customize Toolbar Hover Effect

Open the browser inspection window and select the toolbar button,

![todo:the screen for select inspect toolbar button](gridjs_hover_toolbar_button_inspect.png)

Then we can find that the related CSS key for this button is: `freeze`

![todo:the screen for find CSS key for toolbar button](gridjs_hover_toolbar_button_csskey.png)

Add the following CSS rule:

```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```

The result will be:

![todo:the screen for hover effect for toolbar button](gridjs_hover_toolbar_button_hover.png)

## Customize Items in Bottom Bar

### Overview
The bottom bar contains two interactive buttons:
1. **Add Worksheet Button** (`add` class) – creates new worksheets  
2. **Select Worksheet Button** (`ellipsis` class) – manages worksheet selection

### DOM Access
You can access these elements using:

```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
```

### Customization Examples

#### 1. Hide Buttons
To remove a button from the DOM:

```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);
```

#### 2. Change Icons
You can replace icons using either external SVG files or inline SVG data:

```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

#### 3. Change Button Behavior
You can modify the click event to customize functionality:

```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```
