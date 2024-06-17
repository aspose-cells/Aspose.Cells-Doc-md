---
title: Aspose.Cells 8.6.0中的公共API更改
type: docs
weight: 200
url: /zh/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

本文描述了从版本8.5.2到8.6.0的Aspose.Cells API的更改，这些更改可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-6-0/)，还描述了Aspose.Cells在幕后行为的任何更改。

{{% /alert %}} 
## **添加的 API**
### **支持在不创建工作簿对象的情况下对元数据进行操作**
Aspose.Cells for Java API的此版本已经暴露出两个新类WorkbookMetadata和MetadataOptions，以及一个新的枚举MetadataType，现在可以通过这些类轻松操作文档属性（元数据），而无需创建Workbook的实例。WorkbookMetadata类轻量级，并且提供非常容易使用、高效的机制来[读取、写入和更新文档属性，而不影响整体性能](/cells/zh/java/using-workbookmetadata/)。 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Open Workbook metadata while specifying the appropriate MetadataType

MetadataOptions options = new MetadataOptions(MetadataType.DOCUMENT_PROPERTIES);

WorkbookMetadata metaWorkbook = new WorkbookMetadata("sample.xlsx", options);

//Set some properties

metaWorkbook.getCustomDocumentProperties().add("test", "test");

//Save the metadata information to the spreadsheet file

metaWorkbook.save(filePath);

{{< /highlight >}}
### **新增HtmlSaveOptions.ExportFrameScriptsAndProperties属性**
Aspose.Cells for Java 8.6.0已经暴露出HtmlSaveOptions.ExportFrameScriptsAndProperties属性，可以影响将电子表格转换为HTML格式时生成额外的脚本。使用默认设置，Aspose.Cells API将以与Excel应用程序导出相同的方式导出HTML格式的电子表格；即生成的HTML包含帧和条件注释，用于检测浏览器类型并相应地调整布局。HtmlSaveOptions.ExportFrameScriptsAndProperties属性的默认值为true，这意味着按照Excel标准进行导出。如果将属性设置为false，则API将不会[生成与帧和条件注释相关的脚本](/cells/zh/java/disable-exporting-frame-scripts-and-document-properties/)。在这种情况下，生成的HTML可以在任何浏览器中正确查看，但不能使用Aspose.Cells API导入。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Load the spreadsheet

Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties

HtmlSaveOptions options = new HtmlSaveOptions();

options.setExportFrameScriptsAndProperties(false);

//Save spreadsheet as HTML

book.save("output.html", options)

{{< /highlight >}}
### **新增Shape.MarcoName属性**
Aspose.Cells for Java 8.6.0已经暴露出Shape.MarcoName属性，可以用于[为表单控件分配VBA模块](/cells/zh/java/assign-macro-code-to-form-control/)（如按钮）以提供交互。该属性是字符串类型，因此可以接受模块名称并将其分配给控件。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

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
### **新增OoxmlSaveOptions.UpdateZoom属性**
随着v8.6.0的发布，Aspose.Cells for Java API已经暴露出OoxmlSaveOptions.UpdateZoom属性，该属性可以用于更新PageSetup.Zoom，如果PageSetup.FitToPagesWide和/或PageSetup.FitToPagesTall属性用于控制工作表的缩放。
