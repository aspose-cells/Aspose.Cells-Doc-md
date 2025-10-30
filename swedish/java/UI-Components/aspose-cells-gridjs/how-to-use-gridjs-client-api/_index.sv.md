---
title: Arbeta med GridJs klient sidan
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/
keywords: GridJs, anpassad, logotyp, inställningar, API, JS API, klient API
description: Den här artikeln introducerar klientens javascript API er eller funktioner i GridJs.
aliases:
  - /java/aspose-cells-gridjs/client/
  - /java/aspose-cells-gridjs/work-with-client-api/
  - /java/aspose-cells-gridjs/use-js-api/
  - /java/aspose-cells-gridjs/gridjs-spreadsheet-api/
  - /java/aspose-cells-gridjs/client-api/
  - /java/aspose-cells-gridjs/js-api/
  - /java/aspose-cells-gridjs/javascript-api/
---

# Arbeta med GridJs klient-sidan
Vi utvecklade GridJs klienten baserat på [x-spreadsheet](https://github.com/myliang/x-spreadsheet).

## De huvudsakliga stegen är:

- skapa x_spreadsheet-instans
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
Parametrarna för laddningsalternativ:

| Parameter | Beskrivning | Standardvärde | Valfri |
| --- | --- | --- | --- |
| `allowSelectTextInTextBoxInReadMode` | Tillåta markerings av text i TextBox-kontroller i läs-läge.<br>Standardvärdet är falskt. | `false` | Ja |
| `checkSyntax` | Utföra syntaxkontroll och stavningskorrigering för användarens inmatning av textinnehåll.<br>Fungerar tillsammans med setSyntaxCheckUrl.<br>Standardvärdet är falskt. | `false` | Ja |
| `loadingGif` | URL för laddnings-GIF när bilder/former laddas.<br>Standardvärdet är content/img/updating.gif. | `content/img/updating.gif` | Ja |
| `local` | Ange lokaliseringsinfo för menyer och verktygsfält, stödjer flera språk.<br>Möjliga värden inkluderar:<br>- `en, zh, es, pt, de, ru, nl` (för engelska, kinesiska, spanska, portugisiska, tyska, ryska, nederländska)<br>- `ar, fr, id, it, ja` (för arabiska, franska, indonesiska, italienska, japanska)<br>- `ko, th, tr, vi, cht` (för koreanska, thailändska, turkiska, vietnamesiska, traditionell kinesiska) | `en` | Ja |
| `mode` | Kan vara `read` eller `edit`; `read` betyder ett skrivskyddat kalkylblad; `edit` betyder att kalkylbladet kan redigeras. | Ingen | Nej |
| `isCollaborative` | Behöver stödja samarbetsläge . | `false` | Ja |
| `searchHighlightColor` | Belysningsfärg för söktermen.<br;Färgen måste inkludera en alfa-kanal för transparens. | `#dbe71338` | Ja |
| `showCheckSyntaxButton` | Visa knappar för syntaxkontroll & stavningskorrigering i verktygsfältet.<br>Standardvärdet är falskt. | `false` | Ja |
| `showContextmenu` | Visa kontextmenyn vid högerklick på en cell.<br>Standardvärdet är sant. | `true` | Ja |
| `showFileName` | Visa filnamnet. | `true` | Ja |
| `showFormulaExplain` | Visa forklaring av formler tillämpade på denna cell när musen flyttas över den.<br>Fungerar tillsammans med setFormulaExplainUrl.<br>Standardvärdet är falskt. | `false` | Ja |
| `showFormulaTip` | Om formeln som är tillämpad på denna cell ska visas när musen flyttas över den.<br>Standardvärdet är falskt. | `false` | Ja |
| `showNonEditableSymbolInCell` | Om en klient-sida icke-redigerbar symbol ska visas i cellen.<br>Om satt till sant, efter att ha klickat på högerklickskontextmenyn "Inaktivera redigering", visas symbolen i det avlästa området.<br>Standardvärdet är falskt. | `false` | Ja |
| `showToolbar` | Om verktygsfältet ska visas. | `true` | Ja |
| `updateMode` | För närvarande stöds endast `server`. | `server` | Nej |
| `updateUrl` | Sätt server-URL för uppdateringsåtgärder baserade på JSON. | Ingen | Nej |
| `view` | Ange vistsstorleken för bladet, t.ex., `{width: () => 1000, height: ()=> 500}`. | `{width: () => dokument.documentElement.clientWidth, height: () => dokument.documentElement.clientHeight }` | Ja |
| `token` | Ange autentiseringstoken. När token inte är null kommer `Authorization: Bearer {token}`-huvudet automatiskt läggas till i förfrågningshuvudet. Du kan använda `xs.refreshToken(token)` för att ange ett nytt token. | Ingen | Ja |    
| `showBottombarStats` | Vill du visa statistik för bottenfältet.<br>Standardvärdet är sant. | `true` | Ja |   
| `showRowAppenderToolbar` | Vill du visa verktygsfält för batchrads-appendare.<br>Standardvärdet är sant. | `true` | Ja |   

- ladda med json-data
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
- ställ in aktivt blad med bladnamnet
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
- ställ in aktivt blad med ID
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

- ställ in aktiv cell
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

-  ställ in aktiv för flera instanser 
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
- ställ in anpassad toast
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

- ange information för form-/bildoperationer för server-sidan
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

- ange information för nerladdningsoperationer för server-sidan
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- ange information för ole-objektoperationer för server-sidan
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
- ställ in info för syntaxkontroll & stavningskorrektionsåtgärd för server-sidan
```javascript
xs.setSyntaxCheckUrl(checkUrl);
// the parameters are:
	checkUrl: the  syntax checking & spell correction operation action URL in the server side controller
    for example: 
            const checkurl = "/GridJs2/CheckSyntax";
            xs.setSyntaxCheckUrl(checkurl);
```

- ställ in info för formelförklaring för server-sidan
```javascript
xs.setFormulaExplainUrl(formulaExplainUrl);
// the parameters are:
	formulaExplainUrl: the  formula explanation  action URL in the server side controller
    for example: 
            const formulaExplainUrl = "/GridJs2/FormulaExplain";
            xs.setFormulaExplainUrl(formulaExplainUrl);
```


___
## andra användbara API:er
- Rendera vyn
```javascript
xs.reRender()
```

-  Hämta aktivt blad-ID
```javascript
xs.getActiveSheet()
```

-  Lägg till ett nytt kalkylblad
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
-  Ändra bladnamnet
```javascript
xs.modifySheetName(oldName,newName)
// the parameters are:
	oldName:the sheet name
	newName:the new desired name
   for example:
     xs.modifySheetName('Sheet1','student');
```
- Ta bort bladet
```javascript
xs.deleteSheet(name)
// the parameters is:
	name:the sheet name
   for example:
        xs.deleteSheet('Sheet1');

```

- Ställ in zoomnivå
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

- Ställ in filnamn 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```
-  Ställ in funktionsanrop före spara 
```javascript
xs.setBeforeSaveFunction(func)
// the parameters is:
	func:This function is called before the save action. If it returns true, the save will proceed; otherwise, the save will not proceed.
   for example:
	xs.setBeforeSaveFunction(()=>{console.log('hello before save');return true;});
```

- Callback-funktion för e-postutskick
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

- om fönstertangentbordshändelser ska aktiveras för GridJs
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

- avlänka alla händelser som är kopplade till GridJs, inklusive fönstertangentbordshändelse och fönsterändringhändelse
```javascript
xs.destroy()
```

-  konfigurera de samarbetsinställningar i samarbetsläge, se till att setCollaborativeSetting innan setUniqueId  
```javascript
xs.setCollaborativeSetting(url,wsendpoint,wsapp,wsuser,wstopic)
    //the parameters are:
         url: the basic action URL in the server side controller to get history messages ,the default is '/GridJs2/msg'
	 wsendpoint: the websocket endpoint in the server side , the default is '/ws'
	 wsapp: the websocket destinations prefixed with "/app", the default is '/app/opr'
	 wsuser: the websocket for user-specific queues prefixed with "/usr", the default is '/user/queue'
	 wstopic: the websocket destinations prefixed with "/topic", the default is '/topic/opr'


```

- ställ in synligt filter för bild/form
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

- Hämta den valda bilden/formen, om inget är valt returneras null
```javascript
xs.sheet.selector.getObj()
```
-  Visa eller dölja ett HTML-element vid en angiven cellposition
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

-  Sätt det valbara tillståndet för bild/form 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```


-  Infoga rader
```javascript
xs.sheet.insertRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be inserted
```
-  Infoga kolumner 
```javascript
xs.sheet.insertColumns(start, n)
    // the parameters are:
	start: start column id
	n:how many columns will be inserted
```
-  Ta bort rader 
```javascript
xs.sheet.deleteRows(start, n)
    // the parameters are:
	start: start row id 
	n:how many rows will be deleted
```
-  Ta bort kolumner 
```javascript
xs.sheet.deleteColumns(start, n)
    // the parameters are:
	start: start column id 
	n:how many columns will be deleted
```
-  Ange frysfönstret
```javascript
xs.sheet.freeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
- Frysa inte panelen
```javascript
xs.sheet.freeze(0,0)
```

-  Ställ in redigerbart/skrivt skyddat område
```javascript
xs.sheet.setEditableRange(range,isenable)
    // the parameters are:
	range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	isenable:when set to true,the range is editable.other wise,the range is readonly.
```

-  Dölj rader 
```javascript
xs.sheet.hideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

-  Visa rader igen
```javascript
xs.sheet.unhideRows(sri,eri)
    // the parameters are:
	sri:the start row index 
	eri:the end row index
```

-  Dölj kolumner 
```javascript
xs.sheet.hideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```

-  Visa kolumner igen
```javascript
xs.sheet.unhideColumns(sci,eci)
    // the parameters are:
	sci:the start column index 
	eci:the end column index
```


-  Ange höjden för raden
```javascript
xs.sheet.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
-  Ange höjden för raderna
```javascript
xs.sheet.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

-  Ange höjden för alla rader
```javascript
xs.sheet.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```

-  Ange bredden för kolumnen
```javascript
xs.sheet.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
-  Ange bredden för kolumnerna
```javascript
xs.sheet.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

-  Ange bredden för alla kolumner
```javascript
xs.sheet.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

-  Sätt kommentaren i cellen
```javascript
xs.sheet.setComment(ri,ci,author,note)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
	author:the author for the comment
	note:the content for the comment
```

-  Ta bort kommentaren i cellen
```javascript
xs.sheet.removeComment(ri,ci)
    // the parameters are:
	ri:row index of the cell
	ci:column index of the cell
```


-  Hämta cellobjektet
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Hämta cellstilen
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Ange cellvärdet
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

-  Få / Ange det valda cellområdet
```javascript
xs.sheet.data.selector.range
```
-  Ange cellvärdet för den valda cellen eller cellområdet
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
-  Ange stilen för den valda cellen eller cellområdet
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

-  Sätt stil för det önskade cellområdet
```javascript
xs.sheet.data.setRangeAttr(range,attributename,value)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
   for example:
        xs.sheet.data.setRangeAttr({sri:0,sci:0,eri:2,eci:2},'bgcolor','#11ee2a');
```


-  Sammanfoga det valda cellområdet
```javascript
xs.sheet.data.merge()
```

-  Avbryt sammanslagningen av det valda cellområdet
```javascript
xs.sheet.data.unmerge()
```
-  Ta bort cellinnehåll eller rensa stilen i vald cell  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```

-  Ta bort cellinnehåll eller rensa stilen i det önskade cellområdet
```javascript
xs.sheet.data.deleteRange(range,type)
    // the parameters are:
        range:the cell range ,etc. {sri:0,sci:0,eri:2,eci:2} reprensents range start from cell A1 to C3
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```



-  Få bredden för kolumnen 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```



-  Få höjden för raden 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

-  Få / Ange visningsriktningen
```javascript
xs.sheet.data.displayRight2Left
```

## Händelseåteranrop
-  Vi kan spåra nedanstående händelser
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
- Förhandsgranskning av händelse
  Om returnerar falskt, kommer inte insättnings-/raderingsoperationen att fortsätta.
```javascript
  xs.checkRowInsert = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnInsert = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
  xs.checkRowDelete = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnDelete = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
```

## Anpassning

-  Ange hemikon och länk
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
-  Visa menyraden
```javascript
xs.sheet.menubar.show()
```

-  Dölj menyraden
```javascript
xs.sheet.menubar.hide()
```
## API:er för formobjekt
-  Ändra bakgrundsfärg för formobjekt
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 existed,this will set the background color to Yellow 
     const ashape=xs.sheet.data.shapes[0];
     ashape.setBackgroundColor('#FFFF00');
```

## API:er för TextBox-objekt
TextBox är en speciell typ av form där typen är: "TextBox",
till exempel: koden nedan kommer att visa vilken form som är textrutan

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

- Tillämpa typsnittinställningar för textruteföremål
```javascript
    setFont(fontsettings)
    // the parameter is:
        fontsettings:   {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00', 'italic':true} ,the properties are 'name', 'size', 'bold', 'color', 'italic',they are all optional.
    //for example,we assume shape 0 is a textbox object,this will set the font color to Yellow ,and font size to 12pt,and bold the font. 
     const textbox=xs.sheet.data.shapes[0];
     const fontsettings= {'name':'Arial', 'size':12, 'bold':true, 'color':'#FFFF00'}; 
     textbox.setFont(fontsettings);
```
-  Autoändra bakgrundsfärg och textfärg för att få en visuell aktiv effekt
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  Dölj/visad textinnehåll i textbox-objektet
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```

för detaljerad information kan du kolla exemplet här
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs>





