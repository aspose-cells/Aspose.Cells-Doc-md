---
title: Aspose.Cells 8.6.0中的公共API更改
type: docs
weight: 190
url: /zh/net/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

本文描述了从版本8.5.2到8.6.0的Aspose.Cells API的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加的类等，还包括Aspose.Cells幕后行为中的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **支持在不创建Workbook对象的情况下操纵元数据**
这个Aspose.Cells for .NET API的版本公开了两个新类，WorkbookMetadata和MetadataOptions，以及一个新枚举MetadataType，现在允许在不创建Workbook实例的情况下操作文档属性（元数据）。

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


### **新增 HtmlSaveOptions.ExportFrameScriptsAndProperties 属性**
Aspose.Cells for .NET 8.6.0公开了HtmlSaveOptions.ExportFrameScriptsAndProperties属性，可影响将电子表格转换为HTML格式时生成附加脚本的方式。

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


### **已添加 Shape.MarcoName 属性**
Aspose.Cells for .NET 8.6.0公开了Shape.MarcoName属性，可用于将任何VBA模块分配给形式控件，例如按钮，以提供交互。

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


### **已添加 OoxmlSaveOptions.UpdateZoom 属性**
通过v8.6.0版本的发布，Aspose.Cells for .NET API已公开了OoxmlSaveOptions.UpdateZoom属性，可用于更新PageSetup.Zoom，如果使用了PageSetup.FitToPagesWide和/或PageSetup.FitToPagesTall属性来控制工作表缩放。
