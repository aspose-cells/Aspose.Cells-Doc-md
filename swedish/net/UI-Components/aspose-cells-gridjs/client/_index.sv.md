---
title: Arbeta med GridJs klientsida
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/client/
keywords: custom,logo,setting,api
---
#  Arbeta med GridJs klientsida
 Vi utvecklade GridJs klient baserat på[x-kalkylblad](https://github.com/myliang/x-spreadsheet).

##  huvudstegen är:

- skapa x_spreadsheet-instans
```javascript
xs = x_spreadsheet(id, options)
    // the parameters are:
    id:the html node id ,for example :'#gridjs-demo' for the html  <div id="gridjs-demo"></div>
    options:the load options,
     // the parameters for options:
	    updateMode:  currently we only support 'server'
	    updateUrl:  set the server side  url for update action based on json
		view: set the view size for the sheet,for example `{width: () => 1000, height: ()=> 500}`
	    mode: read means readonly spread sheet/edit means we can edit the spread sheet
            allowSelectTextInTextBoxInReadMode: whether allow select text in TextBox control when in read mode,the default value is false
	    showToolbar:   means whether to show toolbar
	    showFileName:  whether to show the filename 
	    local:         support multiple language for menus ,the locale can be:
	                        en, cn, es, pt, de, ru, nl, 
	                   for  English,Chinese,Spanish,Portuguese,German,Russian,Dutch
			        ar, fr,id,it,ja
                           for  Arabic,French,Indonesian,Italian,Japanese
			        ko,th,tr,vi,cht
                           for  Korean,Thai,Turkey,Vietnamese,Traditional Chinese                  
	    showContextmenu:   means whether to show contextmenu on right click on a cell
            loadingGif:  the loading gif url when loading the image/shape .it is optional,the default value is:content/img/updating.gif
	for example the below code init a x_spreadsheet object.
	xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
			showContextmenu: true
			})
```
    
-  ladda med json-data
```javascript
xs.loadData(data)
// the parameters is:
	data: the json data which describ the data structure for the worksheets
```
-  ställ in aktivt ark efter arknamn
```javascript
xs.setActiveSheetByName(sheetname)
// the parameters is:
	sheetname: the sheet name 
```
-  ställ in aktivt ark efter id
```javascript
xs.setActiveSheet(id)
// the parameters is:
	sheetname: the sheet id 
```

-  ställ in aktiv cell
```javascript
xs.setActiveCell(row,col);
// the parameters are:
	row: the cell row
	col: the cell column
```

- ställ in information för form-/bildoperation för åtgärd på serversidan
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

- ställ in information för nedladdningsoperation för åtgärd på serversidan
```javascript
xs.setFileDownloadInfo(downloadActionUrl);
// the parameters are:
	downloadActionUrl: the get download file action URL in the server side controller
	 
    for example: 
            const fileDownloadUrl = "/GridJs2/Download";
            xs.setFileDownloadInfo(fileDownloadUrl);
```

- ställ in info för ole-objektoperation för serversidans åtgärd
```javascript
xs.setOleDownloadInfo(oleActionUrl);
// the parameters are:
	oleActionUrl: the ole object file action URL in the server side controller
    for example: 
            const oleDownloadUrl = "/GridJs2/Ole";
            xs.setOleDownloadInfo(oleDownloadUrl);
```
  

_
##  andra användbara apis
-  Återge vyn
```javascript
xs.reRender()
```

-  få aktivt ark-id
```javascript
xs.getActiveSheet()
```

-  Ställ in zoomnivå
```javascript
xs.setZoomLevel(zoom)
// the parameters is:
	zoom:the zoom level ,can be number ,for example 0.5 for zoom out, or 2 for zoom in
```

-  Ställ in filnamn
```javascript
xs.setFileName(name)
// the parameters is:
	name:the file name with extension ,for example trip.xlsx
```

- om fönsternyckelhändelse ska aktiveras för GridJs
```javascript
xs.enableKeyEvent(isenable)
// the parameters is:
	isenable:whether the window key event is active for GridJs
//when has other controls in the same page, you may want to ignore the key event in GridJs 
```

-  avbind alla händelser kopplade till GridJs, inklusive fönsternyckelhändelse och fönsterstorlekshändelse.
```javascript
xs.destroy()
```


-  ställ in synligt filter för bild/form
```javascript
    // need to set a function which return true(for visible) or false(for invisible) for the visible filter with the below parameters :
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
		xs.setActiveSheet(xs.getActiveSheet())
```

-  Hämta den valda bilden/formen, om inget välj kommer att returnera null
```javascript
xs.sheet.selector.getObj()
```

-  ställ in det valbara tillståndet för bild/form
```javascript
const shape=xs.sheet.selector.getObj();
shape.setControlable(isenable)
     // the parameter is:
      isenable: when set to true,the image or shape can be selectable and movable/resizeable
```

-  Hämta cellobjektet
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Få cellstilen
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```
-  Ställ in cellvärdet
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
	ri:row index 
	ci:column index
	value:the cell value
	state: input | finished ,if finished ,it will do update action to servside
```

-  Hämta/ställ in det valda cellintervallet
```javascript
xs.sheet.data.selector.range
```
-  Ställ in cellvärdet för den markerade cellen eller cellområdet
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
-  Ställ in stilen för den markerade cellen eller cellområdet
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
	attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

-  Slå samman det markerade cellområdet
```javascript
xs.sheet.data.merge()
```

-  Ta bort det markerade cellområdet
```javascript
xs.sheet.data.unmerge()
```
-  Ta bort den markerade cellen
```javascript
xs.sheet.data.deleteCell(type)
    // the parameters are:
	type:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
-  Ställ in frysrutan
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
	ri:row index 
	ci:column index
```

-  Infoga rad eller kolumner vid den markerade cellen
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
	type: row | column
	n:the row or column number
```
-  Ta bort rad eller kolumner vid den markerade cellen
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
	type: row | column
```

-  Ställ in bredden för kolumnen
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
	ci:column index
	width:the width for the column
```
-  Ställ in bredden för kolumnerna
```javascript
xs.sheet.data.setColsWidth(sci,eci,width)
    // the parameters are:
	sci:the start column index
	eci:the end column index
	width:the width for the column
```

-  Ställ in bredden för alla kolumner
```javascript
xs.sheet.data.setAllColsWidth(width)
    // the parameters are:
	width:the width for the columns
```

-  Hämta bredden för kolumnen
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
	min:the start column index
	max:the end column index,not include
```

-  Ställ in höjden för raden
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
	ri:row index
	height:the height for the row
```
-  Ställ in höjden för raderna
```javascript
xs.sheet.data.setRowsHeight(sri,eri,height)
    // the parameters are:
	sri:start row index
	eri:end row index
	height:the height for the rows
```

- Ställ in höjden för alla rader
```javascript
xs.sheet.data.setAllRowsHeight(height)
    // the parameters are:
	height:the height for the rows
```


-  Få höjden för raden
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
	min:the start row index
	max:the end row index,not include
```

-  Hämta/ställ in visningsriktningen
```javascript
xs.sheet.data.displayRight2Left
```

##  evenemangsuppringning
-  vi kan spåra händelserna nedan
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
                console.log('text:', text, ', ri: ', ri, ', ci:', ci);
            });
```

##  anpassning

-  ställ in hemikon och länk
```javascript
xs.sheet.menubar.icon.setHomeIcon(iconUrl,targetUrl)
    // the parameters are:
	iconUrl:the home icon URL
	targetUrl:the target link URL
	for example ,the below code will set the new logo and with link to google.com
	xs.sheet.menubar.icon.setHomeIcon('https://forum.aspose.com/letter_avatar_proxy/v4/letter/y/3e96dc/45.png','https://www.google.com')
```
-  visa menyraden
```javascript
xs.sheet.menubar.show()
```

-  dölj menyraden
```javascript
xs.sheet.menubar.hide()
```


för detaljerad information kan du kolla exemplet här
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
