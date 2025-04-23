---
title: 使用 StreamProvider 加载 HTML 到 Excel
type: docs
weight: 80
url: /zh/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

加载包含外部资源的 HTML 时，我们经常遇到以下两个问题：
1. 当加载 HTML 流时，无法通过相对路径获取 HTML 文件引用的图像和外部资源。
1. 需要映射 HTML 文件中引用的外部资源路径。

本文说明了如何实现 [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) 接口，以设置 [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) 属性。通过实现该接口，您将能够在加载 HTML 流期间加载外部资源，或者这些外部资源是相对的。

{{% /alert %}} 

这是展示 [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) 使用方法的主要代码



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
{{< app/cells/assistant language="java" >}}
