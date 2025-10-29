---
title: 通过 C++ 在 Golang 中设置字体
linktitle: 字体设置
type: docs
weight: 30
url: /zh/go-cpp/cells-font-settings/
description: Aspose.Cells是一个用于处理电子表格文件的C++库。它支持设置单元格的字体，允许用户自定义单元格的字体样式和属性。本文将介绍如何使用Aspose.Cells库设置单元格字体。
keywords: Aspose.Cells, Cells, 字体设置, 样式, 属性
---

{{% alert color="primary" %}}

通过更改字体设置，可以控制文本的外观。字体设置包括字体名称、样式、大小、颜色及其他效果。就像微软Excel一样，Aspose.Cells也支持配置单元格的字体设置。

{{% /alert %}}

## **配置字体设置**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)，它代表了一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)集合。[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)集合中的每个项代表了[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的对象。

Aspose.Cells提供了[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)类的[**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)和[**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle/)方法，用于获取和设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)类提供了用于配置字体设置的属性。

### **设置字体名称**

开发者可以通过使用 [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) 对象的 [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) 属性，为单元格内的文本应用任何字体。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings.go" >}}
### **将字体样式设置为粗体**

开发人员通过将[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)对象的[**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/)属性设置为**true**来使文本加粗。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-1.go" >}}
### **设置字体大小**

使用[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)对象的[**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/)属性设置字体大小。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-2.go" >}}
### **设置字体颜色**

使用 [**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/) 对象的 [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) 属性设置字体颜色。从颜色枚举（C++框架的一部分）中选择任意颜色并赋值给 [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) 属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-3.go" >}}
### **设置字体下划线类型**

使用[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)对象的[**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/)属性给文本添加下划线。Aspose.Cells在[**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/)枚举中提供了各种预定义的字体下划线类型。

|**字体下划线类型**|**描述**|
| :- | :- |
|Accounting| 单下划线|
|Double| 双下划线|
|DoubleAccounting| 双帐目下划线|
|None| 无下划线|
|Single| 单下划线|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-4.go" >}}
### **设置删除线效果**

通过将[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)对象的[**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/)属性设置为**true**应用删除线。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-5.go" >}}
### **设置下标效果**

通过将[**Style.GetFont()**](https://reference.aspose.com/cells/go-cpp/style/getfont/)对象的[**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/)属性设置为**true**应用下标。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-6.go" >}}
### **在字体上设置上标效果**

开发人员可以通过将[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)对象的[**IsSuperscript**](https://reference.aspose.com/cells/go-cpp/font/issuperscript/)属性设置为**true**在字体上应用上标效果。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FontSettings-7.go" >}}
## **高级主题**
- [在字体上应用上标和下标效果](/cells/zh/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
