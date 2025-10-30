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



## Personalizar la barra de menús 
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


## Personalizar los elementos en la barra de menús 
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

## Personalizar los elementos de la barra de herramientas 
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


## Personalizar el efecto hover de la barra de herramientas

Abre la ventana de inspección del navegador, selecciona el botón de la barra de herramientas,

![falta: la pantalla para seleccionar el botón de inspección en la barra de herramientas](gridjs_hover_toolbar_button_inspect.png)

entonces podemos encontrar la clave CSS relacionada para este botón es: congelar

![todo:la pantalla para encontrar la clave css del botón de la barra de herramientas](gridjs_hover_toolbar_button_csskey.png)

agrega la siguiente regla css:
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
el resultado será :

![todo:la pantalla para efecto hover para el botón de la barra de herramientas](gridjs_hover_toolbar_button_hover.png)


## Personalizar elementos en la barra inferior

### Resumen
La barra inferior contiene dos botones interactivos:
1. &zwnj;**Botón Agregar Hoja de Trabajo**&zwnj; (`add` clase) - Crear nuevas hojas de trabajo
2. &zwnj;**Botón Seleccionar Hoja de Trabajo**&zwnj; (`ellipsis` clase) - Gestionar selección de hojas de trabajo

### Acceso DOM
Puedes acceder a estos elementos usando:
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### Ejemplos de Personalización
1. Ocultar botones
Para eliminar un botón del DOM:
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. Cambiar íconos
Puedes reemplazar íconos usando archivos SVG externos o datos SVG en línea.
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. Cambiar comportamiento del botón
Puedes modificar el evento de clic para personalizar la funcionalidad:
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```





