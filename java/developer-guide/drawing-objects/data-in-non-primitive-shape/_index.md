---
title: Data in Non-Primitive Shape
type: docs
weight: 10
url: /java/data-in-non-primitive-shape/
---

## **Accessing Data of Non-Primitive Shape**

Sometimes, you need to access data from a shape that is not built-in. Built-in shapes are called primitive shapes; ones that aren't are called non-primitive. For example, you can define your own shapes using different curve connected lines.

## **A Non-Primitive Shape**

In Aspose.Cells, non-primitive shapes are assigned the type [**AutoShapeType.NOT_PRIMITIVE**](https://apireference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE). You can check their type using the [**Shape.getAutoShapeType()**](https://apireference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType) method.

Access the shape data using the [**Shape.getPaths()**](https://apireference.aspose.com/cells/java/com.aspose.cells/shape#Paths) method. It returns all the connected paths that comprise the non-primitive shape. These paths are of the type ShapePath that holds a list of all the segments which in turn contain the points in each segment.

The following code snippet demonstrates the use of [**Shape.getPaths()**](https://apireference.aspose.com/cells/java/com.aspose.cells/shape#Paths) method to access path information of non-primitive shape.

**Shows an example of a non-primitive shape** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
