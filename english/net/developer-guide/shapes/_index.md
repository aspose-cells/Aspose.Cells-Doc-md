---
title: Insert Pictures and Shapes of Excel files.
linktitle: Shapes
type: docs
weight: 140
url: /net/insert-shapes/
description: Manage pictures, oleobject, shapes into Excel files.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you need to insert some necessary shapes into the worksheet.You may need to insert the same shape in different positions of the worksheet.Or you need to batch insert shapes in the worksheet.

Do not worry! [Aspose.Cells](https://products.aspose.com/cells/) supports all these operations.

{{% /alert %}}

The shapes in excel are mainly divided into the following types:
- **Pictures**
- **OleObjects**
- **Lines**
- **Rectangles**
- **Basic Shapes**
- **Block Arrows**
- **Equation Shapes**
- **FlowCharts**
- **Stars and Banners**
- **Callouts**

This guide document will select one or two shapes from each type to make samples.Through these examples, you will learn how to use [Aspose.Cells](https://products.aspose.com/cells/) to insert the specified shape into the worksheet.

## **Adding Pictures in Excel Worksheet in C#**

Adding pictures to a spreadsheet is very easy. It only takes a few lines of code:
Simply call the [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) method of the [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) object). The [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) method takes the following parameters:

- **Upper left row index**, the index of the upper left row.
- **Upper left column index**, the index of the upper left column.
- **Image file name**, the name of the image file, complete with path.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Inserting OLE Objects into Excel Worksheet in C#**

Aspose.Cells supports adding, extracting and manipulating OLE objects in worksheets. For this reason, Aspose.Cells has the [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) class, used to add a new OLE Object to the collection list. Another class, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), represents an OLE Object. It has some important members:

- The [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) property specifies the image (icon) data of byte array type. The image will be displayed to show the OLE Object in the worksheet.
- The [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) property specifies the object data in the form of a byte array. This data will be shown in its related program when you double-click on the OLE Object icon.

The following example shows how to add an OLE Object(s) into a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Inserting a Line to Excel Worksheet in C#**

The shape of line belongs to the **lines** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the line
- Click the Insert menu and click Shapes.
- Then,select the line from 'Recently Used Shapes' or 'Lines'

![](line.png)

***Using Aspose.Cells***

You can use the following method to insert a line in the worksheet.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

The method returns a [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) object.

{{% /alert %}}

The following example shows how to insert line to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Execute the above code, you will get the following results:

![](line2.png)



## **Inserting a line arrow to Excel Worksheet in C#**

The shape of line arrow belongs to the **Lines** category.It is a special case of line.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the line arrow
- Click the Insert menu and click Shapes.
- Then,select the line arrow from 'Recently Used Shapes' or 'Lines'

![](line_arrow1.png)

***Using Aspose.Cells***

You can use the following method to insert a line arrow in the worksheet.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn,	int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

The method returns a [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) object.

{{% /alert %}}

The following example shows how to insert line arrow to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Execute the above code, you will get the following results:

![](line_arrow2.png)



## **Inserting a Rectangle to Excel Worksheet in C#**

The shape of rectangle belongs to the **Rectangles** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the rectangle
- Click the Insert menu and click Shapes.
- Then,select the rectangle from 'Recently Used Shapes' or 'Rectangles'

![](rectangle.png)

***Using Aspose.Cells***

You can use the following method to insert a rectangle in the worksheet.

{{% alert color="primary" %}}

[**public RectangleShape AddRectangle(int upperLeftRow,	int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

The method returns a [RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) object.

{{% /alert %}}

The following example shows how to insert rectangle to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Execute the above code, you will get the following results:

![](rectangle2.png)



## **Inserting a Cube to Excel Worksheet in C#**

The shape of cube belongs to the **Basic Shapes** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the cube
- Click the Insert menu and click Shapes.
- Then,select the Cube from **Basic Shapes**

![](cube.png)

***Using Aspose.Cells***

You can use the following method to insert a cube in the worksheet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) object.

{{% /alert %}}

The following example shows how to insert cube to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Execute the above code, you will get the following results:

![](cube2.png)



## **Inserting a callout quad arrow to Excel Worksheet in C#**

The shape of callout quad arrow belongs to the **Block Arrows** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the callout quad arrow
- Click the Insert menu and click Shapes.
- Then,select the callout quad arrow from **Block Arrows**

![](callout_quad_arrow.png)

***Using Aspose.Cells***

You can use the following method to insert a callout quad arrow in the worksheet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) object.

{{% /alert %}}

The following example shows how to insert callout quad arrow to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Execute the above code, you will get the following results:

![](callout_quad_arrow2.png)



## **Inserting a multiplication sign to Excel Worksheet in C#**

The shape of multiplication sign belongs to the **Equation Shapes** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the multiplication sign
- Click the Insert menu and click Shapes.
- Then,select the multiplication sign from **Equation Shapes**

![](multiplication_sign.png)

***Using Aspose.Cells***

You can use the following method to insert a multiplication sign in the worksheet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) object.

{{% /alert %}}

The following example shows how to insert multiplication sign to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Execute the above code, you will get the following results:

![](multiplication_sign2.png)



## **Inserting a multidocument to Excel Worksheet in C#**

The shape of multidocument belongs to the **FlowCharts** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the multidocument
- Click the Insert menu and click Shapes.
- Then,select the multidocument from **FlowCharts**

![](multidocument.png)

***Using Aspose.Cells***

You can use the following method to insert a multidocument in the worksheet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) object.

{{% /alert %}}

The following example shows how to insert multidocument to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Execute the above code, you will get the following results:

![](multidocument2.png)



## **Inserting a Five-pointed star to Excel Worksheet in C#**

The shape of Five-pointed star belongs to the **Stars and Banners** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the Five-pointed star
- Click the Insert menu and click Shapes.
- Then,select the Five-pointed star from **Stars and Banners**

![](star_5_points.png)

***Using Aspose.Cells***

You can use the following method to insert a Five-pointed star in the worksheet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) object.

{{% /alert %}}

The following example shows how to insert Five-pointed star to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Execute the above code, you will get the following results:

![](star_5_points2.png)



## **Inserting a thought bubble cloud to Excel Worksheet in C#**

The shape of thought bubble cloud belongs to the **Callouts** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the thought bubble cloud
- Click the Insert menu and click Shapes.
- Then,select the thought bubble cloud from **Callouts**

![](thought_bubble_cloud.png)

***Using Aspose.Cells***

You can use the following method to insert a thought bubble cloud in the worksheet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) object.

{{% /alert %}}

The following example shows how to insert thought bubble cloud to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Execute the above code, you will get the following results:

![](thought_bubble_cloud2.png)

## **Advance topics**
- [Change Adjustment Values of the Shape](/cells/net/change-adjustment-values-of-the-shape/)
- [Copy Shapes between Worksheets](/cells/net/copy-shapes-between-worksheets/)
- [Data in Non-Primitive Shape](/cells/net/data-in-non-primitive-shape/)
- [Finding Absolute Position of Shape inside the Worksheet](/cells/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Get Connection points from shape](/cells/net/get-connection-points-from-shape/)
- [Managing Controls](/cells/net/managing-controls/)
- [Add Icons to Worksheet](/cells/net/insert-svg-to-excel/)
- [Managing OLE Objects](/cells/net/managing-ole-objects/)
- [Managing Pictures](/cells/net/managing-pictures/)
- [Manage Smart Art](/cells/net/managing-smartart/)
- [Managing TextBox](/cells/net/managing-textbox-of-excel/)
- [Add WordArt Watermark to Worksheet](/cells/net/add-wordart-watermark-to-worksheet/)
- [Refresh Values of Linked Shapes](/cells/net/refresh-values-of-linked-shapes/)
- [Send Shape Front or Back inside the Worksheet](/cells/net/send-shape-front-or-back-inside-the-worksheet/)
- [Manage Shape Options](/cells/net/managing-shape-options/)
- [Manage Shape Text Options](/cells/net/managing-shape-text-options/)
- [Web Extensions - Office Add-ins](/cells/net/web-extensions-office-add-ins/)

{{< app/cells/assistant language="csharp" >}}
