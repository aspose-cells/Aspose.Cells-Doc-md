---
title: Number Settings with Golang via C++
linktitle: Number Settings
description: Aspose.Cells is a C++ library for working with spreadsheet files that supports many different cell number settings. This article will introduce how to use the Aspose.Cells library to manage the number settings of cells so that users can adjust the number format in the spreadsheet as needed.
keywords: Aspose.Cells, C++ library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /go-cpp/cells-number-settings/
---

## **How to Set Display Formats of Numbers and Dates**

A very strong feature of Microsoft Excel is that it allows users to set the display formats of numeric values and dates. We know that numeric data can be used to represent different types, including decimal, currency, percentage, fraction, or accounting values. All these numerical values are displayed in different formats depending on the type of information they represent. Similarly, there are many formats in which a date or time can be displayed.  
Aspose.Cells supports this functionality and allows developers to set any display format for a number or date.

### **How to Set Display Formats in Microsoft Excel**

To set display formats in Microsoft Excel:

1. Right‑click any cell.  
2. Select **Format Cells**. A dialog will appear that is used to set the display formats of any kind of value.

On the left side of the dialog, there are many categories of values like **General**, **Number**, **Currency**, **Accounting**, **Date**, **Time**, **Percentage**, etc. Aspose.Cells supports all of these display formats.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

Aspose.Cells provides [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) methods for the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class. These methods are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides useful properties for dealing with the display formats of numbers and dates.

### **How to Use Built-in Number Formats**

Aspose.Cells offers built‑in number formats to configure the display formats of numbers and dates. These formats can be applied by using the [**Number**](https://reference.aspose.com/cells/go-cpp/style/getnumber/) property of the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object. All built‑in number formats are assigned unique numeric values. Developers can assign any desired numeric value to the [**Number**](https://reference.aspose.com/cells/go-cpp/style/getnumber/) property of the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object to apply the display format. This approach is fast. The built‑in number formats supported by Aspose.Cells are listed below.

| **Value** | **Type**      | **Format String**          |
|-----------|---------------|----------------------------|
| 0         | General       | General                    |
| 1         | Decimal       | 0                          |
| 2         | Decimal       | 0.00                       |
| 3         | Decimal       | #,##0                      |
| 4         | Decimal       | #,##0.00                   |
| 5         | Currency      | $#,##0;$-#,##0              |
| 6         | Currency      | $#,##0;[Red]$-#,##0        |
| 7         | Currency      | $#,##0.00;$-#,##0.00       |
| 8         | Currency      | $#,##0.00;[Red]$-#,##0.00 |
| 9         | Percentage    | 0%                         |
| 10        | Percentage    | 0.00%                      |
| 11        | Scientific    | 0.00E+00                   |
| 12        | Fraction      | # ?/?                      |
| 13        | Fraction      | # */*                      |
| 14        | Date          | m/d/yyyy                   |
| 15        | Date          | d-mmm-yy                   |
| 16        | Date          | d-mmm                      |
| 17        | Date          | mmm-yy                     |
| 18        | Time          | h:mm AM/PM                 |
| 19        | Time          | h:mm:ss AM/PM              |
| 20        | Time          | h:mm                       |
| 21        | Time          | h:mm:ss                    |
| 22        | Time          | m/d/yy h:mm                |
| 37        | Currency      | #,##0;-#,##0               |
| 38        | Currency      | #,##0;[Red]-#,##0          |
| 39        | Currency      | #,##0.00;-#,##0.00         |
| 40        | Currency      | #,##0.00;[Red]-#,##0.00    |
| 41        | Accounting    | _ * #,##0_ ;_ * "_" ;_ @_ |
| 42        | Accounting    | _ $* #,##0_ ;_ $* "_" ;_ @_|
| 43        | Accounting    | _ * #,##0.00_ ;_ * "??_ ;_ @_|
| 44        | Accounting    | _ $* #,##0.00_ ;_ $* "??_ ;_ @_|
| 45        | Time          | mm:ss                      |
| 46        | Time          | h:mm:ss                    |
| 47        | Time          | mm:ss.0                    |
| 48        | Scientific    | ##0.0E+00                  |
| 49        | Text          | @                          |

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberSettings.go" >}}

### **How to Use Custom Number Formats**

To define your own customized format string for setting the display format, use the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's [**Custom**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) property. This approach is not as fast as using preset formats, but it is more flexible.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberSettings-1.go" >}}
{{% alert color="primary" %}}

If you use the [**Custom**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) property to set the number format, any previous format set using the [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) property is overridden and vice versa.

{{% /alert %}}

## **Advanced Topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/go-cpp/check-custom-number-format-when-setting-style-custom-property/)
- [List of Supported Number Formats](/cells/go-cpp/list-of-supported-number-formats/)
- [Render Custom Date Format Pattern g and ge mm dd](/cells/go-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Specify Custom Number Decimal and Group Separators for Workbook](/cells/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Specifying DBNum Custom Pattern Formatting](/cells/go-cpp/specifying-dbnum-custom-pattern-formatting/)