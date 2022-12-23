---
title: 公共 API Aspose.Cells 8.6.0 的变化
type: docs
weight: 200
url: /zh/java/public-api-changes-in-aspose-cells-8-6-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.5.2 到 8.6.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-6-0/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **支持在不创建工作簿对象的情况下进行元数据操作**
此版本 Aspose.Cells for Java API 公开了两个新类，即 WorkbookMetadata 和 MetadataOptions 以及一个新的枚举 MetadataType，现在允许在不创建 Workbook 实例的情况下操作文档属性（元数据）。 WorkbookMetadata 类重量轻，提供了非常易于使用、高效的机制来[在不影响整体性能的情况下读取、写入和更新文档属性](/cells/zh/java/using-workbookmetadata/). 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **添加了属性 HtmlSaveOptions.ExportFrameScriptsAndProperties**
Aspose.Cells for Java 8.6.0 公开了 HtmlSaveOptions.ExportFrameScriptsAndProperties 属性，该属性可用于在将电子表格转换为 HTML 格式时影响其他脚本的创建。在默认设置下，Aspose.Cells API 以 HTML 格式导出电子表格，就像 Excel 应用程序导出一样，即；结果 HTML 包含框架和条件注释，可检测浏览器类型并相应地调整布局。 HtmlSaveOptions.ExportFrameScriptsAndProperties 属性的默认值为 true，这意味着；导出是按照 Excel 标准完成的。如果该属性设置为 false，则 API 不会[生成与框架和条件注释相关的脚本](/cells/zh/java/disable-exporting-frame-scripts-and-document-properties/).在这种情况下，生成的 HTML 可以在任何浏览器中正确查看，但是无法使用 Aspose.Cells API 将其导回。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **添加属性 Shape.MarcoName**
Aspose.Cells for Java 8.6.0 公开了Shape.MarcoName属性，可用于[将 VBA 模块分配给表单控件](/cells/zh/java/assign-macro-code-to-form-control/)这样一个Button是为了提供交互。该属性是字符串类型，因此它可以接受模块名称并将其分配给控件。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create a new Workbook object

Workbook workbook = new Workbook();

//Get the instance of first default worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Add a new module to the first worksheet

int moduleIdx = workbook.getVbaProject().getModules().add(sheet);

//Get the instance of newly added module

VbaModule module = workbook.getVbaProject().getModules().get(moduleIdx);

//Add module code

module.setCodes("Sub ShowMessage()" + "\r\n" +

        "    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

        "End Sub");

//Create a new button to the worksheet and set its various properties

Button button = (Button) sheet.getShapes().addShape(MsoDrawingType.BUTTON, 2, 0, 2, 0, 28, 80);

button.setPlacement(PlacementType.FREE_FLOATING);

button.getFont().setName("Tahoma");

button.getFont().setBold(true);

button.getFont().setColor(Color.getBlue());

button.setText("Aspose");

//Assign the newly added module to the button

button.setMacroName(module.getName() + ".ShowMessage" );

//Save the spreadsheet in XLSM format

workbook.save("output.xlsm");

{{< /highlight >}}
### **属性 OoxmlSaveOptions.UpdateZoom 添加**
随着 v8.6.0 的发布，Aspose.Cells for Java API 公开了 OoxmlSaveOptions.UpdateZoom 属性，如果 PageSetup.FitToPagesWide 和/或 PageSetup.FitToPagesTall 属性已用于控制工作表缩放，则可用于更新 PageSetup.Zoom。
