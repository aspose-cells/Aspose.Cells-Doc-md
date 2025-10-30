---
title: hur man anpassar menyer och verktygsfält i GridJs  
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/how-to-customize-menus/
description: Denna artikel beskriver hur man anpassar menyer och verktygsfält i GridJs.
keywords: GridJs, anpassa menyer, menyer, anpassa
aliases:
  - /python-net/aspose-cells-gridjs/customize-menus/
  - /python-net/aspose-cells-gridjs/customize-ui/
  - /python-net/aspose-cells-gridjs/customize-toolbar/

---

## om anpassning av menyer och verktygsfältknappar
vi tillhandahåller inte användbara API:er direkt.
men vi kan skriva några JS-funktioner baserat på DOM-strukturen för att åstadkomma det.



## Anpassa menyfält 
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


## Anpassa objekt i menyfältet 
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

## Anpassa verktygsfältets objekt 
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


## Anpassa verktygsfältets hover-effekt

öppna webbläsarens inspektionsfönster, välj verktygsfältets knapp,

![todo:skärm för att välja inspektionsverktygsfältets knapp](gridjs_hover_toolbar_button_inspect.png)

då kan vi hitta den relaterade CSS-nyckeln för denna knapp: freeze

![todo:skärm för att hitta CSS-nyckeln för verktygsfältsknappen](gridjs_hover_toolbar_button_csskey.png)

lägg till följande CSS-regel:
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
resultatet blir:

![todo:skärm för hovringseffekt för verktygsfältsknappen](gridjs_hover_toolbar_button_hover.png)


## Anpassa objekt i nedre aktivitetsfältet

### Översikt
Nedre aktivitetsfältet innehåller två interaktiva knappar:
1. &zwnj;**Lägg till kalkylblad-knapp**&zwnj; (`add`-klass) - Skapar nya kalkylblad
2. &zwnj;**Välj kalkylblad-knapp**&zwnj; (`ellipsis`-klass) - Hanterar kalkylbladsval

### DOM-åtkomst
Du kan komma åt dessa element med hjälp av:
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### Anpassningsexempel
1. Dölj knappar
För att ta bort en knapp från DOM:
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. Ändra ikoner
Du kan ersätta ikoner med antingen externa SVG-filer eller inline SVG-data.
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. Ändra knappbeteende
Du kan modifiera klickhändelsen för att anpassa funktionaliteten:
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```





