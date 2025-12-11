---
title: Conversion between cell name and row/column index
linktitle: Cell Name and Index Conversion
type: docs
weight: 10
url: /net/names-and-indices/
description: Learn how to get conversion between cell name and row/column index through the Aspose.Cells for .NET API.
keywords: Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.  
Aspose.Cells provides the **CellsHelper.CellIndexToName** method, which allows developers to get a cell's name if they provide the row and column index.

{{% alert color="primary" %}} 
Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.  
{{% /alert %}} 

The following sample code illustrates how to use **CellsHelper.CellIndexToName** to access the cell's name given a known row and column index. The code generates the following output.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}

## **Get Row and Column Indices from Cell Name**
It is possible to find the row and column index of a cell from its name. This article explains how.  
Aspose.Cells provides the **CellsHelper.CellNameToIndex** method, which allows developers to get a row and column index from the cell's name.

{{% alert color="primary" %}} 
Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.  
{{% /alert %}} 

The following sample code illustrates how to use **CellsHelper.CellNameToIndex** to get the row and column index from the cell's name. The code generates the following output.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}

## **Create Safe Sheet Names**
Sometimes there is a need to assign a sheet name at runtime. In this scenario, sheet names may contain characters such as `<`, `>`, `+`, `(`, `?`, or `"`. These characters are not allowed in a sheet name and must be replaced with a preset character provided by the user. Additionally, the name may exceed 31 characters, which needs to be truncated. Apache POI provides features for creating safe names; Aspose.Cells offers a similar feature to handle all these issues. The following sample code demonstrates this feature:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Output:

this is first name which is cre

` `<> + (adj.Private _ " Private"
