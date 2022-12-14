---
title: 如何以及在何处使用枚举器
linktitle: 迭代数据
type: docs
weight: 55
url: /zh/net/how-and-where-to-use-enumerators/
---
{{% alert color="primary" %}}

枚举数是一个对象，它提供了遍历容器或集合的能力。枚举器可用于读取集合中的数据，但不能用于修改底层集合，而 IEnumerable 是一个接口，它定义了一个方法 GetEnumerator，该方法返回一个 IEnumerator 接口，这反过来又允许只读访问一个集合。

Aspose.Cells API 提供了一堆枚举器，但是本文主要讨论下面列出的三种类型。

1. Cells 枚举器
1. 行枚举器
1. 列枚举器

{{% /alert %}}

## **如何使用枚举器**

### **Cells 枚举器**

访问 Cells 枚举器的方法有很多种，可以根据应用程序的要求使用其中的任何一种方法。以下是返回单元格枚举器的方法。

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**范围.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

所有上述方法都返回允许遍历已初始化单元格集合的枚举器。

{{% alert color="primary" %}}

在遍历单元格时，不应修改集合（将导致实例化新的 Cell 或删除现有的 Cell 的操作）。否则，枚举器可能无法正确遍历所有单元格（可能会重复遍历或跳过某些元素）。

{{% /alert %}}

下面的代码示例演示了 Cells 集合的 IEnumerator 接口的实现。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **行枚举器**

可以在使用时访问行枚举器[**行集合.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator)方法。下面的代码示例演示了 IEnumerator 接口的实现[**行集合**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **列枚举器**

可以在使用时访问列枚举器[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection)方法。下面的代码示例演示了 IEnumerator 接口的实现[**列集合**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **在哪里使用枚举器**

为了讨论使用枚举器的优势，让我们举一个实时示例。

**设想**

一个应用需求是遍历给定的所有单元格[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)读取它们的值。可以有几种方法来实现这个目标。下面展示了一些。

### **使用显示范围**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **使用 MaxDataRow 和 MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

正如您所观察到的，上述两种方法都或多或少地使用了相似的逻辑，即；遍历集合中的所有单元格以读取单元格值。由于如下所述的多种原因，这可能会产生问题。

1.  API，例如[**最大行数**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**最大数据行**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**最大列**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**最大数据列**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**最大显示范围**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)需要额外的时间来收集相应的统计数据。如果数据矩阵（行 x 列）很大，使用这些 API 可能会造成性能损失。
1. 在大多数情况下，并非给定范围内的所有单元格都被实例化。在这种情况下，与仅检查初始化单元格相比，检查矩阵中的每个单元格效率不高。
1. 以Cells row,column的形式循环访问一个cell会导致一个范围内的所有cell对象都被实例化，最终可能导致OutOfMemoryException。

## **结论**

基于上述事实，以下是应该使用枚举器的可能场景。

1. 需要对单元格集合进行只读访问，即；要求是只检查细胞。
1. 要遍历大量的单元格。
1. 只遍历初始化的单元格/行/列。
