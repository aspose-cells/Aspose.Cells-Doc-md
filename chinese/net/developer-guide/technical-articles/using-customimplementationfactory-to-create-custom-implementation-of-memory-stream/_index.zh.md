---
title: 使用CustomImplementationFactory创建Memory Stream的自定义实现
type: docs
weight: 40
url: /zh/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **可能的使用场景**

Aspose.Cells提供了一个名为[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)的API，该API使用户能够提供自定义实现，例如使用可回收内存实现而不是默认的Memory Stream。

## **使用CustomImplementationFactory创建Memory Stream的自定义实现**

以下示例代码说明了如何在程序中使用[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)。有时候在系统中有足够的内存，但内存不是连续的。Memory Stream对象使用连续内存，但您可以提供这样一种Memory Stream的实现，其方式是使用非连续内存。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
{{< app/cells/assistant language="csharp" >}}
