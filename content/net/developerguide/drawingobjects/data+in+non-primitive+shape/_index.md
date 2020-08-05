---
title : "Data in Non-Primitive Shape" 
description : "" 
weight : 12283 
toc : false
type: docs
url: /net/developerguide/drawingobjects/data+in+non-primitive+shape/
---

# Aspose.Cells for .NET : Data in Non-Primitive Shape


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Accessing Data of Non-Primitive Shape](#accessing-data-of-non-primitive-shape)
*   2 [A Non-Primitive Shape](#a-non-primitive-shape)
{{< /panel >}}
 

## Accessing Data of Non-Primitive Shape

Sometimes, you need to access data from a shape that is not built-in. Built-in shapes are called primitive shapes; ones that aren't are called non-primitive. For example, you can define your own shapes using different curve connected lines.

## A Non-Primitive Shape

In Aspose.Cells, non-primitive shapes are assigned the type [AutoShapeType.NotPrimitive](https://apireference.aspose.com/net/cells/aspose.cells.drawing/autoshapetype). You can check their type using the [Shape.AutoShapeType](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shape/properties/autoshapetype) property.

Access the shape data using the [Shape.Paths](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shape/properties/paths) property. It returns all the connected paths that comprise the non-primitive shape. These paths are of the type [ShapePath](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shapepath) that holds a list of all the segments which in turn contain the points in each segment.

{{< table style="table-striped" >}}
|Shows an example of a non-primitive shape|
|:----|
|![image](https://docs2.aspose.com/cells/net/attachments/5017130/92340232.jpg)|
{{< /table >}}

