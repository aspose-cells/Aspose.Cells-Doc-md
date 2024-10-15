---
title: Aspose.Cells Object Model
type: docs
weight: 20
url: /java/aspose-cells-object-model/
---

{{% alert color="primary" %}}

Aspose.Cells Object Model provides information about the structural relationships between the objects of Aspose.Cells class library.

{{% /alert %}}

The top level structure of the Aspose.Cells object model is shown below in a hierarchical manner.

|**Top level structure of Aspose.Cells Object Model**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
As you can see from the above figure that the root of the object model is the Workbook object. A brief description of few of the objects is provided below for the introductory purposes.

## **WorksheetCollection/Worksheet**

Workbook object contains the WorksheetCollection, which represents the collection of all the Worksheet objects in a spreadsheet as shown below:

|**Worksheets & Worksheet objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|

## **Cells/Cell**

Each Worksheet object contains a Cells object that represents the collection of all Cell objects in a worksheet as shown below:

|**Cells & Cell objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
You can use the Cell object to get and set the value, style, formula and other properties of a single cell.

## **ChartCollection/Chart**

Charts object represents a collection of all the Chart objects in a Worksheet. Each Chart object is comprised of several other objects that work together to create and manage charts. The Chart structure in Aspose.Cells is shown in the diagram below:

|**Object model of the Chart**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|

## **CommentCollection/Comment**

Each Worksheet object also contains a Comments object that represents the collection of all Comment objects in a worksheet as shown below:

|**Comments & Comment objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
A Comment object is used to add a comment to any specified cell in the worksheet.

## **HorizontalPageBreakCollection/HorizontalPageBreak**

Each Worksheet object contains a HorizontalPageBreakCollection that represents a collection of all HorizontalPageBreak objects in a worksheet as shown below:

|**HPageBreaks & HPageBreak objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
A HorizontalPageBreak object is used to create a horizontal page break in the worksheet.

## **HyperlinkCollection/Hyperlink**

A Worksheet object also contains a HyperlinkCollection that represents a collection of all Hyperlink objects in the worksheet as shown below:

|**Hyperlinks & Hyperlink objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
A Hyperlink object represents a hyperlink in the worksheet. Developers can set hyperlink address and other related properties using Hyperlink object.

## **PictureCollection/Picture**

Each Worksheet object contains a PictureCollection object that represents a collection of all Picture objects in a worksheet as shown below:

|**Pictures & Picture objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
A Picture object represents a picture in the worksheet. Using Picture object, developers cannot only add pictures into their worksheets but also position these pictures at any location. It is also possible to set borders or other properties of the pictures.

## **VerticalPageBreakCollection/VerticalPageBreak**

Each Worksheet object contains a VerticalPageBreakCollection object that represents a collection of all VerticalPageBreak objects in a worksheet as shown below:

|**VPageBreaks & VPageBreak objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
A VerticalPageBreak object is used to create a vertical page break in the worksheet.

## **PivotTableCollection/PivotTable**
Each Worksheet object contains a PivotTableCollection object that represents a collection of all PivotTable objects in a worksheet as shown below:

|**PivotTables & PivotTable objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_10.png)|
A PivotTable object represents a pivot table in the worksheet. Developers can set the style of pivot table and other related properties using PivotTable object.

## **TimelineCollection/Timeline**
Each Worksheet object contains a TimelineCollection object that represents a collection of all Timeline objects in a worksheet as shown below:

|**Timelines & Timeline objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_11.png)|
A Timeline object represents a timeline in the worksheet. Developers can set the style of timeline and other related properties using Timeline object.

## **SlicerCollection/Slicer**
Each Worksheet object contains a SlicerCollection object that represents a collection of all Slicer objects in a worksheet as shown below:

|**Slicers & Slicer objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_12.png)|
A Slicer object represents a slicer in the worksheet. Developers can set the style of slicer and other related properties using Slicer object.

## **ListObjectCollection/ListObject**
Each Worksheet object contains a ListObjectCollection object that represents a collection of all ListObject objects in a worksheet as shown below:

|**ListObjects & ListObject objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_13.png)|
A ListObject object represents a table in the worksheet. Developers can set the style of table and other related properties using ListObject object.

## **ShapeCollection/Shape**
Each Worksheet object contains a ShapeCollection object that represents a collection of all Shape objects in a worksheet as shown below:

|**Shapes & Shape objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_14.png)|
A Shape object represents a shape in the worksheet. Developers can set the style of shape and other related properties using Shape object.

## **SparklineGroupCollection/SparklineGroup**
Each Worksheet object contains a SparklineGroupCollection object that represents a collection of all SparklineGroup objects in a worksheet as shown below:

|**SparklineGroups & SparklineGroup objects**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_15.png)|
A SparklineGroup object represents a sparkline group in the worksheet. Developers can set the style of sparkline group and other related properties using SparklineGroup object.
{{< app/cells/assistant language="java" >}}