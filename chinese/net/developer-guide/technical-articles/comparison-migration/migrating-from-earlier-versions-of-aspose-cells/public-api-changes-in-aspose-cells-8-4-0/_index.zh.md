---
title: Aspose.Cells 8.4.0 中的公共 API 更改
type: docs
weight: 130
url: /zh/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从8.3.2版本到8.4.0版本的变化，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、[添加的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-0/)和[删除的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-4-0/)，还描述了Aspose.Cells在幕后行为的任何变化

{{% /alert %}} 
## **已添加API**
### **修改电子表格中的 VBA/宏代码的机制**
为了提供[VBA/Macro代码操控特性](/cells/zh/net/modifying-vba-or-macro-code-using-aspose-cells/)，Aspose.Cells for .NET 8.4.0在Aspose.Cells.Vba命名空间中公开了一系列新类和属性。其中一些新类的重要细节如下

- VbaProject 类可用于从给定的电子表格中获取 VBA 项目。
- VbaModuleCollection 类表示给定 VbaProject 的 VBA 模块集合。
- VbaModule 类表示来自 VbaModuleCollection 的单个模块。

以下代码片段显示了如何动态修改 VBA 代码段。

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


### **移除数据透视表的功能**
Aspose.Cells for .NET 8.4.0 为 PivotTableCollection 提供了两种 Pivot Table 移除功能。以下是上述方法的详细信息。

- PivotTableCollection.Remove 方法接受 PivotTable 对象，并将其从集合中移除。
- PivotTableCollection.RemoveAt 方法接受基于零的整数值，并从集合中移除特定的 PivotTable。

以下代码片段显示了如何使用上述两种方法移除 PivotTable。

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


### **支持不同的数据透视表布局**
Aspose.Cells for .NET 8.4.0 提供了不同预定义布局的数据透视表支持。为了提供此功能，Aspose.Cells API 为 PivotTable 类公开了三种方法，详细如下。

- PivotTable.ShowInCompactForm 方法呈现紧凑布局的数据透视表。
- PivotTable.ShowInOutlineForm 方法呈现大纲布局的数据透视表。
- PivotTable.ShowInTabularForm 方法呈现表格布局的数据透视表。

{{% alert color="primary" %}} 

在设置任何上述布局后，重要的是调用 PivotTable.RefreshData 和 PivotTable.CalculateData。

{{% /alert %}} 

以下示例代码为数据透视表设置不同的布局，并将结果存储在磁盘上。

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


### **类 TxtLoadStyleStrategy 和属性 TxtLoadOptions.LoadStyleStrategy 已添加**
Aspose.Cells for .NET 8.4.0 公开了 TxtLoadStyleStrategy 类和 TxtLoadOptions.LoadStyleStrategy 属性，以指定在将字符串值转换为数字或日期时间时格式化解析值的策略。
### **添加了DataBar.ToImage方法**
发布 v8.4.0 后，Aspose.Cells API 提供了 DataBar.ToImage 方法，将有条件格式的 DataBars 保存为图像格式。 DataBar.ToImage 方法接受如下详细的两个参数。

- 第一个参数类型为应用了有条件格式的 Aspose.Cells.Cell。
- 第二个参数类型为 Aspose.Cells.Rendering.ImageOrPrintOptions，用于设置结果图像的不同参数。

以下示例代码演示了 DataBar.ToImage 方法的使用，以图像格式呈现 DataBar。

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


### **添加了Border.ThemeColor属性**
Aspose.Cells API 允许从电子表格中提取与主题相关的格式数据。随着 Aspose.Cells for .NET 8.4.0 的发布，API 公开了 Border.ThemeColor 属性，可用于检索单元格边框的主题颜色属性。
### **添加了DrawObject.ImageBytes属性**
Aspose.Cells for .NET 8.4.0 公开了 DrawObject.ImageBytes 属性，用于从图表或形状获取图像数据。
### **添加了HtmlSaveOptions.ExportBogusRowData属性**
Aspose.Cells for .NET 8.4.0 提供了 HtmlSaveOptions.ExportBogusRowData 属性。这个布尔类型属性确定在将电子表格导出为 HTML 格式时，API 是否将伪造的底部行数据注入其中。

{{% alert color="primary" %}} 

默认值为 true。

{{% /alert %}} 

以下示例代码演示了上述属性的使用。

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


### **新增 HtmlSaveOptions.CellCssPrefix 属性**
新增属性 HtmlSaveOptions.CellCssPrefix 允许设置导出电子表格到 HTML 格式时的 CSS 文件前缀。

{{% alert color="primary" %}} 

默认值为空字符串。

{{% /alert %}}
## **已弃用的API**
### **已弃用 Cells.GetCellByIndex 和 Row.GetCellByIndex 方法**
使用 GetEnumerator 方法来遍历所有单元格。
### **已弃用 DrawObject.Image 属性**
使用 DrawObject.ImageBytes 属性来获取图像数据。
