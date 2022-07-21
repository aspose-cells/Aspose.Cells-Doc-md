---
title: Ignore styles to get better performance in GridWeb
type: docs
weight: 1060
url: /net/aspose-cells-gridweb/ignorestylewithnodata
description: This article describes how to use IgnoreStyleWithNoData to get better performance for  Aspose.Cells.GridWeb library.
keywords: performance
---

## **Possible Usage Scenarios**
Please use [GridWeb.IgnoreStyleWithNoData](https://apireference.aspose.com/cells/net/aspose.cells.gridweb/gridweb/properties/ignorestylewithnodata) property while load less rows/columns from the workbook.
 
## **Filter data while Loading Workbook**
Please check the [sample excel file](largerowswithstyle.xlsx) 

When set  IgnoreStyleWithNoData = true;

As you can see ,It shows rows (to 15) and columns (to L),It will not display the last continus rows and columns without data in cells.Thus the load time will be less.

![workbook with ignore style](ignorestyletrue.png)


When set  IgnoreStyleWithNoData = false;(the default value is false)

As you can see ,It shows much more rows (to 500) and columns (to CZ)

![workbook without ignore style](ignorestylefalse.png)
 
 
 