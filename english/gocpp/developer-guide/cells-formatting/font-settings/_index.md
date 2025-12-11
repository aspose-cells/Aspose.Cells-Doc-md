---
title: Font Settings with Golang via C++
linktitle: Font Settings
type: docs
weight: 30
url: /go-cpp/cells-font-settings/
description: Aspose.Cells is a C++ library for working with spreadsheet files. It supports setting the font settings of cells, allowing users to customize the font style and properties of cells. This article will introduce how to use the Aspose.Cells library to set cell font settings.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
---

{{% alert color="primary" %}}

The look and feel of a text can be controlled by changing font settings. The font settings may include the name, style, size, color, and other effects of the fonts. Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.

{{% /alert %}}

## **Configuring Font Settings**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection. Each item in the [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

Aspose.Cells provides the [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) class' [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/) methods which are used to get and set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides properties for configuring font settings.

### **Setting Font Name**

Developers can apply any font to text inside a cell by using the [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) object’s [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **Setting Font Style to Bold**

Developers can make text bold by setting the [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) object’s [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) property to **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **Setting Font Size**

Set the font size with the [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) object’s [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **Setting Font Color**

Use the [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) object’s [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) property to set the font color. Select any color from the Color enumeration (part of the C++ framework) and assign it to the [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) property.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **Setting Font Underline Type**

Use the [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) object’s [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) property to underline text. Aspose.Cells offers various pre-defined font underline types in the [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/) enumeration.

| **Font Underline Types** | **Description**                |
| ------------------------ | ------------------------------ |
| Accounting               | A single accounting underline  |
| Double                   | Double underline                |
| DoubleAccounting         | Double accounting underline     |
| None                     | No underline                    |
| Single                   | A single underline              |

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **Setting Strikeout Effect**

Apply strikeout by setting the [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) object’s [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) property to **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **Setting Subscript Effect**

Apply subscript by setting the [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) object’s [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) property to **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **Setting Superscript Effect on Font**

Developers can apply the superscript effect on the font by setting the [**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/) property of the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object to **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **Advanced topics**
- [Apply Superscript and Subscript Effects on Fonts](/cells/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Get a List of Fonts used in a Spreadsheet or Workbook](/cells/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)