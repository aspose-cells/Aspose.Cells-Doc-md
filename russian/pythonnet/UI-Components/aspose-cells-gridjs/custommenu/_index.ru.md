---
title: Пользовательские контекстные меню для GridJs  
type: docs
weight: 250
url: /ru/python-net/aspose-cells-gridjs/custommenu/
description: В этой статье описано, как настроить контекстные меню для GridJs.
keywords: GridJs, пользовательские пункты меню, контекстное меню, пользовательские, контекст, меню
aliases:
  - /python-net/aspose-cells-gridjs/how-to-custom-context-menu/
  - /python-net/aspose-cells-gridjs/how-to-custom-context-menus/
  - /python-net/aspose-cells-gridjs/work-with-context-menu/
  - /python-net/aspose-cells-gridjs/work-with-context-menus/
---
# Настраиваемое встроенное контекстное меню
У нас есть некоторые встроенные пункты контекстного меню, например вставка/удаление строки/столбца и так далее.
например: чтобы удалить пункты меню "Удалить строку", "Ссылка", "Скрыть" в контекстных меню, предположим, что id div GridJs — "gridjs-divid"
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
После вызова этой функции 

![todo:страница настройки встроенного меню](gridjs_customize_build_in_context_menu.png)


# Самостоятельное определение контекстных меню
У нас есть некоторые встроенные пункты контекстного меню, например вставка/удаление строки/столбца и так далее.
Однако, если пользователю нужно настраивать элементы контекстного меню.
Мы поддерживаем установку элементов контекстного меню в параметрах загрузки.
например:
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

Мы поддерживаем следующие API JavaScript для пользовательских элементов контекстного меню во время выполнения


-  получить пользовательские элементы контекстного меню
```javascript
xs.sheet.getCustomContextMenuItems()
```

-  добавить пользовательские элементы контекстного меню
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

-  удалить пользовательские элементы контекстного меню
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

-  вставить пользовательский элемент контекстного меню на указанную позицию
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

-  обновить пользовательский элемент контекстного меню по ключу
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


-  получить пользовательские элементы контекстного меню для изображения/формы
```javascript
xs.sheet.getImageContextMenuItems()
```

-  добавить пользовательские элементы контекстного меню для изображения/формы
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

-  удалить пользовательские элементы контекстного меню для изображения/формы
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

Вы можете найти больше информации на нашей демонстрационной странице в GitHub https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net/wwwroot/xspread/index.html



