---
title: как настраивать меню и панель инструментов в GridJs  
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-customize-menus/
description: Эта статья описывает, как настраивать меню и панели инструментов в GridJs.
keywords: GridJs,настройка меню,меню,настройка
aliases:
  - /net/aspose-cells-gridjs/customize-menus/
  - /net/aspose-cells-gridjs/customize-ui/
  - /net/aspose-cells-gridjs/customize-toolbar/

---

## о настройке меню и кнопок на панели инструментов
Мы не предоставляем полезных API напрямую.
Однако мы можем написать некоторые js-функции на основе структуры DOM для достижения этой цели.



## настройка менюбаров 
например: чтобы оставить только меню `Файл`, предполагая, что id div GridJs — "gridjs-divid"
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
После вызова этой функции 

![todo:экран для настройки панели меню](gridjs_customize_menubar.png)


## настройка пунктов меню панели 
например: чтобы оставить только пункт "Скачать как XLSX" в меню "Файл", предполагая, что id div GridJs — "gridjs-divid"
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
После вызова этой функции 

![todo:экран для настройки пункта меню](gridjs_customize_menu.png)

## настройка элементов панели инструментов 
например: оставить только кнопку зума, предполагая, что id div GridJs — "gridjs-divid"
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
После вызова этой функции 

![todo:экран для настройки панели инструментов](gridjs_customize_toolbar.png)





