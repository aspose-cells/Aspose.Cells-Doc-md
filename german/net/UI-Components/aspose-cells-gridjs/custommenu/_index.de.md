---
title:  Benutzerdefinierte Kontextmenüs für GridJs
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/custommenu/
description: Dieser Artikel beschreibt, wie Sie Kontextmenüs für GridJs konfigurieren.
keywords: custom menu items, context menu
---
# Benutzerdefinierte Kontextmenüs
Wir haben einige eingebaute Kontextmenüelemente, zum Beispiel Zeile/Spalte einfügen/löschen und so weiter
Wenn der Benutzer jedoch Kontextmenüelemente anpassen möchte.
Wir unterstützen das Festlegen von Kontextmenüelementen in Ladeoptionen.
zum Beispiel:
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

Wir unterstützen die folgenden JS-APIs für benutzerdefinierte Kontextmenüelemente zur Laufzeit


- Holen Sie sich benutzerdefinierte Kontextmenüelemente
```javascript
xs.sheet.getCustomContextMenuItems()
```

- Fügen Sie benutzerdefinierte Kontextmenüelemente hinzu
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- benutzerdefinierte Kontextmenüelemente löschen
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- benutzerdefiniertes Kontextmenüelement an angegebener Position einfügen
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- Aktualisieren Sie das benutzerdefinierte Kontextmenüelement mit der Taste
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- Holen Sie sich benutzerdefinierte Kontextmenüelemente für Bild/Form
```javascript
xs.sheet.getImageContextMenuItems()
```

- Fügen Sie benutzerdefinierte Kontextmenüelemente für Bild/Form hinzu
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- benutzerdefinierte Kontextmenüelemente für Bild/Form löschen
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Weitere Informationen finden Sie auf unserer Github-Demoseite https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html


 
