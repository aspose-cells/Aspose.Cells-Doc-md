---
title: 调整工作簿的压缩级别
type: docs
weight: 180
url: /zh/net/adjust-workbook-compression-level/
---

## **调整工作簿的压缩级别**

当处理较大的工作簿时，开发人员可以调整工作簿的压缩级别。开发人员可能会在文件大小和处理时间之间进行权衡。Aspose.Cells提供了[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)枚举，您可以使用它来设置工作簿的压缩级别。[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)枚举提供以下成员。

- Level1：最快但效果最差的压缩。
- Level2：比级别1稍慢，但比级别1好。
- Level3：比级别2稍慢，但比级别2好。
- Level4：比级别3稍慢，但比级别3好。
- Level5：比级别4稍慢，但压缩效果更好。
- Level6：速度和压缩效率的良好平衡。
- Level7：非常好的压缩！
- Level8：比Level7更好的压缩！
- Level9："最佳"压缩，最佳意味着输入数据流尺寸的最大减少。这也是最慢的压缩。

以下代码片段演示了使用[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)枚举，并比较Level1、Level6和Level9的转换时间。您还可以比较生成文件的大小。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
