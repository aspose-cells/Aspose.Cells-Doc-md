---
title: Copy Range Data with Style
type: docs
weight: 340
url: /java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[Copy Range Data Only](/cells/java/copy-range-data-only/) explained how to copy the data from a range of cells to another range. Aspose.Cells can also copy a range complete with formatting. This article explains how.

{{% /alert %}} 
## **Copy Range Data with Style**
Aspose.Cells provides a range of classes and methods for working with ranges, for example, [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), etc.

This example:

1. Creates a workbook.
1. Fills a number of cells in the first worksheet with data.
1. Creates a range.
1. Creates a style object with specified formatting attributes.
1. Applies the style to the data range.
1. Creates a second range of cells.
1. Copies data with the formatting from the first range to the second range.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

{{< app/cells/assistant language="java" >}}