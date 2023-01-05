---
title: 非原始形状的数据
type: docs
weight: 300
url: /zh/net/data-in-non-primitive-shape/
---
## **访问非原始形状的数据**

有时，您需要从非内置形状访问数据。内置形状称为原始形状；那些不是的被称为非原始的。例如，您可以使用不同的曲线连接线来定义自己的形状。

## **非原始形状**

在 Aspose.Cells 中，非原始形状被分配类型[**自选图形类型.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) .您可以使用[**形状.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)财产。

使用访问形状数据[**形状.路径**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)财产。它返回构成非原始形状的所有连接路径。这些路径的类型[**形状路径**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)它包含所有段的列表，这些段又包含每个段中的点。

|**显示非原始形状的示例**|
|:- |
|![待办事项：图片_替代_文本](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
