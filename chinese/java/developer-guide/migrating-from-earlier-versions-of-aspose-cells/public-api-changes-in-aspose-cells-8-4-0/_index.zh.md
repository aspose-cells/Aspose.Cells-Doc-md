---
title: Aspose.Cells 8.4.0 中的公共 API 变更
type: docs
weight: 140
url: /zh/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.3.2 到 8.4.0 的 Aspose.Cells API 变更，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[新增类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-0/)和[移除的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-0/)，还描述了在幕后行为中的任何更改。

{{% /alert %}} 
## **添加的 API**
### **修改电子表格中的 VBA/Macro 代码的机制**
为了提供[VBA/Macro Code Manipulation]功能，Aspose.Cells for Java 8.4.0已经在com.aspose.cells.Vba包中暴露了一系列新的类和属性。以下是这些新类的一些重要细节。

- 可以使用 VbaProject 类从给定的电子表格中获取 VBA 项目。
- VbaModuleCollection类表示给定VbaProject的VBA模块集合。
- VbaModule类表示来自VbaModuleCollection的单个模块。

以下代码片段显示了如何动态修改VBA代码段。

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **删除数据透视表的能力**
Aspose.Cells for Java 8.4.0已经为PivotTableCollection暴露了两种方法，用于从给定的电子表格中移除数据透视表。上述方法的详细信息如下。

- PivotTableCollection.remove方法接受一个PivotTable对象，并从集合中删除它。
- PivotTableCollection.removeAt方法接受基于零的整数值，从集合中删除特定的PivotTable。

以下代码片段显示了如何使用上述两种方法删除数据透视表。

**Java**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **不同数据透视表布局的支持**
Aspose.Cells for Java 8.4.0为数据透视表提供了不同预定义布局的支持。为了提供这个功能，Aspose.Cells APIs已经为PivotTable类暴露了三种方法，如下所述。

- PivotTable.showInCompactForm方法以紧凑布局呈现数据透视表。
- PivotTable.showInOutlineForm方法以大纲布局呈现数据透视表。
- PivotTable.showInTabularForm方法以表格布局呈现数据透视表。

{{% alert color="primary" %}} 

在设置上述任何布局之后，重要的是调用PivotTable.refreshData和PivotTable.calculateData。 

{{% /alert %}} 

以下示例代码为数据透视表设置不同的布局，并将结果保存到磁盘。

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **添加了Class TxtLoadStyleStrategy和Property TxtLoadOptions.LoadStyleStrategy**
Aspose.Cells for Java 8.4.0已经为TxtLoadStyleStrategy类和TxtLoadOptions.LoadStyleStrategy属性暴露，以指定在将字符串值转换为数字或日期时间时格式化解析的策略。
### **添加了DataBar.ToImage方法**
发布v8.4.0时，Aspose.Cells API提供了DataBar.toImage方法，以将有条件格式的DataBar保存为图像格式。DataBar.toImage方法接受两个详细参数。

- 第一个参数是已应用条件格式的com.aspose.cells.Cell类型。
- 第二个参数的类型为com.aspose.cells.rendering.ImageOrPrintOptions，以设置结果图像的不同参数。

以下示例代码演示了DataBar.toImage方法的用法，将DataBar呈现为图像格式。

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **添加了 Border.ThemeColor 属性**
Aspose.Cells APIs允许从电子表格中提取与主题相关的数据。随着Aspose.Cells for Java 8.4.0的发布，API已经暴露了Border.ThemeColor属性，可用于检索单元格边框的主题颜色属性。
### **添加了 DrawObject.ImageBytes 属性**
Aspose.Cells for Java 8.4.0已经暴露了DrawObject.ImageBytes属性，用于从图表或形状中获取图像数据。
### **添加了 HtmlSaveOptions.ExportBogusRowData 属性**
Aspose.Cells for Java 8.4.0已经提供了{HtmlSaveOptions.ExportBogusRowData}}属性。布尔类型属性确定API在将电子表格导出为HTML格式时是否注入伪造底部行数据。 

{{% alert color="primary" %}} 

默认值为true。

{{% /alert %}} 

以下示例代码说明了上述属性的用法。

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **添加了 HtmlSaveOptions.CellCssPrefix 属性**
新添加的属性HtmlSaveOptions.CellCssPrefix允许在将电子表格导出为HTML格式时设置CSS文件的前缀。

{{% alert color="primary" %}} 

默认值为""（空字符串）。

{{% /alert %}}
## **弃用的API**
### **弃用的Cells.getCellByIndex和Row.getCellByIndex方法**
请使用getEnumerator方法来迭代所有单元格。
### **弃用的DrawObject.Image Property**
请改用DrawObject.ImageBytes属性获取图像数据。
