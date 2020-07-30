---
title : "Public API Changes in Aspose.Cells 8.6.0" 
description : "" 
weight : 16766 
toc : false
type: docs
url: /net/developerguide/knowledgebase/migratingfromearliervs/public+api+changes+in+aspose.cells+8.6.0/
---

# Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.6.0


This document describes the changes to the Aspose.Cells API from version 8.5.2 to 8.6.0 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](https://docs2.aspose.com/cells/net/developerguide/knowledgebase/migratingfromearliervs/public+api+changes+in+aspose.cells+8.6.0), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Support for Metadata Manipulation Without Creating an Object of Workbook

This release of Aspose.Cells for .NET API has exposed two new classes namely `WorkbookMetadata` & `MetadataOptions` along with a new enumeration `MetadataType` that now allows manipulate the document properties (metadata) without creating an instance of `Workbook`. The `WorkbookMetadata` class is light weight and provides very easy to use, efficient mechanism to [read, write & update document properties without impacting the over all performance](http://www.aspose.com/docs/display/cellsnet/Using+WorkbookMetadata).

Following is the simple usage scenario.

**C#**

{{< code lang="c#" >}}
//Load a spreadsheet with WorkbookMetadata while specifying appropriate MetadataType
MetadataOptions options = new MetadataOptions(MetadataType.DocumentProperties);
WorkbookMetadata metadata = new WorkbookMetadata(filePath, options);

//Set some properties
metadata.CustomDocumentProperties.Add("test", "test");

//Save the metadata info to spreadsheet
metadata.Save(filePath);
{{< /code >}}

### Property HtmlSaveOptions.ExportFrameScriptsAndProperties Added

Aspose.Cells for .NET 8.6.0 has exposed the `HtmlSaveOptions.ExportFrameScriptsAndProperties` property that can be used to influence the creation of additional scripts while converting the spreadsheets to HTML format. With default settings, the Aspose.Cells APIs export the spreadsheet in HTML format as Excel application does the export, that is; the resultant HTML contains the frames and conditional comments, that detects the browser type & adjusts the layout accordingly. The default value of `HtmlSaveOptions.ExportFrameScriptsAndProperties` property is true, that means; the export is done as per Excel standards. However, if the property is set to false, the API will not [generate the scripts related to frames and conditional comments](http://www.aspose.com/docs/display/cellsnet/Disable+exporting+frame+scripts+and+document+properties). In this case, the resultant HTML can be viewed correctly in any browser, however, it cannot be imported back using Aspose.Cells APIs.

Following is the simple usage scenario.

**C#**

{{< code lang="c#" >}}
//Load the spreadsheet
Workbook book = new Workbook(filePath);

//Disable exporting frame scripts and document properties
HtmlSaveOptions options = new HtmlSaveOptions();
options.ExportFrameScriptsAndProperties = false;

//Save spreadsheet as HTML
book.Save("output.html", options);
{{< /code >}}

### Property Shape.MarcoName Added

Aspose.Cells for .NET 8.6.0 has exposed the `Shape.MarcoName` property that can be used to [assign any VBA module to a form control](http://www.aspose.com/docs/display/cellsnet/Assign+Macro+to+Form+Control) such a Button in order to provide the interaction. The property is of type string therefore it can accept the module name and assigns it to the control.

Following is the simple usage scenario.

**C#**

{{< code lang="c#" >}}
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
{{< /code >}}

### Property OoxmlSaveOptions.UpdateZoom Added

With the release of v8.6.0, the Aspose.Cells for .NET API has exposed the `OoxmlSaveOptions.UpdateZoom` property that can be used to update the `PageSetup.Zoom` if `PageSetup.FitToPagesWide` and/or `PageSetup.FitToPagesTall` properties have been used to control the Worksheet scaling.

