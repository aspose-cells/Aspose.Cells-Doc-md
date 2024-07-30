---
title: Menús contextuales personalizados para GridJs  
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-custom-context-menu/
description: Este artículo describe cómo configurar menús contextuales para GridJs.
keywords: GridJs, elementos de menú personalizados, menú contextual, personalizado, contexto, menú
aliases:
  - /java/aspose-cells-gridjs/custommenu/
  - /java/aspose-cells-gridjs/how-to-custom-context-menus/
  - /java/aspose-cells-gridjs/work-with-context-menu/
  - /java/aspose-cells-gridjs/work-with-context-menus/
---

# Menús contextuales personalizados
Tenemos algunos elementos de menú contextuales integrados, por ejemplo, insertar/eliminar fila/columna, etc.
Sin embargo, si el usuario desea personalizar elementos del menú contextual.
Soportamos configurar elementos del menú contextual en las opciones de carga.
por ejemplo:
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

Soportamos las siguientes APIs de JS para elementos del menú contextual personalizados en tiempo de ejecución


- obtener elementos del menú contextual personalizados
```javascript
xs.sheet.getCustomContextMenuItems()
```

- agregar elementos del menú contextual personalizados
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- eliminar elementos del menú contextual personalizados
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- insertar elemento personalizado en el menú contextual en la posición especificada
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- actualizar elemento personalizado en el menú contextual por la clave
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- obtener elementos personalizados del menú contextual para imagen/forma
```javascript
xs.sheet.getImageContextMenuItems()
```

- agregar elementos personalizados del menú contextual para imagen/forma
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- eliminar elementos personalizados del menú contextual para imagen/forma
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Puede encontrar más en nuestra página de demostración en GitHub https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



