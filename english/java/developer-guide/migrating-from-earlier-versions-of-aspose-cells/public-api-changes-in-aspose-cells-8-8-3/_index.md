---
title: Public API Changes in Aspose.Cells 8.8.3
type: docs
weight: 300
url: /java/public-api-changes-in-aspose-cells-8-8-3/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.8.2 to 8.8.3 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for ActiveX Controls**
Aspose.Cells for Java 8.8.3 has exposed the addActiveXControl method that allows to add an ActiveX control to the ShapeCollection. The aforementioned method requires 7 parameters to specify the control type, location to place the control and size of the control. The type can be specified using the ControlType enumeration with following possible values.

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Adding ActiveX Controls to Worksheet](/cells/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Added LoadOptions.setPaperSize Method**
Aspose.Cells for Java 8.8.3 allows to set the default print paper size from the default printer's setting while using the newly exposed LoadOptions.setPaperSize method as demonstrated below. Please note, the input parameter to the aforementioned method is the value from the PaperSizeType enumeration containing the predefined paper sizes.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Load Spreadsheets with Specified Paper Size](/cells/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **Added Cell.getCharacters(flag) Method**
Aspose.Cells APIs allow to get the characters objects in the form of FontSetting array by using the Cell.getCharacters method. With this release, the Aspose.Cells for Java API has exposed an overloaded version of the Cell.getCharacters that could accept Boolean as parameter, indicating if the table style has to be applied on the cell if the cell is part of a ListObject.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **Added OleObject.AutoLoad Property**
Aspose.Cells for Java 8.8.3 has exposed the OleObject.AutoLoad property which allows to refresh the OleObject's image if the contents/data of the underlying object has been changed. The aforementioned property when set to true, forces the Excel application to refresh the OleObject's image when resultant spreadsheet is loaded.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Automatically Refresh OleObjects](/cells/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **Added HTMLLoadOptions.SupportDivTag Property**
Aspose.Cells for Java 8.8.3 has exposed the HTMLLoadOptions.SupportDivTag property which allows to parse the DIV tags embedded in TD tags while loading HTML files/snippet in Aspose.Cells object model. Boolean type property has the default value of false.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Support Inner DIV Tags while Loading HTML](/cells/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Added HtmlSaveOptions.ExportGridLines Property**
Aspose.Cells for Java 8.8.3 has exposed the HtmlSaveOptions.ExportGridLines property which allows to render the grid lines while exporting spreadsheet to HTML format. Boolean type property has the default value of false, however, when set to true, the API renders the grid lines for the available data range in HTML format.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Render Grid Lines to HTML](/cells/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Added ListObject.Comment Property**
Aspose.Cells APIs now allow to get and set the comments for an instance of ListObject. In order provide the aforementioned feature, the Aspose.Cells APIs have exposed the ListObject.Comment property.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Adding Comments for ListObjects](/cells/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **Removed APIs**
### **Removed Workbook.decrypt Method**
The said property was marked obsoleted some time back. This release has completely removed it from the public API. It is advised to set the WorkbookSettings.Password property to null in order to achieve the same goal.
{{< app/cells/assistant language="java" >}}
