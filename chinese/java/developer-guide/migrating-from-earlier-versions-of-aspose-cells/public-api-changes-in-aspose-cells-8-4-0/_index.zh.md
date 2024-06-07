---
title: Aspose.Cells 8.4.0 中的公共 API 更改
type: docs
weight: 140
url: /zh/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

本文描述了 Aspose.Cells API 版本从 8.3.2 到 8.4.0 的更改，这可能对模块/应用程序开发人员有所帮助

{{% /alert %}} 
## **已添加API**
### **修改电子表格中的 VBA/宏代码的机制**
为了提供 VBA/Macro 代码操作功能，Aspose.Cells for Java 8.4.0 在 com.aspose.cells.Vba 包中公开了一系列新类和属性

- VbaProject 类可用于从给定的电子表格中获取 VBA 项目。
- VbaModuleCollection 类表示给定 VbaProject 的 VBA 模块集合。
- VbaModule 类表示来自 VbaModuleCollection 的单个模块。

以下代码片段显示了如何动态修改 VBA 代码段。

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
### **移除数据透视表的功能**
Aspose.Cells for Java 8.4.0 已向 PivotTableCollection 公开了两种方法，用于从给定的电子表格中删除数据透视表

- PivotTableCollection.remove 方法接受一个 PivotTable 对象，并将其从集合中移除。
- PivotTableCollection.removeAt 方法接受基于零的索引整数值，并从集合中移除特定的 PivotTable。

以下代码片段显示了如何使用上述两种方法移除 PivotTable。

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
### **支持不同的数据透视表布局**
Aspose.Cells for Java 8.4.0 提供了对数据透视表不同预定义布局的支持。为实现此功能，Aspose.Cells API已经为 PivotTable 类公开了三种方法，如下所述。

- PivotTable.showInCompactForm 方法将数据透视表呈现为紧凑布局。
- PivotTable.showInOutlineForm 方法将数据透视表呈现为大纲布局。
- PivotTable.showInTabularForm 方法将数据透视表呈现为表格布局。

{{% alert color="primary" %}} 

在设置上述布局后，调用 PivotTable.refreshData 和 PivotTable.calculateData 非常重要。 

{{% /alert %}} 

以下示例代码为数据透视表设置不同的布局，并将结果存储在磁盘上。

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
### **类 TxtLoadStyleStrategy 和属性 TxtLoadOptions.LoadStyleStrategy 已添加**
Aspose.Cells for Java 8.4.0 已经公开了 TxtLoadStyleStrategy 类和 TxtLoadOptions.LoadStyleStrategy 属性，以指定在将字符串值转换为数字或日期时间时格式化解析值的策略。
### **添加了DataBar.ToImage方法**
通过 v8.4.0 版本的发布，Aspose.Cells API提供了 DataBar.toImage 方法，可以将有条件格式的 DataBar 保存为图像格式。DataBar.toImage 方法接受如下两个参数。

- 第一个参数是应用了条件格式的 com.aspose.cells.Cell 类型。
- 第二个参数是 com.aspose.cells.rendering.ImageOrPrintOptions 类型，用于设置结果图像的不同参数。

以下示例代码演示了使用 DataBar.toImage 方法将 DataBar 呈现为图像格式。

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
### **添加了Border.ThemeColor属性**
Aspose.Cells API允许从电子表格中提取与主题相关的数据。随着 Aspose.Cells for Java 8.4.0 的发布，API已经公开了 Border.ThemeColor 属性，可用于检索单元格边框的主题颜色属性。
### **添加了DrawObject.ImageBytes属性**
Aspose.Cells for Java 8.4.0 已经公开了 DrawObject.ImageBytes 属性，以从图表或形状中获取图像数据。
### **添加了HtmlSaveOptions.ExportBogusRowData属性**
Aspose.Cells for Java 8.4.0 提供了 {HtmlSaveOptions.ExportBogusRowData}} 属性。这个布尔类型属性确定 API在将电子表格导出为 HTML 格式时是否注入虚假底部行数据。 

{{% alert color="primary" %}} 

默认值为 true。

{{% /alert %}} 

以下示例代码演示了上述属性的使用。

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
### **新增 HtmlSaveOptions.CellCssPrefix 属性**
新增属性 HtmlSaveOptions.CellCssPrefix 允许设置导出电子表格到 HTML 格式时的 CSS 文件前缀。

{{% alert color="primary" %}} 

默认值为空字符串。

{{% /alert %}}
## **已弃用的API**
### **已废弃 Cells.getCellByIndex 和 Row.getCellByIndex 方法**
使用 getEnumerator 方法来遍历所有单元格。
### **已弃用 DrawObject.Image 属性**
使用 DrawObject.ImageBytes 属性来获取图像数据。
