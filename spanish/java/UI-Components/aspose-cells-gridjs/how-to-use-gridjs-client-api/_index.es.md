---
title: Trabajando con GridJs del lado del cliente
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/
keywords: GridJs, personalizado, logotipo, configuración, API, API JS, API cliente
description: Este artículo introduce las API o funciones de Javascript del cliente en GridJs.
aliases:
  - /java/aspose-cells-gridjs/client/
  - /java/aspose-cells-gridjs/work-with-client-api/
  - /java/aspose-cells-gridjs/use-js-api/
  - /java/aspose-cells-gridjs/gridjs-spreadsheet-api/
  - /java/aspose-cells-gridjs/client-api/
  - /java/aspose-cells-gridjs/js-api/
  - /java/aspose-cells-gridjs/javascript-api/
---

# Trabajando con GridJs del lado del cliente
Desarrollamos el cliente GridJs basado en [x-spreadsheet](https://github.com/myliang/x-spreadsheet).

## los principales pasos son:

- crear una instancia de x_spreadsheet
```javascript
xs = x_spreadsheet(id, options)
    // the parameters are:
    id:the html node id ,for example :'#gridjs-demo' for the html  <div id="gridjs-demo"></div>
    options: the load options


for example the below code init a gridjs_spreadsheet object.
	xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
			showContextmenu: true
			})
```
los parámetros para las opciones de carga:

| Parámetro | Descripción | Valor predeterminado | Opcional |
| --- | --- | --- | --- |
| `allowSelectTextInTextBoxInReadMode` | Permite seleccionar texto en controles TextBox cuando están en modo de lectura.<br>El valor predeterminado es falso. | `false` | Sí |
| `checkSyntax` | Realiza comprobación de sintaxis y corrección ortográfica para la entrada del usuario en contenido de texto.<br>Funciona con setSyntaxCheckUrl.<br>El valor predeterminado es falso. | `false` | Sí |
| `loadingGif` | URL del GIF de carga al cargar imágenes/formas.<br>El valor predeterminado es contenido/img/updating.gif. | `content/img/updating.gif` | Sí |
| `local` | Establecer información de localización para menús y barras de herramientas, soportando múltiples idiomas.<br>Los valores posibles incluyen:<br>- `en, zh, es, pt, de, ru, nl` (para inglés, chino, español, portugués, alemán, ruso, holandés)<br>- `ar, fr, id, it, ja` (para árabe, francés, indonesio, italiano, japonés)<br>- `ko, th, tr, vi, cht` (para coreano, tailandés, turco, vietnamita, chino tradicional) | `en` | Sí |
| `mode` | Puede ser `read` o `edit`; `read` significa hoja de cálculo solo lectura; `edit` significa que la hoja puede ser editada. | Ninguno | No |
| `isCollaborative` | Si se soporta modo colaborativo . | `false` | Sí |
| `searchHighlightColor` | Color de resaltado de fondo para el término de búsqueda.<br>El color debe incluir un canal alfa para la transparencia. | `#dbe71338` | Sí |
| `showCheckSyntaxButton` | Mostrar u ocultar botones de verificación de sintaxis y corrección ortográfica en la barra de herramientas.<br>El valor predeterminado es falso. | `false` | Sí |
| `showContextmenu` | Mostrar u ocultar el menú contextual al hacer clic derecho en una celda.<br>El valor predeterminado es verdadero. | `true` | Sí |
| `showFileName` | Mostrar u ocultar el nombre del archivo. | `true` | Sí |
| `showFormulaExplain` | Si se muestran explicaciones de fórmulas aplicadas a esta celda cuando el mouse lo pasa por encima.<br>Trabaja junto con setFormulaExplainUrl.<br>El valor predeterminado es false. | `false` | Sí |
| `showFormulaTip` | Si se muestra la fórmula existente aplicada a esta celda cuando el mouse lo pasa por encima.<br>El valor predeterminado es false. | `false` | Sí |
| `showNonEditableSymbolInCell` | Si se muestra un símbolo no editable del lado del cliente en la celda.<br>Si se establece en true, después de hacer clic en el menú contextual derecho "Desactivar edición", el área seleccionada que deshabilita la edición mostrará el símbolo.<br>El valor predeterminado es false. | `false` | Sí |
| `showToolbar` | Si se muestra la barra de herramientas. | `true` | Sí |
| `updateMode` | Actualmente, solo admite `server`. | `server` | No |
| `updateUrl` | Establece la URL del lado del servidor para acciones de actualización basadas en JSON. | Ninguno | No |
| `view` | Establece el tamaño de vista para la hoja, por ejemplo, `{width: () => 1000, height: ()=> 500}`. | `{width: () => document.documentElement.clientWidth, height: () => document.documentElement.clientHeight }` | Sí |
| `token` | Establece el token de autenticación. Cuando el token no es null, se añadirá automáticamente la cabecera `Authorization: Bearer {token}` a las solicitudes. Puedes usar `xs.refreshToken(token)` para establecer un nuevo token. | Ninguno | Sí |    
| `showBottombarStats` | Mostrar estadísticas en la barra inferior.<br>El valor por defecto es true. | `true` | Sí |   
| `showRowAppenderToolbar` | Mostrar la barra de herramientas para añadir filas.<br>El valor por defecto es true. | `true` | Sí |   

- cargar con datos json
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
- establecer hoja activa por nombre de hoja
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
- establecer hoja activa por id
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

- establecer celda activa
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

- establecer activo para múltiples instancias 
```javascript
xs.setActiveForMultipleInstance(isacitve);
// the parameters are:
	isacitve: whether need to do edit operation at this xs instanse 
// when there are more than one GridJs instances in one page, we need to call this method.
// we only support do edit operation for one instances at a page.
// for example,if we have two instances: xs1 and xs2 in one html page.
// if we need to keep edit operation in xs1,
// we shall call:
xs1.setActiveForMultipleInstance(true);
xs2.setActiveForMultipleInstance(false);

// if we need not do any edit operation for both,
// we shall call:
xs1.setActiveForMultipleInstance(false);
xs2.setActiveForMultipleInstance(false);

```
- establecer Toast personalizado
```javascript
xs.customToast(customToastFunction);
// the parameter is:
	customToastFunction: user defined function to toast message,it shall have three parameters :title, content,callback
	if set to null,it will use the default build-in toast.

    for example: 
            function myCustomToast(title, content, callback) {
	    //.....
	    }
            xs.customToast(myCustomToast);
```

- establecer información para operaciones de forma/imagen para la acción del lado del servidor
```javascript
xs.setImageInfo(imageGetActionUrl, imageAddByUploadActionUrl, imageAddByUrlActionUrl, imageCopyActionUrl, zindex, loadingGif);
// the parameters are:
	imageGetActionUrl: the get image action URL in the server side controller
	imageAddByUploadActionUrl: the upload image action  URL in the server side controller
	imageAddByUrlActionUrl: the add image from URL action  URL in the server side controller
	imageCopyActionUrl: the copy image action  URL in the server side controller
	zindex: the minimum zindex of the image in the canvas
	loadingGif (optional): the loading gif url when loading the image/shape .it is optional,the default value is:content/img/updating.gif
    for example: 
            const imageurl = "/GridJs2/imageurl";
            const imageuploadurl1 = "/GridJs2/AddImage";
            const imageuploadurl2 = "/GridJs2/AddImageByURL";
            const imagecopyurl = "/GridJs2/CopyImage";  
            const basiczorder = 5678;
    xs.setImageInfo(imageurl, imageuploadurl1, imageuploadurl2, imagecopyurl, basiczorder);
```

- establecer información para la operación de descarga para la acción del lado del servidor
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- establecer información para la operación de objeto OLE para la acción del lado del servidor
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
- establecer información para comprobación de sintaxis y corrección ortográfica para acción del lado del servidor
```javascript
xs.setSyntaxCheckUrl(checkUrl);
// the parameters are:
	checkUrl: the  syntax checking & spell correction operation action URL in the server side controller
    for example: 
            const checkurl = "/GridJs2/CheckSyntax";
            xs.setSyntaxCheckUrl(checkurl);
```

- establecer información para explicación de fórmulas para acción del lado del servidor
```javascript
xs.setFormulaExplainUrl(formulaExplainUrl);
// the parameters are:
	formulaExplainUrl: the  formula explanation  action URL in the server side controller
    for example: 
            const formulaExplainUrl = "/GridJs2/FormulaExplain";
            xs.setFormulaExplainUrl(formulaExplainUrl);
```


___
## otras API útiles
- Renderizar la vista
```javascript
xs.reRender()
```

- Obtener la identificación de la hoja activa
```javascript
xs.getActiveSheet()
```

- Añadir una hoja de cálculo nueva
```javascript
xs.addSheet(name,isactive,tabcolor,fontcolor)
// the parameters are:
	name:the sheet name
	isactive:whether set this sheet as active sheet
	tabcolor:the background color for the sheet in the tab bottom menu
	fontcolor:the font color for the sheet name in the tab bottom menu
   for example:
    xs.addSheet('hello',true,'#12ee5b','#2c5d3b')
```
- Modificar el nombre de la hoja
```javascript
xs.modifySheetName(oldName,newName)
// the parameters are:
	oldName:the sheet name
	newName:the new desired name
   for example:
     xs.modifySheetName('Sheet1','student');
```
- Eliminar la hoja
```javascript
xs.deleteSheet(name)
// the parameters is:
	name:the sheet name
   for example:
        xs.deleteSheet('Sheet1');

```

- establecer nivel de zoom
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

- establecer nombre de archivo 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```
- Establecer llamada de función antes de guardar 
```javascript
xs.setBeforeSaveFunction(func)
// the parameters is:
	func:This function is called before the save action. If it returns true, the save will proceed; otherwise, the save will not proceed.
   for example:
	xs.setBeforeSaveFunction(()=>{console.log('hello before save');return true;});
```

- Función de devolución de llamada para la función de envío de correo electrónico
```javascript
xs.setEmailSendCallFunction(callback)
// the parameters is:
	callback: the callback function to handle email sending, receives a mailObj parameter
		callback: function(mailObj) {
			// mailObj properties:
			// mailObj.receiver: the email address of the receiver, e.g., 'example@gmail.com'
			// mailObj.type: the format of the file to be sent, can be 'html', 'xlsx', or 'pdf'
		}
```

- si habilitar evento de tecla de ventana para GridJs
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

- desvincular todos los eventos adjuntos a GridJs, incluyendo el evento de tecla de ventana y el evento de cambio de tamaño de ventana.
```javascript
xs.destroy()
```

- Configurar los ajustes de colaboración en modo colaborativo, asegurarse de llamar a setCollaborativeSetting antes de setUniqueId  
```javascript
xs.setCollaborativeSetting(url,wsendpoint,wsapp,wsuser,wstopic)
    //the parameters are:
         url: the basic action URL in the server side controller to get history messages ,the default is '/GridJs2/msg'
	 wsendpoint: the websocket endpoint in the server side , the default is '/ws'
	 wsapp: the websocket destinations prefixed with "/app", the default is '/app/opr'
	 wsuser: the websocket for user-specific queues prefixed with "/usr", the default is '/user/queue'
	 wstopic: the websocket destinations prefixed with "/topic", the default is '/topic/opr'


```

- establecer filtro visible para imagen/forma
```javascript
xs.setVisibleFilter((sheet,s) =>{})
    //  to set a function which return true(for visible) or false(for invisible) for the visible filter with the below parameters :
	sheet:the sheet instance
	s:the image or shape instance
    for example: 
	//this will make visible for image/shape in sheet with name 'Sheet3' and 'Sheet1' except for the 'Rectangle' type
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet3'||sheet.data.name==='Sheet1') return s.type!=='Rectangle';  return false; })
	//this will make visible for image/shape in sheet with name  'Sheet1' 
		xs.setVisibleFilter((sheet,s) => { if (sheet.data.name==='Sheet1') return true;  return false; })
	//this will make invisible for image/shape in all sheets 
		xs.setVisibleFilter((sheet,s) => {  return false; })
	//if all the image/shape is already loaded and you want to change the visible filter at runtime,you can call the below code to trigger a reload for image/shape
		xs.reRender()
```

- Obtener la imagen/forma seleccionada, si no se selecciona nada devolverá nulo
```javascript
xs.sheet.selector.getObj()
```
- Mostrar u ocultar un nodo HTML en una posición de celda especificada
```javascript
xs.sheet.showHtmlAtCell(isShow, html, ri, ci, deltaX, deltaY)

    //the parameters are:
      isShow: Boolean value indicating whether to show or hide the HTML content.
      html: The HTML string to be displayed.
      ri: Row index of the target cell.
      ci: Column index of the target cell.
      deltaX: (Optional) Relative X-position adjustment from the top-left corner of the cell.
      deltaY: (Optional) Relative Y-position adjustment from the top-left corner of the cell.

    for example: 
    // Show HTML at cell A1
    xs.sheet.showHtmlAtCell(true, "<span>html span</span><input length='30' id='myinput'>test</input>", 0, 0);

    // Hide the HTML node
    xs.sheet.showHtmlAtCell(false);

    // Note: When an HTML node is shown, the default GridJS event handling is disabled to allow interaction with the HTML content.
    // This means you cannot select any cells or perform edit operations until the HTML node is hidden.
```

- Establecer el estado seleccionable para imagen/forma 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```


- Insertar filas
```javascript
xs.sheet.insertRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be inserted
```
- Insertar columnas 
```javascript
xs.sheet.insertColumns(start, n)
    // the parameters are:
	start: start column id
	n:how many columns will be inserted
```
- Eliminar filas 
```javascript
xs.sheet.deleteRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be deleted
```
- Eliminar columnas 
```javascript
xs.sheet.deleteColumns(start, n)
    // the parameters are:
	start: start column id 
	n:how many columns will be deleted
```
- Establecer el panel congelado
```javascript
xs.sheet.freeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
- Desfijar panel
```javascript
xs.sheet.freeze(0,0)
```

- Establecer rango editable/solo lectura
```javascript
xs.sheet.setEditableRange(range,isenable)
    // the parameters are:
	range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	isenable:when set to true,the range is editable.other wise,the range is readonly.
```

- Ocultar filas 
```javascript
xs.sheet.hideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

- Mostrar filas
```javascript
xs.sheet.unhideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

- Ocultar columnas 
```javascript
xs.sheet.hideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```

- Mostrar columnas
```javascript
xs.sheet.unhideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```


- Establecer la altura de la fila
```javascript
xs.sheet.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
- Establecer la altura de las filas
```javascript
xs.sheet.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

- Establecer la altura de todas las filas
```javascript
xs.sheet.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```

- Establecer el ancho de la columna
```javascript
xs.sheet.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
- Establecer el ancho de las columnas
```javascript
xs.sheet.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

- Establecer el ancho de todas las columnas
```javascript
xs.sheet.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

- Establecer el comentario en la celda
```javascript
xs.sheet.setComment(ri,ci,author,note)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
	author:the author for the comment
	note:the content for the comment
```

- Eliminar el comentario en la celda
```javascript
xs.sheet.removeComment(ri,ci)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
```


- Obtener el objeto de celda
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
- Establecer el valor de celda
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

- Obtener/Establecer el rango de celdas seleccionadas
```javascript
xs.sheet.data.selector.range
```
- Establecer el valor de celda para la celda seleccionada o el área de celdas
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- Establecer el estilo para la celda seleccionada o el área de celdas
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- Establecer el estilo para el área de celdas deseada
```javascript
xs.sheet.data.setRangeAttr(range,attributename,value)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
   for example:
        xs.sheet.data.setRangeAttr({sri:0,sci:0,eri:2,eci:2},'bgcolor','#11ee2a');
```


- Fusionar el área de celdas seleccionadas
```javascript
xs.sheet.data.merge()
```

- Separar la fusión del área de celdas seleccionadas
```javascript
xs.sheet.data.unmerge()
```
- Eliminar el contenido de la celda o borrar el estilo en la celda seleccionada  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```

- Eliminar el contenido de la celda o borrar el estilo en el área de celdas deseada
```javascript
xs.sheet.data.deleteRange(range,type)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```



- Obtener el ancho de la columna 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```



- Obtener la altura de la fila 
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

## Llamada de evento
-  Podemos rastrear los eventos a continuación
```javascript
 xs.on('cell-selected', (cell, ri, ci) => {
                console.log('cell selected:', cell, ', ri:', ri, ', ci:', ci);
                if (ci === -1) {
                    console.log('ci === -1 means a row selected ',ri);
                }
                if (ri === -1) {
                    console.log('ri === -1 means a column selected',ci);
                }
            }).on('cells-selected', (cell, range) => {
                console.log('range   selected:', cell, ', rang:', range);
            }).on('object-selected', (shapeOrImageObj) => {
                console.log('shape or image selected id:', shapeOrImageObj.id, ', type: ', shapeOrImageObj.type);
            }).on('sheet-selected', (id,name) => {
                console.log('sheet selected id:', id, ', name: ',name);
            }).on('sheet-loaded', (id,name) => {
                console.log('sheet load finished:', id, ', name: ',name);
            }).on('cell-edited', (text, ri, ci) => {
	        //just edit the cell
                console.log('text:', text, ', ri: ', ri, ', ci:', ci);
            }).on('cells-updated', (name, cells) => {
	       //cell value got updated
                console.log('cells updated for sheet name:', name);
                cells.forEach((acell, index, array) => {
                console.log('acell got updated:', acell);
            })
            }).on('cells-deleted', (range) => {
                console.log('cells deleted :', range);
            }).on('rows-deleted', (ri, n) => {
                console.log('rows-deleted :', ri, ",size", n);

            }).on('columns-deleted', (ci, n) => {
                console.log('columns-deleted :', ci, ",size", n);

            }).on('rows-inserted', (ri, n) => {
                console.log('rows-inserted :', ri, ",size", n);

            }).on('columns-inserted', (ci, n) => {
                console.log('columns-inserted :', ci, ",size", n);

            });
```
- Evento de pre-verificación
  si devuelve false, la operación de inserción/eliminación no continuará.
```javascript
  xs.checkRowInsert = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnInsert = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
  xs.checkRowDelete = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnDelete = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
```

## Personalización

-  Establecer ícono de inicio y enlace
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
-  Mostrar la barra de menú
```javascript
xs.sheet.menubar.show()
```

-  Ocultar la barra de menú
```javascript
xs.sheet.menubar.hide()
```
## APIs para objeto de forma
- Cambiar color de fondo para el objeto de forma
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 existed,this will set the background color to Yellow 
     const ashape=xs.sheet.data.shapes[0];
     ashape.setBackgroundColor('#FFFF00');
```

## APIs para el objeto TextBox
TextBox es un tipo especial de forma cuya propiedad de tipo es:"TextBox"
por ejemplo: el código a continuación mostrará qué forma es cuadro de texto

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

- Aplicar configuraciones de fuente para el objeto de cuadro de texto
```javascript
    setFont(fontsettings)
    // the parameter is:
        fontsettings:   {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00', 'italic':true} ,the properties are 'name', 'size', 'bold', 'color', 'italic',they are all optional.
    //for example,we assume shape 0 is a textbox object,this will set the font color to Yellow ,and font size to 12pt,and bold the font. 
     const textbox=xs.sheet.data.shapes[0];
     const fontsettings= {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00'}; 
     textbox.setFont(fontsettings);
```
- Cambiar automáticamente el color de fondo y el color del texto para obtener un efecto visual activo
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

- Ocultar/mostrar el contenido de texto en el objeto de cuadro de texto
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```

para información detallada, puede consultar el ejemplo aquí
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs>





