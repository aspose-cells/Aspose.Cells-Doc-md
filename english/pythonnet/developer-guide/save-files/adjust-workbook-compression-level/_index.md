---
title: Adjust workbook compression level
type: docs
weight: 180
url: /python-net/adjust-workbook-compression-level/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adjust Workbook Compression Level**

Developers can adjust the compression level of the workbook when working with larger workbooks. Developers may prioritize smaller file sizes over processing time or vice versa. Aspose.Cells for Python via .NET provides [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) enumeration which you can use to set the compression level of the workbook. The [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) enumeration provides the following members.

- Level1: The fastest but least effective compression.
- Level2: A little slower, but better, than level 1.
- Level3: A little slower, but better, than level 2.
- Level4: A little slower, but better, than level 3.
- Level5: A little slower than level 4, but with better compression.
- Level6: A good balance of speed and compression efficiency.
- Level7: Pretty good compression!
- Level8: Better compression than Level7!
- Level9: The "best" compression, where best means greatest reduction in the size of the input data stream. This is also the slowest compression.

The following code snippet demonstrates the use of [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) enumeration and compares the conversion time for Level1, Level6, and Level9. You may also compare the sizes of the generated files.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-AdjustCompressionLevel-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
