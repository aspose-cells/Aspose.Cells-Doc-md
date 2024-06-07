---
title: 从齿轮类型智能艺术形状中提取文本
type: docs
weight: 500
url: /zh/net/extract-text-from-the-gear-type-smartart-shape/
---

## **可能的使用场景**

Aspose.Cells可以从Gear Type智能艺术形状中提取文本。要实现此目的，您首先应该使用[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart)方法将智能艺术形状转换为组形状。然后，您应该使用[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes)方法获取形成组形状的所有个体形状的数组。最后，您可以循环逐个遍历所有个体形状并使用[**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性提取它们的文本。

## **从齿轮类型智能艺术形状中提取文本**

以下示例代码加载了包含Gear Type智能艺术形状的[sample Excel文件](67338483.xlsx)。然后从各自的形状中提取文本，如上面讨论的。请参考下面给出的代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **控制台输出**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
