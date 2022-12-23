---
title: 插入和删除行和列
type: docs
weight: 60
url: /zh/java/inserting-and-deleting-rows-and-columns/
---
## **介绍**
无论是从头开始创建新工作表还是处理现有工作表，我们都可能需要添加额外的行或列以容纳更多数据。反之，我们可能还需要删除工作表中指定位置的行或列。

为满足这些要求，Aspose.Cells 提供了一组非常简单的类和方法，如下所述。
## **管理行/列**
Aspose.Cells提供了[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)代表工作表中所有单元格的集合。

这[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collection 提供了多种方法来管理工作表中的行和列。下面讨论其中一些。

{{% alert color="primary" %}} 

添加行或列时，工作表中的内容会向下或向右移动，但如果删除行或列，则内容会向上或向左移动。

{{% /alert %}} 
## **插入一行**
通过调用[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))方法将要插入新行的行的索引作为第一个参数，将要插入的行数作为第二个参数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **插入多行**
要将多行插入工作表，请调用[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)方法有两个参数：

- 行索引：将插入新行的行的索引。
- 行数：需要插入的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **插入带格式的行**
要插入带有格式选项的行，请使用[插入行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)超载需要[插入选项](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)作为参数。设置[复制格式类型](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)的财产[插入选项](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)类[复制格式类型](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)枚举。这[复制格式类型](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)枚举具有三个成员，如下所列。

- [相同的_作为_多于](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE)：格式化与上一行相同的行。
- [相同的_作为_以下](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW)格式化与下一行相同的行。
- [清除](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR)：清除格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **删除一行**
要删除任何位置的行，请调用[删除行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[删除行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)方法有两个参数：

- 行索引：将从中删除行的行的索引。
- 行数：需要删除的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **删除多行**
要从工作表中删除多行，请调用[删除行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[删除行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)方法有两个参数：

- 行索引：将从中删除行的行的索引。
- 行数：需要删除的总行数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **插入一列或多列**
开发人员还可以通过调用[插入列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[插入列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)方法有两个参数：

- 列索引，将插入列的列的索引
- Number of columns，需要插入的总列数

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **删除列**
要从工作表的任何位置删除列，请调用[删除列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) 的方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。这[删除列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)方法采用以下参数：

- 列索引：列将被删除的列的索引。
- 列数：需要删除的总列数。
- 更新引用：布尔参数，指示是否更新其他工作表中的引用。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

