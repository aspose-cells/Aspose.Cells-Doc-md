---
title: Copy Ranges of Excel
linktitle: Copy Ranges
type: docs
weight: 30
url: /java/copy-ranges-of-Excel/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

In Excel, you can select a range, copy the range, then paste it with specific options to the same worksheet, other worksheets, or other files.

## **Copy Ranges Using Aspose.Cells**

Aspose.Cells provides several overloaded [Range.Copy](https://reference.aspose.com/cells/java/com.aspose.cells/range) methods to copy a range.

## **Copy Range**

Create two ranges: the source range and the target range, then copy the source range to the target range using the `Range.Copy` method.

See the following code:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **Paste Range With Options**

Aspose.Cells supports pasting the range with a specific paste type.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **Copy Only the Data of the Range**

You can also copy only the data using the `Range.CopyData` method, as shown in the following code:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}

{{< app/cells/assistant language="java" >}}
