---
title: 调整工作簿压缩级别
type: docs
weight: 180
url: /zh/net/adjust-workbook-compression-level/
---
## **调整工作簿压缩级别**

在处理较大的工作簿时，开发人员可以调整工作簿的压缩级别。开发人员可能会优先考虑较小的文件大小而不是处理时间，反之亦然。 Aspose.Cells提供**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**可用于设置工作簿压缩级别的枚举。这**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**枚举提供以下成员。

- Level1：最快但效率最低的压缩。
- Level2：比 Level 1 慢一点，但更好。
- Level3：比 Level 2 慢一点，但更好。
- Level4：比 Level 3 慢一点，但更好。
- Level5：比 Level 4 慢一点，但压缩效果更好。
- Level6：速度和压缩效率的良好平衡。
- Level7：相当不错的压缩！
- Level8：压缩比 Level7 更好！
- 级别 9：“最佳”压缩，其中最佳意味着输入数据流大小的最大减少。这也是最慢的压缩。

下面的代码片段演示了使用**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**枚举并比较 Level1、Level6 和 Level9 的转换时间。您还可以比较生成的文件的大小。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
