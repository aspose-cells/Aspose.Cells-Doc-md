---
title: 使用StreamProvider保存HTML
type: docs
weight: 80
url: /zh/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

当将包含图像和形状的Excel文件转换为HTML文件时, 我们经常会遇到以下两个问题:
1. 将Excel文件保存为HTML流时，应该保存图像和形状的位置。
1. 用期望的路径替换默认路径。

本文解释了如何实现[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口以设置[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)属性. 通过实现该接口, 您将能够将在生成HTML期间所创建的资源保存到特定位置或内存流中.

{{% /alert %}} 

这是展示使用[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)属性的主要代码



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



这是*ExportStreamProvider*类的代码, 该类实现了[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口, 用于上述代码中使用



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

