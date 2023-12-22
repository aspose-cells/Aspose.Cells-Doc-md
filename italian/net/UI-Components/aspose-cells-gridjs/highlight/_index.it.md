---
title: Lavorare con la funzione Evidenzia di GridJ
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/highlight/
description: Questo articolo descrive come utilizzare GridJs per evidenziare il testo delle celle, gli intervalli di celle, le forme e le immagini.
keywords: highlight, highlight spreadsheet,redaction,remarks
---
#  Lavorare con la funzione Evidenzia di GridJ
 Supportiamo le seguenti API JS per la funzione Evidenzia


-  Abilita evidenziazione e Imposta stile di evidenziazione, tutte le API di evidenziazione avranno effetto solo dopo aver impostato lo stile di evidenziazione nel foglio di lavoro attivo
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  aggiorna lo stile di evidenziazione impostato nel foglio di lavoro attivo
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


-  Disabilita l'evidenziazione nel foglio di lavoro attivo
```javascript
xs.sheet.hideHighlights()
```
-  Aggiungi il testo della cella da evidenziare nel foglio di lavoro attivo
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Rimuovi l'evidenziazione per il testo della cella nell'array nel foglio di lavoro attivo
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

-  Aggiungi l'intervallo di celle da evidenziare nel foglio di lavoro attivo
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Rimuovi l'evidenziazione per l'intervallo di celle nella matrice nel foglio di lavoro attivo
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Ottieni la matrice per l'evidenziazione dell'intervallo di celle nel foglio di lavoro attivo
```javascript
xs.sheet.getHighlightRanges()
```

-  Imposta l'intervallo di celle sull'evidenziazione inversa nel foglio di lavoro attivo
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Rimuovi l'evidenziazione per l'evidenziazione inversa nel foglio di lavoro attivo
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Ottieni l'intervallo di celle di evidenziazione inversa nel foglio di lavoro attivo
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Aggiungi forma per evidenziare l'array nel foglio di lavoro attivo
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Rimuovi la forma evidenziata nella matrice nel foglio di lavoro attivo
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Ottieni l'array per la forma evidenziata nel foglio di lavoro attivo
```javascript
xs.sheet.getHighlightShaps()
```

-  Aggiungi la casella di testo per evidenziare, la casella di testo è un tipo speciale di forma la cui proprietà di tipo è: "TextBox", nel foglio di lavoro attivo
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  Rimuovi l'intervallo di evidenziazione nella casella di testo, la casella di testo è un tipo speciale di forma la cui proprietà di tipo è: "TextBox", nel foglio di lavoro attivo
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Aggiungi un'immagine per evidenziare l'array nel foglio di lavoro attivo
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Rimuovi l'immagine evidenziata nell'array nel foglio di lavoro attivo
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Ottieni l'array per l'immagine evidenziata
```javascript
xs.sheet.getHighlightImages()
```

-  imposta se evidenziare tutti gli oggetti nel foglio di lavoro attivo, includere tutte le forme e le immagini e tutta l'area del foglio di lavoro
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Imposta la funzione di evidenziazione dell'immagine personalizzata
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

-  cancellare l'impostazione di evidenziazione per il foglio di lavoro attivo
```javascript
xs.sheet.clearHighlights()

```

###  Evidenzia per l'oggetto casella di testo
textbox è un tipo speciale di forma la cui proprietà di tipo è: "TextBox",
ad esempio: il codice seguente mostrerà quale forma è la casella di testo

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  Aggiungi evidenziazione per l'oggetto casella di testo
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

-  Rimuovi l'evidenziazione per l'oggetto casella di testo
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  Ottieni l'evidenziazione per l'oggetto casella di testo
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  Cambia il colore di sfondo per l'oggetto casella di testo
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  Cambia automaticamente il colore dello sfondo e il colore del testo per ottenere un effetto visivo attivo
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  nascondere/mostrare il contenuto del testo nell'oggetto casella di testo
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



Puoi trovare di più nella nostra pagina demo di Github https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
