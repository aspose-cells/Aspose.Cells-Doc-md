---
title: Trabajar con el lado del cliente de GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/client/
---
# Trabajar con el lado del cliente de GridJs
Desarrollamos el cliente GridJs basado en[hoja de cálculo x](https://github.com/myliang/x-spreadsheet).

## los pasos principales son:

- crear una instancia de hoja de cálculo x_
```javascript
xs = x_spreadsheet(id, options)
```
- cargar datos json
```javascript
xs.loadData(jsondata.data)
```
- establecer hoja activa
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- establecer celda activa
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

por ejemplo, el siguiente código inicia un objeto x_spreadsheet.
```javascript
 xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
            showContextmenu: true
        }).loadData(sheets)
```
 // los parámetros para las opciones:
 updateMode: actualmente solo admitimos 'servidor'
 updateUrl: establezca la URL del lado del servidor para la acción de actualización basada en json
 modo: leer significa hoja de cálculo de solo lectura/editar significa que podemos editar la hoja de cálculo
 showToolbar: significa si mostrar la barra de herramientas
 showFileName: si mostrar el nombre del archivo
 local: admite varios idiomas para los menús, la configuración regional puede ser: en, cn, es, pt, de, ru, nl para inglés, chino, español, portugués, alemania, ruso, holandés
 showContextmenu: significa si mostrar el menú contextual al hacer clic con el botón derecho en una celda
## 

___
## otras API útiles
- Renderizar la vista
```javascript
xs.reRender()
```
- Obtener la imagen/forma seleccionada��si no hay nada, la selección devolverá un valor nulo
```javascript
xs.sheet.selector.getObj()
```

- Obtener el objeto de la celda
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Obtener el estilo de celda
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Establecer el valor de la celda
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- Obtener/Establecer el rango de celdas seleccionado
```javascript
xs.sheet.data.selector.range
```
- Establecer el valor de celda para la celda o área de celda seleccionada
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- Establecer el estilo para la celda o área de celda seleccionada
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- Combinar el área de la celda seleccionada
```javascript
xs.sheet.data.merge()
```

- Separar el área de la celda seleccionada
```javascript
xs.sheet.data.unmerge()
```
-  Eliminar la celda seleccionada
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- Establecer el panel de congelación
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

-  Insertar fila o columnas en la celda seleccionada
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
-  Eliminar fila o columnas en la celda seleccionada
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

- Establecer el ancho de la columna
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
-  Obtener el ancho de la columna.
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- Establecer la altura de la fila
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
-  Obtener la altura de la fila
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- Obtener/Establecer la dirección de visualización
```javascript
xs.sheet.data.displayRight2Left
```



para obtener información detallada, puede consultar el ejemplo aquí
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
