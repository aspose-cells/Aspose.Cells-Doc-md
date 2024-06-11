---
title: 从齿轮型智能图形中提取文本
type: docs
weight: 500
url: /zh/net/extract-text-from-the-gear-type-smartart-shape/
---

## **可能的使用场景**

Aspose.Cells可以从齿轮型智能图形中提取文本。为了实现这一点，您应首先使用[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart)方法将智能图形转为组合形状。然后使用[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes)方法获取组合形状中形成的所有单个形状的数组。最后，您可以循环逐个迭代所有单个形状，并使用[**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)属性提取其文本。

## **从齿轮型智能图形中提取文本**

以下示例代码加载包含齿轮型智能图形的[sample Excel文件](67338483.xlsx)。然后按上述步骤从其各个形状中提取文本。请参阅下面提供的代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **控制台输出**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
