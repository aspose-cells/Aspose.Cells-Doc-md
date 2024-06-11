---
title: Aspose.Cells 8.6.2 中的公共 API 更改
type: docs
weight: 210
url: /zh/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.6.1 到 8.6.2 的 Aspose.Cells API 变化，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加的类，还描述了在 Aspose.Cells 内部行为方面的任何变化。

{{% /alert %}} 
## **添加的 API**
### **对智能标记的回调支持**
此版本的Aspose.Cells for .NET API已公开了WorkbookDesigner.CallBack属性和ISmartMarkerCallBack接口，共同允许[获取有关正在处理的单元格引用和/或智能标记的通知](/cells/zh/net/getting-notifications-while-merging-data-with-smart-markers/)。以下代码演示了使用ISmartMarkerCallBack接口定义一个处理WorkbookDesigner.Process方法的新类。

**C#**

{{< highlight csharp >}}

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



其余的过程包括使用WorkbookDesigner加载包含Smart Markers的设计电子表格，并通过设置数据源进行处理。但是，为了启用通知，有必要在调用WorkbookDesigner.Process方法之前设置WorkbookDesigner.CallBack属性，如下所示。

**C#**

{{< highlight csharp >}}

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


### **添加了Chart.ToPdf方法**
Aspose.Cells for .NET 8.6.2已公开了Chart.ToPdf方法，可用于[直接将图表形状渲染为PDF格式](/cells/zh/net/convert-an-excel-chart-to-image/)。该方法当前接受类型为字符串的参数作为存储结果文件的文件路径位置。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **添加了Workbook.RemoveUnusedStyles方法**
Aspose.Cells for .NET 8.6.2已公开了Workbook.RemoveUnusedStyles方法，该方法可用于[从样式池中删除所有未使用的样式对象](/cells/zh/net/remove-unused-styles-inside-the-workbook/)。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **添加了Cells.Style属性**
Cells.Style属性可用于访问表示默认样式的工作表的样式。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **为GridWeb添加了事件**
Aspose.Cells.GridWeb for .NET 8.6.2 已公开了以下两个新事件。

1. AjaxCallFinished: 当控件的 AJAX 更新完成时触发（EnableAJAX必须设置为true）。
1. CellModifiedOnAjax：在AJAX调用中修改单元格时触发。
