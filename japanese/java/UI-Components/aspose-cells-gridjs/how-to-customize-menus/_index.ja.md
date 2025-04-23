---
title: GridJsでのメニューとツールバーのカスタマイズ方法  
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/how-to-customize-menus/
description: この記事では、GridJsにおけるメニューとツールバーのカスタマイズ方法について説明します。
keywords: GridJs、メニューのカスタマイズ、メニュー、カスタマイズ
aliases:
  - /java/aspose-cells-gridjs/customize-menus/
  - /java/aspose-cells-gridjs/customize-ui/
  - /java/aspose-cells-gridjs/customize-toolbar/

---

## メニューとツールバーボタンのカスタマイズに関して
直接便利なAPIは提供していません。
ただし、DOM構造に基づくJavaScript関数を書いて実現可能です。



## メニューバーのカスタマイズ 
例：Fileメニューだけを残すために、GridJsのdiv idを "gridjs-divid" と仮定します。
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
この関数を呼び出した後 

![カスタマイズされたメニューバーの画面](gridjs_customize_menubar.png)


## メニューバーの項目のカスタマイズ 
例：Fileメニューの「Download As XLSX」メニュー項目だけを残すために、GridJsのdiv idを "gridjs-divid" と仮定します。
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
この関数を呼び出した後 

![カスタマイズされたメニューバー項目の画面](gridjs_customize_menu.png)

## ツールバー項目のカスタマイズ 
例：ズームボタンだけを残すために、GridJsのdiv idを "gridjs-divid" と仮定します。
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
この関数を呼び出した後 

![カスタマイズされたツールバーの画面](gridjs_customize_toolbar.png)





