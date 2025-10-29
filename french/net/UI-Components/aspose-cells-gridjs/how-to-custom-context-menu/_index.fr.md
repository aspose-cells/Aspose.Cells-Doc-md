---
title: Menus contextuels personnalisés pour GridJs  
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/how-to-custom-context-menu/
description: Cet article décrit comment configurer des menus contextuels pour GridJs.
keywords: GridJs, éléments de menu personnalisés, menu contextuel, personnalisé, contexte, menu
aliases:
  - /net/aspose-cells-gridjs/custommenu/
  - /net/aspose-cells-gridjs/how-to-custom-context-menus/
  - /net/aspose-cells-gridjs/work-with-context-menu/
  - /net/aspose-cells-gridjs/work-with-context-menus/
---
# Menus contextuels intégrés personnalisés
Nous avons quelques éléments de menu contextuel intégrés, par exemple insérer/supprimer une ligne/colonne, etc.
par exemple : pour supprimer les items de menu "Supprimer la ligne", "Lien", "Cacher" dans les menus contextuels, supposez que l'ID div de GridJs est "gridjs-divid"
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
Après avoir appelé cette fonction 

![todo: l'écran pour personnaliser les items de menu intégrés](gridjs_customize_build_in_context_menu.png)


# Menus contextuels auto-définis personnalisés
Nous avons quelques éléments de menu contextuel intégrés, par exemple insérer/supprimer une ligne/colonne, etc.
Cependant, si l'utilisateur souhaite personnaliser les éléments de menu contextuel.
Nous prenons en charge la définition des éléments de menu contextuel dans les options de chargement.
par exemple :
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

Nous prenons en charge les API JS ci-dessous pour les éléments de menu contextuel personnalisés en temps d'exécution


- obtenir des éléments de menu contextuel personnalisés
```javascript
xs.sheet.getCustomContextMenuItems()
```

- ajouter des éléments de menu contextuel personnalisés
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- supprimer des éléments de menu contextuel personnalisés
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- insérer un élément de menu contextuel personnalisé à une position spécifiée
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- mettre à jour un élément de menu contextuel personnalisé par la clé
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- obtenir des éléments de menu contextuel personnalisés pour une image/forme
```javascript
xs.sheet.getImageContextMenuItems()
```

- ajouter des éléments de menu contextuel personnalisés pour une image/forme
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- supprimer des éléments de menu contextuel personnalisés pour une image/forme
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Vous pouvez en trouver plus sur notre page de démo github https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



