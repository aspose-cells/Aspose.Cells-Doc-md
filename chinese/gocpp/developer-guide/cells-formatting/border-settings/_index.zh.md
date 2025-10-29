---
title: 通过 C++ 在 Golang 中设置边框
linktitle: 边框设置
description: 如何在C++中使用Aspose.Cells库设置单元格的边框样式和颜色。通过调整边框宽度、样式和颜色，可以更好地控制单元格的外观。
keywords: Aspose.Cells，单元格边框设置，C++，边框宽度，边框样式，边框颜色
type: docs
weight: 40
url: /zh/go-cpp/cells-border-settings/
---

## **向单元格添加边框**

微软Excel允许用户为单元格添加边框。边框类型取决于添加的位置。例如，上边框是添加到单元格顶部的位置。用户还可以修改线条样式和颜色。

借助 Aspose.Cells，开发人员可以以与 Microsoft Excel 中相同的灵活方式添加边框并自定义其外观。

### **向单元格添加边框**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)类，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，可访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合中的每个元素都代表一个[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的对象。

Aspose.Cells在[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类中提供了[**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)方法，用于设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)类还提供了添加边框的属性。

#### **向单元格添加边框**

开发者可以通过使用[**Style**](https://reference.aspose.com/cells/go-cpp/style/)对象的[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)集合为单元格添加边框。边框类型作为索引传入[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)集合。所有边框类型都在[**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/)枚举中预定义。

**边框枚举**

| **边框类型** | **描述** |
|------------------|-----------------|
| BottomBorder     | 底部边框线 |
| DiagonalDown     | 从左上到右下的斜线 |
| DiagonalUp       | 从左下到右上的斜线 |
| LeftBorder       | 左边框线 |
| RightBorder      | 右边框线 |
| TopBorder        | 顶部边框线 |

[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)集合存储所有边框。[**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)集合中的每个边框由[**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/)对象表示，提供两个属性，[**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/)和[**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/)，分别设置边框的线色和线样式。

要设置边框的线色，可以使用Color枚举选择颜色，并将其赋值给Border对象的Color属性。

通过从 [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/) 枚举中选择线条样式来设置边框的线条样式。

**CellBorderType枚举**

| **线条样式** | **说明** |
|------------------------|-------------------------------|
| DashDot               | 细点划线                   |
| DashDotDot            | 细点点划线                 |
| Dashed                | 虚线                     |
| Dotted                | 点线                     |
| Double                | 双线                     |
| Hair                  | 细线                     |
| MediumDashDot         | 中等点划线                 |
| MediumDashDotDot      | 中等点点划线               |
| MediumDashed          | 中等虚线                   |
| None                  | 无线                     |
| Medium                | 中等线                   |
| SlantedDashDot        | 斜点划线（中等）          |
| Thick                 | 厚线                     |
| Thin                  | 薄线                     |

选择一种线条样式，然后将其分配给 [**Border**](https://reference.aspose.com/cells/go-cpp/border/) 对象的 [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/) 属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

你应该同时设置线条样式和颜色。两个对角线边框线应具有相同的线条样式和颜色。

{{% /alert %}}

#### **向单元格范围添加边框**

也可以对一范围单元格添加边框，而不仅仅是单个单元格。首先，通过调用 [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) 集合的 [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/) 方法创建一个单元格范围。它接受以下参数：

- 第一行，范围的第一行。
- 第一列，表示范围的第一列。
- 行数，范围中的行数。
- 列数，范围中的列数。

[**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/) 方法返回一个 [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 对象，其中包含指定范围的单元格。[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 对象提供一个 [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) 方法，可以接受以下参数，为单元格范围添加边框：

- **边框类型**，选择自 [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/) 枚举的边框类型。
- **线条样式**，选择自 [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/) 枚举的边框线条样式。
- **颜色**，线条颜色，从Color枚举中选择。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
