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



## Personnaliser la barre de menus 
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


## Personnaliser les éléments de la barre de menus 
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

## Personnaliser les éléments de la barre d'outils 
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


## Personnaliser l'effet de survol de la barre d'outils

Ouvrez la fenêtre d’inspection du navigateur, sélectionnez le bouton de la barre d’outils,

![todo:l'écran pour sélectionner le bouton inspect de la barre d'outils](gridjs_hover_toolbar_button_inspect.png)

puis nous pouvons trouver que la clé CSS associée à ce bouton est :figer

![todo:l'écran pour trouver la clé CSS du bouton de la barre d'outils](gridjs_hover_toolbar_button_csskey.png)

ajoutez la règle CSS ci-dessous :
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
le résultat sera :

![todo : l'écran pour l'effet de survol du bouton de la barre d'outils](gridjs_hover_toolbar_button_hover.png)


## Personnaliser les éléments dans la barre du bas

### Aperçu
La barre inférieure contient deux boutons interactifs :
1. &zwnj;**Bouton Ajouter une Feuille**&zwnj; (`add` classe) - Crée de nouvelles feuilles de calcul
2. &zwnj;**Bouton Sélectionner une Feuille**&zwnj; (`ellipsis` classe) - Gère la sélection des feuilles de calcul

### Accès DOM
Vous pouvez accéder à ces éléments en utilisant :
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### Exemples de personnalisation
1. Cacher des boutons
Pour supprimer un bouton du DOM :
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. Changer d'icônes
Vous pouvez remplacer des icônes en utilisant des fichiers SVG externes ou des données SVG en ligne.
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. Modifier le comportement du bouton
Vous pouvez modifier l'événement clic pour personnaliser la fonctionnalité :
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```





