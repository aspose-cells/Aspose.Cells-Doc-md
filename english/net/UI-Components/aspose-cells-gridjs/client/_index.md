---
title: Working with GridJs Client Side
type: docs
weight: 250
url: /net/aspose-cells-gridjs/client/
---

# Working with GridJs Client Side
We developed GridJs client based on [x-spreadsheet](https://github.com/myliang/x-spreadsheet).

##  the main steps are:

- create x_spreadsheet instance
```javascript
xs = x_spreadsheet(id, options)
```
-  load json data
```javascript
xs.loadData(jsondata.data)
```
-  set active sheet
```javascript
xs.setActiveSheetByName(jsondata.actname)
```
-  set active cell
```javascript
xs.setActiveCell(jsondata.actrow,jsondata.actcol);
```

for example the below code init a x_spreadsheet object.
```javascript
 xs = x_spreadsheet('#gridjs-demo', {
			updateMode:'server',
			updateUrl:'/GridJs2/UpdateCell',
			mode: 'edit',
			showToolbar: true,
                        local: 'en',
            showContextmenu: true
        }).loadData(sheets)
```
    // the parameters for options:
    updateMode:  currently we only support 'server'
    updateUrl:  set the server side  url for update action based on json
    mode: read means readonly spread sheet/edit means we can edit the spread sheet
    showToolbar:   means whether to show toolbar
    showFileName:  whether to show the filename 
    local:         support multiple language for menus ,the locale can be: en, cn, es, pt, de, ru, nl for english,chinese,Spanish,Portuguese,germany,Russian,Dutch
    showContextmenu:   means whether to show contextmenu on right click on a cell
##  

___
## other useful apis
-  Render the view
```javascript
xs.reRender()
```
-  Get Selected Image/shape£¬if nothing select will return null
```javascript
xs.sheet.selector.getObj()
```

-  Get the cell object
```javascript
xs.sheet.data.getCell(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
-  Get the cell style
```javascript
xs.sheet.data.getCellStyle(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```
-  Set the cell value
```javascript
xs.sheet.data.setCellText(ri,ci,value,state)
    // the parameters are:
    ri:row index 
	ci:column index
	value:the cell value
	state: input | finished
```

-  Get/Set the selected cell range
```javascript
xs.sheet.data.selector.range
```
-  Set the cell value for the selected cell or cell area
```javascript
xs.sheet.data.setSelectedCellText(value)
    // the parameters are:
	value:the  value for the cell
```
-  Set the style for the selected cell or cell area
```javascript
xs.sheet.data.setSelectedCellAttr(attributename,value)
    // the parameters are:
    attributename:font-name | font-bold | font-italic | font-size  | format|border|merge|formula |strike|textwrap |underline |align |valign |color|bgcolor|pattern
	value:the  value for the attribute
```

-  Merge the selected cell area
```javascript
xs.sheet.data.merge()
```

-  Unmerge the selected cell area
```javascript
xs.sheet.data.unmerge()
```
-  Delete the selected cell  
```javascript
xs.sheet.data.deleteCell(what)
    // the parameters are:
    what:all|format  all: means delete the cell and clear the style ;format means delete the cell value and keep the cell style
```
-  Set the freeze pane
```javascript
xs.sheet.data.setFreeze(ri,ci)
    // the parameters are:
    ri:row index 
	ci:column index
```

-  Insert row or columns at  the selected cell  
```javascript
xs.sheet.data.insert(type, n)
    // the parameters are:
    type: row | column
	n:the row or column number
```
-  Delete row or columns at  the selected cell  
```javascript
xs.sheet.data.delete(type)
    // the parameters are:
    type: row | column
```

-  Set the width for the column
```javascript
xs.sheet.data.setColWidth(ci,width)
    // the parameters are:
    ci:column index
	width:the width for the column
```
-  Get the width for the column 
```javascript
xs.sheet.data.cols.sumWidth(min,max)
    // the parameters are:
    min:the start column index
	max:the end column index,not include
```

-  Set the height for the row
```javascript
xs.sheet.data.setRowHeight(ri,height)
    // the parameters are:
    ri:row index
	height:the height for the row
```
-  Get the height for the row 
```javascript
xs.sheet.data.rows.sumHeight(min,max)
    // the parameters are:
    min:the start row index
	max:the end row index,not include
```
-  Get/Set the display direction
```javascript
xs.sheet.data.displayRight2Left
```



for detail info ,you can check the example here
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
