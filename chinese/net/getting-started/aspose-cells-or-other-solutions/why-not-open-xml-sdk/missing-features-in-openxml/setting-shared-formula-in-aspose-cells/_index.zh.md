---
title: 在Aspose.Cells中设置共享公式
type: docs
weight: 110
url: /zh/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

假设您有一个填充有数据的工作表。

您希望在B2中添加一个函数，用于计算第一行数据的销售税。税率为**9%**。计算销售税的公式是：**"=A2*0.09"**。本文介绍了如何使用Aspose.Cells应用此公式。

{{% /alert %}} 

Aspose.Cells允许您使用Cell.Formula属性指定公式。

有两种选项可将公式添加到列中的其他单元格(B3、B4、B5等)。 

要么像第一个单元格所做的那样，为每个单元格设置公式，相应更新单元格引用（A3*0.09，A4*0.09，A5*0.09等）。这需要为每行更新单元格引用。它还需要Aspose.Cells逐个解析每个公式，对于大型电子表格和复杂公式来说可能需要耗费时间。尽管循环可以减少额外的代码行，但它还是会增加额外的代码行。

另一种方法是使用**共享公式**。使用共享公式，公式会自动更新每行的单元格引用，以便正确计算税额。Cell.SetSharedFormula方法比第一种方法更有效。

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
## **下载运行示例**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
