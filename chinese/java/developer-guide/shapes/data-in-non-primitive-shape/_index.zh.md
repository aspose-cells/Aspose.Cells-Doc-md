---
title: 非原始形状的数据
type: docs
weight: 500
url: /zh/java/data-in-non-primitive-shape/
---
## **访问非原始形状的数据**

有时，您需要从非内置形状访问数据。内置形状称为原始形状；那些不是的被称为非原始的。例如，您可以使用不同的曲线连接线来定义自己的形状。

## **非原始形状**

在 Aspose.Cells 中，非原始形状被分配类型[**自选图形类型.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) .您可以使用[**Shape.getAutoShapeType() 方法**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)方法。

使用访问形状数据[**形状.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)方法。它返回构成非原始形状的所有连接路径。这些路径属于 ShapePath 类型，它包含所有线段的列表，而这些线段又包含每个线段中的点。

下面的代码片段演示了使用[**形状.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)方法访问非原始形状的路径信息。

**显示非原始形状的示例** 

![待办事项：图片_替代_文本](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
