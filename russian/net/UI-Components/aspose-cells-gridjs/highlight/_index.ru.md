---
title: Работа с функцией выделения GridJs
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/highlight/
description: В этой статье описывается, как использовать GridJs для выделения текста ячейки, диапазонов ячеек, фигур и изображений.
keywords: highlight, highlight spreadsheet
---
#  Работа с функцией выделения GridJs
 Мы поддерживаем перечисленные ниже API-интерфейсы JS для функции Highlight.


-  Включите выделение и установите стиль выделения, все API-интерфейсы выделения вступят в силу только после установки стиля выделения.
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  Отключить выделение
```javascript
xs.hideHighlights()
```
-  Добавить текст ячейки для выделения
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Удалить выделение текста ячейки в массиве
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

-  Получить массив для выделения текста ячейки
```javascript
xs.sheet.getHighlightTexts()
```

-  Добавить диапазон ячеек для выделения
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Удалить выделение диапазона ячеек в массиве
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Получить массив для выделения диапазона ячеек
```javascript
xs.sheet.getHighlightRanges()
```

-  Установить диапазон ячеек для инверсного выделения
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Удалить выделение для инвертированного выделения
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Получить обратный диапазон ячеек выделения
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Добавить форму, чтобы выделить массив
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Удалить фигуру выделения в массиве
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Получить массив для выделения формы
```javascript
xs.sheet.getHighlightShaps()
```

-  Добавьте текстовое поле для выделения, текстовое поле - это особый вид формы, свойство типа которого: "TextBox",
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- Удалите диапазон выделения в текстовом поле, текстовое поле — это особый вид формы, свойство типа которого: «TextBox»,
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Добавить изображение, чтобы выделить массив
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Удалить выделение изображения в массиве
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Получить массив для выделения изображения
```javascript
xs.sheet.getHighlightImages()
```

-  установить, следует ли выделять весь рабочий лист, включать все фигуры и изображения
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Установить пользовательскую функцию выделения изображения
```javascript
xs.sheet.setCustomHighlightImgFunc(func)
   // the parameters are:
   func: the custom highlight image function, it shall take two parameters ,first is ishighlight,the second one is the fabric image object 
   //we use fabric js to manage image object, please refer to http://fabricjs.com/image-filters to check more info
   below is an example for the decleare function: 
   const customHighlightImage = (ishighlight, imgobj) => {
            imgobj.filters[0] = ishighlight ? new fabric.Image.filters.Sepia() : false;
            imgobj.applyFilters();
        }
    
```

###  Выделение объекта текстового поля
текстовое поле — это особый тип фигуры, свойство типа: «TextBox»,
например: приведенный ниже код покажет, какая фигура является текстовым полем

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  Добавить выделение для объекта текстового поля
```javascript
    addHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox

//for example,we assume shape 0 is a textbox object
const textbox=xs.sheet.data.shapes[0];
//first we shall add to highlight shape to enable the highlight for the textbox shape object,it support multiple range postion 
 xs.sheet.addHighlightShape(textbox.id);
 textbox.addHighlight(5,10);
 textbox.addHighlight(18,28);
```

-  Удалить выделение для объекта текстового поля
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  Получить выделение для объекта текстового поля
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  Изменить цвет фона для объекта текстового поля
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  Автоматическое изменение цвета фона и цвета текста для получения визуально активного эффекта
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  скрыть/отобразить текстовое содержимое в объекте текстового поля
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



Вы можете найти больше на нашей демонстрационной странице github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html.
