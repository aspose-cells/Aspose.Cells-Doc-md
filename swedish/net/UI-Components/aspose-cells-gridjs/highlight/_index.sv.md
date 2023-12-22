---
title: Arbeta med GridJs Highlight-funktion
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/highlight/
description: Den här artikeln beskriver hur du använder GridJs för att markera celltext, cellintervall, former och bilder.
keywords: highlight, highlight spreadsheet,redaction,remarks
---
#  Arbeta med GridJs Highlight-funktion
 Vi stöder nedanstående JS API:er för Highlight-funktionen


-  Aktivera markering och Ställ in markeringsstil, alla markerings-API:er kommer att påverka först efter att markeringsstilen har ställts in i det aktiva kalkylbladet
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  uppdatera markeringsstilen i det aktiva kalkylbladet
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


-  Inaktivera markering i det aktiva kalkylbladet
```javascript
xs.sheet.hideHighlights()
```
-  Lägg till celltext för att markera i det aktiva kalkylbladet
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Ta bort markering för celltext i array i det aktiva kalkylbladet
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

- Hämta array för markering för celltext i det aktiva kalkylbladet
```javascript
xs.sheet.getHighlightTexts()
```

-  Lägg till cellintervall för att markera i det aktiva kalkylbladet
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Ta bort markering för cellintervall i array i det aktiva kalkylbladet
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Hämta array för markering för cellintervall i det aktiva kalkylbladet
```javascript
xs.sheet.getHighlightRanges()
```

-  Ställ in cellintervallet till att invertera markeringen i det aktiva kalkylbladet
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Ta bort markering för inversmarkering i det aktiva kalkylbladet
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Få inverterat markerat cellområde i det aktiva kalkylbladet
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Lägg till form för att markera array i det aktiva kalkylbladet
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Ta bort markeringsformen i arrayen i det aktiva kalkylbladet
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Hämta array för markeringsform i det aktiva kalkylbladet
```javascript
xs.sheet.getHighlightShaps()
```

-  Lägg till textruta för att markera, textbox är en speciell typ av form vars typegenskap är: "TextBox", i det aktiva kalkylbladet
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  Ta bort markeringsområde i textrutan, textbox är en speciell typ av form som typegenskapen är: "TextBox", i det aktiva kalkylbladet
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Lägg till bild för att markera array i det aktiva kalkylbladet
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

- Ta bort markerad bild i arrayen i det aktiva kalkylbladet
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Skaffa array för högdagerbild
```javascript
xs.sheet.getHighlightImages()
```

-  ställ in om alla objekt i det aktiva kalkylbladet ska markeras, inkludera alla former och bilder och alla kalkylbladsområde
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Ställ in anpassad bildmarkeringsfunktion
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

-  rensa markeringsinställningen för det aktiva kalkylbladet
```javascript
xs.sheet.clearHighlights()

```

###  Markera för textboxobjekt
textbox är en speciell typ av form vars typegenskap är:"TextBox",
till exempel: koden nedan visar vilken form som är textbox

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  Lägg till markering för textboxobjekt
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

-  Ta bort markering för textboxobjekt
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  Få markering för textbox-objekt
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```

-  Ändra bakgrundsfärg för textboxobjekt
```javascript
    setBackgroundColor(color)
    // the parameters are:
        color: the html color value in hex string value
    //for example,we assume shape 0 is a textbox object,this will set the background color to Yellow 
     const textbox=xs.sheet.data.shapes[0];
     textbox.setBackgroundColor('#FFFF00');
```
-  Ändra bakgrundsfärg och textfärg automatiskt för att få en visuell aktiv effekt
```javascript
    setActiveEffect(boolvalue)
    // the parameters are:
        boolvalue: if true,will change background color and the text color of the textbox object;if false,restore to original appearence
```

-  dölj/visa textinnehållet i textbox-objektet
```javascript
    hideText(boolvalue)
    // the parameters are:
        boolvalue: if true,will not display the text in the textbox object;if false,restore to original appearence
```



Du kan hitta mer på vår github-demosida https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
