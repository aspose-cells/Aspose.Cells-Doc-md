---
title: Setting Shared Formula in Aspose.Cells
type: docs
weight: 110
url: /net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

Suppose you have a worksheet filled with data.

You want to add a function in B2 that will calculate the sales tax for the first row of data. The tax is **9%**. The formula that calculates the sales tax is: **"=A2*0.09"**. This article explains how to apply this formula with Aspose.Cells.

{{% /alert %}} 

Aspose.Cells lets you specify a formula using the Cell.Formula property.

There are two options for adding formulas to the other cells (B3, B4, B5, and so on) in the column.

Either do what you did for the first cell, effectively setting the formula for each cell, updating the cell reference accordingly (A3*0.09, A4*0.09, A5*0.09 and so on). This requires the cell references for each row to be updated. It also requires Aspose.Cells to parse each formula individually, which can be time consuming for larg spreadsheets and complex formulas. It also adds extra lines of codes although loops can cut them down somewhat.

Another approach is to use a **shared formula**. With a shared formula, the formulas are automatically updated for the cell references in each row so that the tax would be calculated properly. The Cell.SetSharedFormula method is more efficient than the first method.

The following example demonstrates how to use it.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
### **Download Sample Code**
- [Codeplex](https://asposeopenxml.codeplex.com/SourceControl/latest#Aspose.Cells Features missing in OpenXML/Setting Shared Formula/)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
### **Download Running Example**
- [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
