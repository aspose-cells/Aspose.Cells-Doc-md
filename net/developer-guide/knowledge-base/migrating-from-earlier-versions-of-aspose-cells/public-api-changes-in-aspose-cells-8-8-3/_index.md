---
title: Public API Changes in Aspose.Cells 8.8.3
type: docs
weight: 290
url: /net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.8.2 to 8.8.3 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for ActiveX Controls**
Aspose.Cells for .NET 8.8.3 has exposed the AddActiveXControl method that allows to add an ActiveX control to the ShapeCollection. The aforementioned method requires 7 parameters to specify the control type, location to place the control and size of the control. The type can be specified using the ControlType enumeration with following possible values.

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Adding ActiveX Controls to Worksheet](/cells/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Added LoadOptions.SetPaperSize Method**
Aspose.Cells for .NET 8.8.3 allows to set the default print paper size from the default printer's setting while using the newly exposed LoadOptions.SetPaperSize method as demonstrated below. Please note, the input parameter to the aforementioned method is the value from the PaperSizeType enumeration containing the predefined paper sizes.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Load Spreadsheets with Specified Paper Size](/cells/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **Added Cell.GetCharacters(flag) Method**
Aspose.Cells APIs allow to get the characters objects in the form of FontSetting array by using the Cell.GetCharacters method. With this release, the Aspose.Cells for .NET API has exposed an overloaded version of the Cell.GetCharacters that could accept Boolean as parameter, indicating if the table style has to be applied on the cell if the cell is part of a ListObject.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **Added OleObject.AutoLoad Property**
Aspose.Cells for .NET 8.8.3 has exposed the OleObject.AutoLoad property which allows to refresh the OleObject's image if the contents/data of the underlying object has been changed. The aforementioned property when set to true, forces the Excel application to refresh the OleObject's image when resultant spreadsheet is loaded.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Automatically Refresh OleObjects](/cells/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **Added HTMLLoadOptions.SupportDivTag Property**
Aspose.Cells for .NET 8.8.3 has exposed the HTMLLoadOptions.SupportDivTag property which allows to parse the DIV tags embedded in TD tags while loading HTML files/snippet in Aspose.Cells object model. Boolean type property has the default value of false.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Support Inner DIV Tags while Loading HTML](/cells/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **Added HtmlSaveOptions.ExportGridLines Property**
Aspose.Cells for .NET 8.8.3 has exposed the HtmlSaveOptions.ExportGridLines property which allows to render the grid lines while exporting spreadsheet to HTML format. Boolean type property has the default value of false, however, when set to true, the API renders the grid lines for the available data range in HTML format.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Render Grid Lines to HTML](/cells/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Added ListObject.Comment Property**
Aspose.Cells APIs now allow to get and set the comments for an instance of ListObject. In order provide the aforementioned feature, the Aspose.Cells APIs have exposed the ListObject.Comment property.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Adding Comments for ListObjects](/cells/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Added GridWeb.SessionStorePath Property**
Aspose.Cells.GridWeb for .NET 8.8.3 has exposed the SessionStorePath property which allows to get or set the session store path when Session Mode is ViewState. The aforementioned property gets or sets the relative path to the current web application Base Directory.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Specify Path for Temporary Session Files](/cells/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

Following is the simple usage scenario.
## **Removed APIs**
### **Removed Workbook.Decrypt Method**
The said property was marked obsoleted some time back. This release has completely removed it from the public API. It is advised to set the WorkbookSettings.Password property to null in order to achieve the same goal.
