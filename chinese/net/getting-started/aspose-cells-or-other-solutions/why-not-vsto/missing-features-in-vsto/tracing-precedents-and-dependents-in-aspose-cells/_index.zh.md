---
title: 在Aspose.Cells中跟踪前代和所依赖的
type: docs
weight: 130
url: /zh/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

复杂的财务工作表，尤其是合作开发的工作表，可能隐藏最令人尴尬的错误。当公式使用先例单元格和从属单元格时，检查公式的准确性并找到错误的来源可能很困难。

- **前代单元格** 是由另一个单元格的公式引用的单元格。例如，如果单元格D10包含公式=B5，则单元格B5是单元格D10的前代。
- **所依赖的单元格** 包含引用其他单元格的公式。例如，如果单元格D10包含公式=B5，则单元格D10是单元格B5的所依赖的。

为了使电子表格易于阅读，您可能希望清楚地显示电子表格中用于公式的单元格。同样，您可能需要提取其他单元格的依赖单元格。

Aspose.Cells 允许您跟踪单元格并找出哪些是相互关联的。

{{% /alert %}} 
## **跟踪先例和依赖单元格：Microsoft Excel**
公式可能根据客户的修改而变化。例如，如果单元格C1依赖于包含公式的C3和C4，而C1已更改（因此覆盖了公式），则C3和C4或其他单元格需要根据业务规则进行调整以平衡电子表格。

类似地，假设C1包含公式"=(B1*22)/(M2*N32)"。我想找到C1依赖的单元格，即前代单元格B1、M2和N32。

您可能需要跟踪特定单元格对其他单元格的依赖关系。如果业务规则嵌入在公式中，我们希望找出依赖关系并根据其执行一些规则。同样，如果特定单元格的值被修改，工作表中哪些单元格会受到该更改的影响？

Microsoft Excel 允许用户跟踪先例和依赖。

1.在**查看工具栏**上，选择**公式审计**。
   显示【公式审计】对话框。 
   【公式审计对话框】 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. 跟踪先例：
   1. 选择包含您想要查找先例单元格的公式的单元格。
   1. 要向每个直接提供数据给活动单元格的单元格显示跟踪箭头，请单击**公式审计**工具栏上的**跟踪先例**。
1. 跟踪引用特定单元格的公式（依赖项）
   1. 选择要识别其依赖单元格的单元格。
   1. 要向每个依赖于活动单元格的单元格显示跟踪箭头，请单击**公式审计**工具栏上的**跟踪依赖**。
## **跟踪先例和依赖单元格：Aspose.Cells**
### **跟踪先例**
Aspose.Cells使得获取单元格的先行单元格变得轻松。它不仅可以检索提供数据给简单公式先行单元格的单元格，还可以找到提供给具有命名范围的复杂公式先行单元格的单元格。

在下面的示例中，使用了模板Excel文件《Book1.xls》。电子表格在第一个工作表上包含数据和公式。

【输入电子表格】 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells提供了Cell类的GetPrecedents方法，用于跟踪单元格的先行单元格。它返回一个ReferredAreaCollection。如上所示，在Book1.xls中，单元格B7包含公式"=SUM(A1:A3)"。因此，单元格A1:A3是单元格B7的先行单元格。以下示例演示了使用模板文件Book1.xls跟踪先行单元格的功能。

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
### **跟踪依赖项**
Aspose.Cells可以让您在电子表格中获取依赖单元格。Aspose.Cells不仅可以检索提供简单公式数据的单元格，还可以找到提供具有命名范围的复杂公式依赖单元格的单元格。

Aspose.Cells提供了Cell类的GetDependents方法，用于跟踪单元格的依赖单元格。例如，在Book1.xlsx中，有公式：B2单元格中的"=A1+20"和C2单元格中的"=A1+30"。以下示例演示了如何使用模板文件Book1.xlsx跟踪A1单元格的依赖单元格。

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

