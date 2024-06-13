---
title: 从齿轮型智能图形中提取文本
type: docs
weight: 130
url: /zh/java/extract-text-from-the-gear-type-smartart-shape/
---

## **可能的使用场景**

Aspose.Cells 能够从 Gear Type Smart Art Shape 中提取文本。为此，您应该首先使用 [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--) 方法将 Smart Art Shape 转换为 Group Shape。然后使用 [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--) 方法获取形成组合形状的所有 Individual Shapes 的数组。最后，您可以在循环中逐个迭代所有 Individual Shapes 并使用 [**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text) 属性提取它们的文本。

## **从齿轮型智能图形中提取文本**

以下示例代码加载包含 齿轮类型智能图形 的 [示例Excel文件](67338510.xlsx)。然后提取其单个图形的文本，如上所述。请参考下面给出的代码的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **控制台输出**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
