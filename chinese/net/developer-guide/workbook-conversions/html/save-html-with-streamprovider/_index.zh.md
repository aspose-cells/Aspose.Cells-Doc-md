---
title: 使用 StreamProvider 保存 Html
type: docs
weight: 80
url: /zh/net/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}} 

将包含图像和形状的 Excel 文件转换为 HTML 文件时，我们经常面临以下两个问题：
1. 将 Excel 文件保存为 HTML 流时应将图像和形状保存在何处。
1. 将默认路径替换为期望的路径。

本文解释了如何实现[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口来设置[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)属性。通过实现此接口，您将能够在生成 HTML 过程中将创建的资源保存到特定位置或内存流中。

{{% /alert %}} 

这是显示使用[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)属性的主要代码



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



以下是实现[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)接口的 *ExportStreamProvider* 类的代码，该类在上述代码中使用。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

