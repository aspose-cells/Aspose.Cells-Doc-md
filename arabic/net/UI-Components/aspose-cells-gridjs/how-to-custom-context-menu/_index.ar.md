---
title: قوائم سياق مخصصة لـ GridJs  
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/how-to-custom-context-menu/
description: يوضح هذا المقال كيفية تكوين قوائم السياق لـ GridJs.
keywords: GridJs, عناصر القائمة المخصصة، قائمة السياق، مخصص، سياق، قائمة
aliases:
  - /net/aspose-cells-gridjs/custommenu/
  - /net/aspose-cells-gridjs/how-to-custom-context-menus/
  - /net/aspose-cells-gridjs/work-with-context-menu/
  - /net/aspose-cells-gridjs/work-with-context-menus/
---
# قوائم السياق المخصصة المدمجة
لدينا بعض عناصر قائمة السياق المدمجة، على سبيل المثال إدراج/حذف صف/عمود وهكذا.
على سبيل المثال: لحذف عناصر قوائم السياق "حذف الصف"، "الرابط"، "إخفاء"، افترض أن معرف div الخاص بـ GridJs هو "gridjs-divid"
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
بعد استدعاء هذه الدالة 

![قيد التنفيذ: شاشة تخصيص عناصر القائمة المدمجة](gridjs_customize_build_in_context_menu.png)


# قوائم السياق المخصصة ذاتياً
لدينا بعض عناصر قائمة السياق المدمجة، على سبيل المثال إدراج/حذف صف/عمود وهكذا.
ومع ذلك إذا أراد المستخدم تخصيص عناصر قائمة السياق.
ندعم تعيين عناصر قائمة السياق في خيارات التحميل.
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

نحن ندعم واجهات برمجة تطبيقات JavaScript (JS APIs) التالية لبنود قائمة السياق المخصصة خلال التشغيل


- الحصول على بنود قائمة السياق المخصصة
```javascript
xs.sheet.getCustomContextMenuItems()
```

- إضافة بنود قائمة السياق المخصصة
```javascript
xs.sheet.addCustomContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}},{'key':'key3','text':'menu3','callback':(x)=>{console.log('hello3333');}}]
```

- حذف بنود قائمة السياق المخصصة
```javascript
 xs.sheet.delCustomContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

- إدراج بند قائمة سياق مخصص في الموضع المحدد
```javascript
xs.sheet.insertCustomContextMenuItem(item,postion)
 // the parameter is:
 item: the custom menu item,the callback function x parameter will be the js variable of xs.sheet
 for example: {'key':'key4','text':'menu4','callback':(x)=>{console.log('hello4444');}} 
 postion:the postion for the inserted item in the items array
```

- تحديث بند قائمة السياق المخصص بواسطة المفتاح
```javascript
xs.sheet.updateCustomContextMenuItem(key,item)
 // the parameter is:
 item: the updated properties that with text or callback
 for example: {'text':'menu updated'}
 key:the key of the menu item
```


- الحصول على بنود قائمة السياق المخصصة للصورة/الشكل
```javascript
xs.sheet.getImageContextMenuItems()
```

- إضافة بنود قائمة السياق المخصصة للصورة/الشكل
```javascript
xs.sheet.addImageContextMenuItems(itemsarray)
 // the parameter is:
 itemsarray: the array of custom menu items,the callback function x parameter will be the js variable of xs.sheet
 for example: [{'key':'key4','text':'img operation1','callback':(x)=>{console.log('operation1 on image');}},{'key':'key3','text':'img operation2','callback':(x)=>{console.log('operation2 on image');}}]
```

- حذف بنود قائمة السياق المخصصة للصورة/الشكل
```javascript
 xs.sheet.delImageContextMenuItems(keysarray)()
 // the parameter is:
 keysarray: the array of the keys of the menu items
 for example: ['key4','key3']
```

يمكنك العثور على المزيد في صفحة العرض التوضيحي على github https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html



