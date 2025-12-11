---
title: Public API Changes in Aspose.Cells 8.6.0
type: docs
weight: 190
url: /net/public-api-changes-in-aspose-cells-8-6-0/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.5.2 to 8.6.0 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/net/public-api-changes-in-aspose-cells-8-6-0/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Metadata Manipulation Without Creating an Object of Workbook**
This release of Aspose.Cells for .NET API has exposed two new classes, namely **WorkbookMetadata** and **MetadataOptions**, along with a new enumeration **MetadataType** that now allows **manipulating** the document properties (metadata) without creating an instance of **Workbook**. The **WorkbookMetadata** class is **lightweight** and provides a **very easy-to-use, efficient mechanism to** [read, write & update document properties without impacting the **overall** performance](/cells/net/using-workbookmetadata/).

Following is the simple usage scenario.

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


### **Added HtmlSaveOptions.ExportFrameScriptsAndProperties Property**
Aspose.Cells for .NET 8.6.0 has exposed the **HtmlSaveOptions.ExportFrameScriptsAndProperties** property that can be used to influence the creation of additional scripts while converting the spreadsheets to HTML format. With default settings, the Aspose.Cells APIs export the spreadsheet in HTML format as the Excel application does, that is, the resultant HTML contains the frames and conditional comments, which detect the browser type and adjust the layout accordingly. The default value of **HtmlSaveOptions.ExportFrameScriptsAndProperties** property is **true**, which means the export is done as per Excel standards. However, if the property is set to **false**, the API will not [generate the scripts related to frames and conditional comments](/cells/net/disable-exporting-frame-scripts-and-document-properties/). In this case, the resultant HTML can be viewed correctly in any browser; however, it cannot be imported back using Aspose.Cells APIs.

Following is the simple usage scenario.

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


### **Added Shape.MacroName Property**
Aspose.Cells for .NET 8.6.0 has exposed the **Shape.MacroName** property that can be used to [assign any VBA module to a form control](/cells/net/assign-macro-to-form-control/) such **as** a Button in order to provide the interaction. The property is of type **string**, therefore it can accept the module name and **assign** it to the control.

Following is the simple usage scenario.

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


### **Added OoxmlSaveOptions.UpdateZoom Property**
With the release of **v8.6.0**, the Aspose.Cells for .NET API has exposed the **OoxmlSaveOptions.UpdateZoom** property that can be used to update the **PageSetup.Zoom** if **PageSetup.FitToPagesWide** and/or **PageSetup.FitToPagesTall** properties have been used to control the worksheet scaling.
