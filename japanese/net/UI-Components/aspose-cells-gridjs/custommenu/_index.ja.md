---
title: GridJsのカスタムコンテキストメニュー  
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/custommenu/
description: この記事では、GridJsのコンテキストメニューを構成する方法について説明します。
keywords: GridJs、カスタムメニューアイテム、コンテキストメニュー、カスタム、コンテキスト、メニュー
---

# カスタムコンテキストメニュー
ビルトインのコンテキストメニューアイテム（例：行/列の挿入/削除など）があります
ただし、ユーザーがカスタムコンテキストメニューアイテムを使用したい場合は。
ロードオプションでコンテキストメニューアイテムを設定するサポートを行っています。
たとえば：
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

ランタイムでカスタムコンテキストメニューアイテムのために以下のJS APIをサポートしています


- カスタムコンテキストメニューアイテムを取得する
```javascript
xs.sheet.getCustomContextMenuItems()
```

- カスタムコンテキストメニューアイテムを追加する
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- カスタムコンテキストメニューアイテムを削除する
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- 指定した位置にカスタムコンテキストメニューアイテムを挿入する
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- キーによってカスタムコンテキストメニューアイテムを更新する
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- 画像/図形のためのカスタムコンテキストメニューアイテムを取得する
```javascript
xs.sheet.getImageContextMenuItems()
```

- 画像/図形のためのカスタムコンテキストメニューアイテムを追加する
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- 画像/図形のためのカスタムコンテキストメニューアイテムを削除する
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

GitHubのデモページで詳細をご覧いただけます：https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



