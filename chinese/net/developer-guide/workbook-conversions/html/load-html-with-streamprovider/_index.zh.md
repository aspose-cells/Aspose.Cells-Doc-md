---
title: 通过StreamProvider加载HTML到Excel
type: docs
weight: 80
url: /zh/net/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

当加载包含外部资源的HTML文件时，通常会遇到以下两个问题:
1. 加载HTML流时，无法通过相对路径获得HTML文件引用的图像和外部资源。
1. HTML文件中引用的外部资源路径需要映射

本文介绍了如何为设置HtmlLoadOptions.StreamProvider属性实现[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口。通过实现此接口，您将能够在加载HTML流时加载外部资源或相对这些外部资源。

{{% /alert %}} 

这是展示如何使用[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) 属性的主要代码



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
