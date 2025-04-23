---
title: Arbeiten mit GridJs auf der Clientseite
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/
keywords: GridJs,benutzerdefiniert,Logo,Einstellungen,API,JS API,Client API
description: Dieser Artikel stellt die Client JavaScript APIs oder Funktionen in GridJs vor.
aliases:
  - /java/aspose-cells-gridjs/client/
  - /java/aspose-cells-gridjs/work-with-client-api/
  - /java/aspose-cells-gridjs/use-js-api/
  - /java/aspose-cells-gridjs/gridjs-spreadsheet-api/
  - /java/aspose-cells-gridjs/client-api/
  - /java/aspose-cells-gridjs/js-api/
  - /java/aspose-cells-gridjs/javascript-api/
---

# Arbeiten mit GridJs auf der Clientseite
Wir haben GridJs auf der Clientseite basierend auf [x-spreadsheet](https://github.com/myliang/x-spreadsheet) entwickelt.

## Die Hauptschritte sind:

- Erstellen einer x_spreadsheet-Instanz
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
Die Parameter für Laden-Optionen:

| Parameter | Beschreibung | Standardwert | Optional |
| --- | --- | --- | --- |
| `allowSelectTextInTextBoxInReadMode` | Ob die Textauswahl in TextBox-Steuerelementen im Lesemodus erlaubt ist.<br>Der Standardwert ist false. | `false` | Ja |
| `checkSyntax` | Ob die Syntaxprüfung und Rechtschreibkorrektur für die Benutzereingabe für Textinhalte durchgeführt wird.<br>Funktioniert mit setSyntaxCheckUrl.<br>Der Standardwert ist false. | `false` | Ja |
| `loadingGif` | Die URL des Lade-GIFs beim Laden von Bildern/Shapes.<br>Der Standardwert ist content/img/updating.gif. | `content/img/updating.gif` | Ja |
| `local` | Legen Sie Lokalisierungsinformationen für Menüs & Symbolleisten fest, die mehrere Sprachen unterstützen.<br>Mögliche Werte sind:<br>- `en, zh, es, pt, de, ru, nl` (für Englisch, Chinesisch, Spanisch, Portugiesisch, Deutsch, Russisch, Niederländisch)<br>- `ar, fr, id, it, ja` (für Arabisch, Französisch, Indonesisch, Italienisch, Japanisch)<br>- `ko, th, tr, vi, cht` (für Koreanisch, Thailändisch, Türkisch, Vietnamesisch, Traditionelles Chinesisch) | `en` | Ja |
| `mode` | Kann `read` oder `edit` sein; `read` bedeutet eine nur lesbare Tabelle; `edit` bedeutet, dass die Tabelle bearbeitet werden kann. | Keine | Nein |
| `searchHighlightColor` | Die Hervorhebungsfarbe für den Suchbegriff.<br>Die Farbe muss einen Alpha-Kanal für Transparenz enthalten. | `#dbe71338` | Ja |
| `showCheckSyntaxButton` | Ob die Schaltflächen für Syntaxprüfung & Rechtschreibkorrektur in der Symbolleiste angezeigt werden.<br>Der Standardwert ist false. | `false` | Ja |
| `showContextmenu` | Ob das Kontextmenü beim Rechtsklick auf eine Zelle angezeigt wird.<br>Der Standardwert ist true. | `true` | Ja |
| `showFileName` | Ob der Dateiname angezeigt wird. | `true` | Ja |
| `showFormulaExplain` | Ob ob Formelerklärungen angezeigt werden, wenn die Maus über die Zelle bewegt wird.<br>Arbeitet zusammen mit setFormulaExplainUrl.<br>Der Standardwert ist falsch. | `falsch` | Ja |
| `showFormulaTip` | Ob die vorhandene Formel angezeigt wird, wenn die Maus über die Zelle bewegt wird.<br>Der Standardwert ist falsch. | `falsch` | Ja |
| `showNonEditableSymbolInCell` | Ob ein clientseitiges Nicht-Bearbeitbar-Symbol in der Zelle angezeigt wird.<br>Wenn auf true gesetzt, zeigt die ausgewählte Fläche nach Klick auf das Kontextmenü "Bearbeitung deaktivieren" das Symbol.<br>Der Standardwert ist falsch. | `falsch` | Ja |
| `showToolbar` | Ob die Leiste angezeigt wird. | `wahr` | Ja |
| `updateMode` | Unterstützt derzeit nur `server`. | `server` | Nein |
| `updateUrl` | Legt die serverseitige URL für Update-Aktionen anhand von JSON fest. | Keine | Nein |
| `view` | Legt die Ansichtgröße für das Blatt fest, z.B. `{width: () => 1000, height: () => 500}`. | `{width: () => dokument.documentElement.clientWidth, height: () => dokument.documentElement.clientHeight}` | Ja |

- Laden mit JSON-Daten
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
- Aktives Blatt nach Blattnamen festlegen
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
- Aktives Blatt nach ID festlegen
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

- Aktive Zelle festlegen
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

- Für mehrere Instanzen aktiv setzen 
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

- Informationen für Form/Bilder-Bearbeitung für serverseitige Aktion festlegen
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

- Informationen für Download-Bearbeitung für serverseitige Aktion festlegen
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller

    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- Informationen für OLE-Objekt-Bearbeitung für serverseitige Aktion festlegen
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
- Informationen für Syntaxprüfung & Rechtschreibkorrektur für serverseitige Aktionen setzen
```javascript
xs.setSyntaxCheckUrl(checkUrl);
// the parameters are:
	checkUrl: the  syntax checking & spell correction operation action URL in the server side controller
    for example: 
            const checkurl = "/GridJs2/CheckSyntax";
            xs.setSyntaxCheckUrl(checkurl);
```

- Informationen zur Formelerklärung für serverseitige Aktionen setzen
```javascript
xs.setFormulaExplainUrl(formulaExplainUrl);
// the parameters are:
	formulaExplainUrl: the  formula explanation  action URL in the server side controller
    for example: 
            const formulaExplainUrl = "/GridJs2/FormulaExplain";
            xs.setFormulaExplainUrl(formulaExplainUrl);
```


___
## Weitere nützliche APIs
- Die Ansicht rendern
```javascript
xs.reRender()
```

-  Aktuelle Blatt-ID abrufen
```javascript
xs.getActiveSheet()
```

-  Zoom-Ebene festlegen
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

-  Dateiname festlegen 
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```

- Rückruffunktion für die E-Mail-Versandfunktion
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

-  Einstellen, ob Fenstertastenereignisse für GridJs aktiviert sein sollen
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

-  Alle Ereignisse von GridJs lösen, einschließlich der Fenstertastenereignisse und der Ereignisse zur Änderung der Fenstergröße, aufheben
```javascript
xs.destroy()
```


-  Sichtbaren Filter für Bild/Form festlegen
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

-  Ausgewähltes Bild/Form abrufen, falls nichts ausgewählt ist, wird null zurückgegeben
```javascript
xs.sheet.selector.getObj()
```
- HTML-Knoten an einer bestimmten Zellenposition anzeigen oder verbergen
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

- Den auswählbaren Zustand für Bild/Shape festlegen 
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```

-  Objektzelle abrufen
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Zellenstil abrufen
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Zellenwert festlegen
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

-  Auswählen/Festlegen des ausgewählten Zellenbereichs
```javascript
xs.sheet.data.selector.range
```
-  Zellenwert für die ausgewählte Zelle oder Zellbereich festlegen
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
-  Stil für die ausgewählte Zelle oder Zellbereich festlegen
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

-  Zellenbereich zusammenführen
```javascript
xs.sheet.data.merge()
```

-  Zellenbereich trennen
```javascript
xs.sheet.data.unmerge()
```
-  Ausgewählte Zelle löschen  
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
-  Fensterbereich fixieren
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```

-  Zeile oder Spalten an der ausgewählten Zelle einfügen  
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
	type: row | column
	n:the row or column number
```
-  Zeile oder Spalten an der ausgewählten Zelle löschen  
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
	type: row | column
```

- Legen Sie die Breite für die Spalte fest
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
- Legen Sie die Breite für die Spalten fest
```javascript
xs.sheet.data.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

- Legen Sie die Breite für alle Spalten fest
```javascript
xs.sheet.data.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

- Holen Sie sich die Breite für die Spalte 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```

- Legen Sie die Höhe für die Zeile fest
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
- Legen Sie die Höhe für die Zeilen fest
```javascript
xs.sheet.data.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

- Legen Sie die Höhe für alle Zeilen fest
```javascript
xs.sheet.data.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```


- Holen Sie sich die Höhe für die Zeile 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

- Get/Set die Anzeigerichtung
```javascript
xs.sheet.data.displayRight2Left
```

## Ereignisrückruf
-  Wir können die folgenden Ereignisse verfolgen
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
- Pre-Check-Ereignis
  Wenn Rückgabewert falsch, wird die Einfüge-/Löschoperation nicht fortgesetzt.
```javascript
  xs.checkRowInsert = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnInsert = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
  xs.checkRowDelete = (ri, size) => { if (ri % 2 == 1) return true; else return false; };
  xs.checkColumnDelete = (ci, size) => { if (ci % 2 == 1) return true; else return false; };
```

## Anpassung

-  Home-Symbol und Link festlegen
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
-  Menüleiste anzeigen
```javascript
xs.sheet.menubar.show()
```

-  Menüleiste ausblenden
```javascript
xs.sheet.menubar.hide()
```


## APIs für TextBox-Objekte
TextBox ist eine spezielle Art von Form, bei der die Eigenschaft "TextBox" ist :"TextBox",
zum Beispiel: Der nachstehende Code zeigt, welche Form ein Textfeld ist

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

- Hintergrundfarbe für Textfeldobjekt ändern
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
- Automatische Änderung der Hintergrundfarbe und Textfarbe für einen visuellen aktiven Effekt
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  Textinhalt im Textfeldobjekt ausblenden/einblenden
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```

Für ausführlichere Informationen können Sie hier das Beispiel überprüfen
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>





