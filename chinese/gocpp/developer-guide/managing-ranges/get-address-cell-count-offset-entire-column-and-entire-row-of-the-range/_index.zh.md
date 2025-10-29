---
title: 用Golang通过C++获取范围的地址、单元格数、偏移量、整列和整行
linktitle: 获取范围的地址、单元格数、偏移、整列和整行
type: docs
weight: 330
url: /zh/go-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: 学习如何使用Aspose.Cells for C++获取范围的地址、单元格数量、偏移量、整列和整行。
---

## **可能的使用场景**
Aspose.Cells提供了`Range`对象，该对象具有多种实用方法，方便操作Excel范围。本文介绍以下`Range`对象的方法或属性的用法：

- **地址**

  获取范围的地址。

- **单元格计数**

  获取范围内的总单元格数。

- **偏移**

  通过偏移获取范围。

- **整列**

  获取表示整个列（或列）的`Range`对象，该范围包含指定的范围。

- **整行**

  获取表示整个行（或行）的`Range`对象，该范围包含指定的范围。

## **获取范围的地址、单元格数、偏移、整列和整行**
以下示例代码演示了上述方法和属性的使用。请参考以下代码的控制台输出。

## **示例代码**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange.go" >}}
## **控制台输出**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
