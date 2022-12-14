---
title: 使用 StreamProvider 将 Html 加载到 Excel
type: docs
weight: 80
url: /zh/net/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

在加载包含外部资源的 html 字段时，我们经常面临以下两个问题：
1. 加载html流时，无法通过相对路径获取html文件引用的图片和外部资源。
1. 需要映射html文件中引用的外部资源路径

这篇文章解释了如何实现[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)用于设置的界面[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)财产。通过实现这个接口，你将能够在加载Html流时加载外部资源或者这些外部资源是相对的。

{{% /alert %}} 

这是显示用法的主要代码[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)财产



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
