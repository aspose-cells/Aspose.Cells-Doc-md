---
title: Lavorare con GridJs lato client
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/client/
---
# Lavorare con GridJs lato client
Abbiamo sviluppato il client GridJs basato su[foglio di calcolo x](https://github.com/myliang/x-spreadsheet).

## i passaggi principali sono:

- crea un'istanza x_spreadsheet
```javascript
xs = x_spreadsheet(id, options)
```
- caricare i dati json
```javascript
xs.loadData(jsondata.data)
```
- imposta foglio attivo
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- imposta la cella attiva
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

ad esempio il codice seguente avvia un oggetto x_spreadsheet.
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
 // i parametri per le opzioni:
 updateMode: attualmente supportiamo solo 'server'
 updateUrl: imposta l'URL lato server per l'azione di aggiornamento basata su json
 modalità: leggi significa foglio di calcolo di sola lettura/modifica significa che possiamo modificare il foglio di calcolo
 showToolbar: indica se mostrare la barra degli strumenti
 showFileName: se mostrare il nome del file
 locale: supporta più lingue per i menu, le impostazioni locali possono essere: en, cn, es, pt, de, ru, nl per inglese, cinese, spagnolo, portoghese, germania, russo, olandese
 showContextmenu: indica se mostrare il menu contestuale al clic destro su una cella
## 

___
## altre API utili
- Renderizza la vista
```javascript
xs.reRender()
```
- Ottieni immagine/forma selezionata��se non viene selezionata alcuna selezione restituirà null
```javascript
xs.sheet.selector.getObj()
```

- Ottieni l'oggetto cella
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Ottieni lo stile della cella
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Imposta il valore della cella
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- Ottieni/Imposta l'intervallo di celle selezionato
```javascript
xs.sheet.data.selector.range
```
- Impostare il valore della cella per la cella o l'area della cella selezionata
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- Imposta lo stile per la cella o l'area della cella selezionata
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- Unisci l'area della cella selezionata
```javascript
xs.sheet.data.merge()
```

- Separa l'area della cella selezionata
```javascript
xs.sheet.data.unmerge()
```
-  Elimina la cella selezionata
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- Imposta il riquadro di blocco
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

-  Inserisci righe o colonne nella cella selezionata
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
-  Elimina righe o colonne nella cella selezionata
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

- Imposta la larghezza della colonna
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
-  Ottieni la larghezza della colonna
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

- Imposta l'altezza della riga
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
-  Ottieni l'altezza per la riga
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- Ottieni/Imposta la direzione del display
```javascript
xs.sheet.data.displayRight2Left
```



per informazioni dettagliate, puoi controllare l'esempio qui
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
