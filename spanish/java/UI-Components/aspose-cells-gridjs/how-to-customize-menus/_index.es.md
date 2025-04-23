---
title: cómo personalizar menús y barras de herramientas en GridJs  
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-customize-menus/
description: Este artículo describe cómo personalizar menús y barras de herramientas en GridJs.
keywords: GridJs, personalizar menús, menús, personalizar
aliases:
  - /java/aspose-cells-gridjs/customize-menus/
  - /java/aspose-cells-gridjs/customize-ui/
  - /java/aspose-cells-gridjs/customize-toolbar/

---

## sobre personalización de menús y botones de la barra de herramientas
no proporcionamos APIs útiles directamente.
sin embargo, podemos escribir algunas funciones js basadas en la estructura DOM para lograrlo.



## personalizar barra de menús 
por ejemplo: mantener solo el menú Archivo, asumiendo que el id del div de GridJs es "gridjs-divid"
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
Después de llamar a esta función 

![por hacer: la pantalla para personalizar la barra de menús](gridjs_customize_menubar.png)


## personalizar ítems en la barra de menús 
por ejemplo: mantener solo la opción "Descargar como XLSX" en el menú Archivo, asumiendo que el id del div de GridJs es "gridjs-divid"
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
Después de llamar a esta función 

![por hacer: la pantalla para personalizar ítems del menú](gridjs_customize_menu.png)

## personalizar ítems de la barra de herramientas 
por ejemplo: mantener solo el botón de zoom, asumando que el id del div de GridJs es "gridjs-divid"
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
Después de llamar a esta función 

![todo:la pantalla para personalizar la barra de herramientas](gridjs_customize_toolbar.png)





