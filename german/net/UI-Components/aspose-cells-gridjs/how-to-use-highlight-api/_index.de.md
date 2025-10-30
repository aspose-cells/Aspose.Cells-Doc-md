---
title: Arbeiten mit der GridJs Hervorhebungs Funktion
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/how-to-use-highlight-api/
description: Dieser Artikel beschreibt, wie die Hervorhebung von Zellentext, Zellbereichen, Formen und Bildern in GridJs verwendet wird.
keywords: GridJs, Hervorhebung, Hervorhebungstabelle, Schwärzung, Bemerkungen
aliases:
  - /net/aspose-cells-gridjs/highlight/
  - /net/aspose-cells-gridjs/how-to-highlight/
  - /net/aspose-cells-gridjs/work-with-highlight-api/
  - /net/aspose-cells-gridjs/work-with-highlight-apis/
---

# Arbeiten mit der GridJs-Hervorhebungs-Funktion 
Wir unterstützen die folgenden JS-APIs für die Hervorhebungs-Funktion 


- Hervorhebung aktivieren und Hervorhebungsstil festlegen, alle Hervorhebungs-APIs werden erst wirksam, nachdem der Hervorhebungsstil im aktiven Arbeitsblatt festgelegt wurde 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  Aktualisieren Sie den Hervorhebungsstil im aktiven Arbeitsblatt 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


-  Deaktivieren Sie die Hervorhebung im aktiven Arbeitsblatt    
```javascript
xs.sheet.hideHighlights()
```
-  Zelltext zur Hervorhebung im aktiven Arbeitsblatt hinzufügen 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Hervorhebung für Zelltext in Array im aktiven Arbeitsblatt entfernen 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

-  Array für Hervorhebung von Zelltext im aktiven Arbeitsblatt abrufen   
```javascript
xs.sheet.getHighlightTexts()
```

-  Zellbereich zur Hervorhebung im aktiven Arbeitsblatt hinzufügen 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Hervorhebung für Zellbereich in Array im aktiven Arbeitsblatt entfernen 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Array für Hervorhebung von Zellbereichen im aktiven Arbeitsblatt abrufen   
```javascript
xs.sheet.getHighlightRanges()
```

-  Zellbereich für inverses Hervorheben im aktiven Arbeitsblatt festlegen 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Hervorhebung für inverses Hervorheben im aktiven Arbeitsblatt entfernen 
```javascript
xs.sheet.removeHighlightInverseRange()

```

-  Inverse Hervorhebung für Zellbereich im aktiven Arbeitsblatt abrufen 
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Form zur Hervorhebung im Array im aktiven Arbeitsblatt hinzufügen 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Hervorhebungsform im Array im aktiven Arbeitsblatt entfernen 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Array für Hervorhebungsform im aktiven Arbeitsblatt abrufen  
```javascript
xs.sheet.getHighlightShaps()
```

-  Textfeld zur Hervorhebung im Textfeld hinzufügen, das ein spezieller Typ Formular ist und dessen Typ-Eigenschaft: "TextBox", im aktiven Arbeitsblatt 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  Hervorhebungsbereich im Textfeld entfernen, das ein spezieller Typ Formular ist und dessen Typ-Eigenschaft: "TextBox", im aktiven Arbeitsblatt 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Bild zum Hervorhebungsarray im aktiven Arbeitsblatt hinzufügen 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Hervorhebungsbild im Array im aktiven Arbeitsblatt entfernen 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Array für Hervorhebungsbild im aktiven Arbeitsblatt abrufen  
```javascript
xs.sheet.getHighlightImages()
```

- Legen Sie fest, ob alle Objekte im aktiven Arbeitsblatt markiert werden sollen, einschließlich aller Formen und Bilder sowie des gesamten Arbeitsblattbereichs.
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- Funktion zum Festlegen eines benutzerdefinierten Bild-Highlights
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

- Löschen Sie die Markierungseinstellung für das aktive Arbeitsblatt.
```javascript
xs.sheet.clearHighlights()

```

### Highlight für Textfeldobjekt
Textfeld ist eine spezielle Art von Form, dessen Typ-Eigenschaft ist: "TextBox"
zum Beispiel: Der nachstehende Code zeigt, welche Form ein Textfeld ist

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- Highlight für Textfeldobjekt hinzufügen
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

- Highlight für Textfeldobjekt entfernen 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- Highlight für Textfeldobjekt abrufen 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




Mehr finden Sie auf unserer github-Demo-Seite https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
