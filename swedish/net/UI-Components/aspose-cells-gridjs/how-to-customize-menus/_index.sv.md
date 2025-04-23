---
title: hur man anpassar menyer och verktygsfält i GridJs  
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/how-to-customize-menus/
description: Denna artikel beskriver hur man anpassar menyer och verktygsfält i GridJs.
keywords: GridJs, anpassa menyer, menyer, anpassa
aliases:
  - /net/aspose-cells-gridjs/customize-menus/
  - /net/aspose-cells-gridjs/customize-ui/
  - /net/aspose-cells-gridjs/customize-toolbar/

---

## om anpassning av menyer och verktygsfältknappar
vi tillhandahåller inte användbara API:er direkt.
men vi kan skriva några JS-funktioner baserat på DOM-strukturen för att åstadkomma det.



## anpassa menyrad 
Till exempel: att behålla endast File-menyn, anta att div-id för GridJs är "gridjs-divid"
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
Efter att ha anropat denna funktion 

![todo: skärm för att anpassa menyrad](gridjs_customize_menubar.png)


## anpassa objekt i menyraden 
Till exempel: att behålla "Ladda ner som XLSX"-menyalternativet endast i File-menyn, anta att div-id för GridJs är "gridjs-divid"
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
Efter att ha anropat denna funktion 

![todo: skärm för att anpassa menyradsobjekt](gridjs_customize_menu.png)

## anpassa verktygsfältobjekt 
Till exempel: att behålla zoomknappen endast, anta att div-id för GridJs är "gridjs-divid"
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
Efter att ha anropat denna funktion 

![todo: skärm för att anpassa verktygsfält](gridjs_customize_toolbar.png)





