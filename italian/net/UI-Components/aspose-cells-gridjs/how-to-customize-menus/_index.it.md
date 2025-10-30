---
title: come personalizzare menu e barre degli strumenti in GridJs  
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/how-to-customize-menus/
description: Questo articolo descrive come personalizzare menu e barre degli strumenti in GridJs.
keywords: GridJs, personalizzare menu, menu, personalizzare
aliases:
  - /net/aspose-cells-gridjs/customize-menus/
  - /net/aspose-cells-gridjs/customize-ui/
  - /net/aspose-cells-gridjs/customize-toolbar/

---

## riguardo alla personalizzazione di menu e pulsanti della barra degli strumenti
Non forniamo API utili direttamente.
Tuttavia, possiamo scrivere alcune funzioni js basate sulla struttura DOM per ottenerlo.



## Personalizza menubar 
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


## Personalizza elementi nel menubar 
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

## Personalizza elementi della toolbar 
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


## Personalizza effetto hover della toolbar

apri la finestra di ispezione del browser, seleziona il pulsante della barra degli strumenti,

![todo:lo schermo per selezionare il pulsante di ispezione della barra degli strumenti](gridjs_hover_toolbar_button_inspect.png)

poi possiamo trovare la chiave CSS correlata a questo pulsante: freeze

![todo:lo schermo per trovare la chiave CSS del pulsante della barra degli strumenti](gridjs_hover_toolbar_button_csskey.png)

aggiungi la seguente regola CSS:
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
il risultato sarà:

![todo:lo schermo per l'effetto hover per il pulsante della barra degli strumenti](gridjs_hover_toolbar_button_hover.png)


## Personalizza gli elementi nella barra inferiore

### Panoramica
La barra inferiore contiene due pulsanti interattivi:
1. &zwnj;**Pulsante Aggiungi Foglio di Lavoro**&zwnj; (`add` classe) - Crea nuovi fogli di lavoro
2. &zwnj;**Pulsante Seleziona Foglio di Lavoro**&zwnj; (`ellipsis` classe) - Gestisce la selezione del foglio di lavoro

### Accesso DOM
Puoi accedere a questi elementi usando:
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### Esempi di personalizzazione
1. Nascondi i pulsanti
Per rimuovere un pulsante dal DOM:
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. Cambia le icone
Puoi sostituire le icone usando file SVG esterni o dati SVG inline.
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. Cambia il comportamento del pulsante
Puoi modificare l'evento click per personalizzare la funzionalità:
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```

