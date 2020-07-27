+++
title = "Refresh Values of Linked Shapes" 
description = "" 
weight = 20509 
+++

Aspose.Cells for .NET : Refresh Values of Linked Shapes  

# Aspose.Cells for .NET : Refresh Values of Linked Shapes


Sometimes, you have a linked shape in your Excel file which is linked to some cell. In Microsoft Excel, changing the value of the linked cell also changes the value of the linked shape. This also works fine with Aspose.Cells if you want to save your workbook in XLS or XLSX format. However, if you want to save your workbook in PDF or HTML format, then you will have to call [Worksheet.Shapes.UpdateSelectedValue()](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) method to refresh the value of the linked shape.

## Example

The following screenshot shows the source Excel file used in the sample code below. It has a linked picture linked to cells A1 to E4. We will change the value of cell B4 with Aspose.Cells and then call [Worksheet.Shapes.UpdateSelectedValue()](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) method to refresh the value of the picture and save it in PDF format.

![](https://docs2.aspose.com/cells/net/attachments/5017331/95584293.jpg)

You can download the [source Excel file](https://docs2.aspose.com/cells/net/attachments/5017331/95584291.xlsx) and the [output PDF](https://docs2.aspose.com/cells/net/attachments/5017331/95584292.pdf) from the given links.

## Code

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Refresh Values of Linked Objects.png](https://docs2.aspose.com/cells/net/attachments/5017331/5112315.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [LinkedShape.xlsx](https://docs2.aspose.com/cells/net/attachments/5017331/5112314.xlsx) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [output.pdf](https://docs2.aspose.com/cells/net/attachments/5017331/5112338.pdf) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleRefreshValueOfLinkedShapes.xlsx](https://docs2.aspose.com/cells/net/attachments/5017331/95584291.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [outputRefreshValueOfLinkedShapes.pdf](https://docs2.aspose.com/cells/net/attachments/5017331/95584292.pdf) (application/pdf)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [RefreshValueOfLinkedShapes.jpg](https://docs2.aspose.com/cells/net/attachments/5017331/95584293.jpg) (image/jpeg)  

