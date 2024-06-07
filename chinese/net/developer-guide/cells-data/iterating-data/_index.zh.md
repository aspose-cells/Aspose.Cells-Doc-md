---
title: 如何在何处使用枚举器
linktitle: Iterate Data
type: docs
weight: 55
url: /zh/net/how-and-where-to-use-enumerators/
description: 通过Aspose.Cells for .NET API学习如何使用枚举器
keywords: 如何使用枚举器、单元格枚举器、行枚举器、列枚举器
---

{{% alert color="primary" %}}

枚举器是一种提供遍历容器或集合的能力的对象。枚举器可用于读取集合中的数据，但不能用于修改底层集合，IEnumerable是定义一个返回IEnumerator接口的GetEnumerator方法的接口，这反过来允许对集合进行只读访问

Aspose.Cells APIs提供一系列枚举器，但本文主要讨论下面列出的三种类型

1. 单元格枚举器
1. 行枚举器
1. 列枚举器

{{% /alert %}}

## **如何使用枚举器**

### **单元格枚举器**

有多种方法可以访问单元格枚举器，根据应用程序的要求可以选择任何一种。以下是返回单元格枚举器的方法

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

上述所有方法均返回一个允许遍历已初始化单元格集合的枚举器

{{% alert color="primary" %}}

在遍历单元格时，不应修改集合(会导致实例化新单元格或删除现有单元格的操作)。否则，枚举器可能无法正确遍历所有单元格(有些元素可能会被重复遍历或跳过)

{{% /alert %}}

以下代码示例演示了为Cells集合实现IEnumerator接口

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **行枚举器**

在使用[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator)方法时可以访问行枚举器。以下代码示例演示了为[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection)实现IEnumerator接口

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **列枚举器**

在使用[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection)方法时可以访问列枚举器。以下代码示例演示了为[**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection)实现IEnumerator接口

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **何时使用枚举器**

为了讨论使用枚举器的优势，让我们以一个实时示例为例

**场景**

应用程序的要求是遍历给定的[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)中的所有单元格以读取它们的值。可以有几种实现此目标的方法。以下演示了其中一些

### **使用显示范围**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **使用MaxDataRow和MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

您可以观察到上述两种方法使用更多或更少相似的逻辑，即;循环遍历集合中的所有单元格以读取单元格的值。就下面讨论的一些原因而言，这可能会存在问题

1.诸如[**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow),[**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow),[**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn),[**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)等API需要额外的时间来收集相应的统计信息。如果数据矩阵(行x列)较大，使用这些API可能会导致性能损失
1. 在大多数情况下，给定范围内并非所有单元格都被实例化。在这种情况下，检查矩阵中的每个单元格与仅检查初始化的单元格相比效率不是很高。
1. 在循环中以Cells行，列方式访问单元格将导致范围内的所有单元格对象被实例化，最终可能导致OutOfMemoryException。

## **结论**

基于上述事实，以下是可能需要使用枚举器的场景。

1. 需要只读访问单元格集合，即只需检查单元格。
1. 需要遍历大量单元格。
1. 需要遍历仅初始化的单元格/行/列。
