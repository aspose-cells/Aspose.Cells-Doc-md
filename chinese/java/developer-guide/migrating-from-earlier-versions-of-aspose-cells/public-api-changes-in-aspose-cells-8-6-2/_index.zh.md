---
title: Aspose.Cells 8.6.2 中的公共 API 更改
type: docs
weight: 220
url: /zh/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.6.1 到 8.6.2 的 Aspose.Cells API 变化，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加的类，还描述了在 Aspose.Cells 内部行为方面的任何变化。

{{% /alert %}} 
## **添加的 API**
### **对智能标记的回调支持**
Aspose.Cells for Java API的此版本已公开了WorkbookDesigner.CallBack字段和ISmartMarkerCallBack接口，可以一起用于[获取关于正在处理的单元引用和/或智能标记的通知](/cells/zh/java/getting-notifications-while-merging-data-with-smart-markers/)。下面的代码片段演示了ISmartMarkerCallBack接口的用法，用于定义一个新类来处理WorkbookDesigner.process方法的回调。 

**Java**

{{< highlight csharp >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

其余的流程包括使用WorkbookDesigner加载包含Smart Markers的设计电子表格，或者从头开始创建一个，并通过设置数据源来处理它。但是，为了启用通知，需要在调用WorkbookDesigner.process方法之前设置WorkbookDesigner.CallBack属性，如下所示。

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **添加了Chart.toPdf方法**
Aspose.Cells for Java 8.6.2已公开了Chart.toPdf方法，可用于直接将图表形状呈现为PDF格式。该方法目前接受一个String类型的参数作为文件路径位置，用于存储结果文件到磁盘上。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **添加了Workbook.removeUnusedStyles方法**
Aspose.Cells for Java 8.6.2已公开了Workbook.removeUnusedStyles方法，可用于[从样式池中删除所有未使用的样式对象](/cells/zh/java/remove-unused-styles-inside-the-workbook/)。 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **添加了Cells.Style属性**
Cells.Style属性可用于访问表示默认样式的工作表的样式。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **为GridWeb添加了事件**
Aspose.Cells.GridWeb for Java 8.6.2公开了以下两个新事件。

1. AjaxCallFinished：在控件的AJAX更新完成时触发。（EnableAJAX应设置为true）。
1. CellModifiedOnAjax：在AJAX调用中修改单元格时触发。
{{< app/cells/assistant language="java" >}}
