---
title: Conversion between cell name and row/column index
linktitle: Cell Name and Index Conversion
type: docs
weight: 10
url: /python-net/names-and-indices/
description: Learn how to get Conversion between cell name and row/column index through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Get Cell Name from Row and Column Indices, Python Get Row and Column Indices from Cell Name, Python Create safe worksheet names, Python Add safe worksheet names
---

## **Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.
Aspose.Cells provides the CellsHelper.CellIndexToName method which allows developers to get a cell's name if they provide the row and column index.

{{% alert color="primary" %}} 

Unlike Microsoft Excel, where row and column indices start from 1, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use CellsHelper.CellIndexToName to access the cell's name given a known row and column index. The code generates the following output.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Get Row and Column Indices from Cell Name**
It is possible to find a row and column index of the cell from its name. This article explains how.
Aspose.Cells provides the CellsHelper.CellNameToIndex method which allows developers to get a row and column index from the cell's name.

{{% alert color="primary" %}} 

Unlike Microsoft Excel, where row and column indices start from 1, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use CellsHelper.CellNameToIndex to get the row and column index from the cell's name. The code generates the following output.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Create safe sheet names**
Sometimes there is a need of assigning the sheet name at runtime. In this scenario, there may be sheet names which may contain some additional characters like <>+(?”. There is a need to replace any such character, which is not allowed as a sheet name with some preset character provided by user. Similarly the length may increase to more than 31 characters which needs to be truncated. Apache POI provides certain features of creating safe names, hence similar feature is provided by Aspose.Cells to handle all these issues. Following sample code demonstrates this feature:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Output:

this is first name which is cre

` `<> + (adj.Private _ " Private"
