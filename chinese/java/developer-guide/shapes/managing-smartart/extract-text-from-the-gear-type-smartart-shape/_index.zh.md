﻿---
title: 从齿轮类型 SmartArt 形状中提取文本
type: docs
weight: 130
url: /zh/java/extract-text-from-the-gear-type-smartart-shape/
---
## **可能的使用场景**

Aspose.Cells 可以从齿轮类型智能艺术形状中提取文本。为此，您应该首先使用[**形状.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()） 方法。然后你应该使用[**GroupShape.getGroupedShapes() 方法**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()） 方法。最后，您可以在一个循环中一个一个地迭代所有单独的形状，并使用[**形状.文字**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)财产。

## **从齿轮类型 SmartArt 形状中提取文本**

下面的示例代码加载[示例 Excel 文件](67338510.xlsx)包含齿轮类型智能艺术形状。然后它从上面讨论的各个形状中提取文本。请参阅下面给出的代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **控制台输出**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
