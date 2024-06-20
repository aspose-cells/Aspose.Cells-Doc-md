---
title: Trabajando con la función de resaltado de GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/highlight/
description: Este artículo describe cómo usar el resaltado en texto de celda, rangos de celdas, formas e imágenes en GridJs.
keywords: GridJs, resaltar, resaltar hoja de cálculo, redacción, observaciones
---

# Trabajando con la función de resaltado de GridJs 
Apoyamos las siguientes APIs de JS para la función de resaltado 


- Habilitar resaltado y Establecer estilo de resaltado, todas las APIs de resaltado solo funcionarán después de que se establezca el estilo de resaltado en la hoja de cálculo activa 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- actualizar el estilo de resaltado establecido en la hoja de cálculo activa 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- Deshabilitar resaltado en la hoja de cálculo activa    
```javascript
xs.sheet.hideHighlights()
```
- Agregar texto de celda para resaltar en la hoja de cálculo activa 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- Eliminar resaltado para texto de celda en matriz en la hoja de cálculo activa 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Obtener matriz para resaltar texto de celda en la hoja de cálculo activa   
```javascript
xs.sheet.getHighlightTexts()
```

- Agregar rango de celdas para resaltar en la hoja de cálculo activa 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Eliminar resaltado para rango de celdas en matriz en la hoja de cálculo activa 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Obtener matriz para resaltar rango de celdas en la hoja de cálculo activa   
```javascript
xs.sheet.getHighlightRanges()
```

- Establecer rango de celdas para resaltar inversamente en la hoja de cálculo activa 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Quitar resaltado para resaltar inversamente en la hoja de cálculo activa 
```javascript
xs.sheet.removeHighlightInverseRange()

```

- Obtener rango de celdas de resaltado inverso en la hoja de cálculo activa 
```javascript
xs.sheet.getHighlightInverseRange()
```


- Agregar forma al conjunto de resaltado en la hoja de cálculo activa 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Quitar forma resaltada en conjunto en la hoja de cálculo activa 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Obtener arreglo de formas resaltadas en la hoja de cálculo activa  
```javascript
xs.sheet.getHighlightShaps()
```

- Agregar cuadro de texto para resaltar, el cuadro de texto es un tipo especial de forma cuya propiedad de tipo es :"TextBox", en la hoja de cálculo activa 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- Quitar rango resaltado en el cuadro de texto, el cuadro de texto es un tipo especial de forma cuya propiedad de tipo es :"TextBox", en la hoja de cálculo activa 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

- Agregar imagen al conjunto de resaltado en la hoja de cálculo activa 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Quitar imagen resaltada en conjunto en la hoja de cálculo activa 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Obtener arreglo de imágenes resaltadas  
```javascript
xs.sheet.getHighlightImages()
```

- Establecer si resaltar todos los objetos en la hoja de cálculo activa, incluyendo todas las formas e imágenes y toda el área de la hoja de cálculo
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- Establecer función de resaltado de imagen personalizada
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

- Borrar configuración de resaltado para la hoja de cálculo activa
```javascript
xs.sheet.clearHighlights()

```

### Resaltar para objeto cuadro de texto
el cuadro de texto es un tipo especial de forma cuya propiedad de tipo es :"TextBox",
por ejemplo: el código a continuación mostrará qué forma es cuadro de texto

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- Agregar resaltado para objeto cuadro de texto
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

- Quitar resaltado para objeto cuadro de texto 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- Obtener resaltado para objeto cuadro de texto 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




Puede encontrar más en nuestra página de demostración en GitHub https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
