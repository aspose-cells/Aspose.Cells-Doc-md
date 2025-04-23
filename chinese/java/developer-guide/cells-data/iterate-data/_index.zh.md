---
title: 如何使用和何时使用迭代器
linktitle: 迭代数据
type: docs
weight: 640
url: /zh/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

迭代器接口的对象可以用来遍历集合的所有元素。迭代器可以用来检查集合中的数据，但不能用来修改基础集合。一般来说，要使用迭代器循环遍历集合的内容，必须执行以下步骤：

1. 通过调用集合的迭代器方法获取集合的起始迭代器。
1. 建立一个循环，调用hasNext方法。让循环在hasNext方法返回true的时候迭代。
1. 在循环内，通过调用next方法获取每个元素。

Aspose.Cells APIs提供了许多迭代器，但本文主要讨论以下三种类型。

1. 单元格迭代器
1. 行迭代器
1. 列迭代器

{{% /alert %}} 
## **如何使用迭代器**
### **单元格迭代器**
有各种方式可以访问单元格迭代器，根据应用程序的要求可以使用任何这些方法。以下是返回单元格迭代器的方法。

1. Cells.iterator
1. Row.iterator
1. Range.iterator

以上提到的所有方法都返回允许遍历已初始化的单元格集合的迭代器。

{{% alert color="primary" %}} 

在遍历单元格时，不应修改集合（执行会导致实例化新单元格或删除现有单元格的操作）。否则迭代器可能无法正确遍历所有单元格（一些元素可能被重复遍历或被跳过）。

{{% /alert %}} 

以下示例代码演示了为单元格集合实现迭代器类的实现。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **行迭代器**
在使用RowCollection.iterator方法时可以访问行迭代器。下面的示例代码演示了对RowCollection类实现迭代器的方法。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **列迭代器**
在使用ColumnCollection.iterator方法时可以访问列迭代器。下面的示例代码演示了对ColumnCollection类实现迭代器的方法。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **迭代器的使用场景**
为了讨论使用迭代器的优势，让我们举一个实时的例子。
##### **场景**
一个应用程序的需求是遍历给定工作表中的所有单元格以读取它们的值。有几种实现这个目标的方法。以下是其中一些示例。
###### **使用显示范围**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **使用MaxDataRow和MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





正如你所观察到的，上述两种方法使用的逻辑几乎相似，即循环遍历集合中的所有单元格以读取单元格的值。这可能会出现一些问题，如下所讨论的。

1. MaxRow、MaxDataRow、MaxColumn、MaxDataColumn和MaxDisplayRange等API需要额外的时间来收集相应的统计信息。如果数据矩阵（行x列）很大，使用这些API可能会导致性能损失。
1. 在大多数情况下，给定范围中并非所有单元格都被实例化。在这种情况下，检查矩阵中的每个单元格比仅检查初始化的单元格效率低。
1. 在循环中访问单元格，如Cells.get(rowIndex, columnIndex)将导致范围中的所有单元格对象被实例化，这可能最终导致OutOfMemoryError。
##### **结论**
根据上述事实，以下是应使用迭代器的可能场景。

1. 需要对单元格集合进行只读访问，即只需要检查单元格。
1. 需要遍历大量单元格。
1. 只需要遍历已初始化的单元格/行/列。
{{< app/cells/assistant language="java" >}}
