---
title: Arbeiten mit der Highlight-Funktion von GridJ
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/highlight/
description: Dieser Artikel beschreibt, wie Sie GridJs verwenden, um Zelltext, Zellbereiche, Formen und Bilder hervorzuheben.
keywords: highlight, highlight spreadsheet
---
# Arbeiten mit der Highlight-Funktion von GridJ
 Wir unterstützen die folgenden JS-APIs für die Highlight-Funktion


- Hervorhebung aktivieren und Hervorhebungsstil festlegen, alle Hervorhebungs-APIs werden erst wirksam, nachdem der Hervorhebungsstil festgelegt wurde
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- Hervorhebung deaktivieren
```javascript
xs.hideHighlights()
```
- Fügen Sie Zellentext zum Hervorheben hinzu
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Hervorhebung für Zellentext im Array entfernen
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

-  Holen Sie sich ein Array für die Hervorhebung von Zellentext
```javascript
xs.sheet.getHighlightTexts()
```

- Zellbereich zum Hervorheben hinzufügen
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Hervorhebung für Zellbereich im Array entfernen
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Holen Sie sich ein Array für die Hervorhebung des Zellbereichs
```javascript
xs.sheet.getHighlightRanges()
```

- Stellen Sie den Zellbereich auf die invertierte Hervorhebung ein
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Hervorhebung für inverse Hervorhebung entfernen
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Holen Sie sich den inversen Hervorhebungszellenbereich
```javascript
xs.sheet.getHighlightInverseRange()
```


- Form hinzufügen, um Array hervorzuheben
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Entfernen Sie die Hervorhebungsform im Array
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Holen Sie sich ein Array für die Hervorhebungsform
```javascript
xs.sheet.getHighlightShaps()
```


- Bild zum Highlight-Array hinzufügen
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Hervorgehobenes Bild im Array entfernen
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Holen Sie sich ein Array für das Hervorhebungsbild
```javascript
xs.sheet.getHighlightImages()
```

-  Legen Sie fest, ob alle Arbeitsblätter hervorgehoben werden sollen, einschließlich aller Formen und Bilder
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- Stellen Sie die benutzerdefinierte Bildhervorhebungsfunktion ein
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

Weitere Informationen finden Sie auf unserer Github-Demoseite https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
