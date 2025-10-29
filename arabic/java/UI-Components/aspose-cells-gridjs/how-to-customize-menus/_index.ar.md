---
title: كيفية تخصيص القوائم وأشرطة الأدوات في GridJs  
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-customize-menus/
description: يصف هذا المقال كيفية تخصيص القوائم وأشرطة الأدوات في GridJs.
keywords: GridJs،تخصيص القوائم،القوائم،تخصيص
aliases:
  - /java/aspose-cells-gridjs/customize-menus/
  - /java/aspose-cells-gridjs/customize-ui/
  - /java/aspose-cells-gridjs/customize-toolbar/

---

## حول تخصيص القوائم وأزرار شريط الأدوات
نحن لا نوفر واجهات برمجة تطبيقات مفيدة مباشرة.
ولكن يمكننا كتابة بعض وظائف جافا سكريبت استنادًا إلى بنية DOM لتحقيق ذلك.



## تخصيص شريط القوائم 
على سبيل المثال: للحفاظ على قائمة الملفات فقط، افترض أن معرف div لـ GridJs هو "gridjs-divid"
```javascript
   //get menubar parent dom
   const menubar=document.querySelector("#gridjs-divid > div > div:nth-child(1) > div > div.x-spreadsheet-banner-info-s > div.x-spreadsheet-toolbar.x-spreadsheet-menubar");
   var childs = menubar.childNodes;


   for (var i = childs.length - 1; i >= 0; i--)
   {  
     // keep File menu  only
     if(childs[i].childNodes[0].childNodes[0].textContent!=="File")
       {
         menubar.removeChild(childs[i]);
       }
   }


```
بعد استدعاء هذه الدالة 

![مهم: الشاشة لتخصيص شريط القوائم](gridjs_customize_menubar.png)


## تخصيص عناصر في شريط القوائم 
على سبيل المثال: للحفاظ على عنصر قائمة "تحميل كملف XLSX" في قائمة الملف فقط، افترض أن معرف div لـ GridJs هو "gridjs-divid"
```javascript
   //get menubar parent dom
   const menubar=document.querySelector("#gridjs-divid > div > div:nth-child(1) > div > div.x-spreadsheet-banner-info-s > div.x-spreadsheet-toolbar.x-spreadsheet-menubar");
   var childs = menubar.childNodes;

   // keep the first one ->File menu  only
   for (var i = childs.length - 1; i >= 0; i--)
   {  //find the File menu
     if(childs[i].childNodes[0].childNodes[0].textContent==="File")
       {
            var dropdownparent = childs[i].childNodes[0].childNodes[1];
            var menuitems = dropdownparent.childNodes;
            for (var ii = menuitems.length - 1; ii >=0; ii--)
            {   
	        //remove other menu item that is not "Download As XLSX"
                if (menuitems[ii].textContent !== 'Download As XLSX')
                {
                    dropdownparent.removeChild(menuitems[ii]);
                }
            }
       }
   }


```
بعد استدعاء هذه الدالة 

![مهم: الشاشة لتخصيص عنصر شريط القوائم](gridjs_customize_menu.png)

## تخصيص عناصر شريط الأدوات 
على سبيل المثال: للحفاظ على زر التكبير فقط، افترض أن معرف div لـ GridJs هو "gridjs-divid"
```javascript
   //get toolbar parent dom
   const toolbar=document.querySelector("#gridjs-divid > div > div.x-spreadsheet-toolbar > div.x-spreadsheet-toolbar-btns");
   var childs = toolbar.childNodes;


   for (var i = childs.length - 1; i >= 0; i--)
   {  
     // keep File menu  only
     if(childs[i].getAttribute("data-tooltip")!=="Zoom")
       {
         toolbar.removeChild(childs[i]);
       }
   }


```
بعد استدعاء هذه الدالة 

![مهم: الشاشة لتخصيص شريط الأدوات](gridjs_customize_toolbar.png)


## تخصيص تأثير المرور على شريط الأدوات

افتح نافذة فحص المتصفح، اختر زر شريط الأدوات،

![صورة: شاشة اختيار زر الفحص في الشريط](gridjs_hover_toolbar_button_inspect.png)

ثم يمكننا العثور على المفتاح المرتبط بـ CSS لهذا الزر وهو: تجميد

![todo: الشاشة للعثور على مفتاح CSS ​​لزر شريط الأدوات](gridjs_hover_toolbar_button_csskey.png)

أضف قاعدة CSS التالية:
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
النتيجة ستكون:

![todo: الشاشة لتأثير التحويم على زر شريط الأدوات](gridjs_hover_toolbar_button_hover.png)


## تخصيص العناصر في شريط الأسفل

### نظرة عامة
يحتوي شريط الأسفل على زرَّين تفاعليين:
1. &zwnj;**زر إضافة ورقة عمل**&zwnj; (`add` class) - ينشئ أوراق عمل جديدة
2. &zwnj;**زر اختيار ورقة العمل**&zwnj; (`ellipsis` class) - يدير اختيار ورقة العمل

### الوصول إلى DOM
يمكنك الوصول إلى هذه العناصر باستخدام:
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### أمثلة على التخصيص
1. إخفاء الأزرار
لإزالة زر من DOM:
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. تغيير الأيقونات
يمكنك استبدال الأيقونات إما باستخدام ملفات SVG خارجية أو بيانات SVG مدمجة.
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. تغيير سلوك الزر
يمكنك تعديل حدث النقر لتخصيص الوظيفة:
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```





