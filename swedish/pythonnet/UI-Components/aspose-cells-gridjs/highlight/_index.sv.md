---
title: Arbetar med GridJs Markera funktion
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/highlight/
description: Denna artikel beskriver hur man använder GridJs för att markera celltext, cellområden, former och bilder.
keywords: markera, kalkylblad, sekretess, anmärkningar, excel, kommentar	
---

# Arbeta med GridJs Markera funktion 
Vi stöder följande JS-API:er för markeringsegenskapen 


- Aktivera markering och Ange markeringstil, alla markering-API:er kommer endast att ha effekt efter att markeringstilen har ställts in i den aktiva arbetsbladet 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

- Uppdatera markeringstilen som ställts in i den aktiva arbetsbladet 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


- Inaktivera markering på den aktiva arbetsbladet    
```javascript
xs.sheet.hideHighlights()
```
- Lägg till celltext för markeringen på den aktiva arbetsbladet 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

- Ta bort markering för celltext i arrayen på den aktiva arbetsbladet 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Hämta array för markering av celltext på den aktiva arbetsbladet   
```javascript
xs.sheet.getHighlightTexts()
```

- Lägg till cellintervall för markering på den aktiva arbetsbladet 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Ta bort markering för cellintervall i arrayen på den aktiva arbetsbladet 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Hämta array för markering av cellintervall på den aktiva arbetsbladet   
```javascript
xs.sheet.getHighlightRanges()
```

- Ange cellintervall för att markera omvänd markering på den aktiva arbetsbladet 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

- Ta bort markering för omvänd markering på den aktiva arbetsbladet 
```javascript
xs.sheet.removeHighlightInverseRange()

```

- Hämta omvänd markering cellintervall på den aktiva arbetsbladet 
```javascript
xs.sheet.getHighlightInverseRange()
```


- Lägg till form till markering arrayen på den aktiva arbetsbladet 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Ta bort markering för form i arrayen på den aktiva arbetsbladet 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

- Hämta array för formmarkering på den aktiva arbetsbladet  
```javascript
xs.sheet.getHighlightShaps()
```

- Lägg till textruta för markering, textrutan är en särskild typ av form vars typ är: "TextBox", på den aktiva arbetsbladet 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


- Ta bort markering för textruta, textrutan är en särskild typ av form vars typ är: "TextBox", på den aktiva arbetsbladet 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

- Lägg till bild i markering arrayen på den aktiva arbetsbladet 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Ta bort markering för bild i arrayen på den aktiva arbetsbladet 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Hämta array för bildmarkering  
```javascript
xs.sheet.getHighlightImages()
```

-  ange om du vill markera alla objekt i den aktiva kalkylbladet, inkludera alla former och bilder samt alla kalkylbladsområden
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


- Ange anpassad bildmarkerafunktion
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

-  rensa markeringen för den aktiva kalkylbladet
```javascript
xs.sheet.clearHighlights()

```

### Markera för textrutobjekt
Textrutan är en särskild typ av form vars typ är: "TextBox",
till exempel: koden nedan kommer att visa vilken form som är textrutan

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
- Lägg till markering för textrutobjekt
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

- Ta bort markering för textrutobjekt 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

- Hämta markering för textrutobjekt 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  Ändra bakgrundsfärg för textbox-objekt
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  Autoändra bakgrundsfärg och textfärg för att få en visuell aktiv effekt
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  dölj/visa textinnehållet i textrutan objekt
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



Du hittar mer på vår github-demo sida https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/blob/main/Examples.GridJs/templates/index.html
