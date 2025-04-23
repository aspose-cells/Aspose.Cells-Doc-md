---
title: Aspose.Cells 8.4.0 中的公共 API 变更
type: docs
weight: 130
url: /zh/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.3.2 升级到 8.4.0 的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-0/)和[移除的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-0/)，还描述了 Aspose.Cells 后台行为的任何更改。

{{% /alert %}} 
## **添加的 API**
### **修改电子表格中的 VBA/Macro 代码的机制**
为了提供[VBA/Macro Code Manipulation](/cells/zh/net/modifying-vba-or-macro-code-using-aspose-cells/)功能，Aspose.Cells for .NET 8.4.0已在Aspose.Cells.Vba命名空间中公开了一系列新类和属性。其中一些新类的重要详细信息如下。

- 可以使用 VbaProject 类从给定的电子表格中获取 VBA 项目。
- VbaModuleCollection类表示给定VbaProject的VBA模块集合。
- VbaModule类表示来自VbaModuleCollection的单个模块。

以下代码片段显示了如何动态修改VBA代码段。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **删除数据透视表的能力**
Aspose.Cells for .NET 8.4.0已为PivotTableCollection公开了两种方法，以删除给定电子表格中的数据透视表。上述方法的详细信息如下。

- PivotTableCollection.Remove 方法接受 PivotTable 对象，并从集合中移除它。
- PivotTableCollection.RemoveAt方法接受基于零的整数值并从集合中删除特定的数据透视表。

以下代码片段显示了如何使用上述两种方法删除数据透视表。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **不同数据透视表布局的支持**
Aspose.Cells for .NET 8.4.0为数据透视表提供了不同预定义布局的支持。为了提供此功能，Aspose.Cells APIs为PivotTable类公开了三种方法，详细信息如下。

- PivotTable.ShowInCompactForm方法以紧凑布局呈现数据透视表。
- PivotTable.ShowInOutlineForm方法以大纲布局呈现数据透视表。
- PivotTable.ShowInTabularForm方法以表格布局呈现数据透视表。

{{% alert color="primary" %}} 

重要的是在设置了上述任一布局之后调用PivotTable.RefreshData和PivotTable.CalculateData。

{{% /alert %}} 

以下示例代码为数据透视表设置不同的布局，并将结果保存到磁盘。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **添加了Class TxtLoadStyleStrategy和Property TxtLoadOptions.LoadStyleStrategy**
Aspose.Cells for .NET 8.4.0已公开了TxtLoadStyleStrategy类和TxtLoadOptions.LoadStyleStrategy属性，以指定在将字符串值转换为数字或日期时间时格式化解析后的值的策略。
### **添加了DataBar.ToImage方法**
在v8.4.0发布时，Aspose.Cells API提供了DataBar.ToImage方法，以将有条件格式的数据条保存为图像格式。DataBar.ToImage方法接受下面详细说明的两个参数。

- 第一个参数是已应用条件格式的Aspose.Cells.Cell类型。
- 第二个参数是Aspose.Cells.Rendering.ImageOrPrintOptions类型，用于设置结果图像的不同参数。

以下示例代码演示了使用DataBar.ToImage方法将数据条呈现为图像格式。

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **添加了 Border.ThemeColor 属性**
Aspose.Cells APIs允许从电子表格中提取主题相关的格式数据。随着Aspose.Cells for .NET 8.4.0的发布，API已公开了Border.ThemeColor属性，可用于检索单元格边框的主题颜色属性。
### **添加了 DrawObject.ImageBytes 属性**
Aspose.Cells for .NET 8.4.0已公开了DrawObject.ImageBytes属性，以从图表或形状中获取图像数据。
### **添加了 HtmlSaveOptions.ExportBogusRowData 属性**
Aspose.Cells for .NET 8.4.0已提供了{HtmlSaveOptions.ExportBogusRowData}}属性。该布尔类型属性确定在将电子表格导出为HTML格式时，API是否将注入虚假底部行数据。

{{% alert color="primary" %}} 

默认值为true。

{{% /alert %}} 

以下示例代码说明了上述属性的用法。

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **添加了 HtmlSaveOptions.CellCssPrefix 属性**
新添加的属性HtmlSaveOptions.CellCssPrefix允许在将电子表格导出为HTML格式时设置CSS文件的前缀。

{{% alert color="primary" %}} 

默认值为""（空字符串）。

{{% /alert %}}
## **弃用的API**
### **弃用了Cells.GetCellByIndex和Row.GetCellByIndex方法**
使用GetEnumerator方法代替遍历所有单元格。
### **弃用的DrawObject.Image Property**
请改用DrawObject.ImageBytes属性获取图像数据。
{{< app/cells/assistant language="csharp" >}}
