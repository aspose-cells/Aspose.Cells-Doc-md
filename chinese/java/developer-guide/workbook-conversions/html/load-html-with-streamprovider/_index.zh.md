---
title: 使用 StreamProvider 将 Html 加载到 Excel
type: docs
weight: 80
url: /zh/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

在加载包含外部资源的html时，我们经常面临以下两个问题：
1. 加载html流时，无法通过相对路径获取html文件引用的图片和外部资源。
1. 需要映射html文件中引用的外部资源路径。

这篇文章解释了如何实现[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)用于设置的界面[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)财产。通过实现这个接口，你将能够在加载Html流时加载外部资源或者这些外部资源是相对的。

{{% /alert %}} 

这是显示用法的主要代码[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
