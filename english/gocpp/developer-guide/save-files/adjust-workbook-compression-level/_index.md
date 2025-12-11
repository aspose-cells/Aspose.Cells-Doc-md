---
title: Adjust Workbook Compression Level with Golang via C++
linktitle: Adjust Workbook Compression Level
type: docs
weight: 180
url: /go-cpp/adjust-workbook-compression-level/
description: Learn how to adjust the compression level of a workbook using Aspose.Cells for C++ to optimize file size and processing time.
---

## **Adjust Workbook Compression Level**

Developers can adjust the compression level of the workbook when working with larger workbooks. Developers may prioritize smaller file sizes over processing time or vice versa. Aspose.Cells provides the [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) enumeration, which you can use to set the compression level of the workbook. The [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) enumeration provides the following members.

- Level1: The fastest but least effective compression.
- Level2: A little slower, but better, than Level1.
- Level3: A little slower, but better, than Level2.
- Level4: A little slower, but better, than Level3.
- Level5: A little slower than Level4, but with better compression.
- Level6: A good balance of speed and compression efficiency.
- Level7: Pretty good compression!
- Level8: Better compression than Level7!
- Level9: The "best" compression, where best means greatest reduction in the size of the input data stream. This is also the slowest compression.

The following code snippet demonstrates the use of the [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) enumeration and compares the conversion time for Level1, Level6, and Level9. You may also compare the sizes of the generated files.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdjustWorkbookCompressionLevel.go" >}}