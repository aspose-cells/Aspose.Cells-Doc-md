---
title: Conversion between cell name and row/column index
linktitle: Cell Name and Index Conversion
type: docs
weight: 5
url: /java/names-and-indices/
description: Learn how to get conversion results between cell name and row/column index using Aspose.Cells for Java APIs.
keywords: Java Convert cell index to name, Convert cell name to row/column index using Java APIs, How to Get Cell Name from Row and Column Indices with Java, Java How to Get Row and Column Indices from Cell Name.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.

Aspose.Cells provides the [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) method which allows developers to get a cell's name if they provide the row and column indices.

{{% alert color="primary" %}} 

Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) to access the cell's name given a known row and column index. The code generates the following output.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}

## **How to Get Row and Column Indices from Cell Name**
It is possible to find the row and column indices of a cell from its name. This article explains how.

Aspose.Cells provides the [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) method which allows developers to get the row and column indices from the cell's name.

{{% alert color="primary" %}} 

Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) to get the row and column indices from the cell's name. The code generates the following output.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}

## **How to Create Safe Sheet Names**
Sometimes there is a need to assign the sheet name at runtime. In this scenario, sheet names may contain additional characters such as `<>+("?`. There is a need to replace any such character that is not allowed in a sheet name with a preset character provided by the user. Similarly, if the length exceeds 31 characters, it needs to be truncated. Apache POI provides certain features for creating safe names; Aspose.Cells provides a similar feature to handle these issues. The following sample code demonstrates this feature:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Console Output**

this is first name which is cre

` `<> + (adj.Private _ " Private"

{{< app/cells/assistant language="java" >}}
