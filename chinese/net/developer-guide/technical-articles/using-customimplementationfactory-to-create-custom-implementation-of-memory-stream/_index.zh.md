---
title: 使用 CustomImplementationFactory 创建内存流的自定义实现
type: docs
weight: 40
url: /zh/net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---
## **可能的使用场景**

Aspose.Cells 提供了一个名为 API[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)这使用户能够提供自定义实现，例如使用可回收内存实现而不是默认的 MemoryStream。

## **使用 CustomImplementationFactory 创建内存流的自定义实现**

下面的示例代码说明了如何使用[**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory)在你的程序中。有时，系统中有足够的内存，但内存不连续。 Memory Stream 对象使用连续内存，但您可以提供 Memory Stream 的实现，使其使用非连续内存，

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
