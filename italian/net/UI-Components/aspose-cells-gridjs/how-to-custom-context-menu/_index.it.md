---
title: Menu contestuali personalizzati per GridJs  
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/how-to-custom-context-menu/
description: Questo articolo descrive come configurare i menu contestuali per GridJs.
keywords: GridJs, elementi di menu personalizzati, menu contestuale, personalizzato, contesto, menu
aliases:
  - /net/aspose-cells-gridjs/custommenu/
  - /net/aspose-cells-gridjs/how-to-custom-context-menus/
  - /net/aspose-cells-gridjs/work-with-context-menu/
  - /net/aspose-cells-gridjs/work-with-context-menus/
---

# Menu contestuali personalizzati
Abbiamo alcuni elementi di menu contestuali predefiniti, ad esempio inserisci/elimina riga/colonna e così via
Tuttavia, se l'utente vuole elementi di menu contestuali personalizzati.
Supportiamo impostare gli elementi di menu contestuale nelle opzioni di caricamento.
ad esempio:
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

Supportiamo le seguenti API JS per gli elementi di menu contestuali personalizzati in fase di esecuzione


-  ottenere elementi di menu contestuali personalizzati
```javascript
xs.sheet.getCustomContextMenuItems()
```

-  aggiungere elementi di menu contestuali personalizzati
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

-  eliminare elementi di menu contestuali personalizzati
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

-  inserire elemento di menu contestuale personalizzato in posizione specificata
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

-  aggiornare elemento di menu contestuale personalizzato dalla chiave
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


-  ottenere elementi di menu contestuali personalizzati per immagine/forma
```javascript
xs.sheet.getImageContextMenuItems()
```

-  aggiungere elementi di menu contestuali personalizzati per immagine/forma
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

-  eliminare elementi di menu contestuali personalizzati per immagine/forma
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Puoi trovare altro sulla nostra pagina demo di github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



