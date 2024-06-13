---
title: 调整工作簿压缩级别
type: docs
weight: 130
url: /zh/java/adjust-workbook-compression-level/
---

## **调整工作簿压缩级别**

开发人员在处理较大的工作簿时可以调整工作簿的压缩级别。开发人员可以优先考虑文件大小而不是处理时间，反之亦然。 Aspose.Cells提供[**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)枚举，您可以使用它来设置工作簿的压缩级别。[**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)枚举提供以下成员。

- [**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)：速度最快，但压缩效果最差。
- [**LEVEL_2**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)：比级别1稍慢，但更好。
- [**LEVEL_3**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)：比级别2稍慢，但更好。
- [**LEVEL_4**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)：比级别3稍慢，但更好。
- [**LEVEL_5**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)：比级别4稍慢，但压缩更好。
- [**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)：速度和压缩效率的良好平衡。
- [**LEVEL_7**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)：压缩相当不错！
- [**LEVEL_8**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)：比Level7更好的压缩！
- [**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)：最好的压缩，最大程度减少输入数据流的大小。也是最慢的压缩。

以下代码片段演示了[**OoxmlCompressionType**](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)枚举的使用，并比较了[**LEVEL_1**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)、[**LEVEL_6**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)和[**LEVEL_9**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)的转换时间。您也可以比较生成文件的大小。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
