---
title: comment personnaliser les menus et les barres d outils dans GridJs  
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/how-to-customize-menus/
description: Cet article décrit comment personnaliser les menus et les barres d outils dans GridJs.
keywords: GridJs, personnaliser les menus, menus, personnaliser
aliases:
  - /java/aspose-cells-gridjs/customize-menus/
  - /java/aspose-cells-gridjs/customize-ui/
  - /java/aspose-cells-gridjs/customize-toolbar/

---

## à propos de la personnalisation des menus et des boutons de la barre d'outils
nous ne fournissons pas d'API utiles directement.
 toutefois, nous pouvons écrire quelques fonctions JS basées sur la structure DOM pour y parvenir.



## personnaliser la barre de menu 
par exemple : pour ne garder que le menu Fichier, supposez que l'ID du div de GridJs est "gridjs-divid"
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
Après avoir appelé cette fonction 

![à faire : l'écran pour personnaliser la barre de menu](gridjs_customize_menubar.png)


## personnaliser les éléments dans la barre de menu 
par exemple : pour ne garder que l'option "Télécharger en XLSX" dans le menu Fichier, supposez que l'ID du div de GridJs est "gridjs-divid"
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
Après avoir appelé cette fonction 

![à faire : l'écran pour personnaliser l'élément de la barre de menu](gridjs_customize_menu.png)

## personnaliser les éléments de la barre d'outils 
par exemple : pour ne garder que le bouton de zoom, supposez que l'ID du div de GridJs est "gridjs-divid"
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
Après avoir appelé cette fonction 

![à faire : l'écran pour personnaliser la barre d'outils](gridjs_customize_toolbar.png)





