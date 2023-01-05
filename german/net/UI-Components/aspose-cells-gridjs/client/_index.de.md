---
title: Arbeiten mit GridJs Client-Seite
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/client/
---
# Arbeiten mit GridJs Client-Seite
Wir haben GridJs Client basierend auf entwickelt[x-Tabelle](https://github.com/myliang/x-spreadsheet).

## Die wichtigsten Schritte sind:

- x_spreadsheet-Instanz erstellen
```javascript
xs = x_spreadsheet(id, options)
```
- json-Daten laden
```javascript
xs.loadData(jsondata.data)
```
- Aktives Blatt setzen
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
- Aktive Zelle setzen
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

Der folgende Code zum Beispiel initiert ein x_spreadsheet-Objekt.
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
 // die Parameter für Optionen:
 updateMode: derzeit unterstützen wir nur 'server'
 updateUrl: Legen Sie die serverseitige URL für die Aktualisierungsaktion basierend auf JSON fest
 Modus: Lesen bedeutet schreibgeschützte Tabellenkalkulation/Bearbeiten bedeutet, dass wir die Tabellenkalkulation bearbeiten können
 showToolbar: bedeutet, ob die Symbolleiste angezeigt werden soll
 showFileName: ob der Dateiname angezeigt werden soll
 local: unterstützt mehrere Sprachen für Menüs, das Gebietsschema kann sein: en, cn, es, pt, de, ru, nl für Englisch, Chinesisch, Spanisch, Portugiesisch, Deutschland, Russisch, Niederländisch
 showContextmenu: bedeutet, ob das Kontextmenü beim Rechtsklick auf eine Zelle angezeigt werden soll
## 

___
## andere nützliche APIs
- Rendern Sie die Ansicht
```javascript
xs.reRender()
```
- Ausgewähltes Bild/Form abrufen��wenn nichts ausgewählt wird, wird null zurückgegeben
```javascript
xs.sheet.selector.getObj()
```

- Holen Sie sich das Zellobjekt
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Holen Sie sich den Zellenstil
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
- Legen Sie den Zellenwert fest
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

- Abrufen/Setzen des ausgewählten Zellbereichs
```javascript
xs.sheet.data.selector.range
```
- Legen Sie den Zellenwert für die ausgewählte Zelle oder den ausgewählten Zellenbereich fest
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
- Legen Sie den Stil für die ausgewählte Zelle oder den Zellbereich fest
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

- Ausgewählten Zellbereich zusammenführen
```javascript
xs.sheet.data.merge()
```

- Trennen Sie den ausgewählten Zellbereich
```javascript
xs.sheet.data.unmerge()
```
-  Löschen Sie die ausgewählte Zelle
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
- Stellen Sie das Einfrierfenster ein
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

-  Zeile oder Spalten in der ausgewählten Zelle einfügen
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
-  Zeile oder Spalten in der ausgewählten Zelle löschen
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
-  Holen Sie sich die Breite für die Spalte
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
-  Holen Sie sich die Höhe für die Zeile
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
- Abrufen/Setzen der Anzeigerichtung
```javascript
xs.sheet.data.displayRight2Left
```



Für Detailinformationen können Sie das Beispiel hier überprüfen
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
