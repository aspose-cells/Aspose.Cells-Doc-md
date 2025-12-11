---
title: Adjust workbook compression level
type: docs
weight: 130
url: /java/adjust-workbook-compression-level/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adjust workbook compression level**

Developers can adjust the compression level of the workbook when working with larger workbooks. Developers may prioritize smaller file sizes over processing time or vice versa. Aspose.Cells provides the [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) enumeration which you can use to set the compression level of the workbook. The [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) enumeration provides the following members.

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-1): The fastest but least effective compression.
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-2): A little slower but better than level 1.
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-3): A little slower but better than level 2.
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-4): A little slower but better than level 3.
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-5): A little slower than level 4 but with better compression.
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-6): A good balance of speed and compression efficiency.
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-7): Pretty good compression!
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-8): Better compression than Level 7!
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-9): The "best" compression, where best means greatest reduction in the size of the input data stream. This is also the slowest compression.

The following code snippet demonstrates the use of the [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) enumeration and compares the conversion times for [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-1), [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-6), and [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL-9). You may also compare the sizes of the generated files.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
{{< app/cells/assistant language="java" >}}
