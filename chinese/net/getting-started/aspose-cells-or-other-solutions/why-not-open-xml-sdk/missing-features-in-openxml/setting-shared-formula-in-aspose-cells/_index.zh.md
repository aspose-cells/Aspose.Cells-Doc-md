---
title: 在 Aspose.Cells 中设置共享公式
type: docs
weight: 110
url: /zh/net/setting-shared-formula-in-aspose-cells/
---
{{% alert color="primary" %}} 

假设您有一个充满数据的工作表。

您想要在 B2 中添加一个函数来计算第一行数据的销售税。税收是**9%**.计算销售税的公式是：**“=A2*0.09”**.本文介绍如何将此公式应用于 Aspose.Cells。

{{% /alert %}} 

Aspose.Cells 允许您使用 Cell.Formula 属性指定公式。

有两个选项可用于将公式添加到列中的其他单元格（B3、B4、B5 等）。

要么做你对第一个单元格所做的，有效地为每个单元格设置公式，相应地更新单元格引用（A3*0.09，A4*0.09、A5*0.09 等）。这需要更新每一行的单元格引用。它还需要 Aspose.Cells 来单独解析每个公式，这对于大型电子表格和复杂公式来说可能很耗时。它还添加了额外的代码行，尽管循环可以在一定程度上减少它们。

另一种方法是使用**共享公式**.使用共享公式，公式会自动更新每行中的单元格引用，以便正确计算税金。 Cell.SetSharedFormula 方法比第一种方法更有效。

下面的例子演示了如何使用它。

**C#**

{{< highlight "csharp" >}}

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
## **下载运行示例**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
