---
title: Arbeta med GridJs Highlight-funktion
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/highlight/
description: Den här artikeln beskriver hur du använder GridJs för att markera celltext, cellintervall, former och bilder.
keywords: highlight, highlight spreadsheet
---
# Arbeta med GridJs Highlight-funktion
 Vi stöder nedanstående JS API:er för Highlight-funktionen


- Aktivera markering och Ange markeringsstil, alla markerings-API:er kommer att påverka först efter att markeringsstilen har ställts in
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- Inaktivera markering
```javascript
xs.hideHighlights()
```
- Lägg till celltext för att markera
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Ta bort markering för celltext i array
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

-  Få array för markering för celltext
```javascript
xs.sheet.getHighlightTexts()
```

- Lägg till cellintervall för att markera
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Ta bort markering för cellintervall i array
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Få array för markering för cellintervall
```javascript
xs.sheet.getHighlightRanges()
```

- Ställ in cellintervallet på invers markering
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Ta bort markering för inversmarkering
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Få omvänt markeringscellintervall
```javascript
xs.sheet.getHighlightInverseRange()
```


- Lägg till form för att markera array
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Ta bort markeringsformen i arrayen
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Få array för högdagerform
```javascript
xs.sheet.getHighlightShaps()
```


- Lägg till bild för att markera array
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Ta bort markerad bild i arrayen
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Skaffa array för högdagerbild
```javascript
xs.sheet.getHighlightImages()
```

-  ställ in om du vill markera alla kalkylblad, inkludera alla former och bilder
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- ställ in anpassad bildmarkeringsfunktion
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

Du kan hitta mer på vår github-demosida https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
