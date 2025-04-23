---
title: Работа с GridJs на стороне клиента
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/
keywords: GridJs,кастом,логотип,настройка,api,js API,клиентский API
description: В этой статье представлены клиентские javascript API или функции в GridJs.
aliases:
  - /net/aspose-cells-gridjs/client/
  - /net/aspose-cells-gridjs/work-with-client-api/
  - /net/aspose-cells-gridjs/use-js-api/
  - /net/aspose-cells-gridjs/gridjs-spreadsheet-api/
  - /net/aspose-cells-gridjs/client-api/
  - /net/aspose-cells-gridjs/js-api/
  - /net/aspose-cells-gridjs/javascript-api/
---

# Работа с GridJs на стороне клиента
Мы разработали клиент GridJs на основе [x-spreadsheet](https://github.com/myliang/x-spreadsheet).

## Основные этапы:

- создать экземпляр x_spreadsheet
```javascript
xs = x_spreadsheet(id, options)
    // the parameters are:
    id: the html node id ,for example :'#gridjs-demo' for the html  <div id="gridjs-demo"></div>
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
 параметры для опций загрузки:

| Параметр | Описание | Значение по умолчанию | Необязательный |
| --- | --- | --- | --- |
| `allowSelectTextInTextBoxInReadMode` | Разрешать ли выделение текста в элементах TextBox в режиме чтения.<br>Значение по умолчанию — false. | `false` | Да |
| `checkSyntax` | Выполнять ли проверку синтаксиса и исправление орфографии для пользовательского ввода текста.<br>Работает с setSyntaxCheckUrl.<br>Значение по умолчанию — false. | `false` | Да |
| `loadingGif` | URL GIF-изображения загрузки при загрузке изображений/форм.<br>Значение по умолчанию — content/img/updating.gif. | `content/img/updating.gif` | Да |
| `local` | Установка локализации для меню и панелей инструментов, поддержка нескольких языков.<br>Возможные значения включают:<br>- `en, zh, es, pt, de, ru, nl` (для английского, китайского, испанского, португальского, немецкого, русского, нидерландского)<br>- `ar, fr, id, it, ja` (для арабского, французского, индонезийского, итальянского, японского)<br>- `ko, th, tr, vi, cht` (для корейского, тайского, турецкого, вьетнамского, традиционного китайского) | `en` | Да |
| `mode` | Может быть `read` или `edit`; `read` означает только для чтения; `edit` — лист можно редактировать. | Нет | Нет |
| `searchHighlightColor` | Цвет подсветки для поискового термина.<br>Цвет должен включать канал альфа для прозрачности. | `#dbe71338` | Да |
| `showCheckSyntaxButton` | Показывать ли кнопку проверки синтаксиса и исправления орфографии на панели инструментов.<br>Значение по умолчанию — false. | `false` | Да |
| `showContextmenu` | Показывать ли контекстное меню при правом клике по ячейке.<br>Значение по умолчанию — true. | `true` | Да |
| `showFileName` | Показывать ли имя файла. | `true` | Да |
| `showFormulaExplain` | Показывать объяснения формул, применённые к этой ячейке, при наведении мыши.<br>Работает вместе с setFormulaExplainUrl.<br>Значение по умолчанию — false. | `false` | Да |
| `showFormulaTip` | Показывать существующую формулу, применённую к этой ячейке, при наведении мыши.<br>Значение по умолчанию — false. | `false` | Да |
| `showNonEditableSymbolInCell` | Показывать символ, обозначающий несценарий в ячейке.<br>Если установлено на true, после нажатия правой кнопкой мыши на "Disable editing", выбранная область, исключённая из редактирования, покажет этот символ.<br>Значение по умолчанию — false. | `false` | Да |
| `showToolbar` | Показывать панель инструментов. | `true` | Да |
| `updateMode` | В настоящее время поддерживается только `server`. | `server` | Нет |
| `updateUrl` | Установите URL-адрес серверной стороны для обновлений на основе JSON. | Нет | Нет |
| `view` | Установите размер вида для листа, например, `{width: () => 1000, height: ()=> 500}`. | `{width: () => document.documentElement.clientWidth, height: () => document.documentElement.clientHeight }` | Да |

- загрузить данные в формате json
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
- установить активный лист по имени листа
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
-  установить активный лист по идентификатору
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

-  установить активную ячейку
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

- устанавливать активным для нескольких экземпляров 
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

- установить информацию для операции над формами/изображениями на серверной стороне
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

- установить информацию для операции загрузки на серверной стороне
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- установить информацию для операции с объектом OLE на серверной стороне
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
- задавать информацию для проверки синтаксиса и исправления орфографических ошибок для серверных действий
```javascript
xs.setSyntaxCheckUrl(checkUrl);
// the parameters are:
	checkUrl: the  syntax checking & spell correction operation action URL in the server side controller
    for example: 
            const checkurl = "/GridJs2/CheckSyntax";
            xs.setSyntaxCheckUrl(checkurl);
```

- задавать информацию для объяснения формулы для серверных действий
```javascript
xs.setFormulaExplainUrl(formulaExplainUrl);
// the parameters are:
	formulaExplainUrl: the  formula explanation  action URL in the server side controller
    for example: 
            const formulaExplainUrl = "/GridJs2/FormulaExplain";
            xs.setFormulaExplainUrl(formulaExplainUrl);
```


___
## другие полезные API
-  Отрисовать вид
```javascript
xs.reRender()
```

-  получить идентификатор активного листа
```javascript
xs.getActiveSheet()
```

-   Установить уровень масштабирования
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

-   Установить имя файла 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```

- Функция обратного вызова для функции отправки электронной почты.
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

-   разрешить обработку клавиш окна для GridJs
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

-  отвязать все события, привязанные к GridJs, включая событие клавиш окна и изменение размера окна.
```javascript
xs.destroy()
```


-  установить видимый фильтр для изображения/формы
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

-  Получить выбранное изображение/форму, если ничего не выбрано, вернуть null
```javascript
xs.sheet.selector.getObj()
```
- отображать или скрывать HTML-элемент в указанной ячейке
```javascript
xs.sheet.showHtmlAtCell(isShow, html, ri, ci, deltaX, deltaY)

    //the parameters are:
    // - isShow: Boolean value indicating whether to show or hide the HTML content.
    // - html: The HTML string to be displayed.
    // - ri: Row index of the target cell.
    // - ci: Column index of the target cell.
    // - deltaX: (Optional) Relative X-position adjustment from the top-left corner of the cell.
    // - deltaY: (Optional) Relative Y-position adjustment from the top-left corner of the cell.

    // Example usage:
    // Show HTML at cell A1
    xs.sheet.showHtmlAtCell(true, "<span>html span</span><input length='30' id='myinput'>test</input>", 0, 0);

    // Hide the HTML node
    xs.sheet.showHtmlAtCell(false);

    // Note: When an HTML node is shown, the default GridJS event handling is disabled to allow interaction with the HTML content.
    // This means you cannot select any cells or perform edit operations until the HTML node is hidden.
```

- устанавливать состояние выбора для изображения/фигуры 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```

-  Получить объект ячейки
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Получить стиль ячейки
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Установить значение ячейки
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

-  Получить/установить выбранный диапазон ячеек
```javascript
xs.sheet.data.selector.range
```
-  Установить значение ячейки для выбранной ячейки или области ячеек
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
-  Установить стиль для выбранной ячейки или области ячеек
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

-  Объединить выбранную область ячеек
```javascript
xs.sheet.data.merge()
```

-  Разъединить выбранную область ячеек
```javascript
xs.sheet.data.unmerge()
```
-  Удалить выбранную ячейку  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
-  Закрепить область
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```

-  Вставить строку или столбцы в выбранную ячейку  
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
	type: row | column
	n:the row or column number
```
-  Удалить строку или столбцы в выбранной ячейке  
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
	type: row | column
```

-  Установить ширину столбца
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
-  Установить ширину столбцов
```javascript
xs.sheet.data.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

-  Установить ширину для всех столбцов
```javascript
xs.sheet.data.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

-  Получить ширину столбца 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```

-  Установить высоту строки
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
-  Установить высоту строк
```javascript
xs.sheet.data.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

-  Установить высоту для всех строк
```javascript
xs.sheet.data.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```


-  Получить высоту строки 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

-  Получить/установить направление отображения
```javascript
xs.sheet.data.displayRight2Left
```

## Обратный вызов события
-  Мы можем отслеживать следующие события
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
- предварительное событие проверки
  если возвращает false, операция вставки/удаления не продолжится.
```javascript
  xs.checkRowInsert = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnInsert = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
  xs.checkRowDelete = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnDelete = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
```

## Настройка

-  Установить значок домой и ссылку
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
-  Показать панель меню
```javascript
xs.sheet.menubar.show()
```

-  Скрыть панель меню
```javascript
xs.sheet.menubar.hide()
```


## API для объекта TextBox
TextBox - это особый вид формы, свойство типа которой: "TextBox",
например: нижеприведенный код покажет, какая форма является текстовым полем

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

- Изменить цвет фона для объекта текстового поля
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
- Автоматически изменить цвет фона и цвет текста для получения визуального активного эффекта
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  Скрыть/показать текстовое содержимое в объекте текстового поля
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```

для подробной информации вы можете посмотреть пример здесь
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>





