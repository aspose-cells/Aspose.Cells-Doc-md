---
title: 如何以及在何处使用枚举器，结合Golang通过C++
linktitle: 迭代数据
type: docs
weight: 55
url: /zh/go-cpp/how-and-where-to-use-enumerators/
description: 学习如何通过 Aspose.Cells for C++ API使用枚举器的方法和位置。
keywords: 如何使用枚举器，单元格枚举器，行枚举器，列枚举器
---

{{% alert color="primary" %}}

枚举器是一个提供遍历容器或集合能力的对象。枚举器可以用来读取集合中的数据，但不能用来修改底层集合，而 IEnumerable 是定义了一个名为 GetEnumerator 的方法的接口，它返回一个 IEnumerator 接口，从而允许只读访问集合。

Aspose.Cells API提供了一堆枚举器，但本文主要讨论如下三种类型。

1. 单元格枚举器
1. 行枚举器
1. 列枚举器

{{% /alert %}}

## **如何使用枚举器**

### **单元格枚举器**

有各种方式可以访问单元格枚举器，并且可以根据应用程序的要求使用任何这些方法。以下是返回单元格枚举器的方法。

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

上述所有方法都返回允许遍历初始化的单元格集合的枚举器。

{{% alert color="primary" %}}

在遍历单元格时，集合不应被修改（进行会导致实例化新单元格或删除现有单元格的操作）。否则，枚举器可能无法正确遍历所有单元格（某些元素可能会被重复遍历或被跳过）。

{{% /alert %}}

以下代码示例演示了为Cells集合实现IEnumerator接口。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **行枚举器**

在使用 [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/) 方法时可以访问行枚举器。以下示例演示了如何为 [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) 实现IEnumerator接口。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **获取列**

在使用 [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/) 方法时可以访问列。以下示例演示了如何为 [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/) 实现Get方法。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **枚举器的使用场景**

为了讨论使用枚举器的优势，让我们举一个实时例子。

**情景**

应用程序需要遍历给定 [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) 中的所有单元格以读取它们的值。实现此目标的方法可能有多种，以下列出几种示例。

### **使用显示范围**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **使用MaxDataRow和MaxDataColumn**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
正如您所注意到的，上述两种方法都使用了几乎相似的逻辑，即在集合中循环遍历所有单元格以读取单元格的值。对于许多原因，这可能会有问题，如下所讨论的。

1. [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/)、[**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)、[**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/)、[**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) 和 [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) 等API需要额外时间来收集相应的统计信息。如果数据矩阵（行×列）很大，使用这些API可能会影响性能。
1. 在大多数情况下，给定范围中并非所有单元格都被实例化。在这种情况下，检查矩阵中的每个单元格比仅检查初始化的单元格效率低。
1. 在循环中访问单元格作为Cells row, column将导致范围内的所有单元格对象被实例化，这最终可能导致OutOfMemoryException。

## **结论**

基于上述事实，以下是应该使用枚举器的可能情况。

1. 需要只读访问单元格集合，即只需检查单元格。
1. 需要遍历大量的单元格。
1. 只需遍历已初始化的单元格/行/列。
