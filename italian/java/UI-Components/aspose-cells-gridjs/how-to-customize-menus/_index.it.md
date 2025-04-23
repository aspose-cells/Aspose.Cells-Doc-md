---
title: come personalizzare menu e barre degli strumenti in GridJs  
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/how-to-customize-menus/
description: Questo articolo descrive come personalizzare menu e barre degli strumenti in GridJs.
keywords: GridJs, personalizzare menu, menu, personalizzare
aliases:
  - /java/aspose-cells-gridjs/customize-menus/
  - /java/aspose-cells-gridjs/customize-ui/
  - /java/aspose-cells-gridjs/customize-toolbar/

---

## riguardo alla personalizzazione di menu e pulsanti della barra degli strumenti
Non forniamo API utili direttamente.
Tuttavia, possiamo scrivere alcune funzioni js basate sulla struttura DOM per ottenerlo.



## personalizzazione della barra dei menu 
ad esempio: per mantenere solo il menu File, supponi che l'id del div di GridJs sia "gridjs-divid"
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
Dopo aver chiamato questa funzione 

![todo:la schermata di personalizzazione della barra dei menu](gridjs_customize_menubar.png)


## personalizza gli elementi nella barra dei menu 
ad esempio: per mantenere solo l'elemento di menu "Download As XLSX" nel menu File, supponi che l'id del div di GridJs sia "gridjs-divid"
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
Dopo aver chiamato questa funzione 

![todo:la schermata di personalizzazione dell'elemento del menu](gridjs_customize_menu.png)

## personalizza gli elementi della barra degli strumenti 
ad esempio: per mantenere solo il pulsante di zoom, supponi che l'id del div di GridJs sia "gridjs-divid"
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
Dopo aver chiamato questa funzione 

![todo:la schermata di personalizzazione della barra degli strumenti](gridjs_customize_toolbar.png)





