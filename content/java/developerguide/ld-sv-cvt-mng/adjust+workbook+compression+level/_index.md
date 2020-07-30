---
title : "Adjust workbook compression level" 
description : "" 
weight : 12061 
toc : false
type: docs
url: /java/developerguide/ld-sv-cvt-mng/adjust+workbook+compression+level/
---

# Aspose.Cells for Java : Adjust workbook compression level


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adjust workbook compression level](#adjust-workbook-compression-level)
{{< /panel >}}
 

## Adjust workbook compression level

Developers can adjust the compression level of the workbook when working with larger workbooks. Developers may prioritize smaller file sizes over processing time or vice versa. Aspose.Cells provides [OoxmlCompressionType](https://apireference.aspose.com/java/cells/com.aspose.cells/OoxmlCompressionType) enumeration which you can use to set the compression level of the workbook. The [OoxmlCompressionType](https://apireference.aspose.com/java/cells/com.aspose.cells/OoxmlCompressionType) enumeration provides the following members.

*   [LEVEL\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_1): The fastest but least effective compression.
*   [LEVEL\_2](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_2): A little slower, but better, than level 1.
*   [LEVEL\_3](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_3): A little slower, but better, than level 2.
*   [LEVEL\_4](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_4): A little slower, but better, than level 3.
*   [LEVEL\_5](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_5): A little slower than level 4, but with better compression.
*   [LEVEL\_6](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_6): A good balance of speed and compression efficiency.
*   [LEVEL\_7](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_7): Pretty good compression!
*   [LEVEL\_8](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_8): Better compression than Level7!
*   [LEVEL\_9](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_9): The "best" compression, where best means greatest reduction in the size of the input data stream. This is also the slowest compression.

The following code snippet demonstrates the use of [OoxmlCompressionType](https://apireference.aspose.com/java/cells/com.aspose.cells/OoxmlCompressionType) enumeration and compares the conversion time for [LEVEL\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_1), [LEVEL\_6](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_6), and [LEVEL\_9](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_9). You may also compare the sizes of the generated files.

  
  

`[LEVEL_7](https://apireference.aspose.com/java/cells/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)`

