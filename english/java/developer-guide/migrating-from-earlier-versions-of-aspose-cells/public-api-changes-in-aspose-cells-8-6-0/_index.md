---
title: Public API Changes in Aspose.Cells 8.6.0
type: docs
weight: 200
url: /java/public-api-changes-in-aspose-cells-8-6-0/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.5.2 to 8.6.0 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/java/public-api-changes-in-aspose-cells-8-6-0/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Metadata Manipulation Without Creating an Object of Workbook**
This release of Aspose.Cells for Java API has exposed two new classes namely WorkbookMetadata & MetadataOptions along with a new enumeration MetadataType that now allows to manipulate the document properties (metadata) without creating an instance of Workbook. The WorkbookMetadata class is light weight and provides very easy to use, efficient mechanism to [read, write & update document properties without impacting the over all performance](/cells/java/using-workbookmetadata/). 

Following is the simple usage scenario.

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
### **Property HtmlSaveOptions.ExportFrameScriptsAndProperties Added**
Aspose.Cells for Java 8.6.0 has exposed the HtmlSaveOptions.ExportFrameScriptsAndProperties property that can be used to influence the creation of additional scripts while converting the spreadsheets to HTML format. With default settings, the Aspose.Cells APIs export the spreadsheet in HTML format as Excel application does the export, that is; the resultant HTML contains the frames and conditional comments, that detects the browser type & adjusts the layout accordingly. The default value of HtmlSaveOptions.ExportFrameScriptsAndProperties property is true, that means; the export is done as per Excel standards. If the property is set to false, the API will not [generate the scripts related to the frames and conditional comments](/cells/java/disable-exporting-frame-scripts-and-document-properties/). In this case, the resultant HTML can be viewed correctly in any browser, however, it cannot be imported back using Aspose.Cells APIs.

Following is the simple usage scenario.

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
### **Property Shape.MarcoName Added**
Aspose.Cells for Java 8.6.0 has exposed the Shape.MarcoName property that can be used to [assign a VBA module to a form control](/cells/java/assign-macro-code-to-form-control/) such a Button in order to provide the interaction. The property is of type string therefore it can accept the module name and assigns it to the control.

Following is the simple usage scenario.

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
### **Property OoxmlSaveOptions.UpdateZoom Added**
With the release of v8.6.0, the Aspose.Cells for Java API has exposed the OoxmlSaveOptions.UpdateZoom property that can be used to update the PageSetup.Zoom if PageSetup.FitToPagesWide and/or PageSetup.FitToPagesTall properties have been used to control the Worksheet scaling.
