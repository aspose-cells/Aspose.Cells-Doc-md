---
title: Working with GridJs Highlight feature
type: docs
weight: 250
url: /net/aspose-cells-gridjs/highlight/
description: This article describes how to use GridJs to highlight on cell text, cell ranges ,shapes and pictures.
keywords: highlight, highlight spreadsheet
---

# Working with GridJs Highlight feature 
We support the below JS APIs for Highlight feature 


-  Enable highlight and Set highlight style ,all the highlight APIs will take affect only after highlight style is set
```javascript
xs.showHighlights(style)
 // the parameter is:
 style: the style for highlight ,currently only support color
 for example: {'color':'rgba(85, 57, 47, 0.08)'}
```

-  Disable highlight    
```javascript
xs.hideHighlights()
```
-  Add cell text to highlight
```javascript
xs.sheet.addHighlightText(row,col,startpostion,endposition)
    // the parameters are:
    row:row index 
	col:column index
	startpostion: highlight start postion in cell text 
	endpostion: highlight end postion in cell text 
```

-  Remove highlight for cell text in array
```javascript
xs.sheet.removeHighlightText(row,col)
    // the parameters are:
    row:row index 
	col:column index
```

-  Get array for highlight for cell text  
```javascript
xs.sheet.getHighlightTexts()
```

-  Add cell range to highlight
```javascript
xs.sheet.addHighlightRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Remove highlight for cell range in array
```javascript
xs.sheet.removeHighlightRange(sri,sci,eri,eci)
     // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Get array for highlight for cell range  
```javascript
xs.sheet.getHighlightRanges()
```

-  Set cell range to invers highlight
```javascript
xs.sheet.setHighlightInverseRange(sri,sci,eri,eci)
    // the parameters are:
    sri:start row index of cell range
	sci:start column index of cell range
	 eri:end row index of cell range
	eci:end column index of cell range
```

-  Remove highlight for invers highlight
```javascript
xs.sheet.removeHighlightInverseRange()
     
```

-  Get   inverse highlight  cell range  
```javascript
xs.sheet.getHighlightInverseRange()
```


-  Add shape to highlight array
```javascript
xs.sheet.addHighlightShape(shapeid)
    // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Remove highlight shape in array
```javascript
xs.sheet.removeHighlightShape(shapeid)
     // the parameters are:
    shapeid: the id of shape, can be find in xs.sheet.data.shapes
```

-  Get array for highlight shape  
```javascript
xs.sheet.getHighlightShaps()
```


-  Add image to highlight array
```javascript
xs.sheet.addHighlightImage(imageid)
    // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Remove highlight image in array
```javascript
xs.sheet.removeHighlightImage(imageid)
     // the parameters are:
    imageid: the id of image, can be find in xs.sheet.data.images
```

-  Get array for highlight image  
```javascript
xs.sheet.getHighlightImages()
```

-  set whether to highlight all worksheet ,include all shapes and images 
```javascript
xs.sheet.setHighlightAll(ishighlightall,isrerender=true)
   // the parameters are:
   ishighlightall: true or false,whether to highlight all
   isrerender: true or false,whether to reRender
```
