---
title: 插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns/
description: 学习如何通过 Aspose.Cells for Java API 插入和删除行和列。
keywords: 如何在Java中插入和删除行和列，使用Java插入行和列，Java删除行和列，使用Java插入行或列，删除行或列via Java。
---

## **介绍**
无论是从头开始创建新工作表还是在现有工作表上操作，我们可能需要添加额外的行或列来容纳更多数据。反之，我们可能还需要从工作表中的指定位置删除行或列。

为了满足这些需求，Aspose.Cells提供了一组非常简单的类和方法，下面将讨论其中一些。
## **如何管理行/列**
Aspose.Cells提供了一个[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，表示Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个表示工作表中所有单元格的[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合。

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合提供了几种用于在工作表中管理行和列的方法。其中一些方法如下所述。

{{% alert color="primary" %}} 

当添加行或列时，工作表中的内容向下移动或向右移动，但如果删除行或列，则内容向上移动或向左移动。

{{% /alert %}} 
## **如何插入行**
通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) 方法在任意位置插入一行。该方法的第一个参数为插入位置的索引，第二个参数为要插入的行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **如何插入多行**
要在工作表中插入多行，请调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) 方法。该方法接受两个参数：

- 行索引：新行将插入的行的索引。
- 行数：需要插入的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **如何插入带有格式的行**
要插入带格式的行，请使用带有 [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) 参数的 [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) 重载方法。可以通过设置 [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions#CopyFormatType) 属性来指定格式复制类型。该枚举有以下三种成员：

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE)： 格式与上方行相同。
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW)： 格式与下方行相同。
- [清除](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): 清除格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **如何删除行**
要在任意位置删除一行，调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) 方法。该方法接受两个参数：

- 行索引：要删除行的起始行的索引。
- 行数：需要删除的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **如何删除多行**
要删除工作表中的多行，可以调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) 方法。该方法接受两个参数：

- 行索引：要删除行的起始行的索引。
- 行数：需要删除的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **如何插入一个或多个列**
开发者还可以通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) 方法在任意位置插入列。该方法接受两个参数：

- 列索引，需要插入列的索引
- 列数，需要插入的总列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **如何删除列**
要在工作表中删除任意列，调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) 方法。该方法接受以下参数：

- 列索引：要删除列的起始列的索引。
- 列数：需要删除的总列数。
- 更新引用：布尔参数，指示是否在其他工作表中更新引用。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
