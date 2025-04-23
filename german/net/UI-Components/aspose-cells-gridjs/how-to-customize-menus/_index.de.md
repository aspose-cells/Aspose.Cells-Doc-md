---
title: wie man Menüs und Symbolleisten in GridJs anpasst  
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/how-to-customize-menus/
description: Dieser Artikel beschreibt, wie man Menüs und Symbolleisten in GridJs anpasst.
keywords: GridJs, Menüs anpassen, Menüs, anpassen
aliases:
  - /net/aspose-cells-gridjs/customize-menus/
  - /net/aspose-cells-gridjs/customize-ui/
  - /net/aspose-cells-gridjs/customize-toolbar/

---

## Über die Anpassung von Menüs und Toolbar-Buttons
Wir stellen keine nützlichen APIs direkt bereit.
Wir können jedoch einige JS-Funktionen basierend auf der DOM-Struktur schreiben, um dies zu erreichen.



## Menüleiste anpassen 
zum Beispiel:Nur das Datei-Menü beibehalten, nehmen Sie an, die div-id von GridJs ist "gridjs-divid"
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
Nach Aufruf dieser Funktion 

![Todo: Der Bildschirm zum Anpassen der Menüleiste](gridjs_customize_menubar.png)


## Elemente in der Menüleiste anpassen 
zum Beispiel:Nur den "Download as XLSX" Menüpunkt in der Datei-Menü beibehalten, nehmen Sie an, die div-id von GridJs ist "gridjs-divid"
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
Nach Aufruf dieser Funktion 

![Todo: Der Bildschirm zum Anpassen des Menüeintrags](gridjs_customize_menu.png)

## Toolbar-Elemente anpassen 
zum Beispiel:Nur die Zoom-Schaltfläche beibehalten, nehmen Sie an, die div-id von GridJs ist "gridjs-divid"
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
Nach Aufruf dieser Funktion 

![Todo: Der Bildschirm zum Anpassen der Werkzeugleiste](gridjs_customize_toolbar.png)





