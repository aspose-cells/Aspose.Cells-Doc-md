---
title: Data in Non-Primitive Shape
type: docs
weight: 300
url: /net/data-in-non-primitive-shape/
---

## **Accessing Data of Non-Primitive Shape**

Sometimes, you need to access data from a shape that is not built-in. Built-in shapes are called primitive shapes; ones that aren't are called non-primitive. For example, you can define your own shapes using different curve connected lines.

## **A Non-Primitive Shape**

In Aspose.Cells, non-primitive shapes are assigned the type [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype). You can check their type using the [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype) property.

Access the shape data using the [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths) property. It returns all the connected paths that comprise the non-primitive shape. These paths are of the type [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath) that holds a list of all the segments which in turn contain the points in each segment.

|**Shows an example of a non-primitive shape**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}