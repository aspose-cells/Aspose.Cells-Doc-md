---
title: Detect Merged Cells in a Worksheet
type: docs
weight: 3000
url: /java/detect-merged-cells-in-a-worksheet/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In Microsoft Excel, several cells can be merged into one. This is often used to create complex tables or to create a cell that holds a heading that spans several columns.

Aspose.Cells allows you to identify merged cell areas in a worksheet. You can unmerge them too. This article provides the simplest lines of code for performing the task using Aspose.Cells.

This article provides compact instructions on how to find and then unmerge merged cells in a worksheet.

{{% /alert %}}

## **Demonstration**

This example uses a template Microsoft Excel file called **MergeTrial**. It has some merged cell areas in a sheet also called Merge Trial.

**The template file**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells provides the [**Cells.getMergedCells()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells/#getMergedCells--) method which is used to get all merged cells.

When the code below is executed, it clears the contents of the sheet and unmerges all the cell areas before saving the file again.

**The Output File**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Code Example**

Please see the following sample code to find how to identify merged cell areas in a worksheet and unmerge them.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Related Articles**

- [Merging and splitting cells](/cells/java/merging-and-unmerging-cells/).
{{< app/cells/assistant language="java" >}}
