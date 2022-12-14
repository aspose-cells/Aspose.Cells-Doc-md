---
title: 如何以及在何处使用迭代器
linktitle: 迭代数据
type: docs
weight: 640
url: /zh/java/how-and-where-to-use-iterators/
---
{{% alert color="primary" %}} 

迭代器接口的对象可用于遍历集合的所有元素。迭代器可用于检查集合中的数据，但不能用于修改基础集合。通常，要使用迭代器循环访问集合的内容，必须执行以下步骤：

1. 通过调用集合的迭代器方法获取指向集合开头的迭代器。
1. 设置一个调用 hasNext 方法的循环。只要 hasNext 方法返回 true，就让循环迭代。
1. 在循环中，通过调用 next 方法获取每个元素。

Aspose.Cells API提供了一堆迭代器，但是本文主要讨论下面列出的三种类型。

1. Cells 迭代器
1. 行迭代器
1. 列迭代器

{{% /alert %}} 
## **如何使用迭代器**
### **Cells 迭代器**
有多种方法可以访问单元格的迭代器，可以根据应用程序要求使用这些方法中的任何一种。以下是返回单元格迭代器的方法。

1. Cells.iterator
1. 行.迭代器
1. 范围.迭代器

上述所有方法都返回允许遍历已初始化单元格集合的迭代器。

{{% alert color="primary" %}} 

在遍历单元格时，不应修改集合（将导致实例化新的 Cell 或删除现有的 Cell 的操作）。否则迭代器可能无法正确遍历所有单元格（可能会重复遍历或跳过某些元素）。

{{% /alert %}} 

以下代码示例演示了单元格集合的 Iterator 类的实现。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **行迭代器**
可以在使用 RowCollection.iterator 方法时访问行迭代器。下面的代码示例演示了 Iterator for RowCollection 类的实现。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **列迭代器**
可以在使用 ColumnCollection.iterator 方法时访问 Columns Iterator。下面的代码示例演示了 ColumnCollection 类的 Iterator 的实现。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **在哪里使用迭代器**
为了讨论使用迭代器的优点，让我们举一个实时的例子。
##### **设想**
一个应用程序需求是遍历给定工作表中的所有单元格以读取它们的值。可以有几种方法来实现这个目标。下面展示了一些。
###### **使用显示范围**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **使用 MaxDataRow 和 MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





正如您所观察到的，上述两种方法都使用或多或少相似的逻辑，即；遍历集合中的所有单元格以读取单元格值。由于如下所述的多种原因，这可能会产生问题。

1. MaxRow、MaxDataRow、MaxColumn、MaxDataColumn 和 MaxDisplayRange 等 API 需要额外的时间来收集相应的统计信息。如果数据矩阵（行 x 列）很大，使用这些 API 可能会造成性能损失。
1. 在大多数情况下，并非给定范围内的所有单元格都被实例化。在这种情况下，与仅检查初始化单元格相比，检查矩阵中的每个单元格效率不高。
1. 以 Cells.get(rowIndex, columnIndex) 的方式在循环中访问单元格会导致一个范围内的所有单元格对象都被实例化，最终可能会导致 OutOfMemoryError。
##### **结论**
基于上述事实，以下是应该使用迭代器的可能场景。

1. 需要对单元格集合进行只读访问，即；要求是只检查细胞。
1. 要遍历大量单元格。
1. 只遍历初始化的单元格/行/列。
