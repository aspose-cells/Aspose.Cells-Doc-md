---
title: 公共 API Aspose.Cells 8.4.0 的变化
type: docs
weight: 140
url: /zh/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.3.2 到 8.4.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-0/)和[删除的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-4-0/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **修改电子表格中 VBA/宏代码的机制**
为了提供以下功能[VBA/宏代码操作](/cells/zh/java/modifying-vba-or-macro-code-using-aspose-cells/)Aspose.Cells for Java 8.4.0在com.aspose.cells.Vba包中暴露了一系列新的类和属性。这些新类的一些重要细节如下。

- VbaProject 类可用于从给定的电子表格中获取 VBA 项目。
- VbaModuleCollection 类表示属于给定 VbaProject 的 VBA 模块的集合。
- VbaModule 类表示 VbaModuleCollection 中的单个模块。

以下代码片段显示了如何动态修改 VBA 代码段。

**Java**

{{< highlight "csharp" >}}

工作簿 workbook = new Workbook("source.xlsm");

//更改VBA模块代码

VbaModuleCollection 模块 = workbook.getVbaProject().getModules();

对于（int i=0；我< modules.getCount(); i++)

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
### **能够删除数据透视表**
Aspose.Cells for Java 8.4.0 公开了 PivotTableCollection 的两种方法，以提供从给定电子表格中删除数据透视表的功能。上述方法的详情如下。

- PivotTableCollection.remove 方法接受数据透视表的对象，并将其从集合中删除。
- PivotTableCollection.removeAt 方法接受基于零索引的整数值，并从集合中删除特定的数据透视表。

以下代码片段显示了如何使用上述两种方法删除数据透视表。

**Java**

{{< highlight "csharp" >}}

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
### **支持不同的数据透视表布局**
Aspose.Cells for Java 8.4.0 支持数据透视表的不同预定义布局。为了提供此功能，Aspose.Cells API 公开了 PivotTable 类的三种方法，如下所述。

- PivotTable.showInCompactForm 方法以紧凑布局呈现数据透视表。
- PivotTable.showInOutlineForm 方法以大纲布局呈现数据透视表。
- PivotTable.showInTabularForm 方法以表格布局呈现数据透视表。

{{% alert color="primary" %}} 

在设置上述任何布局后调用 PivotTable.refreshData 和 PivotTable.calculateData 很重要。

{{% /alert %}} 

以下示例代码为数据透视表设置不同的布局并将结果存储在光盘上。

**Java**

{{< highlight "csharp" >}}

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
### **类 TxtLoadStyleStrategy 和属性 TxtLoadOptions.LoadStyleStrategy 添加**
Aspose.Cells for Java 8.4.0 公开了 TxtLoadStyleStrategy 类和 TxtLoadOptions.LoadStyleStrategy 属性，以便在将字符串值转换为数字或日期时间时指定格式化解析值的策略。
### **添加了方法 DataBar.ToImage**
随着v8.4.0的发布，Aspose.Cells API 提供了DataBar.toImage方法将条件格式化的DataBar保存为图片格式。 {DataBar.toImage}} 方法接受两个参数，详情如下。

- 第一个参数的类型为 com.aspose.cells.Cell，已应用条件格式。
- 第二个参数是 com.aspose.cells.rendering.ImageOrPrintOptions 类型，以便设置结果图像的不同参数。

以下示例代码演示了如何使用 DataBar.toImage 方法以图像格式呈现 DataBar。

**Java**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **属性 Border.ThemeColor 添加**
Aspose.Cells API 允许从电子表格中提取与主题相关的数据。随着Aspose.Cells for Java 8.4.0的发布，API已经暴露了Border.ThemeColor属性，可以用来获取Cell边框的主题颜色属性。
### **添加了属性 DrawObject.ImageBytes**
Aspose.Cells for Java 8.4.0 公开了 DrawObject.ImageBytes 属性以从图表或形状获取图像数据。
### **已添加属性 HtmlSaveOptions.ExportBogusRowData**
 Aspose.Cells for Java 8.4.0 提供了 {HtmlSaveOptions.ExportBogusRowData}} 属性。布尔类型属性确定 API 是否会在将电子表格导出为 HTML 格式时注入伪造的底行数据。

{{% alert color="primary" %}} 

默认值是true。

{{% /alert %}} 

以下示例代码说明了上述属性的使用。

**Java**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **已添加属性 HtmlSaveOptions.CellCssPrefix**
新添加的属性 HtmlSaveOptions.CellCssPrefix 允许在将电子表格导出为 HTML 格式时设置 CSS 文件的前缀。

{{% alert color="primary" %}} 

默认值为“”（空字符串）。

{{% /alert %}}
## **废弃的 API**
### **方法 Cells.getCellByIndex 和 Row.getCellByIndex 已废弃**
改为使用 getEnumerator 方法迭代所有单元格。
### **属性 DrawObject.Image 已废弃**
使用 DrawObject.ImageBytes 属性来获取图像数据。
