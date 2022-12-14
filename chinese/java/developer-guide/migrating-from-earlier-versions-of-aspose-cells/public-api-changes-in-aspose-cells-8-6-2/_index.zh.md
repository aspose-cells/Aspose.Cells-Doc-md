---
title: 公共 API Aspose.Cells 8.6.2 的变化
type: docs
weight: 220
url: /zh/java/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.6.1 到 8.6.2 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加的类，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持使用智能标记回叫**
此版本 Aspose.Cells for Java API 公开了 WorkbookDesigner.CallBack 字段和 ISmartMarkerCallBack 接口，它们一起允许[获取有关正在处理的单元格引用和/或智能标记的通知](/cells/zh/java/getting-notifications-while-merging-data-with-smart-markers/).以下代码演示了如何使用 ISmartMarkerCallBack 接口来定义一个新类来处理 WorkbookDesigner.process 方法的回调。

**Java**

{{< highlight "csharp" >}}

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

其余过程包括使用 WorkbookDesigner 加载包含智能标记的设计器电子表格，或从头开始创建并通过设置数据源来处理它。但是，为了启用通知，必须在调用 WorkbookDesigner.process 方法之前设置 WorkbookDesigner.CallBack 属性，如下所示。

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[]{ "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **添加方法 Chart.toPdf**
Aspose.Cells for Java 8.6.2 公开了 Chart.toPdf 方法，可用于直接将 Chart 形状渲染为 PDF 格式。该方法目前接受一个字符串类型的参数作为文件路径位置，将生成的文件存储在磁盘上。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **添加方法 Workbook.removeUnusedStyles**
 Aspose.Cells for Java 8.6.2公开了Workbook.removeUnusedStyles方法，可以用来[从样式池中移除所有未使用的 Style 对象](/cells/zh/java/remove-unused-styles-inside-the-workbook/). 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **物业 Cells. 添加样式**
Cells.Style 属性可用于访问代表默认样式的工作表的样式。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **为 GridWeb 添加的事件**
Aspose.Cells.GridWeb for Java 8.6.2 暴露了以下两个新事件。

1. AjaxCallFinished：当控件的 AJAX 更新完成时触发。 （EnableAJAX 应设置为 true）。
1. CellModifiedOnAjax：在 AJAX 调用中修改单元格时触发。
