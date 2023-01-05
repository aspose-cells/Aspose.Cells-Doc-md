---
title:  Anpassade sammanhangsmenyer för GridJs
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/custommenu/
description: Den här artikeln beskriver hur du konfigurerar snabbmenyer för GridJs.
keywords: custom menu items, context menu
---
# Anpassade sammanhangsmenyer
Vi har några inbyggda kontextmenyalternativ, till exempel infoga/ta bort rad/kolumn och så vidare
Men om användaren vill anpassa kontextmenyalternativ.
Vi stöder inställning av snabbmenyalternativ i laddningsalternativ.
till exempel:
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

Vi stöder nedanstående JS API:er för anpassade kontextmenyobjekt vid körning


- få anpassade snabbmenyalternativ
```javascript
xs.sheet.getCustomContextMenuItems()
```

- lägg till anpassade kontextmenyobjekt
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- ta bort anpassade snabbmenyalternativ
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- infoga ett anpassat snabbmenyalternativ på angiven position
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- uppdatera anpassad snabbmenypost med tangenten
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- få anpassade kontextmenyalternativ för bild/form
```javascript
xs.sheet.getImageContextMenuItems()
```

- lägg till anpassade kontextmenyalternativ för bild/form
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- ta bort anpassade kontextmenyalternativ för bild/form
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Du kan hitta mer på vår github-demosida https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html


 
