---
title: Setting Print Options
type: docs
weight: 40
url: /net/setting-print-options/
description: This article demonstrates how to programmatically set the Print Options of the Excel Worksheet Page Setup feature using the C# API and .NET Library. You can set the Print Area, Print Titles and Page Order.
keywords: set excel print area c#, set exce print titles c#, set excel page order c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel's page setup settings provide several print options (also referred to as sheet options) that allow users to control how worksheet pages are printed.

{{% /alert %}}

## **Setting Print Options**

These print options allow users to:

- Select a specific print area on a worksheet.
- Print titles.
- Print gridlines.
- Print row/column headings.
- Achieve draft quality.
- Print comments.
- Print cell errors.
- Define page ordering.

Aspose.Cells supports all the print options offered by Microsoft Excel and developers can easily configure these options for worksheets using the properties offered by the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class. How these properties are used is discussed below in more detail.

### **Set Print Area**

By default, the print area incorporates all areas of the worksheet that contain data. Developers can establish a specific print area of the worksheet.

To select a specific print area, use the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class' [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea) property. Assign a cell range that defines the print area to this property.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Set Print Titles**

Aspose.Cells allows you to designate row and column headers to repeat on all pages of a printed worksheet. To do so, use the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class' [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) and [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows) properties.

The rows or columns that will be repeated are defined by passing their row or column numbers. For example, rows are defined as $1:$2 and columns are defined as $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Set Other Print Options**

The [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class also provides several other properties to set general print options as follows:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): a Boolean property that defines whether to print gridlines or not print.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): a Boolean property that defines whether to print row and column headings or not.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): a Boolean property that defines whether to print the worksheet in black and white mode or not.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): defines whether to display the print comments on the worksheet or at the end of the worksheet.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): a boolean property that defines whether to print the sheet without graphics..
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): defines whether to print cell errors as displayed, blank, dash or N/A.

To set the [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) and [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) properties, Aspose.Cells also provides two enumerations, [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , and [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) that contain pre-defined values to be assigned to the [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) and [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) properties respectively.

The pre-defined values in the [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) enumeration are listed below with their descriptions.

|**Print Comments Types**|**Description**|
| :- | :- |
|PrintInPlace|Specifies to print comments as displayed on the worksheet.|
|PrintNoComments|Specifies not to print comments.|
|PrintSheetEnd|Specifies to print comments at the end of the worksheet.|

The pre-defined values of [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) enumeration are listed below with their descriptions.



|**Print Errors Types**|**Description**|
| :- | :- |
|PrintErrorsBlank|Specifies not to print errors.|
|PrintErrorsDash|Specifies to print errors as "--".|
|PrintErrorsDisplayed|Specifies to print errors as displayed.|
|PrintErrorsNA|Specifies to print errors as "#N/A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Set Page Order**

The [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class provides the [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) property that is used to order multiple pages of your worksheet to be printed. There are two possibilities to order the pages as follows.

- **Down then over:** prints all the pages down before printing any pages to the right.
- **Over then down:** prints pages left to right before printing the pages below.

Aspose.Cells provides an enumeration, [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) that contains all pre-defined order types.

The pre-defined values of the [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) enumeration are listed below.

|**Print Order Types**|**Description**|
| :- | :- |
|DownThenOver|Represents printing order as down then over.|
|OverThenDown|Represents printing order as over then down.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
