---
title: 格式化和修改已命名范围
type: docs
weight: 85
url: /zh/net/format-and-modify-named-ranges/
---

## **格式化范围**

### **将背景颜色和字体属性设置给命名范围**

要应用格式，定义一个对象以指定样式设置，并将其应用于对象。

以下示例显示如何设置具有字体设置的实填充颜色（阴影颜色）到某个范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **向已命名范围添加边框**

可以向一个单元格范围而不仅仅是单个单元格添加边框。对象提供一个方法，该方法采用以下参数向单元格范围添加边框：

- 边框类型，从枚举中选择的边框类型。
- 线条样式，从枚举中选择的线条样式。
- 颜色，选自Color枚举的线条颜色。

以下示例显示如何将轮廓边框设置为区域。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

以下示例显示如何设置范围内每个单元格周围的边框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **重命名命名范围**

Aspose.Cells允许您根据需要重命名命名范围。您可以使用[**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)属性获取命名范围并对其重命名。以下示例显示如何重命名命名范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **区域并集**

Aspose.Cells提供[**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)方法来对区域进行并集运算，该方法返回一个*ArrayList*对象。以下示例显示如何对区域进行并集运算。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **区域交集**

Aspose.Cells提供[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)方法来求两个区域的交集。该方法返回一个[**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)对象。要检查一个区域是否与另一个区域相交，请使用返回布尔值的[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)方法。以下示例显示如何求交集。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **合并命名范围中的单元格**

Aspose.Cells提供[**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)方法来合并范围中的单元格。以下示例显示如何合并命名范围中的单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **删除命名范围**

Aspose.Cells提供[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat)方法来擦除区域的名称。要清除区域的内容，请使用[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)方法。以下示例显示如何删除命名范围及其内容。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
