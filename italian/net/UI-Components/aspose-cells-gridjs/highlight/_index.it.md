---
title: Lavorare con la funzione Highlight di GridJ
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/highlight/
description: Questo articolo descrive come utilizzare GridJs per evidenziare il testo della cella, gli intervalli di celle, le forme e le immagini.
keywords: highlight, highlight spreadsheet
---
# Lavorare con la funzione Highlight di GridJ
 Supportiamo le seguenti API JS per la funzione Highlight


- Abilita l'evidenziazione e imposta lo stile di evidenziazione, tutte le API di evidenziazione avranno effetto solo dopo aver impostato lo stile di evidenziazione
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- Disabilita l'evidenziazione
```javascript
xs.hideHighlights()
```
- Aggiungi il testo della cella da evidenziare
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Rimuovi l'evidenziazione per il testo della cella nell'array
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

-  Ottieni matrice per l'evidenziazione per il testo della cella
```javascript
xs.sheet.getHighlightTexts()
```

- Aggiungi l'intervallo di celle da evidenziare
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Rimuovi l'evidenziazione per l'intervallo di celle nell'array
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Ottieni l'array per l'evidenziazione dell'intervallo di celle
```javascript
xs.sheet.getHighlightRanges()
```

- Imposta l'intervallo di celle sull'evidenziazione inversa
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

- Rimuovi l'evidenziazione per l'evidenziazione inversa
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Ottieni l'intervallo di celle di evidenziazione inverso
```javascript
xs.sheet.getHighlightInverseRange()
```


- Aggiungi forma per evidenziare la matrice
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Rimuovi la forma di evidenziazione nell'array
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Ottieni l'array per la forma evidenziata
```javascript
xs.sheet.getHighlightShaps()
```


- Aggiungi un'immagine per evidenziare l'array
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Rimuovi l'immagine evidenziata nell'array
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Ottieni l'array per l'immagine evidenziata
```javascript
xs.sheet.getHighlightImages()
```

-  impostare se evidenziare tutto il foglio di lavoro, includere tutte le forme e le immagini
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- imposta la funzione di evidenziazione dell'immagine personalizzata
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

Puoi trovare di più nella nostra pagina demo github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
