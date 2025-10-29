---
title: 格式和修改命名区域
type: docs
weight: 85
url: /zh/python-net/format-and-modify-named-ranges/
description: 本文演示了如何通过Aspose.Cells for Python via .NET API格式和修改命名区域。
keywords: Python Excel库，Python格式和修改命名区域，Python设置命名区域的背景颜色和字体属性，Python向命名区域添加边框，Python重命名命名区域，Python区域的并集，Python区域的交集，Python合并命名区域中的单元格。
---

## **格式化区域**

### **如何为命名区域设置背景颜色和字体属性**

要应用格式设置，定义一个[**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)对象以指定样式设置，并将其应用于[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)对象。

以下示例显示如何为范围设置实填充颜色（着色颜色）并带有字体设置。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **如何为命名区域添加边框**

可以为一系列的单元格添加边框，而不仅仅是单个单元格。[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)对象提供了一个[**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor)方法，以及以下参数来向单元格范围添加边框：

- 边框类型，边框的类型，从[**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype)枚举中选择。
- 线条样式，线条的样式，从[**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)枚举中选择。
- 颜色，线条颜色，从Color枚举中选择。

以下示例显示如何将范围设置为轮廓边框。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **如何重命名已命名范围**

Aspose.Cells允许您根据需要重命名已命名范围。您可以通过使用[**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text)属性获取命名范围并将其重命名。以下示例显示如何重命名已命名范围。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **如何取并集范围**

Aspose.Cells提供[**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range)方法以获取范围的并集。以下示例显示如何获取范围的并集。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **如何求范围的交集**

Aspose.Cells提供[**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range)方法以求两个范围的交集。该方法返回[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)对象。要检查一个范围是否与另一个范围相交，请使用返回布尔值的[**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range)方法。以下示例显示如何求范围的交集。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **如何合并命名范围中的单元格**

Aspose.Cells提供[**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#)方法以合并范围中的单元格。以下示例显示如何合并命名范围的单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
