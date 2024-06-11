---
title: 格式和修改命名区域
type: docs
weight: 85
url: /zh/net/format-and-modify-named-ranges/
---

## **格式化区域**

### **将背景颜色和字体属性设置为已命名范围**

要应用格式设置，定义一个[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象以指定样式设置，并将其应用于[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)对象。

以下示例显示如何为范围设置实填充颜色（着色颜色）并带有字体设置。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **为已命名范围添加边框**

可以为一系列的单元格添加边框，而不仅仅是单个单元格。[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)对象提供了一个[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)方法，以及以下参数来向单元格范围添加边框：

- 边框类型，边框的类型，从[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)枚举中选择。
- 线条样式，线条的样式，从[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)枚举中选择。
- 颜色，线条颜色，从Color枚举中选择。

以下示例显示如何将范围设置为轮廓边框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

以下示例显示了如何在范围中的每个单元格周围设置边框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **重命名命名范围**

Aspose.Cells允许您根据需要重命名已命名范围。您可以通过使用[**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)属性获取命名范围并将其重命名。以下示例显示如何重命名已命名范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **范围的并集**

Aspose.Cells提供了[**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)方法来获取范围的并集，该方法返回一个[ArrayList](https://docs.microsoft.com/zh-cn/dotnet/api/system.collections.arraylist?view=netframework-4.8)对象。以下示例显示了如何获取范围的并集。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **范围的交集**

Aspose.Cells提供[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)方法以求两个范围的交集。该方法返回[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)对象。要检查一个范围是否与另一个范围相交，请使用返回布尔值的[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)方法。以下示例显示如何求范围的交集。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **合并命名范围中的单元格**

Aspose.Cells提供[**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)方法以合并范围中的单元格。以下示例显示如何合并命名范围的单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **移除命名范围**

Aspose.Cells提供了[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat)方法来删除命名范围的名称。要清除范围的内容，使用[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)方法。以下示例显示了如何删除带有内容的命名范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
