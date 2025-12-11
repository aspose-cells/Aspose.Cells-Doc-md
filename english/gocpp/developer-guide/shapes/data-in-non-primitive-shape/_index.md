---
title: Data in Non-Primitive Shape with Golang via C++
linktitle: Data in Non-Primitive Shape
type: docs
weight: 300
url: /go-cpp/data-in-non-primitive-shape/
description: Access and manipulate data in non-primitive shapes using Aspose.Cells with Golang via C++.
---

## **Accessing Data of Non-Primitive Shape**

Sometimes you need to access data from a shape that is not built‑in. Built‑in shapes are called primitive shapes; those that aren't are called non‑primitive. For example, you can define your own shapes using different curved, connected lines.

## **A Non-Primitive Shape**

In Aspose.Cells, non‑primitive shapes are assigned the type [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/). You can check their type using the [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/) property.

You can access the shape data using the [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/) property. It returns all the connected paths that comprise the non‑primitive shape. These paths are of type [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/), which holds a list of all the segments, each of which contains the points in that segment.

| **Shows an example of a non-primitive shape** |
| :- |
| ![Non‑primitive shape example](data-in-non-primitive-shape_1.jpg) |

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}