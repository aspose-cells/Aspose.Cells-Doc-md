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

## Werkzeugleisten-Elemente anpassen 
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


## Hover-Effekt der Werkzeugleiste anpassen

Öffnen Sie das Browser-Inspektionsfenster, wählen Sie die Symbolleiste-Schaltfläche,

![todo: der Bildschirm zum Auswählen der Inspektions-Schaltfläche](gridjs_hover_toolbar_button_inspect.png)

dann können wir den zugehörigen CSS-Schlüssel für diese Schaltfläche finden:freeze

![todo:Der Bildschirm für die Suche nach CSS-Schlüssel für Toolbar-Schaltfläche](gridjs_hover_toolbar_button_csskey.png)

Fügen Sie die folgende CSS-Regel hinzu:
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
Das Ergebnis wird sein:

![todo:Der Bildschirm für Hover-Effekt für Toolbar-Schaltfläche](gridjs_hover_toolbar_button_hover.png)


## Items im unteren Balken anpassen

### Übersicht
Der untere Balken enthält zwei interaktive Schaltflächen:
1. &zwnj;**Schaltfläche zum Hinzufügen eines Arbeitsblatts**&zwnj; (`add` Klasse) - Erstellt neue Arbeitsblätter
2. &zwnj;**Schaltfläche zur Auswahl des Arbeitsblatts**&zwnj; (`ellipsis` Klasse) - Verwalte die Arbeitsblatt-Auswahl

### DOM-Zugriff
Sie können auf diese Elemente zugreifen mit:
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### Anpassungsbeispiele
1. Schaltflächen ausblenden
Um eine Schaltfläche aus dem DOM zu entfernen:
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. Symbole ändern
Sie können Symbole entweder durch externe SVG-Dateien oder Inline-SVG-Daten ersetzen.
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. Button-Verhalten ändern
Sie können das Klick-Ereignis anpassen, um die Funktionalität zu ändern:
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```

