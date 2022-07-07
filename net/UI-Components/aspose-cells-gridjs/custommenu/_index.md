---
title: Custom context menus for GridJs  
type: docs
weight: 250
url: /net/aspose-cells-gridjs/custommenu/
description: This article describes how to configure context menus for GridJs.
keywords: custom menu, context menu
---

# Custom context menus
We have some build in context menus ,for example insert/delete row/column and so on
However if user want to custom context menus.
We support set context menus in load options.
for example:
```javascript
        const onMyActionClick1 = (sheet) => {
            console.log('my action clicked1' +  sheet.data.name)
        };
        const onMyActionClick2 = (sheet) => {
            console.log('my action clicked2' + sheet.data.name)
        };
  xs = x_spreadsheet('#gridjs-demo', {
                updateMode: 'server',
                updateUrl: '/GridJs2/UpdateCell',
                showToolbar: true,
                mode: 'edit',
                local: 'en',
                showContextmenu: true,
		//this option is for context menus,we need to set usedefault to false to load custom context menus
                contextMenuItems: {
                    usedefault: false,
                    customItems: [{ 'key': 'key1', 'text': 'c title 11111', 'callback': onMyActionClick1 },
                                  { 'key': 'key2', 'text': 'c title 22222', 'callback': onMyActionClick2 }]
                }
            })
```

We support the below JS APIs for custom context menus at runtime


-  get custom context menus
```javascript
xs.sheet.getCutomContextMenuItems()
```

-  add custom context menus
```javascript
xs.sheet.addCutomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

-  delete custom context menus
```javascript
 xs.sheet.delCutomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```
 
