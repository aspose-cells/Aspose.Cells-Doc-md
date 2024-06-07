---
title: 从齿轮类型智能艺术形状中提取文本
type: docs
weight: 130
url: /zh/java/extract-text-from-the-gear-type-smartart-shape/
---

## **可能的使用场景**

Aspose.Cells可以从齿轮类型的智能艺术形状中提取文本。为此，您首先应使用[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()方法将智能艺术形状转换为分组形状。然后，您应使用[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()方法获取形成分组形状的所有单个形状的数组。最后，您可以循环逐个迭代所有单个形状，并使用[**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)属性提取它们的文本。

## **从齿轮类型智能艺术形状中提取文本**

以下示例代码加载包含齿轮类型智能艺术形状的示例Excel文件。然后从其各个形状中提取文本，如上所述。请查看下面给出的代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **控制台输出**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
