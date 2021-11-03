---
title: Working with GridJs Client Side
type: docs
weight: 250
url: /net/aspose-cells-gridjs/client/
---

# Working with GridJs Client Side
We developed GridJs client based on [x-spreadsheet](https://github.com/myliang/x-spreadsheet "x-spreadsheet").

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
            showContextmenu: true
        }).loadData(sheets)
```

## the parameters for options:
- updateMode:  currently we only support 'server'
- updateUrl:  set the server side  url for update action based on json
- mode: read means readonly spread sheet/edit means we can edit the spread sheet
- showToolbar:   means whether to show toolbar
- showContextmenu:   means whether to show contextmenu on right click on a cell

for detail info ,you can check the example here
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>



 
 
