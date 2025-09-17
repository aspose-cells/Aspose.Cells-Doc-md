##Data in Non-Primitive Shape
This article shows Data in Non-Primitive Shape through the Aspose.Cells for Python via .NET API.
## **Accessing Data of Non-Primitive Shape**
Sometimes, you need to access data from a shape that is not built-in. Built-in shapes are called primitive shapes; ones that aren't are called non-primitive. For example, you can define your own shapes using different curve connected lines.
## **A Non-Primitive Shape**
In Aspose.Cells for Python via .NET, non-primitive shapes are assigned the type [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype). You can check their type using the [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type) property.
Access the shape data using the [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths) property. It returns all the connected paths that comprise the non-primitive shape. These paths are of the type [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath) that holds a list of all the segments which in turn contain the points in each segment.
|**Shows an example of a non-primitive shape**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|
