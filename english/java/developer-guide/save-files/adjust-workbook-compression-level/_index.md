---
title: Adjust workbook compression level
type: docs
weight: 130
url: /java/adjust-workbook-compression-level/
---

## **Adjust workbook compression level**

Developers can adjust the compression level of the workbook when working with larger workbooks. Developers may prioritize smaller file sizes over processing time or vice versa. Aspose.Cells provides [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) enumeration which you can use to set the compression level of the workbook. The [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) enumeration provides the following members.

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1): The fastest but least effective compression.
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2): A little slower, but better, than level 1.
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3): A little slower, but better, than level 2.
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4): A little slower, but better, than level 3.
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5): A little slower than level 4, but with better compression.
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6): A good balance of speed and compression efficiency.
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7): Pretty good compression!
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8): Better compression than Level7!
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9): The "best" compression, where best means greatest reduction in the size of the input data stream. This is also the slowest compression.

The following code snippet demonstrates the use of [**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType) enumeration and compares the conversion time for [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1), [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6), and [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9). You may also compare the sizes of the generated files.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
{{< app/cells/assistant language="java" >}}