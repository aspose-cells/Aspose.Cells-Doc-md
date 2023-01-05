---
title: 公共 API Aspose.Cells 8.6.2 的变化
type: docs
weight: 210
url: /zh/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.6.1 到 8.6.2 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加的类，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持使用智能标记回叫**
此版本 Aspose.Cells for .NET API 公开了 WorkbookDesigner.CallBack 属性和 ISmartMarkerCallBack 接口，它们一起允许[获取有关正在处理的单元格引用和/或智能标记的通知](/cells/zh/net/getting-notifications-while-merging-data-with-smart-markers/).下面的一段代码演示了如何使用 ISmartMarkerCallBack 接口来定义一个新类来处理 WorkbookDesigner.Process 方法的回调。

**C#**

{{< highlight "csharp" >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



其余过程包括使用 WorkbookDesigner 加载包含智能标记的设计器电子表格，并通过设置数据源来处理它。但是，为了启用通知，必须在调用 WorkbookDesigner.Process 方法之前设置 WorkbookDesigner.CallBack 属性，如下所示。

**C#**

{{< highlight "csharp" >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **添加方法 Chart.ToPdf**
 Aspose.Cells for .NET 8.6.2公开了Chart.ToPdf方法，可以用来[直接将 Chart 形状渲染为 PDF 格式](/cells/zh/net/convert-an-excel-chart-to-image/).该方法目前接受字符串类型的参数作为文件路径位置，将生成的文件存储在磁盘上。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **方法 Workbook.RemoveUnusedStyles 添加**
Aspose.Cells for .NET 8.6.2公开了Workbook.RemoveUnusedStyles方法，可以用来[从样式池中移除所有未使用的 Style 对象](/cells/zh/net/remove-unused-styles-inside-the-workbook/).

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **物业 Cells. 添加样式**
Cells.Style 属性可用于访问代表默认样式的工作表的样式。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **为 GridWeb 添加的事件**
Aspose.Cells.GridWeb for .NET 8.6.2 暴露了以下两个新事件。

1. AjaxCallFinished：当控件的 AJAX 更新完成时触发。 （EnableAJAX 应设置为 true）。
1. CellModifiedOnAjax：在 AJAX 调用中修改单元格时触发。
