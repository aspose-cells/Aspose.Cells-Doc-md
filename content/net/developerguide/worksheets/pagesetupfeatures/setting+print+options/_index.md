---
title : "Setting Print Options" 
description : "" 
weight : 16156 
toc : false
type: docs
url: /net/developerguide/worksheets/pagesetupfeatures/setting+print+options/
---

# Aspose.Cells for .NET : Setting Print Options


Microsoft Excel's page setup settings provide several print options (also referred to as sheet options) that allow users to control how worksheet pages are printed.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Setting Print Options](#setting-print-options)
    *   1.1 [Set Print Area](#set-print-area)
    *   1.2 [Set Print Titles](#set-print-titles)
    *   1.3 [Set Other Print Options](#set-other-print-options)
    *   1.4 [Set Page Order](#set-page-order)
{{< /panel >}}
 

 

## Setting Print Options

These print options allow users to:

*   Select a specific print area on a worksheet.
*   Print titles.
*   Print gridlines.
*   Print row/column headings.
*   Achieve draft quality.
*   Print comments.
*   Print cell errors.
*   Define page ordering.

Aspose.Cells supports all the print options offered by Microsoft Excel and developers can easily configure these options for worksheets using the properties offered by the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class. How these properties are used is discussed below in more detail.

### Set Print Area

By default, the print area incorporates all areas of the worksheet that contain data. Developers can establish a specific print area of the worksheet.

To select a specific print area, use the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class' [PrintArea](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printarea) property. Assign a cell range that defines the print area to this property.

### Set Print Titles

Aspose.Cells allows you to designate row and column headers to repeat on all pages of a printed worksheet. To do so, use the [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class' [PrintTitleColumns](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printtitlecolumns) and [PrintTitleRows](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printtitlerows) properties.

The rows or columns that will be repeated are defined by passing their row or column numbers. For example, rows are defined as $1:$2 and columns are defined as $A:$B.

### Set Other Print Options

The [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class also provides several other properties to set general print options as follows:

*   [PrintGridlines](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printgridlines): a Boolean property that defines whether to print gridlines or not print.
*   [PrintHeadings](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printheadings): a Boolean property that defines whether to print row and column headings or not.
*   [BlackAndWhite](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/blackandwhite): a Boolean property that defines whether to print the worksheet in black and white mode or not.
*   [PrintComments](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printcomments): defines whether to display the print comments on the worksheet or at the end of the worksheet.
*   [PrintDraft](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printdraft): a boolean property that defines whether to print the sheet without graphics..
*   [PrintErrors](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printerrors): defines whether to print cell errors as displayed, blank, dash or N/A.

To set the [PrintComments](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printcomments) and [PrintErrors](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printerrors) properties, Aspose.Cells also provides two enumerations, [PrintCommentsType](https://apireference.aspose.com/net/cells/aspose.cells/printcommentstype) , and [PrintErrorsType](https://apireference.aspose.com/net/cells/aspose.cells/printerrorstype) that contain pre-defined values to be assigned to the [PrintComments](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printcomments) and [PrintErrors](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/printerrors) properties respectively.

The pre-defined values in the [PrintCommentsType](https://apireference.aspose.com/net/cells/aspose.cells/printcommentstype) enumeration are listed below with their descriptions.

{{< table style="table-striped" >}}
|Print Comments Types|Description|
|:----|:----|
|PrintInPlace|Specifies to print comments as displayed on the worksheet.|
|PrintNoComments|Specifies not to print comments.|
|PrintSheetEnd|Specifies to print comments at the end of the worksheet.|
{{< /table >}}

The pre-defined values of [PrintErrorsType](https://apireference.aspose.com/net/cells/aspose.cells/printerrorstype) enumeration are listed below with their descriptions.

{{< table style="table-striped" >}}
|Print Errors Types|Description|
|:----|:----|
|PrintErrorsBlank|Specifies not to print errors.|
|PrintErrorsDash|Specifies to print errors as "--".|
|PrintErrorsDisplayed|Specifies to print errors as displayed.|
|PrintErrorsNA|Specifies to print errors as "#N/A".|
{{< /table >}}

### Set Page Order

The [PageSetup](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup) class provides the [Order](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/order) property that is used to order multiple pages of your worksheet to be printed. There are two possibilities to order the pages as follows.

*   **Down then over:** prints all the pages down before printing any pages to the right.
*   **Over then down:** prints pages left to right before printing the pages below.

Aspose.Cells provides an enumeration, [PrintOrderType](https://apireference.aspose.com/net/cells/aspose.cells/printordertype) that contains all pre-defined order types to be assigned to the [Go ](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/order "https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/order")property.

The pre-defined values of the [PrintOrderType](https://apireference.aspose.com/net/cells/aspose.cells/printordertype) enumeration are listed below.

{{< table style="table-striped" >}}
|Print Order Types|Description|
|:----|:----|
|DownThenOver|Represents printing order as down then over.|
|OverThenDown|Represents printing order as over then down.|
{{< /table >}}

