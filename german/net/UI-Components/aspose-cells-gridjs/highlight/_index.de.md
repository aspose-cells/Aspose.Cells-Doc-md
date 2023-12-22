---
title: Arbeiten mit der Highlight-Funktion von GridJ
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/highlight/
description: In diesem Artikel wird beschrieben, wie Sie GridJs verwenden, um Zellentext, Zellbereiche, Formen und Bilder hervorzuheben.
keywords: highlight, highlight spreadsheet,redaction,remarks
---
#  Arbeiten mit der Highlight-Funktion von GridJ
 Wir unterstützen die folgenden JS-APIs für die Hervorhebungsfunktion


-  Aktivieren Sie die Hervorhebung und legen Sie den Hervorhebungsstil fest. Alle Hervorhebungs-APIs werden erst wirksam, nachdem der Hervorhebungsstil im aktiven Arbeitsblatt festgelegt wurde
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  Aktualisieren Sie den im aktiven Arbeitsblatt festgelegten Hervorhebungsstil
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
-  Fügen Sie Zelltext hinzu, um ihn im aktiven Arbeitsblatt hervorzuheben
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Entfernen Sie die Hervorhebung für Zellentext im Array im aktiven Arbeitsblatt
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Rufen Sie ein Array zur Hervorhebung des Zellentexts im aktiven Arbeitsblatt ab
```javascript
xs.sheet.getHighlightTexts()
```

-  Fügen Sie den Zellbereich hinzu, um ihn im aktiven Arbeitsblatt hervorzuheben
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Entfernen Sie die Hervorhebung des Zellbereichs im Array im aktiven Arbeitsblatt
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Rufen Sie das Array zur Hervorhebung des Zellbereichs im aktiven Arbeitsblatt ab
```javascript
xs.sheet.getHighlightRanges()
```

-  Stellen Sie den Zellbereich so ein, dass die Hervorhebung im aktiven Arbeitsblatt umgekehrt wird
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Entfernen Sie die Hervorhebung, um die Hervorhebung im aktiven Arbeitsblatt umzukehren
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Holen Sie sich den inversen Hervorhebungszellenbereich im aktiven Arbeitsblatt
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Fügen Sie eine Form hinzu, um das Array im aktiven Arbeitsblatt hervorzuheben
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

-  Rufen Sie das Array für die Hervorhebungsform im aktiven Arbeitsblatt ab
```javascript
xs.sheet.getHighlightShaps()
```

-  Fügen Sie ein Textfeld zur Hervorhebung hinzu. Das Textfeld ist eine spezielle Art von Form, deren Typeigenschaft „TextBox“ im aktiven Arbeitsblatt ist
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  Entfernen Sie den Hervorhebungsbereich im Textfeld. Das Textfeld ist eine spezielle Art von Form, deren Typeigenschaft im aktiven Arbeitsblatt „TextBox“ lautet
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Fügen Sie ein Bild hinzu, um das Array im aktiven Arbeitsblatt hervorzuheben
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Hervorhebungsbild im Array im aktiven Arbeitsblatt entfernen
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Array für Hervorhebungsbild abrufen
```javascript
xs.sheet.getHighlightImages()
```

-  Legen Sie fest, ob alle Objekte im aktiven Arbeitsblatt, einschließlich aller Formen und Bilder sowie des gesamten Arbeitsblattbereichs, hervorgehoben werden sollen
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Stellen Sie eine benutzerdefinierte Bildhervorhebungsfunktion ein
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

-  klare Hervorhebungseinstellung für das aktive Arbeitsblatt
```javascript
xs.sheet.clearHighlights()

```

###  Hervorhebung für Textfeldobjekt
Textbox ist eine besondere Art von Form, deren Typeigenschaft „TextBox“ lautet.
Beispiel: Der folgende Code zeigt, welche Form ein Textfeld ist

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  Hervorhebung für Textfeldobjekt hinzufügen
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

-  Hervorhebung für Textfeldobjekt entfernen
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  Hervorhebung für Textfeldobjekt abrufen
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  Hintergrundfarbe für Textfeldobjekt ändern
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  Ändern Sie automatisch die Hintergrund- und Textfarbe, um einen visuell aktiven Effekt zu erzielen
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  Blendet den Textinhalt im Textfeldobjekt ein/aus
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



Weitere Informationen finden Sie auf unserer Github-Demoseite https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
