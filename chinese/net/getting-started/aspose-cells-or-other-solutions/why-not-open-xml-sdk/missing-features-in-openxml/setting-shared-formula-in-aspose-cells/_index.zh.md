---
title: 在Aspose.Cells中设置共享公式
type: docs
weight: 110
url: /zh/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

假设您有一个填满数据的工作表。

您希望在B2中添加一个函数，用于为数据的第一行计算销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文解释了如何使用Aspose.Cells应用此公式。

{{% /alert %}} 

Aspose.Cells允许您使用Cell.Formula属性指定公式。

在列中向其他单元格（B3、B4、B5等）添加公式有两个选项。

对于其他单元格，您可以像为第一个单元格所做的那样，有效地为每个单元格设置公式，并相应地更新单元格引用（A3*0.09、A4*0.09、A5*0.09等）。这需要更新每行的单元格引用。它还要求Aspose.Cells逐个解析每个公式，这对于大型电子表格和复杂公式来说可能是耗时的。虽然循环可以减少一些额外的代码行，但仍会增加额外的代码行。

另一种方法是使用**共享公式**。有了共享公式，可以自动为每行中的单元格引用更新公式，以便正确计算税收。Cell.SetSharedFormula方法比第一种方法更高效。

以下示例演示了如何使用它。

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
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **下载示例**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
