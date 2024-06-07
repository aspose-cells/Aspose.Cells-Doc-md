---
title: Aspose.Cells 8.6.2 中的公共API更改
type: docs
weight: 210
url: /zh/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.6.1 到 8.6.2 的 Aspose.Cells API 的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加的类，还描述了在 Aspose.Cells 后台行为中的任何更改。

{{% /alert %}} 
## **已添加API**
### **支持回调与智能标记**
这个Aspose.Cells for .NET API的版本公开了WorkbookDesigner.CallBack属性和ISmartMarkerCallBack接口，共同允许获取关于正在处理的单元格引用和/或智能标记的通知。以下代码段演示了使用ISmartMarkerCallBack接口定义一个可处理WorkbookDesigner.Process方法的新类的用法。

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



其余流程包括使用 WorkbookDesigner 加载包含智能标记的设计电子表格，并通过设置数据源处理它。然而，为了启用通知，在调用 WorkbookDesigner.Process 方法之前，必须设置 WorkbookDesigner.CallBack 属性，如下所示。

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


### **添加Chart.ToPdf方法**
Aspose.Cells for .NET 8.6.2公开了Chart.ToPdf方法，可用于直接将图表形状渲染为PDF格式。

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


### **添加Workbook.RemoveUnusedStyles方法**
Aspose.Cells for .NET 8.6.2公开了Workbook.RemoveUnusedStyles方法，用于从样式池中移除所有未使用的样式对象。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **已添加 Cells.Style 属性**
Cells.Style 属性可用于访问代表默认样式的工作表的样式。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **为 GridWeb 添加了事件**
Aspose.Cells.GridWeb for .NET 8.6.2 暴露了以下两个新事件。

1. AjaxCallFinished: 当控件的 AJAX 更新完成时触发。(要将 EnableAJAX 设置为 true)。
1. CellModifiedOnAjax: 当在 AJAX 调用中修改单元格时触发。
