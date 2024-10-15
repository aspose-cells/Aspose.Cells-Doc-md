---
title: Conversion between cell name and row/column index
linktitle: Cell Name and Index Conversion
type: docs
weight: 5
url: /java/names-and-indices/
description: Learn how to get Conversion result between cell name and row/column index with Aspose.Cells for Java APIs.
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---

## **How to Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.

Aspose.Cells provides the [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) method which allows developers to get a cell's name if they provide the row and column index.

{{% alert color="primary" %}} 

Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) to access the cell's name given at a known row and column index. The code generates the following output.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **How to Get Row and Column Indices from Cell Name**
It is possible to find a row and column index of the cell from its name. This article explains how.

Aspose.Cells provides the [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) method which allows developers to get a row and column index from the cell's name.

{{% alert color="primary" %}} 

Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) to get the row and column index from the cell's name. The code generates the following output.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **How to Create safe sheet names**
Sometimes there is a need for assigning the sheet name at runtime. In this scenario, there may be sheet names which may contain some additional characters like <>+(?”. There is a need to replace any such character, which is not allowed as a sheet name with some preset character provided by the user. Similarly, the length may increase to more than 31 characters which needs to be truncated. Apache POI provides certain features of creating safe names, hence similar feature is provided by Aspose.Cells to handle all these issues. Following sample code demonstrates this feature:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Console Output**

this is first name which is cre

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}