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

The shapes in excel are mainly divided into the following types:
- **Lines**
- **Rectangles**
- **Basic Shapes**
- **Block Arrows**
- **Equation Shapes**
- **FlowCharts**
- **Stars and Banners**
- **Callouts**

This guide document will select one or two shapes from each type to make samples.Through these examples, you will learn how to use [Aspose.Cells](https://products.aspose.com/cells/) to insert the specified shape into the worksheet.

## **Inserting a Line to Worksheet**

The shape of line belongs to the **lines** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the line
- Click the Insert menu and click Shapes.
- Then,select the line from 'Recently Used Shapes' or 'Lines'

![](line.png)

***Using Aspose.Cells***

You can use the following method to insert a line in the worksheet.

{{< tabs tabTotal="2" tabID="1" tabName1="for .net" tabName2="for java" >}}
  {{< tab tabNum="1" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public LineShape AddLine(
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

The method returns a [LineShape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/lineshape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="2" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert line to a worksheet.

{{< tabs tabTotal="2" tabID="3" tabName3="C#" tabName4="Java" >}}
  {{< tab tabNum="3" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="4" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](line2.png)

## **Inserting a line arrow to Worksheet**

The shape of line arrow belongs to the **Lines** category.It is a special case of line.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the line arrow
- Click the Insert menu and click Shapes.
- Then,select the line arrow from 'Recently Used Shapes' or 'Lines'

![](line_arrow1.png)

***Using Aspose.Cells***

You can use the following method to insert a line arrow in the worksheet.

{{< tabs tabTotal="2" tabID="5" tabName5="for .net" tabName6="for java" >}}
  {{< tab tabNum="5" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public LineShape AddLine(
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

The method returns a [LineShape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/lineshape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="6" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert line arrow to a worksheet.

{{< tabs tabTotal="2" tabID="7" tabName7="C#" tabName8="Java" >}}
  {{< tab tabNum="7" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="8" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](line_arrow2.png)

## **Inserting a Rectangle to Worksheet**

The shape of rectangle belongs to the **Rectangles** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the rectangle
- Click the Insert menu and click Shapes.
- Then,select the rectangle from 'Recently Used Shapes' or 'Rectangles'

![](rectangle.png)

***Using Aspose.Cells***

You can use the following method to insert a rectangle in the worksheet.

{{< tabs tabTotal="2" tabID="9" tabName9="for .net" tabName10="for java" >}}
  {{< tab tabNum="9" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public RectangleShape AddRectangle(
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

The method returns a [RectangleShape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="10" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert rectangle to a worksheet.

{{< tabs tabTotal="2" tabID="11" tabName11="C#" tabName12="Java" >}}
  {{< tab tabNum="11" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="12" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](rectangle2.png)

## **Inserting a Cube to Worksheet**

The shape of cube belongs to the **Basic Shapes** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the cube
- Click the Insert menu and click Shapes.
- Then,select the Cube from **Basic Shapes**

![](cube.png)

***Using Aspose.Cells***

You can use the following method to insert a cube in the worksheet.

{{< tabs tabTotal="2" tabID="13" tabName13="for .net" tabName14="for java" >}}
  {{< tab tabNum="13" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape AddAutoShape(
	AutoShapeType type,
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="14" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert cube to a worksheet.

{{< tabs tabTotal="2" tabID="15" tabName15="C#" tabName16="Java" >}}
  {{< tab tabNum="15" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="16" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](cube2.png)

## **Inserting a callout quad arrow to Worksheet**

The shape of callout quad arrow belongs to the **Block Arrows** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the callout quad arrow
- Click the Insert menu and click Shapes.
- Then,select the callout quad arrow from **Block Arrows**

![](callout_quad_arrow.png)

***Using Aspose.Cells***

You can use the following method to insert a callout quad arrow in the worksheet.

{{< tabs tabTotal="2" tabID="17" tabName17="for .net" tabName18="for java" >}}
  {{< tab tabNum="17" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape AddAutoShape(
	AutoShapeType type,
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="18" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert callout quad arrow to a worksheet.

{{< tabs tabTotal="2" tabID="19" tabName19="C#" tabName20="Java" >}}
  {{< tab tabNum="19" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="20" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](callout_quad_arrow2.png)

## **Inserting a multiplication sign to Worksheet**

The shape of multiplication sign belongs to the **Equation Shapes** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the multiplication sign
- Click the Insert menu and click Shapes.
- Then,select the multiplication sign from **Equation Shapes**

![](multiplication_sign.png)

***Using Aspose.Cells***

You can use the following method to insert a multiplication sign in the worksheet.

{{< tabs tabTotal="2" tabID="21" tabName21="for .net" tabName22="for java" >}}
  {{< tab tabNum="21" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape AddAutoShape(
	AutoShapeType type,
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="22" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert multiplication sign to a worksheet.

{{< tabs tabTotal="2" tabID="23" tabName23="C#" tabName24="Java" >}}
  {{< tab tabNum="23" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="24" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](multiplication_sign2.png)






## **Inserting a multidocument to Worksheet**

The shape of multidocument belongs to the **FlowCharts** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the multidocument
- Click the Insert menu and click Shapes.
- Then,select the multidocument from **FlowCharts**

![](multidocument.png)

***Using Aspose.Cells***

You can use the following method to insert a multidocument in the worksheet.

{{< tabs tabTotal="2" tabID="25" tabName25="for .net" tabName26="for java" >}}
  {{< tab tabNum="25" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape AddAutoShape(
	AutoShapeType type,
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="26" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert multidocument to a worksheet.

{{< tabs tabTotal="2" tabID="27" tabName27="C#" tabName28="Java" >}}
  {{< tab tabNum="27" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="28" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](multidocument2.png)



## **Inserting a Five-pointed star to Worksheet**

The shape of Five-pointed star belongs to the **Stars and Banners** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the Five-pointed star
- Click the Insert menu and click Shapes.
- Then,select the Five-pointed star from **Stars and Banners**

![](star_5_points.png)

***Using Aspose.Cells***

You can use the following method to insert a Five-pointed star in the worksheet.

{{< tabs tabTotal="2" tabID="29" tabName29="for .net" tabName30="for java" >}}
  {{< tab tabNum="29" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape AddAutoShape(
	AutoShapeType type,
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="30" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert Five-pointed star to a worksheet.

{{< tabs tabTotal="2" tabID="31" tabName31="C#" tabName32="Java" >}}
  {{< tab tabNum="31" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="32" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](star_5_points2.png)



## **Inserting a thought bubble cloud to Worksheet**

The shape of thought bubble cloud belongs to the **Callouts** category.

***In Microsoft Excel (for example 2007):***

- Select the cell where you want to insert the thought bubble cloud
- Click the Insert menu and click Shapes.
- Then,select the thought bubble cloud from **Callouts**

![](thought_bubble_cloud.png)

***Using Aspose.Cells***

You can use the following method to insert a thought bubble cloud in the worksheet.

{{< tabs tabTotal="2" tabID="33" tabName33="for .net" tabName34="for java" >}}
  {{< tab tabNum="33" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape AddAutoShape(
	AutoShapeType type,
	int upperLeftRow,
	int top,
	int upperLeftColumn,
	int left,
	int height,
	int width
)](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

The method returns a [Shape](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="34" >}}
  <div class="row">
    <div class="col-md-6">
<p>

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://apireference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

The method returns a [Shape](https://apireference.aspose.com/cells/java/com.aspose.cells/Shape) object.
</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

The following example shows how to insert thought bubble cloud to a worksheet.

{{< tabs tabTotal="2" tabID="35" tabName35="C#" tabName36="Java" >}}
  {{< tab tabNum="35" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}</p>
    </div>
  </div>
  {{< /tab >}}
  {{< tab tabNum="36" >}}
  <div class="row">
    <div class="col-md-6">
      <p>{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}</p>
    </div>
  </div>
  {{< /tab >}}
{{< /tabs >}}

Execute the above code, you will get the following results:

![](thought_bubble_cloud2.png)
