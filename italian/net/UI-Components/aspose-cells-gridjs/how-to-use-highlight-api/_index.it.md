---
title: Lavorare con la funzionalità di evidenziazione di GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/how-to-use-highlight-api/
description: Questo articolo descrive come utilizzare l evidenziazione sul testo della cella, sugli intervalli delle celle, sulle forme e sulle immagini in GridJs.
keywords: GridJs, evidenzia, foglio di calcolo evidenziato, redazione, osservazioni
aliases:
  - /net/aspose-cells-gridjs/highlight/
  - /net/aspose-cells-gridjs/how-to-highlight/
  - /net/aspose-cells-gridjs/work-with-highlight-api/
  - /net/aspose-cells-gridjs/work-with-highlight-apis/
---

# Lavorare con la funzionalità di evidenziazione di GridJs 
Supportiamo le seguenti API JS per la funzionalità di evidenziazione 


- Abilitare l'evidenziazione e impostare lo stile di evidenziazione, tutte le API di evidenziazione avranno effetto solo dopo che lo stile di evidenziazione è impostato nel foglio di lavoro attivo 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- Aggiornare lo stile di evidenziazione impostato nel foglio di lavoro attivo 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- Disabilita l'evidenziazione nel foglio di lavoro attivo    
```javascript
xs.sheet.hideHighlights()
```
- Aggiungi il testo della cella da evidenziare nel foglio di lavoro attivo 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- Rimuovi l'evidenziazione per il testo della cella in array nel foglio di lavoro attivo 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Ottieni l'array per l'evidenziazione del testo della cella nel foglio di lavoro attivo   
```javascript
xs.sheet.getHighlightTexts()
```

- Aggiungi l'intervallo di celle da evidenziare nel foglio di lavoro attivo 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Rimuovi l'evidenziazione per l'intervallo di celle nell'array nel foglio di lavoro attivo 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Ottieni l'array per l'evidenziazione dell'intervallo di celle nel foglio di lavoro attivo   
```javascript
xs.sheet.getHighlightRanges()
```

- Imposta l'intervallo di celle da evidenziare in modo inverso nel foglio di lavoro attivo 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Rimuovi l'evidenziazione per l'evidenziazione inversa nel foglio di lavoro attivo 
```javascript
xs.sheet.removeHighlightInverseRange()

```

- Ottieni l'intervallo di evidenziazione inversa delle celle nel foglio di lavoro attivo 
```javascript
xs.sheet.getHighlightInverseRange()
```


- Aggiungi la forma all'array di evidenziazione nel foglio di lavoro attivo 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Rimuovi la forma di evidenziazione nell'array nel foglio di lavoro attivo 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Ottenere array per evidenziare la forma nel foglio di lavoro attivo  
```javascript
xs.sheet.getHighlightShaps()
```

-  Aggiungi casella di testo per evidenziare, la casella di testo è un tipo speciale di forma il cui tipo di proprietà è: "TextBox", nel foglio di lavoro attivo 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  Rimuovi intervallo evidenziazione nella casella di testo, la casella di testo è un tipo speciale di forma il cui tipo di proprietà è: "TextBox", nel foglio di lavoro attivo 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Aggiungi immagine per evidenziare l'array nel foglio di lavoro attivo 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Rimuovi immagine di evidenziazione nell'array nel foglio di lavoro attivo 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Ottieni array per evidenziare immagine  
```javascript
xs.sheet.getHighlightImages()
```

-  Imposta se evidenziare tutti gli oggetti nel foglio di lavoro attivo, inclusi tutte le forme e immagini e tutta l'area del foglio di lavoro
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Imposta la funzione di evidenziazione immagine personalizzata
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

-  Cancella impostazione di evidenziazione per il foglio di lavoro attivo
```javascript
xs.sheet.clearHighlights()

```

### Evidenziazione per oggetto casella di testo
la casella di testo è un tipo speciale di forma il cui tipo di proprietà è: "TextBox",
ad esempio: il codice seguente mostrerà quale forma è la casella di testo

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  Aggiungi evidenziazione per oggetto casella di testo
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

-  Rimuovi evidenziazione per oggetto casella di testo 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  Ottieni evidenziatura per oggetto casella di testo 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




Puoi trovare altro nella nostra pagina demo github https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
