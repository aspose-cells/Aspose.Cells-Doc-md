---
title : "Refresh Values of Linked Shapes" 
description : "" 
weight : 20509 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngchartsandshapes/refresh+values+of+linked+shapes/
---

# Aspose.Cells for .NET : Refresh Values of Linked Shapes


Sometimes, you have a linked shape in your Excel file which is linked to some cell. In Microsoft Excel, changing the value of the linked cell also changes the value of the linked shape. This also works fine with Aspose.Cells if you want to save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, then you will have to call [Worksheet.Shapes.UpdateSelectedValue()](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) method to refresh the value of the linked shape.

## Example

The following screenshot shows the source Excel file used in the sample code below. It has a linked picture linked to cells A1 to E4. We will change the value of cell B4 with Aspose.Cells and then call [Worksheet.Shapes.UpdateSelectedValue()](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) method to refresh the value of the picture and save it in PDF format.

![](https://docs2.aspose.com/cells/net/attachments/5017331/95584293.jpg)

You can download the [source Excel file](https://docs2.aspose.com/cells/net/attachments/5017331/95584291.xlsx) and the [output PDF](https://docs2.aspose.com/cells/net/attachments/5017331/95584292.pdf) from the given links.

## Code

