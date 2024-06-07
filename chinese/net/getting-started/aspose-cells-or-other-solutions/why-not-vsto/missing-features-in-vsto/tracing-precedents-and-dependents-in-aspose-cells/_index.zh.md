---
title: 在Aspose.Cells中跟踪先例和依赖关系
type: docs
weight: 130
url: /zh/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

特别是在协作开发的复杂财务工作表中，可能会隐藏最尴尬的错误。当公式使用前置单元格和后置单元格时，检查公式的准确性并找到错误来源可能会变得困难。

- **前置单元格** 是由另一个单元格中的公式引用的单元格。例如，如果单元格 D10 包含公式 =B5，则单元格 B5 是单元格 D10 的前置。
- **依赖单元格** 包含引用其他单元格的公式。例如，如果单元格D10包含公式=B5，则单元格D10是单元格B5的依赖项。

为了使电子表格易于阅读，您可能希望清楚地显示电子表格上使用的公式单元格。同样，您可能希望提取其他单元格的后置单元格。

Aspose.Cells允许您跟踪单元格并找出哪些单元格是链接的。

{{% /alert %}} 
## **跟踪先行和从属单元格：Microsoft Excel**
根据客户所做的修改，公式可能会发生变化。例如，如果单元格C1依赖于包含公式的C3和C4，并且C1发生改变（因此覆盖了该公式），则C3和C4或其他单元格需要根据业务规则调整平衡表格。

类似地，假设C1包含公式"=(B1*22)/(M2*N32)"。我希望找出C1依赖的单元格，即先例单元格B1、M2和N32。

您可能需要跟踪特定单元格对其他单元格的依赖关系。如果业务规则嵌入在公式中，我们希望找出依赖关系并根据此执行一些规则。同样，如果特定单元格的值被修改，哪些单元格在工作表上受到该更改的影响？

Microsoft Excel 允许用户跟踪先行和从属。

1.在**查看工具栏**中，选择**公式审计**。
   显示公式审计对话框。 
   **公式审计对话框** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. 追踪先行：
   1. 选择包含您要查找先行单元格公式的单元格。
   1. 要为直接提供数据给活动单元格的每个单元格显示跟踪箭头，请在**公式审计**工具栏上单击**跟踪先行**。
1. 追踪引用特定单元格的公式（从属）
   1. 选择要识别从属单元格的单元格。
   1. 要为依赖于活动单元格的每个单元格显示跟踪箭头，请在公式审计工具栏上单击“跟踪从属”。
## **跟踪先行和从属单元格：Aspose.Cells**
### **跟踪先行**
Aspose.Cells可以轻松获取先例单元格。它不仅可以检索向简单公式先例提供数据的单元格，还可以找到向具有命名范围的复杂公式先例提供数据的单元格。

在下面的示例中，使用一个模板excel文件 Book1.xls。电子表格在第一个工作表上有数据和公式。

**输入的电子表格** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells提供了Cell类的GetPrecedents方法，用于跟踪单元格的先例。它返回一个ReferredAreaCollection。正如上面所示，在Book1.xls中，单元格B7包含公式"=SUM(A1:A3)"。因此，单元格A1:A3是单元格B7的先例。以下示例演示了如何使用模板文件Book1.xls跟踪先例功能。

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **跟踪从属**
Aspose.Cells让您可以获取电子表格中的依赖单元格。Aspose.Cells不仅可以检索提供有关简单公式的数据的单元格，还可以找到向具有命名范围的复杂公式的依赖提供数据的单元格。

Aspose.Cells提供了Cell类的GetDependents方法，用于跟踪单元格的依赖项。例如，在Book1.xlsx中有公式:"=A1+20"和"=A1+30"分别在B2和C2单元格中。以下示例演示了如何使用模板文件Book1.xlsx跟踪A1单元格的依赖项。

**C#**

{{< highlight csharp >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

