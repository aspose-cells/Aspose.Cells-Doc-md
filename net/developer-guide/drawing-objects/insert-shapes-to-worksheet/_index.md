---
title: Insert Shapes To Worksheet In Aspose.Cells
type: docs
weight: 10
url: /net/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

Sometimes you need to insert some necessary shapes into the worksheet.You may need to insert the same shape in different positions of the worksheet.Or you need to batch insert shapes in the worksheet.

Do not worry! [Aspose.Cells](https://products.aspose.com/cells/) supports all these operations.

{{% /alert %}}

## **Inserting a Rectangle to Worksheet**

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the rectangle
- Click the Insert menu and click Shapes.
- Then,select the rectangle from 'Recently Used Shapes' or 'Rectangle'

![](1.png)

***Using Aspose.Cells for .NET:***

For C#:

You can use the [AddRectangle(
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) method to insert a rectangle in the worksheet.The method returns a [RectangleShape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) object.

For java:

You can use the [addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int)) method to insert a rectangle in the worksheet.The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.

The following example shows how to insert rectangle to a worksheet.

{{< tabs tabTotal="2" tabID="1" tabName1="C#" tabName2="Java" >}}

  {{< tab tabNum="1" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="2" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}
