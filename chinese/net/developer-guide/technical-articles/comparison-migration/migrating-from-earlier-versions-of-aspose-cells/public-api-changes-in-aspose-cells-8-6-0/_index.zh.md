---
title: 公共 API Aspose.Cells 8.6.0 的变化
type: docs
weight: 190
url: /zh/net/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.5.2 到 8.6.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-6-0/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **支持在不创建工作簿对象的情况下进行元数据操作**
此版本 Aspose.Cells for .NET API 公开了两个新类，即 WorkbookMetadata 和 MetadataOptions 以及一个新的枚举 MetadataType，现在允许在不创建 Workbook 实例的情况下操作文档属性（元数据）。 WorkbookMetadata 类重量轻，提供了非常易于使用、高效的机制来[在不影响整体性能的情况下读取、写入和更新文档属性](/cells/zh/net/using-workbookmetadata/).

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **添加了属性 HtmlSaveOptions.ExportFrameScriptsAndProperties**
Aspose.Cells for .NET 8.6.0 公开了 HtmlSaveOptions.ExportFrameScriptsAndProperties 属性，该属性可用于在将电子表格转换为 HTML 格式时影响其他脚本的创建。在默认设置下，Aspose.Cells API 以 HTML 格式导出电子表格，就像 Excel 应用程序导出一样，即；生成的 HTML 包含框架和条件注释，可检测浏览器类型并相应地调整布局。 HtmlSaveOptions.ExportFrameScriptsAndProperties 属性的默认值为 true，这意味着；导出是按照 Excel 标准完成的。但是，如果该属性设置为 false，则 API 不会[生成与框架和条件注释相关的脚本](/cells/zh/net/disable-exporting-frame-scripts-and-document-properties/).在这种情况下，生成的 HTML 可以在任何浏览器中正确查看，但是无法使用 Aspose.Cells API 将其导回。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **添加属性 Shape.MarcoName**
 Aspose.Cells for .NET 8.6.0 公开了Shape.MarcoName属性，可用于[将任何 VBA 模块分配给表单控件](/cells/zh/net/assign-macro-to-form-control/)这样一个Button是为了提供交互。该属性是字符串类型，因此它可以接受模块名称并将其分配给控件。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook workbook = new Workbook();

//Access first default worksheet

Worksheet sheet = workbook.Worksheets[0];

//Add a module to the worksheet

int moduleIdx = workbook.VbaProject.Modules.Add(sheet);

//Access newly added module from the collection

VbaModule module = workbook.VbaProject.Modules[moduleIdx];

//Add code to the module

module.Codes =

    "Sub ShowMessage()" + "\r\n" +

    "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

    "End Sub";

//Add a Button on the worksheet and set its various properties

Aspose.Cells.Drawing.Button button = sheet.Shapes.AddButton(2, 0, 2, 0, 28, 80);

button.Placement = Aspose.Cells.Drawing.PlacementType.FreeFloating;

button.Font.Name = "Tahoma";

button.Font.IsBold = true;

button.Font.Color = System.Drawing.Color.Blue;

button.Text = "Aspose";

//Assign the VBA module to the button

button.MacroName = sheet.Name + ".ShowMessage";

//Save the result

workbook.Save("output.xlsm");

{{< /highlight >}}


### **属性 OoxmlSaveOptions.UpdateZoom 添加**
随着 v8.6.0 的发布，Aspose.Cells for .NET API 公开了 OoxmlSaveOptions.UpdateZoom 属性，如果 PageSetup.FitToPagesWide 和/或 PageSetup.FitToPagesTall 属性已用于控制工作表缩放，则可用于更新 PageSetup.Zoom。
