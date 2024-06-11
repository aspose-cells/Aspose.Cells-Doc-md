---
title: 格式化和修改已命名范围
type: docs
weight: 85
url: /zh/python-net/format-and-modify-named-ranges/
description: 本文展示如何通过Aspose.Cells for Python通过.NET API格式化和修改命名范围。
keywords: Python Excel库，Python格式化和修改命名范围，Python设置命名范围的背景色和字体属性，Python向命名范围添加边框，Python重命名命名范围，Python范围的并集，Python范围的交集，Python合并命名范围。
---

## **格式化范围**

### **如何为命名范围设置背景颜色和字体属性**

要应用格式，定义一个对象以指定样式设置，并将其应用于对象。

以下示例显示如何设置具有字体设置的实填充颜色（阴影颜色）到某个范围。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **如何向命名范围添加边框**

可以向一个单元格范围而不仅仅是单个单元格添加边框。对象提供一个方法，该方法采用以下参数向单元格范围添加边框：

- 边框类型，从枚举中选择的边框类型。
- 线条样式，从枚举中选择的线条样式。
- 颜色，选自Color枚举的线条颜色。

以下示例显示如何将轮廓边框设置为区域。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **如何重命名命名范围**

Aspose.Cells允许您根据需要重命名命名范围。您可以使用[**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text)属性获取命名范围并对其重命名。以下示例显示如何重命名命名范围。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **如何取范围的并集**

Aspose.Cells提供[**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range)方法以获得范围的并集。以下示例显示如何获得范围的并集。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **如何取范围的交集**

Aspose.Cells提供[**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range)方法来求两个区域的交集。该方法返回一个[**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)对象。要检查一个区域是否与另一个区域相交，请使用返回布尔值的[**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range)方法。以下示例显示如何求交集。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **如何合并命名范围中的单元格**

Aspose.Cells提供[**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#)方法来合并范围中的单元格。以下示例显示如何合并命名范围中的单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
