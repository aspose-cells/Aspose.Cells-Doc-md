---
title : "Refresh Values of Linked Shapes" 
description : "" 
weight : 16468 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngchartsandshapes/refresh+values+of+linked+shapes/
---

# Aspose.Cells for Java : Refresh Values of Linked Shapes


Sometimes, you have a linked shape in your Excel file which is linked to some cell. In Microsoft Excel, changing the value of the linked cell also changes the value of linked shape. This also works fine with Aspose.Cells if you want to save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, then you will have to call [Worksheet.getShapes().updateSelectedValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/shapecollection#updateSelectedValue()) method to refresh the value of the linked shape.

#### Example

The following screenshot shows the source Excel file used in the sample code below. It has a linked **Picture 1** linked to cell A1. We will change the value of cell A1 with Aspose.Cells and then call [Worksheet.getShapes().updateSelectedValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/shapecollection#updateSelectedValue()) method to refresh the value of **Picture 1** and save it in PDF format.

![image](5472954.png)

You can download the [source Excel file](https://docs2.aspose.com/cells/java/attachments/5276461/5472956.xlsx) and the [output PDF](https://docs2.aspose.com/cells/java/attachments/5276461/5472955.pdf) from the given links.

#### Code


