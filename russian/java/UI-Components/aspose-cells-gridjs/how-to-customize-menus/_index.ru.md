---
title: как настраивать меню и панель инструментов в GridJs  
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-customize-menus/
description: Эта статья описывает, как настраивать меню и панели инструментов в GridJs.
keywords: GridJs,настройка меню,меню,настройка
aliases:
  - /java/aspose-cells-gridjs/customize-menus/
  - /java/aspose-cells-gridjs/customize-ui/
  - /java/aspose-cells-gridjs/customize-toolbar/

---

## о настройке меню и кнопок на панели инструментов
Мы не предоставляем полезных API напрямую.
Однако мы можем написать некоторые js-функции на основе структуры DOM для достижения этой цели.



## Настройка менюбар 
например: чтобы оставить только меню `Файл`, предполагая, что id div GridJs — "gridjs-divid"
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
После вызова этой функции 

![todo:экран для настройки панели меню](gridjs_customize_menubar.png)


## Настройка элементов менюбар 
например: чтобы оставить только пункт "Скачать как XLSX" в меню "Файл", предполагая, что id div GridJs — "gridjs-divid"
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
После вызова этой функции 

![todo:экран для настройки пункта меню](gridjs_customize_menu.png)

## Настройка элементов панели инструментов 
например: оставить только кнопку зума, предполагая, что id div GridJs — "gridjs-divid"
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
После вызова этой функции 

![todo:экран для настройки панели инструментов](gridjs_customize_toolbar.png)


## Настройка эффекта наведения на панель инструментов

открыть окно инспекции браузера, выбрать кнопку панели инструментов,

![для выбораInspect кнопки инструментария](gridjs_hover_toolbar_button_inspect.png)

затем мы можем найти связанный css-ключ для этой кнопки:freeze

![todo:экран для поиска css ключа для кнопки панели инструментов](gridjs_hover_toolbar_button_csskey.png)

добавьте следующее правило css:
```css
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn:hover .x-spreadsheet-icon-img.freeze,
.x-spreadsheet-toolbar .x-spreadsheet-toolbar-btn.active .x-spreadsheet-icon-img.freeze {
  background: rgba(4, 71, 33, 0.08);
  filter: brightness(0) saturate(100%) invert(27%) sepia(51%) saturate(2878%) hue-rotate(346deg) brightness(104%) contrast(97%);
}
```
результат будет:

![todo:экран для эффекта наведения для кнопки панели инструментов](gridjs_hover_toolbar_button_hover.png)


## Настройка элементов нижней панели

### Обзор
В нижней панели расположены две интерактивные кнопки:
1. &zwnj;**Добавить кнопку листа**&zwnj; (`add` класс) - Создает новые листы
2. &zwnj;**Выбрать лист**&zwnj; (`ellipsis` класс) - Управление выбором листа

### Доступ к DOM
Вы можете получить доступ к этим элементам с помощью:
```javascript
// Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');

// Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');

```

### Примеры настройки
1. Скрыть кнопки
Чтобы удалить кнопку из DOM:
```javascript
// Hide Add Worksheet Button
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.parentElement.removeChild(addButton);

// Hide Select Worksheet Button
const selectButton = document.querySelector('.x-spreadsheet-icon-img.ellipsis');
selectButton.parentElement.removeChild(selectButton);

```

2. Изменить иконки
Вы можете заменить иконки, используя внешние SVG файлы или встроенные данные SVG.
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.style.backgroundImage = "url('https://example.com/fish-icon.svg')";
// Adjust size and position
addButton.style.width = '18px';
addButton.style.height = '18px';
addButton.style.left = '0';
addButton.style.top = '0';
```

3. Изменить поведение кнопки
Вы можете изменить событие клика для настройки функциональности:
```javascript
const addButton = document.querySelector('.x-spreadsheet-icon-img.add');
addButton.addEventListener('click', function() {
  // Custom action here
  console.log('Custom add worksheet action');
});
```





