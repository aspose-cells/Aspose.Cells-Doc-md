---
title: 非基本形状中的数据
type: docs
weight: 300
url: /zh/python-net/data-in-non-primitive-shape/
description: 本文通过Aspose.Cells for Python via .NET API展示了非原始形状中的数据。
keywords: Python Excel库，Python非原始形状中的数据，Python如何访问非原始形状中的数据。
---

## **访问非基本形状的数据**

有时，您需要访问非内置形状的形状的数据。内置形状称为基本形状；而不是内置形状的称为非基本形状。例如，您可以使用不同的曲线连接线定义自己的形状。

## **非基本形状**

在Aspose.Cells for Python via .NET中，非原始形状被赋予类型 [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype)。您可以使用 [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type) 属性检查它们的类型。

使用 [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths) 属性访问形状数据。它返回组成非原始形状的所有连接路径。这些路径的类型为 [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath)，包含了所有段的列表，而每个段又包含了每个段中的点。

|**显示了非原始形状的示例**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
