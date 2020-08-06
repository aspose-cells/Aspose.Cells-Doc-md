---
title: Search and Replace Data in a Range
type: docs
weight: 60
url: /java/search-and-replace-data-in-a-range/
---

{{% alert color="primary" %}} 

Sometimes, you need to search for and replace specific data in a range, ignoring any cell values outside the desired range. Aspose.Cells allows you to limit a search to a specific range. This article explains how.

{{% /alert %}} 

Aspose.Cells provides the [FindOptions.setRange()](https://apireference.aspose.com/java/cells/com.aspose.cells/findoptions#setRange\(com.aspose.cells.CellArea\)) method for specifying a range when searching for data.

Suppose you want to search for the string **"search"** and replace it with **"replace"** in the range **E3:H6**. In the screenshot below, the string "search" can be seen in several cells but we want to replace it only in a given range, here highlighted in yellow.

**Input file** 

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

After the execution of the code, the output file looks like the below. All "search" strings within the range have been replaced with "replace".

**Output file** 

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}
