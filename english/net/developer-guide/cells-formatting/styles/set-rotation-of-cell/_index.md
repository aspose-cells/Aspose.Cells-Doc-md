---
title: How to Rotate Text of Cell
type: docs
weight: 80
url: /net/how-to-rotate-text-of-cell/
description: C# code to rotate text of Cell with Aspose.Cells for .NET API
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---

## **Rotate Text of Cell in Aspose.Cells**

Aspose.Cells is a powerful .NET and Java component that enables developers to work with Excel spreadsheets programmatically. One of the features provided by Aspose.Cells is the ability to rotate cells, allowing you to customize the orientation of text and improve the visual presentation of your data. In this document, we will explore how to rotate cells using Aspose.Cells.

## **How to Rotate Text of Cell in Excel**
To rotate a cell in Excel, you can use the following steps:
1. Open Excel and select the cell or range of cells that you want to rotate.
1. Right-click on the selected cell(s) and choose "Format Cells" from the context menu. Alternatively, you can go to the "Home" tab in the Excel ribbon, click on the "Format" dropdown in the "Cells" group, and select "Format Cells."
1. In the "Format Cells" dialog box, navigate to the "Alignment" tab.
1. Under the "Orientation" section, you will see the options to rotate the text. You can directly input the desired rotation angle in degrees in the "Degrees" box. Positive values rotate the text counterclockwise, and negative values rotate it clockwise.
<br>
![todo:image_alt_text](alignment.png)
1. Once you have selected the desired rotation, click "OK" to apply the changes. The selected cell(s) will now be rotated based on your chosen rotation angle or orientation.

## **How to Rotate Text of Cell using Aspose.Cells API**

[**Style.RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/) property makes it convenient to rotate cells. To rotate cells in Aspose.Cells, you need to follow these steps:
1. Load the Excel Workbook
<br>
First, you need to load the Excel workbook using Aspose.Cells. You can use the Workbook class to open an existing Excel file or create a new one. 

1. Access the Worksheet
<br>
Once the workbook is loaded, you need to access the worksheet where you want to rotate the cells. You can either access the worksheet by its index or name. 

1. Rotate the text of Cell
<br>
Now that you have access to the worksheet, you can rotate the cells by modifying the Style object of the desired cells. The Style object allows you to set various formatting options, including rotation. 

1. Save the Workbook
<br>
After rotating the cells, you can save the modified workbook back to a file or stream using the Save method.

## **C# Sample Code**

Please see the following code, it creates a workbook object and set different rotation angles for several cells. The screenshot shows the result after the execution of the sample code.

![todo:image_alt_text](rotation.png)



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
