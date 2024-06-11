---
title: 使用 StreamProvider 加载 HTML 到 Excel
type: docs
weight: 80
url: /zh/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

在加载包含外部资源的html文件时，我们经常会遇到以下两个问题:
1. 当加载 HTML 流时，无法通过相对路径获取 HTML 文件引用的图像和外部资源。
1. html文件中引用的外部资源路径需要映射

本文介绍了如何实现[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口来设置[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)属性。通过实现此接口，您将能够在加载Html流期间加载外部资源，或者这些外部资源是相对的。

{{% /alert %}} 

下面是显示使用[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)属性的主要代码



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
