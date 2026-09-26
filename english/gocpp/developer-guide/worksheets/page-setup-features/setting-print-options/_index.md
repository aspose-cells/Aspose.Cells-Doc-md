---
title: Setting Print Options with Golang via C++
linktitle: Setting Print Options
type: docs
weight: 40
url: /go-cpp/setting-print-options/
description: This article demonstrates how to programmatically set the Print Options of the Excel Worksheet Page Setup feature using the Go API and Library. You can set the Print Area, Print Titles, and Page Order.
keywords: set excel print area c++, set excel print titles c++, set excel page order c++
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
- Print in draft quality.
- Print comments.
- Print cell errors.
- Define page ordering.

Aspose.Cells supports all the print options offered by Microsoft Excel, and developers can easily configure these options for worksheets using the properties offered by the [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class. How these properties are used is discussed below in more detail.

### **Set Print Area**

By default, the print area incorporates all areas of the worksheet that contain data. Developers can establish a specific print area of the worksheet.

To select a specific print area, use the [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class's [**GetPrintArea()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprintarea/) method. Assign a cell range that defines the print area to this property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingPrintOptions.go" >}}

### **Set Print Titles**

Aspose.Cells allows you to designate row and column headers to repeat on all pages of a printed worksheet. To do so, use the [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class's [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprinttitlecolumns/) and [**GetPrintTitleRows()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprinttitlerows/) properties.

The rows or columns that will be repeated are defined by passing their row or column numbers. For example, rows are defined as $1:$2 and columns are defined as $A:$B.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingPrintOptions-1.go" >}}

### **Set Other Print Options**

The [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class also provides several other properties to set general print options as follows:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprintgridlines/): a Boolean property that defines whether to print gridlines or not.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprintheadings/): a Boolean property that defines whether to print row and column headings or not.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getblackandwhite/): a Boolean property that defines whether to print the worksheet in black and white mode or not.
- [**GetPrintComments()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprintcomments/): defines whether to print comments on the worksheet or at the end of the worksheet.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprintdraft/): a Boolean property that defines whether to print the sheet without graphics.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprinterrors/): defines whether to print cell errors as displayed, blank, dash, or N/A.

To set the [**GetPrintComments()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprintcomments/) and [**GetPrintErrors()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getprinterrors/) properties, Aspose.Cells also provides two enumerations, [**PrintCommentsType**](https://reference.aspose.com/cells/go-cpp/printcommentstype/) and [**PrintErrorsType**](https://reference.aspose.com/cells/go-cpp/printerrorstype/) that contain pre‑defined values to be assigned to those properties respectively.

The pre‑defined values in the [**PrintCommentsType**](https://reference.aspose.com/cells/go-cpp/printcommentstype/) enumeration are listed below with their descriptions.

| **Print Comments Types** | **Description** |
| :- | :- |
| PrintInPlace | Specifies to print comments as displayed on the worksheet. |
| PrintNoComments | Specifies not to print comments. |
| PrintSheetEnd | Specifies to print comments at the end of the worksheet. |

The pre‑defined values of [**PrintErrorsType**](https://reference.aspose.com/cells/go-cpp/printerrorstype/) enumeration are listed below with their descriptions.

| **Print Errors Types** | **Description** |
| :- | :- |
| PrintErrorsBlank | Specifies not to print errors. |
| PrintErrorsDash | Specifies to print errors as “--”. |
| PrintErrorsDisplayed | Specifies to print errors as displayed. |
| PrintErrorsNA | Specifies to print errors as “#N/A”. |

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingPrintOptions-2.go" >}}

### **Set Page Order**

The [**PageSetup**](https://reference.aspose.com/cells/go-cpp/pagesetup/) class provides the [**GetOrder()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getorder/) property, which is used to specify the order of multiple pages of your worksheet to be printed. There are two possible orders:

- **Down then over:** prints all the pages downward before printing any pages to the right.
- **Over then down:** prints pages left to right before printing the pages below.

Aspose.Cells provides an enumeration, [**PrintOrderType**](https://reference.aspose.com/cells/go-cpp/printordertype/) that contains all pre‑defined order types.

The pre‑defined values of the [**PrintOrderType**](https://reference.aspose.com/cells/go-cpp/printordertype/) enumeration are listed below.

| **Print Order Types** | **Description** |
| :- | :- |
| DownThenOver | Represents printing order as down then over. |
| OverThenDown | Represents printing order as over then down. |

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingPrintOptions-3.go" >}}
{{< app/cells/assistant language="go" >}}
