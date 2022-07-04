---
title: Public API Changes in Aspose.Cells 8.8.2
type: docs
weight: 280
url: /net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.8.1 to 8.8.2 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Update References Automatically while Deleting Blank Rows & Columns**
Aspose.Cells for .NET 8.8.2 has exposed the overloaded versions of the Cells.DeleteBlankRows & Cells.DeleteBlankColumns methods. The new methods can accept an instance of DeleteOptions class and can be used to overcome the situations that could arise due to the broken references in formulas, chart series data and so on. The DeleteOptions class currently has only one member, a Boolean type property by the name UpdateReference. If the said property is set to true and the instance of DeleteOptions class is passed to the Cells.DeleteBlankRows & Cells.DeleteBlankColumns methods, the API will internally adjust the formula references (if any) to accommodate the changes.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Deleting Blank Rows & Columns with Updated References](/cells/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
