---
title: 将网络图片从URL加载到Excel工作表
type: docs
weight: 30
url: /zh/net/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: 如何将URL中的图像转换为实际的Excel图像？本文演示了如何使用C#和易于使用的 Aspose.Cells for .NET API实现此目的。
keywords: Excel从URL显示图像，Excel URL转为图像，在Excel中从URL显示图像，Excel从URL插入图像，将URL转为Excel图像，Excel从URL加载图像，在Excel中从URL加载图像，C#，Excel
---

## 从URL加载图像到Excel工作表

Aspose.Cells for .NET API提供了一种简单易行的方法，可以从URL中加载图像到Excel工作表中。本文介绍了使用Aspose.Cells API将图像数据下载到流中，然后将其插入工作表的方法。使用这种方法，图像将成为Excel文件的一部分，并且每次打开工作表时都不会重新下载。

## 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWebImage-1.cs" >}}

{{% alert color="primary" %}}

可能存在情况，您总是希望从URL获取更新后的图像。要实现这一点，可以按照[从Web地址插入链接图片](/cells/zh/net/insert-a-linked-picture-from-web-address/)文章中给出的说明。通过遵循这种方法，图像在每次打开工作表时都从URL加载。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
