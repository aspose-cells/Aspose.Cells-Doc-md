---
title: Conversion between cell name and row/column index
linktitle: Cell Name and Index Conversion
type: docs
weight: 10
url: /python-net/names-and-indices/
description: Learn how to perform conversion between cell name and row/column index using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Get Cell Name from Row and Column Indices, Python Get Row and Column Indices from Cell Name, Python Create safe worksheet names, Python Add safe worksheet names
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.  
Aspose.Cells for Python via .NET provides the [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) method which allows developers to get a cell's name if they provide the row and column index.

{{% alert color="primary" %}} 

Unlike Microsoft Excel, where row and column indices start from 1, Aspose.Cells for Python via .NET starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) to access the cell's name given a known row and column index. The code generates the following output.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Get Row and Column Indices from Cell Name**
It is possible to find a row and column index of the cell from its name. This article explains how.  
Aspose.Cells for Python via .NET provides the [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) method which allows developers to get a row and column index from the cell's name.

{{% alert color="primary" %}} 

Unlike Microsoft Excel, where row and column indices start from 1, Aspose.Cells for Python via .NET starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) to get the row and column index from the cell's name. The code generates the following output.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Create Safe Sheet Names**
Sometimes there is a need to assign the sheet name at runtime. In this scenario, sheet names may contain characters such as `< > + ( ? "` that are not allowed. There is a need to replace any such character with a preset character provided by the user. Similarly, the length may exceed 31 characters, which needs to be truncated. Apache POI provides certain features for creating safe names; a similar feature is provided by Aspose.Cells for Python via .NET to handle all these issues. The following sample code demonstrates this feature:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Output:

this is first name which is cre

` `<> + (adj.Private _ " Private"
{{< app/cells/assistant language="python-net" >}}
