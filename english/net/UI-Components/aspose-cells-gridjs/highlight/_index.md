---
title: Working with GridJs Highlight feature
type: docs
weight: 250
url: /net/aspose-cells-gridjs/highlight/
description: This article describes how to use highlight on cell text, cell ranges ,shapes and pictures in GridJs.
keywords: GridJs,highlight, highlight spreadsheet,redaction,remarks
aliases:
  - /net/aspose-cells-gridjs/how-to-use-highlight-api/
  - /net/aspose-cells-gridjs/how-to-highlight/
  - /net/aspose-cells-gridjs/work-with-highlight-api/
  - /net/aspose-cells-gridjs/work-with-highlight-apis/
---

# Working with GridJs Highlight feature 
We support the below JS APIs for Highlight feature 


-  Enable highlight and Set highlight style ,all the highlight APIs will take affect only after highlight style is set in the active worksheet 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  update the highlight style set in the active worksheet 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```


-  Disable highlight  in the active worksheet    
```javascript
xs.sheet.hideHighlights()
```
-  Add cell text to highlight in the active worksheet 
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
    //it support multiple range postion inside one cell
```

-  Remove highlight for cell text in array in the active worksheet 
```javascript
xs.sheet.removeHighlightText(row,col,startpostion,endposition)
    // the parameters are:
	row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

-  Get array for highlight for cell text in the active worksheet   
```javascript
xs.sheet.getHighlightTexts()
```

-  Add cell range to highlight in the active worksheet 
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Remove highlight for cell range in array in the active worksheet 
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Get array for highlight for cell range in the active worksheet   
```javascript
xs.sheet.getHighlightRanges()
```

-  Set cell range to invers highlight in the active worksheet 
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
	sri:start row index of cell range
	sci:start column index of cell range
	eri:end row index of cell range
	eci:end column index of cell range
```

-  Remove highlight for invers highlight in the active worksheet 
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Get   inverse highlight  cell range  in the active worksheet 
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Add shape to highlight array  in the active worksheet 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Remove highlight shape in array  in the active worksheet 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Get array for highlight shape  in the active worksheet  
```javascript
xs.sheet.getHighlightShaps()
```

-  Add textbox to highlight,textbox is a special kind of shape which type property is :"TextBox", in the active worksheet 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```


-  Remove highlight range in the textbox,textbox is a special kind of shape which type property is :"TextBox", in the active worksheet 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startpostion, endposition)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes whose type is 'TextBox'
    startpostion: highlight start postion in the text of textbox
    endpostion: highlight end postion in the text of textbox
    //it support multiple range postion inside one textbox
```

-  Add image to highlight array  in the active worksheet 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Remove highlight image in array  in the active worksheet 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Get array for highlight image  
```javascript
xs.sheet.getHighlightImages()
```

-  Set whether to highlight all objects in the active worksheet ,include all shapes and images and all worksheet area
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```


-  Set custom image highlight function
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

-  Clear highlight setting for the active worksheet
```javascript
xs.sheet.clearHighlights()

```

### Highlight for textbox object
textbox is a special kind of shape which type property is :"TextBox",
for example: the below code will show which shape is textbox

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```
-  Add highlight for textbox object
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

-  Remove highlight for textbox object 
```javascript
    removeHighlight(startpostion,endposition)
    // the parameters are:
	startpostion: highlight start postion in textbox
	endpostion: highlight end postion in textbox
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.removeHighlight(5,10);
```

-  Get highlight for textbox object 
```javascript
    getHighlight()
    //for example,we assume shape 0 is a textbox object
     const textbox=xs.sheet.data.shapes[0];
     textbox.getHighlight();
```




You can find more in our github demo page https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/index.html
