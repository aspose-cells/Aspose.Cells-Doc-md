---
title: Working with GridJs Highlight feature
type: docs
weight: 250
url: /java/aspose-cells-gridjs/how-to-use-highlight-api/
description: This article describes how to use highlight on cell text, cell ranges, shapes and pictures in GridJs.
keywords: GridJs, highlight, highlight spreadsheet, redaction, remarks
aliases:
  - /java/aspose-cells-gridjs/highlight/
  - /java/aspose-cells-gridjs/how-to-highlight/
  - /java/aspose-cells-gridjs/work-with-highlight-api/
  - /java/aspose-cells-gridjs/work-with-highlight-apis/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Working with GridJs Highlight feature 
We support the following JS APIs for the Highlight feature 

-  Enable highlight and set highlight style; all highlight APIs will take effect only after the highlight style is set in the active worksheet 
```javascript
xs.sheet.showHighlights(style)
 // the parameter is:
 style: the style for highlight, currently only supports color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  Update the highlight style set in the active worksheet 
```javascript
xs.sheet.updateHighlightStyle(style)
 // the parameter is:
 style: the style for highlight, currently only supports color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  Disable highlight in the active worksheet    
```javascript
xs.sheet.hideHighlights()
```

-  Add cell text to highlight in the active worksheet 
```javascript
xs.sheet.addHighlightText(row, col, startposition, endposition)
    // the parameters are:
	row: row index 
	col: column index
	startposition: highlight start position in cell text 
	endposition: highlight end position in cell text 
    // it supports multiple range positions inside one cell
```

-  Remove highlight for cell text in array in the active worksheet 
```javascript
xs.sheet.removeHighlightText(row, col, startposition, endposition)
    // the parameters are:
	row: row index 
	col: column index
	startposition: highlight start position in cell text 
	endposition: highlight end position in cell text 
```

-  Get array for highlight for cell text in the active worksheet   
```javascript
xs.sheet.getHighlightTexts()
```

-  Add cell range to highlight in the active worksheet 
```javascript
xs.sheet.addHighlightRange(sri, sci, eri, eci)
    // the parameters are:
	sri: start row index of cell range
	sci: start column index of cell range
	eri: end row index of cell range
	eci: end column index of cell range
```

-  Remove highlight for cell range in array in the active worksheet 
```javascript
xs.sheet.removeHighlightRange(sri, sci, eri, eci)
     // the parameters are:
	sri: start row index of cell range
	sci: start column index of cell range
	eri: end row index of cell range
	eci: end column index of cell range
```

-  Get array for highlight for cell range in the active worksheet   
```javascript
xs.sheet.getHighlightRanges()
```

-  Set cell range to inverse highlight in the active worksheet 
```javascript
xs.sheet.setHighlightInverseRange(sri, sci, eri, eci)
    // the parameters are:
	sri: start row index of cell range
	sci: start column index of cell range
	eri: end row index of cell range
	eci: end column index of cell range
```

-  Remove highlight for inverse highlight in the active worksheet 
```javascript
xs.sheet.removeHighlightInverseRange()
```

-  Get inverse highlight cell range in the active worksheet 
```javascript
xs.sheet.getHighlightInverseRange()
```

-  Add shape to highlight array in the active worksheet 
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of the shape, can be found in xs.sheet.data.shapes
```

-  Remove highlight shape in array in the active worksheet 
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of the shape, can be found in xs.sheet.data.shapes
```

-  Get array for highlight shape in the active worksheet  
```javascript
xs.sheet.getHighlightShapes()
```

-  Add TextBox to highlight; TextBox is a special kind of shape whose type property is `"TextBox"`, in the active worksheet 
```javascript
xs.sheet.addHighlightTextBox(shapeid, startposition, endposition)
    // the parameters are:
    shapeid: the id of the shape, can be found in xs.sheet.data.shapes whose type is 'TextBox'
    startposition: highlight start position in the text of the TextBox
    endposition: highlight end position in the text of the TextBox
    // it supports multiple range positions inside one TextBox
```

-  Remove highlight range in the TextBox; TextBox is a special kind of shape whose type property is `"TextBox"`, in the active worksheet 
```javascript
xs.sheet.removeHighlightTextBox(shapeid, startposition, endposition)
    // the parameters are:
    shapeid: the id of the shape, can be found in xs.sheet.data.shapes whose type is 'TextBox'
    startposition: highlight start position in the text of the TextBox
    endposition: highlight end position in the text of the TextBox
    // it supports multiple range positions inside one TextBox
```

-  Add image to highlight array in the active worksheet 
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of the image, can be found in xs.sheet.data.images
```

-  Remove highlight image in array in the active worksheet 
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of the image, can be found in xs.sheet.data.images
```

-  Get array for highlight image  
```javascript
xs.sheet.getHighlightImages()
```

-  Set whether to highlight all objects in the active worksheet, including all shapes, images, and the entire worksheet area
```javascript
xs.sheet.setHighlightAll(isHighlightAll, isRerender = true)
   // the parameters are:
   isHighlightAll: true or false, whether to highlight all
   isRerender: true or false, whether to re-render
```

-  Set custom image highlight function
```javascript
xs.sheet.setCustomHighlightImgFunc(func)
   // the parameters are:
   func: the custom highlight image function; it shall take two parameters, the first is isHighlight, the second one is the Fabric image object 
   // we use Fabric.js to manage image objects; please refer to http://fabricjs.com/image-filters for more information
   // below is an example for the declared function: 
   const customHighlightImage = (isHighlight, imgObj) => {
            imgObj.filters[0] = isHighlight ? new fabric.Image.filters.Sepia() : false;
            imgObj.applyFilters();
        }
```

-  Clear highlight setting for the active worksheet
```javascript
xs.sheet.clearHighlights()
```

### Highlight for TextBox object
TextBox is a special kind of shape whose type property is `"TextBox"`.  
For example, the code below will show which shape is a TextBox:

```javascript
for (let shape of xs.sheet.data.shapes) {
    if (shape.type === 'TextBox') {
        console.log(shape.id + ' is a textbox');
    }
}
```

-  Add highlight for TextBox object
```javascript
addHighlight(startposition, endposition)
    // the parameters are:
    startposition: highlight start position in the TextBox
    endposition: highlight end position in the TextBox

// For example, we assume shape 0 is a TextBox object
const textbox = xs.sheet.data.shapes[0];
// First we shall add the highlight shape to enable highlighting for the TextBox shape object; it supports multiple range positions 
xs.sheet.addHighlightShape(textbox.id);
textbox.addHighlight(5, 10);
textbox.addHighlight(18, 28);
```

-  Remove highlight for TextBox object 
```javascript
removeHighlight(startposition, endposition)
    // the parameters are:
    startposition: highlight start position in the TextBox
    endposition: highlight end position in the TextBox

// For example, we assume shape 0 is a TextBox object
const textbox = xs.sheet.data.shapes[0];
textbox.removeHighlight(5, 10);
```

-  Get highlight for TextBox object 
```javascript
getHighlight()
    // For example, we assume shape 0 is a TextBox object
    const textbox = xs.sheet.data.shapes[0];
    textbox.getHighlight();
```

You can find more in our GitHub demo page: https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html
