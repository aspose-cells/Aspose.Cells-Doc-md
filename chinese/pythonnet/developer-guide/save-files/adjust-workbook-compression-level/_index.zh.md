---
title: 调整工作簿压缩级别
type: docs
weight: 180
url: /zh/python-net/adjust-workbook-compression-level/
---

## **调整工作簿压缩级别**

开发者在处理较大工作簿时，可以调整工作簿的压缩级别。可以优先考虑较小的文件大小，或者优先考虑处理时间。Aspose.Cells for Python via .NET提供[**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype)枚举，您可以用来设置工作簿的压缩级别。[**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype)枚举包含以下成员。

- Level1：最快但效果最差的压缩。
- Level2：比级别1稍慢，但更好。
- Level3: 稍慢于级别2，但更好。
- Level4: 稍慢于级别3，但更好。
- Level5: 比级别4略慢，但压缩效果更好。
- Level6: 速度和压缩效率的良好平衡。
- Level7: 压缩效果相当不错！
- Level8: 比Level7压缩更好！
- Level9: "最佳"压缩，指的是数据流大小降低最多。也是最慢的压缩。

以下代码片段演示了使用 [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) 枚举，并比较了 Level1、Level6 和 Level9 的转换时间。 您还可以比较生成文件的大小。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-AdjustCompressionLevel-1.py" >}}

