---
title:  قوائم السياق المخصصة لـ GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/custommenu/
description: توضح هذه المقالة كيفية تكوين قوائم السياق لـ GridJs.
keywords: custom menu items, context menu
---
# قوائم السياق المخصصة
لدينا بعض عناصر قائمة السياق ، على سبيل المثال إدراج / حذف صف / عمود وما إلى ذلك
ومع ذلك ، إذا كان المستخدم يريد تخصيص عناصر قائمة السياق.
نحن ندعم عناصر قائمة السياق المحددة في خيارات التحميل.
على سبيل المثال:
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

نحن ندعم JS APIs أدناه لعناصر قائمة السياق المخصصة في وقت التشغيل


- الحصول على عناصر قائمة السياق المخصصة
```javascript
xs.sheet.getCustomContextMenuItems()
```

- إضافة عناصر قائمة السياق المخصصة
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- حذف عناصر قائمة السياق المخصصة
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- إدراج عنصر قائمة سياق مخصص في موضع محدد
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- تحديث عنصر قائمة السياق المخصص بواسطة المفتاح
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- الحصول على عناصر قائمة السياق المخصصة للصورة / الشكل
```javascript
xs.sheet.getImageContextMenuItems()
```

- إضافة عناصر قائمة السياق المخصصة للصورة / الشكل
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- حذف عناصر قائمة السياق المخصصة للصورة / الشكل
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

يمكنك العثور على المزيد في صفحة العرض التوضيحي الخاصة بنا على github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html


 
