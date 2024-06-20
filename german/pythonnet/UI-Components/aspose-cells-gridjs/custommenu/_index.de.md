---
title: Benutzerdefinierte Kontextmenüs für GridJs  
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/custommenu/
description: Dieser Artikel beschreibt, wie Sie Kontextmenüs für GridJs konfigurieren können.
keywords: gridjs, menü, benutzerdefiniertes Menü, Kontextmenü
---

# Benutzerdefinierte Kontextmenüs
Wir haben einige integrierte Kontextmenüelemente, zum Beispiel Zeile/Spalte einfügen/löschen und so weiter
Wenn der Benutzer jedoch benutzerdefinierte Kontextmenüelemente wünscht.
Wir unterstützen das Festlegen von Kontextmenüelementen in den Ladenoptionen.
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


- Abrufen benutzerdefinierter Kontextmenüelemente
```javascript
xs.sheet.getCustomContextMenuItems()
```

- Hinzufügen benutzerdefinierter Kontextmenüelemente
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- Löschen benutzerdefinierter Kontextmenüelemente
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- Benutzerdefiniertes Kontextmenüelement an angegebener Position einfügen
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- Aktualisieren benutzerdefiniertes Kontextmenüelement anhand des Schlüssels
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- Abrufen benutzerdefinierter Kontextmenüelemente für Bild/Form
```javascript
xs.sheet.getImageContextMenuItems()
```

- Hinzufügen benutzerdefinierter Kontextmenüelemente für Bild/Form
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- Löschen benutzerdefinierter Kontextmenüelemente für Bild/Form
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Weitere Informationen finden Sie auf unserer Github-Demo-Seite https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net/wwwroot/xspread/index.html



