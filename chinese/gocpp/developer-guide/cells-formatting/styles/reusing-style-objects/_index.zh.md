---
title: 使用C++通过Golang重用样式对象
linktitle: 重用样式对象
description: 在Aspose.Cells for C++中，通过创建和使用可重用的样式对象，可以简化样式管理并提高代码效率。我们的指南将帮助您利用可重用样式对象的优势，并将其实现于您的应用程序中。
keywords: Aspose.Cells for C++，重用样式对象，样式管理，代码效率，可重用样式，应用程序开发，API参考，示例代码，下载，支持。
type: docs
weight: 3000
url: /zh/go-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}

重用样式对象可以节省内存并加快程序运行速度。

{{% /alert %}}

若要对工作表中的大范围单元格应用一些格式设置：

1. 创建一个样式对象。
1. 指定属性。
1. 将样式应用于范围中的单元格。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReusingStyleObjects.go" >}}
{{% alert color="primary" %}}

由于 [**Cell.GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)/[**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) 方法占用的内存明显较少，并且效率更高，旧的 Cell.Style 属性在 Aspose.Cells 7.1.0 版本中已被移除，因为它消耗了大量不必要的内存。

{{% /alert %}}
