---
title: Trabajar con la función Resaltar de GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/highlight/
description: Este artículo describe cómo usar GridJs para resaltar texto de celda, rangos de celdas, formas e imágenes.
keywords: highlight, highlight spreadsheet,redaction,remarks
---
#  Trabajar con la función Resaltar de GridJs
 Admitimos las siguientes API JS para la función Resaltar


-  Habilite el resaltado y establezca el estilo de resaltado. Todas las API de resaltado tendrán efecto solo después de que se establezca el estilo de resaltado en la hoja de trabajo activa.
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  actualizar el estilo de resaltado establecido en la hoja de trabajo activa
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


-  Deshabilitar resaltado en la hoja de trabajo activa
```javascript
xs.sheet.hideHighlights()
```
-  Agregue texto de celda para resaltar en la hoja de trabajo activa
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Eliminar resaltado del texto de la celda en una matriz en la hoja de trabajo activa
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Obtenga una matriz para resaltar el texto de la celda en la hoja de trabajo activa
```javascript
xs.sheet.getHighlightTexts()
```

-  Agregar rango de celdas para resaltar en la hoja de trabajo activa
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Eliminar resaltado del rango de celdas en una matriz en la hoja de trabajo activa
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Obtenga una matriz para resaltar el rango de celdas en la hoja de trabajo activa
```javascript
xs.sheet.getHighlightRanges()
```

-  Establezca el rango de celdas para invertir el resaltado en la hoja de trabajo activa
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Eliminar resaltado para resaltado inverso en la hoja de trabajo activa
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Obtenga el rango de celdas de resaltado inverso en la hoja de trabajo activa
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Agregue forma para resaltar la matriz en la hoja de trabajo activa
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Eliminar la forma resaltada en una matriz en la hoja de trabajo activa
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Obtener matriz para resaltar la forma en la hoja de trabajo activa
```javascript
xs.sheet.getHighlightShaps()
```

-  Agregue un cuadro de texto para resaltar, el cuadro de texto es un tipo especial de forma cuya propiedad de tipo es: "Cuadro de texto", en la hoja de trabajo activa
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  Elimine el rango resaltado en el cuadro de texto, el cuadro de texto es un tipo especial de forma cuya propiedad de tipo es: "Cuadro de texto", en la hoja de trabajo activa
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Agregue una imagen para resaltar la matriz en la hoja de trabajo activa
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Eliminar la imagen resaltada en una matriz en la hoja de trabajo activa
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Obtener matriz para imagen resaltada
```javascript
xs.sheet.getHighlightImages()
```

-  establezca si se resaltarán todos los objetos en la hoja de trabajo activa, incluirá todas las formas e imágenes y toda el área de la hoja de trabajo
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Establecer función de resaltado de imagen personalizada
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

-  configuración clara de resaltado para la hoja de trabajo activa
```javascript
xs.sheet.clearHighlights()

```

###  Resaltado para objeto de cuadro de texto
El cuadro de texto es un tipo especial de forma cuya propiedad de tipo es: "Cuadro de texto",
por ejemplo: el siguiente código mostrará qué forma es el cuadro de texto

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  Agregar resaltado para el objeto de cuadro de texto
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

-  Eliminar resaltado del objeto de cuadro de texto
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  Obtener resaltado para el objeto de cuadro de texto
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  Cambiar el color de fondo del objeto del cuadro de texto
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  Cambie automáticamente el color de fondo y el color del texto para obtener un efecto visual activo
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  ocultar/mostrar el contenido del texto en el objeto del cuadro de texto
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



Puede encontrar más en nuestra página de demostración de github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
