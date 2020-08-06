---
title: Rename Worksheets
type: docs
weight: 40
url: /net/rename-worksheets/
---

{{% alert color="primary" %}} 

Renaming a worksheet can be very useful when working with many worksheets in Aspose.Cells.GridWeb and decide to change their names to make them more meaningful. For example, a worksheet containing an invoice can be renamed Invoice instead of Sheet1. This topic describes this simple but useful feature.

{{% /alert %}} 
## **Renaming a Worksheet**
All worksheets contain a Name property that allows developers to access or modify worksheets' names. To rename a worksheet:

1. Access a worksheet from the GridWorksheetCollection.
1. Rename the selected worksheet.



{{% alert color="primary" %}} 

For more details on how to access worksheets in Aspose.Cells.GridWeb, please refer to [Access Worksheets](/cells/net/access-worksheets-html/).

{{% /alert %}} 

Before executing the code, the worksheet has a default name, such as Sheet1.

**Input file: a worksheet with a default name Sheet1** 

![todo:image_alt_text](rename-worksheets_1.png)

After running the code, the worksheet is renamed Students.

**Output: the worksheet is renamed Students** 

![todo:image_alt_text](rename-worksheets_2.png)



{{< gist "aspose-cells" "18f6c28b77ee30c773fb2199168e73ed" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}
