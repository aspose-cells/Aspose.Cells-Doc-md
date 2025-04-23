---
title: 如何在 GridJs 中自定义菜单和工具栏  
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/how-to-customize-menus/
description: 本文介绍了如何在 GridJs 中自定义菜单和工具栏。
keywords: GridJs，自定义菜单，菜单，自定义
aliases:
  - /python-net/aspose-cells-gridjs/customize-menus/
  - /python-net/aspose-cells-gridjs/customize-ui/
  - /python-net/aspose-cells-gridjs/customize-toolbar/

---

## 关于自定义菜单和工具栏按钮
我们没有直接提供有用的 API。
但是我们可以根据 DOM 结构编写一些 JS 函数来实现它。



## 自定义菜单栏 
例如：只保留文件菜单，假设GridJs的div ID为"gridjs-divid"
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
调用此函数后 

![待办：自定义菜单栏界面](gridjs_customize_menubar.png)


## 自定义菜单栏项目 
例如：只保留“另存为XLSX”菜单项，假设GridJs的div ID为"gridjs-divid"
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
调用此函数后 

![待办：自定义菜单栏项目界面](gridjs_customize_menu.png)

## 自定义工具栏项目 
例如：只保留缩放按钮，假设GridJs的div ID为"gridjs-divid"
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
调用此函数后 

![待办：自定义工具栏界面](gridjs_customize_toolbar.png)





