---
title: GridJs的自定义右键菜单  
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/custommenu/
description: 本文描述了如何配置GridJs的右键菜单。
keywords: gridjs,menu,custom menu,右键菜单
---

# GridJs的自定义右键菜单
我们有一些内置的右键菜单项，例如插入/删除行/列等等。
但是如果用户想要自定义右键菜单项。
我们支持在加载选项中设置右键菜单项。
例如：
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

我们支持以下JS API来在运行时定制右键菜单项


- 获取自定义右键菜单项
```javascript
xs.sheet.getCustomContextMenuItems()
```

- 添加自定义右键菜单项
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- 删除自定义右键菜单项
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- 在指定位置插入自定义右键菜单项
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- 按键更新自定义右键菜单项
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- 获取图像/形状的自定义右键菜单项
```javascript
xs.sheet.getImageContextMenuItems()
```

- 添加图像/形状的自定义右键菜单项
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- 删除图像/形状的自定义右键菜单项
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

您可以在我们的github演示页面https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net/wwwroot/xspread/index.html上找到更多信息



