---
title: Create Table by Using Border Lines for a Range
type: docs
weight: 50
url: /java/create-table-by-using-border-lines-for-a-range/
description: How to create a table from a range by using border lines. Aspose.Cells for Java provides a simple, easy‑to‑use API that can be used to add borders to a range.
keywords: create table, range to table, range to table excel, excel range to table, range to table with borders, how to create table from range, convert range to table, excel convert range to table, excel create table, range to table java
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you want to create a table by adding border lines for a **Range**/**CellArea** based on the address of the cells you have. You can use [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) method to create a range of cells. The [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) method returns a [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) object. You can create a [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) object and specify the borders (top, left, bottom, right) options accordingly. Later, you may get the cells of the [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) and apply your desired formatting to the cells.

{{% /alert %}}

The following example shows how to create a [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) and specify the border lines for the range cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

After running the above code, we get the generated Excel file containing the formatted table; here is a screenshot of the file.

![Formatted table screenshot](create-table-by-using-border-lines-for-a-range_1.png)
{{< app/cells/assistant language="java" >}}
