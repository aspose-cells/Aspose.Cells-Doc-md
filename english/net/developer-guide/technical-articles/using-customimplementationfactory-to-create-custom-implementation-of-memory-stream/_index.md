---
title: Using CustomImplementationFactory to create custom implementation of Memory Stream
type: docs
weight: 40
url: /net/using-customimplementationfactory-to-create-custom-implementation-of-memory-stream/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells has provided an API named [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) which enables the user to provide custom implementation such as using Recyclable memory implementation instead of the default MemoryStream.

## **Using CustomImplementationFactory to create custom implementation of Memory Stream**

The following sample code illustrates how to make use of [**CellsHelper.CustomImplementationFactory**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/customimplementationfactory) in your program. Sometimes, there is enough memory in your system but the memory is not contiguous. Memory Stream objects use contiguous memory but you can provide the implementation of Memory Stream in such a way that it uses the non-contiguous memory instead,

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-UsingCustomImplementationFactoryToCreateCustomImplementationOfMemoryStream.cs" >}}
{{< app/cells/assistant language="csharp" >}}
