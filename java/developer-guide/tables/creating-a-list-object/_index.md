---
title: Creating a Table
type: docs
weight: 40
url: /java/creating-a-list-object/
---

{{% alert color="primary" %}}

One of the advantages of spreadsheets is that they allow you to create different types of lists, for example, phone lists, task lists, lists of transactions, assets or liabilities. Several users can work together to use, create and maintain various lists.

Aspose.Cells supports creating and managing Lists.

{{% /alert %}}

## **Advantages of a table**

There are quite a few advantages when you convert a list of data to an actual List Object:

- New rows and columns are automatically included.
- A total row at the bottom of your list can be easily added to display SUM, AVERAGE, COUNT, etc.
- Columns added to the right are automatically incorporated into the List object.
- Charts based on rows and columns will be expanded automatically.
- Named ranges assigned to rows and columns will be expanded automatically.
- The list is protected from accidental row and column deletion.

## **Creating a table using Microsoft Excel**

**Selecting data range for creating a list object** 

![todo:image_alt_text](creating-a-list-object_1.png)

This displays the Create List dialog.

**Create List dialog** 

![todo:image_alt_text](creating-a-list-object_2.png)

Implementing the List object and specifying Total Row (Select **Data**, then **List**, followed by **Total Row**).

**Creating a List object** 

![todo:image_alt_text](creating-a-list-object_3.png)

## **Creating a table using Using Aspose.Cells API**

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [**Worksheets**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) collection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet) class. The [**Worksheet**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet) class provides a wide range of properties and methods for managing a worksheet. To create a [**ListObject**](https://apireference.aspose.com/cells/java/com.aspose.cells/ListObject) in a worksheet, use [**ListObjects**](https://apireference.aspose.com/cells/java/com.aspose.cells/worksheet#ListObjects) collection property of the Worksheet class. Each [**ListObject**](https://apireference.aspose.com/cells/java/com.aspose.cells/ListObject) is, in fact, an object of the [**ListObjectCollection**](https://apireference.aspose.com/cells/java/com.aspose.cells/listobjectcollection) class, which further provides the add method for adding a List object and specifying a range of cells for the list.

According to the specified range of cells, the List object is created in the worksheet by Aspose.Cells. Use attributes (for example, ShowTotals, ListColumns etc.) of the [**ListObject**](https://apireference.aspose.com/cells/java/com.aspose.cells/ListObject) class to control the list.

In the example given below, we have created the same [**ListObject**](https://apireference.aspose.com/cells/java/com.aspose.cells/ListObject) using Aspose.Cells API as we created using Microsoft Excel in the above section.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-CreatingListObject-CreatingListObject.java" >}}
