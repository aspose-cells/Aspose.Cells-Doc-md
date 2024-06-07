---
title: 通过StreamProvider加载HTML到Excel
type: docs
weight: 80
url: /zh/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

加载包含外部资源的HTML文件时，通常会遇到以下两个问题:
1. 加载HTML流时，无法通过相对路径获得HTML文件引用的图像和外部资源。
1. HTML文件中引用的外部资源路径需要映射。

本文解释了如何实现[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)接口以设置[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)属性。通过实现此接口，您将能够在加载Html流时加载外部资源，或者这些外部资源是相对的。

{{% /alert %}} 

这是展示[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)用法的主要代码



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
