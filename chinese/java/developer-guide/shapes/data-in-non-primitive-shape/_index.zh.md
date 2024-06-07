---
title: 非基本形状的数据
type: docs
weight: 500
url: /zh/java/data-in-non-primitive-shape/
---

## **访问非基本形状的数据**

有时，您需要访问不是内置的形状的数据。内置的形状称为基本形状；不是内置形状的称为非基本形状。例如，您可以使用不同的曲线连接线定义自己的形状。

## **非基本形状**

在Aspose.Cells中，非基本形状被赋予类型[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE)。您可以使用[**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)方法来检查它们的类型。

使用[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)方法访问形状数据。它返回构成非基本形状的所有连接路径。这些路径是类型为ShapePath的列表，该列表包含每段中的点。

以下代码片段演示了使用[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)方法访问非基本形状的路径信息。

**显示一个非基本形状的示例** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
