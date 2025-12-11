---
title: Search and Replace Data in a Range
type: docs
weight: 60
url: /java/search-and-replace-data-in-a-range/
description: This article **shows** how to search and replace data in a range in Excel using Java code.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to search for and replace specific data in a range, ignoring any cell values outside the desired range. Aspose.Cells allows you to limit a search to a specific range. This article explains how.

{{% /alert %}}

Aspose.Cells provides the [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange-com.aspose.cells.CellArea-) method for specifying a range when searching for data.

Suppose you want to search for the string **"search"** and replace it with **"replace"** in the range **E3:H6**. In the screenshot below, the string "search" can be seen in several cells, but we want to replace it only in a given range, **which is highlighted in yellow**.

**Input file**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

After the execution of the code, the output file looks **as shown below**. All "search" strings within the range have been replaced with "replace".

**Output file**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Related Articles

- [Find or Search Data](/cells/java/find-or-search-data/)
{{< app/cells/assistant language="java" >}}
