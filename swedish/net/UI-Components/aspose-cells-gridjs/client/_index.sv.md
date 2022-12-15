---
title: Arbeta med GridJs klientsida
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/client/
---
# Arbeta med GridJs klientsida
Vi utvecklade GridJs klient baserat på[x-kalkylblad](https://github.com/myliang/x-spreadsheet).

## huvudstegen är:

- skapa x_spreadsheet-instans
```javascript
xs = x_spreadsheet(id, options)
```
- ladda json-data
```javascript
xs.loadData(jsondata.data)
```
- ställ in aktivt ark
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- ställ in aktiv cell
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

till exempel koden nedan init ett x_spreadsheet-objekt.
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
 // parametrarna för alternativ:
 updateMode: för närvarande stöder vi bara 'server'
 updateUrl: ställ in webbadressen på serversidan för uppdateringsåtgärd baserat på json
 läge: läs betyder skrivskyddat kalkylblad/redigera betyder att vi kan redigera kalkylarket
 showToolbar: betyder om verktygsfältet ska visas
 showFileName: om filnamnet ska visas
 lokalt: stöder flera språk för menyer, språket kan vara: en, cn, es, pt, de, ru, nl för engelska, kinesiska, spanska, portugisiska, tyskland, ryska, holländska
 showContextmenu: betyder om man vill visa sammanhangsmenyn vid högerklick på en cell
## 

___
## andra användbara apis
- Återge vyn
```javascript
xs.reRender()
```
- Hämta vald bild/form��om inget valt kommer att returnera null
```javascript
xs.sheet.selector.getObj()
```

- Hämta cellobjektet
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Få cellstilen
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Ställ in cellvärdet
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- Hämta/ställ in det valda cellintervallet
```javascript
xs.sheet.data.selector.range
```
- Ställ in cellvärdet för den markerade cellen eller cellområdet
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- Ställ in stilen för den markerade cellen eller cellområdet
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- Slå samman det markerade cellområdet
```javascript
xs.sheet.data.merge()
```

- Ta bort det markerade cellområdet
```javascript
xs.sheet.data.unmerge()
```
-  Ta bort den markerade cellen
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- Ställ in frysrutan
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

- Ställ in bredden för kolumnen
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
-  Få bredden för kolumnen
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- Ställ in höjden för raden
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
-  Få höjden för raden
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- Hämta/ställ in visningsriktningen
```javascript
xs.sheet.data.displayRight2Left
```



för detaljerad information kan du kolla exemplet här
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
