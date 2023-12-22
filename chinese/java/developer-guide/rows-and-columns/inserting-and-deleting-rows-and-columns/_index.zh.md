---
title: 插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns/
description: 了解如何通过 Aspose.Cells for Java API 插入和删除行和列。
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **介绍**
无论是从头开始创建新工作表还是处理现有工作表，我们可能需要添加额外的行或列以容纳更多数据。反过来，我们可能还需要删除工作表中指定位置的行或列。

为了满足这些要求，Aspose.Cells 提供了一组非常简单的类和方法，如下所述。
##  **如何管理行/列**
Aspose.Cells 提供[练习册](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[练习册](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由以下形式表示[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)代表工作表中所有单元格的集合。

这[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合提供了多种管理工作表中的行和列的方法。下面讨论其中一些。

{{% alert color="primary" %}} 

添加行或列时，工作表中的内容会向下或向右移动，但如果删除行或列，则工作表中的内容会向上或向左移动。

{{% /alert %}} 
##  **如何插入行**
通过调用在任意位置插入一行[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)）的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)方法将要插入新行的行索引作为第一个参数，将要插入的行数作为第二个参数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **如何插入多行**
要在工作表中插入多行，请调用[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)）的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)方法有两个参数：

- 行索引：将插入新行的行索引。
- 行数：需要插入的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **如何插入带格式的行**
要插入带有格式选项的行，请使用[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)）过载需要[插入选项](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)作为参数。设置[复制格式类型](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)的财产[插入选项](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)与 一起上课[复制格式类型](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)枚举。这[复制格式类型](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)枚举具有如下列出的三个成员。

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE)：设置与上行相同的行格式。
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW)：将行的格式设置为与下面的行相同。
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR)：清除格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **如何删除一行**
要删除任意位置的行，请调用[删除行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)）的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[删除行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)方法有两个参数：

- 行索引：要删除行的行的索引。
- 行数：需要删除的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **如何删除多行**
要从工作表中删除多行，请调用[删除行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)）的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[删除行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)方法有两个参数：

- 行索引：要删除行的行的索引。
- 行数：需要删除的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **如何插入一列或多列**
开发人员还可以通过调用以下函数将列插入工作表中的任意位置[插入列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)）的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[插入列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)方法有两个参数：

- 列索引，将插入列的列的索引
- Number of columns，需要插入的总列数

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **如何删除列**
要从工作表的任意位置删除列，请调用[删除列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)）的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[删除列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)方法采用以下参数：

- 列索引：要删除列的列的索引。
- 列数：需要删除的列总数。
- 更新引用：布尔参数，指示是否更新其他工作表中的引用。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

