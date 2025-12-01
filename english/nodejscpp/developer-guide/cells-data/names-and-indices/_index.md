---
title: Conversion between cell name and row/column index
linktitle: Cell Name and Index Conversion
type: docs
weight: 10
url: /nodejs-cpp/names-and-indices/
description: Learn how to get Conversion between cell name and row/column index through the Aspose.Cells for Node.js via C++ API.
keywords: Node.js via C++ Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.
Aspose.Cells for Node.js via C++ provides the CellsHelper.cellIndexToName method which allows developers to get a cell's name if they provide the row and column index.

{{% alert color="primary" %}} 

Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells for Node.js via C++ starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use CellsHelper.cellIndexToName to access the cell's name given a known row and column index. The code generates the following output.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **Get Row and Column Indices from Cell Name**
It is possible to find a row and column index of the cell from its name. This article explains how.
Aspose.Cells for Node.js via C++ provides the CellsHelper.cellNameToIndex method which allows developers to get a row and column index from the cell's name.

{{% alert color="primary" %}} 

Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells for Node.js via C++ starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use CellsHelper.cellNameToIndex to get the row and column index from the cell's name. The code generates the following output.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **Create safe sheet names**
Sometimes there is a need of assigning the sheet name at runtime. In this scenario, there may be sheet names which may contain some additional characters like <>+(?”. There is a need to replace any such character, which is not allowed as a sheet name with some preset character provided by user. Similarly the length may increase to more than 31 characters which needs to be truncated. Apache POI provides certain features of creating safe names, hence similar feature is provided by Aspose.Cells for Node.js via C++ to handle all these issues. Following sample code demonstrates this feature:



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

Output:

this is first name which is cre

` `<> + (adj.Private _ " Private"
{{< app/cells/assistant language="nodejs-cpp" >}}
