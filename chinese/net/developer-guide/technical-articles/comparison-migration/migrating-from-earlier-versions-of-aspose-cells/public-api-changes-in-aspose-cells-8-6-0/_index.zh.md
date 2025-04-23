---
title: Aspose.Cells 8.6.0中的公共API更改
type: docs
weight: 190
url: /zh/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.5.2 更新到 8.6.0 的更改，可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、[添加的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-6-0/)，还包括了 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持在不创建工作簿对象的情况下对元数据进行操作**
此版本的Aspose.Cells for .NET API已公开了两个新类WorkbookMetadata和MetadataOptions以及一个新的MetadataType枚举，现在可以在不创建Workbook实例情况下操作文档属性（元数据）。WorkbookMetadata类轻量且提供非常易于使用、高效的机制来[读取、写入和更新文档属性而不影响整体性能](/cells/zh/net/using-workbookmetadata/)。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);

WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties

metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet

metadata.Save(filePath);

{{< /highlight >}}


### **新增HtmlSaveOptions.ExportFrameScriptsAndProperties属性**
Aspose.Cells for .NET 8.6.0已公开了HtmlSaveOptions.ExportFrameScriptsAndProperties属性，可用于影响将电子表格转换为HTML格式时生成附加脚本。使用默认设置，Aspose.Cells API将按照Excel应用程序进行导出，即：生成的HTML包含框架和条件注释，用于检测浏览器类型并相应调整布局。HtmlSaveOptions.ExportFrameScriptsAndProperties属性的默认值为true，这意味着按照Excel标准进行导出。然而，如果将属性设置为false，API将不会[生成与框架和条件注释有关的脚本](/cells/zh/net/disable-exporting-frame-scripts-and-document-properties/)。在这种情况下，生成的HTML可以在任何浏览器中正确查看，但不能使用Aspose.Cells API导入。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML

book.Save("output.html", options);

{{< /highlight >}}


### **新增Shape.MarcoName属性**
Aspose.Cells for .NET 8.6.0已公开了Shape.MarcoName属性，可用于[将任何VBA模块分配给表单控件](/cells/zh/net/assign-macro-to-form-control/)，例如按钮，以提供交互。该属性是字符串类型，因此可以接受模块名称并将其分配给控件。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **新增OoxmlSaveOptions.UpdateZoom属性**
通过v8.6.0的发布，Aspose.Cells for .NET API已公开了OoxmlSaveOptions.UpdateZoom属性，可用于更新PageSetup.Zoom，如果PageSetup.FitToPagesWide和/或PageSetup.FitToPagesTall属性已用于控制工作表缩放。
{{< app/cells/assistant language="csharp" >}}
