---
title: 格式化和修改命名范围
type: docs
weight: 85
url: /zh/net/format-and-modify-named-ranges/
---
## **格式范围**

### **将背景颜色和字体属性设置为命名范围**

要应用格式，定义一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象来指定样式设置并将其应用到[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)目的。

以下示例显示如何使用字体设置将纯色填充颜色（底纹颜色）设置为一个范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **为命名范围添加边框**

可以为一系列单元格而不是单个单元格添加边框。这[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)对象提供了一个[**设置轮廓边框**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)采用以下参数为单元格区域添加边框的方法：

-  border type，边框的类型，从中选择[**边框类型**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)枚举。
- 线条样式，线条样式，选自[**单元格边框类型**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)枚举。
- Color，线条颜色，从 Color 枚举中选择。

下面的示例演示如何将轮廓边框设置为范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

以下示例显示如何在区域中的每个单元格周围设置边框。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **重命名命名范围**

Aspose.Cells 允许您根据需要重命名命名范围。您可以获得命名范围并使用[**姓名.文字**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)属性。以下示例显示如何重命名命名范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **范围联盟**

Aspose.Cells提供[**范围.联合**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)为范围取并集的方法，该方法返回一个[*数组列表*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)目的。以下示例显示如何对范围进行联合。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **范围的交集**

Aspose.Cells 提供了[**范围.相交**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)方法相交两个范围。该方法返回一个[**范围**](https://reference.aspose.com/cells/net/aspose.cells/range)目的。要检查一个范围是否与另一个范围相交，请使用[**范围.相交**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)返回布尔值的方法。以下示例显示了如何与范围相交。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **在命名范围内合并 Cells**

Aspose.Cells提供[**范围.合并()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)合并区域中单元格的方法。以下示例显示如何合并命名区域的各个单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **删除命名范围**

Aspose.Cells 提供了[**名称集合.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat)擦除范围名称的方法。要清除范围的内容，请使用[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)方法。以下示例显示如何删除命名范围及其内容。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
