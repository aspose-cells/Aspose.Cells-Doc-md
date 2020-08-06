---
title: Using CustomImplementationFactory to create custom implementation of Memory Stream
type: docs
weight: 40
url: /net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
---

## **Possible Usage Scenarios**
Aspose.Cells has provided an API named [CellsHelper.CustomImplementationFactory](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/properties/customimplementationfactory) which enables the user to provide custom implementation such as using Recyclable memory implementation instead of the default MemoryStream.
## **Using CustomImplementationFactory to create custom implementation of Memory Stream**
The following sample code illustrates how to make use of [CellsHelper.CustomImplementationFactory](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/properties/customimplementationfactory) in your program. Sometimes, there is enough memory in your system but the memory is not contiguous. Memory Stream objects use contiguous memory but you can provide the implementation of Memory Stream in such a way that it uses the non-contiguous memory instead,
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
