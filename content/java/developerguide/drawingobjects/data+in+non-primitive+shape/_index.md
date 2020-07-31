---
title : "Data in Non-Primitive Shape" 
description : "" 
weight : 12218 
toc : false
type: docs
url: /java/developerguide/drawingobjects/data+in+non-primitive+shape/
---

# Aspose.Cells for Java : Data in Non-Primitive Shape



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Accessing Data of Non-Primitive Shape](#accessing-data-of-non-primitive-shape)
*   2 [A Non-Primitive Shape](#a-non-primitive-shape)
{{< /panel >}}
 

## Accessing Data of Non-Primitive Shape

Sometimes, you need to access data from a shape that is not built-in. Built-in shapes are called primitive shapes; ones that aren't are called non-primitive. For example, you can define your own shapes using different curve connected lines.

## A Non-Primitive Shape

In Aspose.Cells, non-primitive shapes are assigned the type [AutoShapeType.NOT\_PRIMITIVE](https://apireference.aspose.com/java/cells/com.aspose.cells/autoshapetype#NOT_PRIMITIVE). You can check their type using the [Shape.getAutoShapeType()](https://apireference.aspose.com/java/cells/com.aspose.cells/shape#AutoShapeType) method.

Access the shape data using the [Shape.getPaths()](https://apireference.aspose.com/java/cells/com.aspose.cells/shape#Paths) method. It returns all the connected paths that comprise the non-primitive shape. These paths are of the type ShapePath that holds a list of all the segments which in turn contain the points in each segment.

The following code snippet demonstrates the use of [Shape.getPaths()](https://apireference.aspose.com/java/cells/com.aspose.cells/shape#Paths) method to access path information of non-primitive shape.

**Shows an example of a non-primitive shape**  
![](https://docs2.aspose.com/cells/java/attachments/5276021/92340231.jpg)

