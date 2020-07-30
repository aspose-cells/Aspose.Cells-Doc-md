---
title : "Using CustomImplementationFactory to create custom implementation of Memory Stream" 
description : "" 
weight : 12302 
toc : false
type: docs
url: /net/developerguide/helper/using+customimplementationfactory+to+create+custom+implementation+of+memory+stream/
---

# Aspose.Cells for .NET : Using CustomImplementationFactory to create custom implementation of Memory Stream


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Using CustomImplementationFactory to create custom implementation of Memory Stream](#using-customimplementationfactory-to-create-custom-implementation-of-memory-stream)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells has provided an API named [CellsHelper.CustomImplementationFactory](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/properties/customimplementationfactory) which enables the user to provide custom implementation such as using Recyclable memory implementation instead of the default MemoryStream.

## Using CustomImplementationFactory to create custom implementation of Memory Stream

The following sample code illustrates how to make use of [CellsHelper.CustomImplementationFactory](https://apireference.aspose.com/net/cells/aspose.cells/cellshelper/properties/customimplementationfactory) in your program. Sometimes, there is enough memory in your system but the memory is not contiguous. Memory Stream objects use contiguous memory but you can provide the implementation of Memory Stream in such a way that it uses the non-contiguous memory instead,

## Sample Code

