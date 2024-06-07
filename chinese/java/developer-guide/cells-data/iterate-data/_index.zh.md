---
title: 如何以及何处使用迭代器
linktitle: Iterate Data
type: docs
weight: 640
url: /zh/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

迭代器接口的对象可用于遍历集合的所有元素。迭代器可用于检查集合中的数据，但不能用于修改底层集合。通常，要使用迭代器循环遍历集合的内容，需要遵循以下步骤：

1. 通过调用集合的iterator方法获取集合的起始迭代器。
1. 设立一个循环，调用hasNext方法。让循环在hasNext方法返回true时迭代。
1. 在循环中，通过调用next方法获取每个元素。

Aspose.Cells APIs提供了一堆迭代器，然而，本文主要讨论如下三种类型。

1. 单元格迭代器
1. 行迭代器
1. 列迭代器

{{% /alert %}} 
## **如何使用迭代器**
### **单元格迭代器**
有多种访问单元格迭代器的方法，可以根据应用程序需求选择任何一种方法。以下是返回单元格迭代器的方法。

1. Cells.iterator
1. Row.iterator
1. Range.iterator

所有上述提到的方法返回允许遍历已初始化的单元格集合的迭代器。

{{% alert color="primary" %}} 

在遍历单元格时，不应修改集合（会导致实例化新单元格或删除现有单元格的操作）。否则，迭代器可能无法正确遍历所有单元格（某些元素可能会重复遍历或被跳过）。

{{% /alert %}} 

以下代码示例演示了为单元格集合实现Iterator类的实现。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **行迭代器**
在使用RowCollection.iterator方法时可以访问行迭代器。以下代码示例演示了为RowCollection类实现迭代器。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **列迭代器**
在使用ColumnCollection.iterator方法时可以访问列迭代器。以下代码示例演示了为ColumnCollection类实现迭代器。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **迭代器用途**
为了讨论使用迭代器的优点，让我们举一个实时例子。
##### **场景**
一个应用程序需求是遍历给定工作表中的所有单元格以读取它们的值。实现此目标有几种方式。下面演示了其中一些。
###### **使用显示范围**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **使用MaxDataRow和MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





正如您可以观察到的，上述两种方法都使用了更多或更少相似的逻辑，也就是遍历集合中的所有单元格以读取单元格值。这可能因为以下原因成为问题。

1、诸如MaxRow、MaxDataRow、MaxColumn、MaxDataColumn和MaxDisplayRange等API需要额外的时间来收集相应的统计信息。如果数据矩阵（行x列）很大，则使用这些API可能会导致性能损失。
1. 在大多数情况下，给定范围内并非所有单元格都被实例化。在这种情况下，检查矩阵中的每个单元格与仅检查初始化的单元格相比效率不是很高。
1、在循环中访问单元格，如Cells.get(rowIndex，columnIndex)将导致范围内的所有单元对象被实例化，这最终可能导致OutOfMemoryError。
##### **结论**
基于上述事实，以下是应使用迭代器的可能情况。

1、需要对单元格集合进行只读访问，也就是只需要检查单元格。
1、需要遍历大量单元格。
1、需要遍历仅初始化的单元格/行/列。
