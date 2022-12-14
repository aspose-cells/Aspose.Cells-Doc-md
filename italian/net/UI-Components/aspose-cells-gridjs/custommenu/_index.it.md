---
title:  Menu contestuali personalizzati per GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/custommenu/
description: Questo articolo descrive come configurare i menu contestuali per GridJs.
keywords: custom menu items, context menu
---
# Menu contestuali personalizzati
Abbiamo alcune voci di menu contestuali integrate, ad esempio inserisci/elimina riga/colonna e così via
Tuttavia, se l'utente desidera personalizzare le voci del menu contestuale.
Supportiamo le voci del menu contestuale impostate nelle opzioni di caricamento.
per esempio:
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

Supportiamo le seguenti API JS per voci di menu contestuali personalizzate in fase di esecuzione


- ottieni voci di menu contestuali personalizzate
```javascript
xs.sheet.getCustomContextMenuItems()
```

- aggiungere voci di menu contestuali personalizzate
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- eliminare le voci del menu contestuale personalizzato
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- inserire una voce di menu contestuale personalizzata nella posizione specificata
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- aggiorna la voce del menu contestuale personalizzato con la chiave
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- ottieni voci di menu contestuali personalizzate per immagine/forma
```javascript
xs.sheet.getImageContextMenuItems()
```

- aggiungere voci di menu contestuali personalizzate per immagine/forma
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- eliminare le voci del menu di scelta rapida personalizzate per immagine/forma
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Puoi trovare di più nella nostra pagina demo github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html


 
