---
title: 公共 API Aspose.Cells 8.4.0 的变化
type: docs
weight: 130
url: /zh/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.3.2 到 8.4.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-0/)和[删除的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-0/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **修改电子表格中 VBA/宏代码的机制**
为了提供以下功能[VBA/宏代码操作](/cells/zh/net/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for .NET 8.4.0 在 Aspose.Cells.Vba 命名空间中暴露了一系列新的类和属性。这些新类的一些重要细节如下。

- VbaProject 类可用于从给定的电子表格中获取 VBA 项目。
- VbaModuleCollection 类表示属于给定 VbaProject 的 VBA 模块的集合。
- VbaModule 类表示 VbaModuleCollection 中的单个模块。

以下代码片段显示了如何动态修改 VBA 代码段。

**C#**

{{< highlight "csharp" >}}

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


### **能够删除数据透视表**
Aspose.Cells for .NET 8.4.0 公开了 PivotTableCollection 的两种方法，以提供从给定电子表格中删除数据透视表的功能。上述方法的详情如下。

- PivotTableCollection.Remove 方法接受数据透视表的对象，并将其从集合中删除。
- PivotTableCollection.RemoveAt 方法接受基于零索引的整数值并从集合中删除特定的数据透视表。

以下代码片段显示了如何使用上述两种方法删除数据透视表。

**C#**

{{< highlight "csharp" >}}

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


### **支持不同的数据透视表布局**
Aspose.Cells for .NET 8.4.0 支持数据透视表的不同预定义布局。为了提供此功能，Aspose.Cells API 公开了 PivotTable 类的三种方法，如下所述。

- PivotTable.ShowInCompactForm 方法以紧凑布局呈现数据透视表。
- PivotTable.ShowInOutlineForm 方法以大纲布局呈现数据透视表。
- PivotTable.ShowInTabularForm 方法以表格布局呈现数据透视表。

{{% alert color="primary" %}} 

在设置上述任何布局后调用 PivotTable.RefreshData 和 PivotTable.CalculateData 很重要。

{{% /alert %}} 

以下示例代码为数据透视表设置不同的布局并将结果存储在光盘上。

**C#**

{{< highlight "csharp" >}}

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


### **类 TxtLoadStyleStrategy 和属性 TxtLoadOptions.LoadStyleStrategy 添加**
Aspose.Cells for .NET 8.4.0 公开了 TxtLoadStyleStrategy 类和 TxtLoadOptions.LoadStyleStrategy 属性，以便在将字符串值转换为数字或日期时间时指定格式化解析值的策略。
### **添加了方法 DataBar.ToImage**
随着v8.4.0的发布，Aspose.Cells API 提供了DataBar.ToImage方法将条件格式的DataBars保存为图片格式。 {DataBar.ToImage}} 方法接受两个参数，详情如下。

- 第一个参数的类型为 Aspose.Cells.Cell，已应用条件格式。
- 第二个参数的类型为 Aspose.Cells.Rendering.ImageOrPrintOptions 以便设置结果图像的不同参数。

以下示例代码演示了如何使用 DataBar.ToImage 方法以图像格式呈现 DataBar。

**C#**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **属性 Border.ThemeColor 添加**
Aspose.Cells API 允许从电子表格中提取与主题相关的格式数据。随着Aspose.Cells for .NET 8.4.0的发布，API已经暴露了Border.ThemeColor属性，可以用来获取Cell边框的主题颜色属性。
### **添加了属性 DrawObject.ImageBytes**
Aspose.Cells for .NET 8.4.0 公开了 DrawObject.ImageBytes 属性以从图表或形状获取图像数据。
### **已添加属性 HtmlSaveOptions.ExportBogusRowData**
Aspose.Cells for .NET 8.4.0 提供了 {HtmlSaveOptions.ExportBogusRowData}} 属性。布尔类型属性决定 API 在将电子表格导出为 HTML 格式时是否会注入伪造的底行数据。

{{% alert color="primary" %}} 

默认值是true。

{{% /alert %}} 

以下示例代码说明了上述属性的使用。

**C#**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **已添加属性 HtmlSaveOptions.CellCssPrefix**
新添加的属性 HtmlSaveOptions.CellCssPrefix 允许在将电子表格导出为 HTML 格式时设置 CSS 文件的前缀。

{{% alert color="primary" %}} 

默认值为“”（空字符串）。

{{% /alert %}}
## **废弃的 API**
### **方法 Cells.GetCellByIndex & Row.GetCellByIndex 已废弃**
改为使用 GetEnumerator 方法迭代所有单元格。
### **属性 DrawObject.Image 已废弃**
使用 DrawObject.ImageBytes 属性来获取图像数据。
