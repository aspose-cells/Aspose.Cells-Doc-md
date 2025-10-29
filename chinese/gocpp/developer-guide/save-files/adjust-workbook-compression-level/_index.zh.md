---
title: 用 Golang 通过 C++ 调整工作簿压缩级别。
linktitle: 调整工作簿压缩级别
type: docs
weight: 180
url: /zh/go-cpp/adjust-workbook-compression-level/
description: 学习如何使用Aspose.Cells for C++调整工作簿的压缩级别以优化文件大小和处理时间。
---

## **调整工作簿压缩级别**

开发人员在处理较大的工作簿时可以调整工作簿的压缩级别。 开发人员可以优先考虑较小的文件大小，也可以优先考虑处理时间。 Aspose.Cells 提供了一个枚举 [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/)，您可以用它来设置工作簿的压缩级别。 [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) 枚举提供以下成员。

- Level1：最快但效果最差的压缩。
- Level2：比级别1稍慢，但更好。
- Level3: 稍慢于级别2，但更好。
- Level4: 稍慢于级别3，但更好。
- Level5: 比级别4略慢，但压缩效果更好。
- Level6: 速度和压缩效率的良好平衡。
- Level7: 压缩效果相当不错！
- Level8: 比Level7压缩更好！
- Level9: "最佳"压缩，指的是数据流大小降低最多。也是最慢的压缩。

以下代码片段演示了使用 [**OoxmlCompressionType**](https://reference.aspose.com/cells/go-cpp/ooxmlcompressiontype/) 枚举，并比较了 Level1、Level6 和 Level9 的转换时间。 您还可以比较生成文件的大小。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AdjustWorkbookCompressionLevel.go" >}}
