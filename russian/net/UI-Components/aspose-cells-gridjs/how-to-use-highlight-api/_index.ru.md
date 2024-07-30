---
title: Работа с функцией выделения GridJs
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-use-highlight-api/
description: В этой статье описано, как использовать выделение текста ячейки, диапазонов ячеек, форм и изображений в GridJs.
keywords: GridJs, выделение, выделить таблицу, редактирование, примечания
aliases:
  - /net/aspose-cells-gridjs/highlight/
  - /net/aspose-cells-gridjs/how-to-highlight/
  - /net/aspose-cells-gridjs/work-with-highlight-api/
  - /net/aspose-cells-gridjs/work-with-highlight-apis/
---

# Работа с функцией выделения GridJs 
Мы поддерживаем следующие JS API для функции выделения 


- Включить выделение и установить стиль выделения, все API выделения будут применяться только после установки стиля выделения в активном рабочем листе 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- Обновить установленный стиль выделения в активном рабочем листе 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- Отключить выделение  в активном рабочем листе    
```javascript
xs.sheet.hideHighlights()
```
- Добавить текст ячейки для выделения в активный рабочий лист 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- Удалить выделение для текста ячейки в массиве в активном рабочем листе 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Получить массив для выделения текста ячейки в активном рабочем листе   
```javascript
xs.sheet.getHighlightTexts()
```

- Добавить диапазон ячеек для выделения в активном рабочем листе 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Удалить выделение для диапазона ячеек в массиве в активном рабочем листе 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Получить массив для выделения диапазона ячеек в активном рабочем листе   
```javascript
xs.sheet.getHighlightRanges()
```

- Установить диапазон ячеек для инверсного выделения в активном рабочем листе 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Удалить выделение для инверсного выделения в активном рабочем листе 
```javascript
xs.sheet.removeHighlightInverseRange()

```

- Получить диапазон ячеек инверсного выделения в активном рабочем листе 
```javascript
xs.sheet.getHighlightInverseRange()
```


- Добавить форму в массив выделения в активном рабочем листе 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Удалить выделение формы в массиве в активном рабочем листе 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Получить массив для выделения формы в активном рабочем листе  
```javascript
xs.sheet.getHighlightShaps()
```

- Добавить текстовое поле для выделения, текстовое поле - это особый тип формы, свойство типа которой: "TextBox", в активном рабочем листе 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- Удалить выделение диапазона в текстовом поле, текстовое поле - это особый тип формы, свойство типа которой: "TextBox", в активном рабочем листе 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

- Добавить изображение для выделения массива в активном рабочем листе 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Удалить выделение изображения в массиве в активном рабочем листе 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Получить массив для выделения изображения  
```javascript
xs.sheet.getHighlightImages()
```

- Установить, следует ли выделять все объекты на активном листе, включая все формы и изображения, а также всю область листа
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- Установить пользовательскую функцию выделения изображения
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

- Очистить настройки выделения для активного листа
```javascript
xs.sheet.clearHighlights()

```

### Выделение для объекта текстового поля
текстовое поле - это особый тип формы, свойство типа которой: "TextBox",
например: нижеприведенный код покажет, какая форма является текстовым полем

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- Добавить выделение для объекта текстового поля
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

- Удалить выделение для объекта текстового поля 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- Получить выделение для объекта текстового поля 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




Вы можете найти больше на нашей демонстрационной странице github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
