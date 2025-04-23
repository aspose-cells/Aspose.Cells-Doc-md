---
title: كيفية تخصيص القوائم وأشرطة الأدوات في GridJs  
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/how-to-customize-menus/
description: يصف هذا المقال كيفية تخصيص القوائم وأشرطة الأدوات في GridJs.
keywords: GridJs،تخصيص القوائم،القوائم،تخصيص
aliases:
  - /net/aspose-cells-gridjs/customize-menus/
  - /net/aspose-cells-gridjs/customize-ui/
  - /net/aspose-cells-gridjs/customize-toolbar/

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





