---
title: Aspose.Cells 8.6.0中的公共API更改
type: docs
weight: 200
url: /zh/java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.5.2到8.6.0的Aspose.Cells API的更改，可能对模块/应用程序开发人员感兴趣。它包括不仅有新的和更新的公共方法，[添加的类等。](/cells/zh/java/public-api-changes-in-aspose-cells-8-6-0/), 还包括Aspose.Cells背后行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **支持在不创建Workbook对象的情况下操纵元数据**
Aspose.Cells for Java API的此版本已公开了两个新类，即WorkbookMetadata和MetadataOptions，以及一个名为MetadataType的新枚举类型，现在允许在不创建Workbook实例的情况下操作文档属性（元数据）。WorkbookMetadata类轻量级，提供非常易于使用，高效的机制来[读取，编写和更新文档属性，而不影响整体性能](/cells/zh/java/using-workbookmetadata/)。 

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
### **新增 HtmlSaveOptions.ExportFrameScriptsAndProperties 属性**
Aspose.Cells for Java 8.6.0已公开了HtmlSaveOptions.ExportFrameScriptsAndProperties属性，可用于在将电子表格转换为HTML格式时影响创建附加脚本。使用默认设置，Aspose.Cells API将以与Excel应用程序执行导出相同的方式将电子表格导出为HTML，也就是说，结果HTML包含框架和条件注释，可检测浏览器类型并相应调整布局。HtmlSaveOptions.ExportFrameScriptsAndProperties属性的默认值为true，这意味着按照Excel标准进行导出。如果将属性设置为false，则API将不会[生成与框架和条件注释相关的脚本](/cells/zh/java/disable-exporting-frame-scripts-and-document-properties/)。在这种情况下，结果HTML可以在任何浏览器中正确查看，但不能使用Aspose.Cells API导入。

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
### **已添加 Shape.MarcoName 属性**
Aspose.Cells for Java 8.6.0已公开了Shape.MarcoName属性，可用于[将VBA模块分配给形式控件](/cells/zh/java/assign-macro-code-to-form-control/)，例如按钮，以提供交互。该属性是字符串类型，因此可以接受模块名称并将其分配给控件。

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
### **已添加 OoxmlSaveOptions.UpdateZoom 属性**
使用版本v8.6.0的Aspose.Cells for Java API已公开了OoxmlSaveOptions.UpdateZoom属性，可用于在使用PageSetup.FitToPagesWide和/或PageSetup.FitToPagesTall属性控制工作表缩放的情况下[更新PageSetup.Zoom](/cells/zh/java/update-zoom-setting-of-the-page-setup/)。
