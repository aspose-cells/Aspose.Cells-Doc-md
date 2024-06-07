---
title: 插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns/
description: 学习如何通过Aspose.Cells for Java API插入和删除行和列。
keywords: 如何在Java中插入和删除行和列，使用Java插入行和列，Java删除行和列，使用Java插入行或列，通过Java删除行或列。
---

## **介绍**
无论是从头开始创建新工作表还是在现有工作表上工作，我们可能需要添加额外的行或列以容纳更多数据。反之，我们可能还需要从工作表中指定的位置删除行或列。

为了满足这些要求，Aspose.Cells提供了一套非常简单的类和方法，如下所述。
## **如何管理行/列**
Aspose.Cells提供了代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含了[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了表示工作表中所有单元格的[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合。

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合提供了一些方法来管理工作表中的行和列。以下是其中一些讨论的方法。

{{% alert color="primary" %}} 

当添加行或列时，工作表中的内容向下或向右移动，但如果删除行或列，则内容向上或向左移动。

{{% /alert %}} 
## **如何插入一行**
通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))方法，在任何位置插入一行。[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))方法的第一个参数是要插入新行的行索引，第二个参数是要插入的行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **如何插入多行**
要在工作表中插入多行，调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))方法。[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))方法接受两个参数：

- 行索引：要从哪一行开始插入新行。
- 行数：需要插入的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **如何插入具有格式的行**
要插入带有格式选项的行，请使用带有[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)参数的[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\))重载。使用[InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)类的[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)属性设置[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)枚举。[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)枚举有以下三个成员：

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE)：格式与上一行相同。
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW)：格式与下一行相同。
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR)：清除格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **如何删除一行**
要在任何位置删除一行，请调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\))方法。[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\))方法接受两个参数：

- 行索引：要删除行的行索引。
- 行数：需要删除的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **如何删除多行**
要从工作表中删除多行，请调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\))方法。[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\))方法接受两个参数：

- 行索引：要删除行的行索引。
- 行数：需要删除的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **如何插入一个或多个列**
开发人员还可以通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\))方法在工作表中任何位置插入列。[insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\))方法接受两个参数：

- 列索引，要插入列的列索引
- 列数，需要插入的总列数

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **如何删除一列**
要在工作表中任何位置删除列，请调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\))方法。[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\))方法接受以下参数：

- 列索引：要删除列的列索引。
- 列数：需要删除的总列数。
- 更新引用：指示是否要更新其他工作表中的引用的布尔参数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

