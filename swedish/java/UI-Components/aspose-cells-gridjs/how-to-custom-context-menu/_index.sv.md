---
title: Anpassade kontextmenyer för GridJs  
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-custom-context-menu/
description: Denna artikel beskriver hur du konfigurerar kontextmenyer för GridJs.
keywords: GridJs, anpassade menyobjekt, kontextmeny, anpassad, kontext, meny
aliases:
  - /java/aspose-cells-gridjs/custommenu/
  - /java/aspose-cells-gridjs/how-to-custom-context-menus/
  - /java/aspose-cells-gridjs/work-with-context-menu/
  - /java/aspose-cells-gridjs/work-with-context-menus/
---
# Anpassade inbyggda menyval
Vi har några inbyggda menyalternativ, till exempel infoga/ta bort rad/kolumn och så vidare.
Till exempel: att ta bort "Ta bort rad", "Länk", "Dölj"-menyalternativ i kontextmenyer, anta att div-id för GridJs är "gridjs-divid"
```javascript
   //get context menus parent dom
   const menus=document.querySelector("#gridjs-divid > div > div.x-spreadsheet-sheet > div.x-spreadsheet-contextmenu");
   var childs = menus.childNodes;
   for (var i = childs.length - 1; i >= 0; i--)
   {  
     // check the item text
     if(childs[i].childNodes[0]?.textContent==="Delete row"||childs[i].childNodes[0]?.textContent==="Link"||childs[i].childNodes[0]?.textContent==="Hide")
       {
         menus.removeChild(childs[i]);
       }
   }
```
Efter att ha anropat denna funktion 

![todo: skärm för att anpassa inbyggda menyalternativ](gridjs_customize_build_in_context_menu.png)


# Anpassade egendefinierade kontextmenyer
Vi har några inbyggda menyalternativ, till exempel infoga/ta bort rad/kolumn och så vidare.
Om användaren vill anpassa menyobjekt
Vi stöder att ställa in menyobjekt i laddningsalternativ.
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

Vi stöder följande JS API för anpassade menyobjekt vid körning


-  få anpassade menyobjekt
```javascript
xs.sheet.getCustomContextMenuItems()
```

-  lägg till anpassade menyobjekt
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

-  ta bort anpassade menyobjekt
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

-  infoga anpassad menyobjekt på specificerad position
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

-  uppdatera anpassat menyobjektet med nyckeln
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


-  få anpassade menyobjekt för bild/form
```javascript
xs.sheet.getImageContextMenuItems()
```

-  lägg till anpassade menyobjekt för bild/form
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

-  ta bort anpassade menyobjekt för bild/form
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Du kan hitta mer på vår github demosida https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



