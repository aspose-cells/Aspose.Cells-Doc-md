---
title: 使用 StreamProvider 保存 HTML
type: docs
weight: 80
url: /zh/net/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}} 

在将包含iamges和shapes的excel字段转换为html文件时，我们经常会遇到以下两个问题：
1. 将 excel 文件保存到 html 流时，我们应该将图像和形状保存在哪里。
1. 用例外路径替换默认路径。

这篇文章解释了如何实现[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)用于设置的界面[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)财产。通过实现此接口，您将能够将在 HTML 生成期间创建的资源保存到您的特定位置或内存流。

{{% /alert %}} 

这是显示用法的主要代码[HtmlSaveOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/streamprovider)财产



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ImplementIStreamProvider.cs" >}}



这是代码*导出流提供者*实现的类[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)上面代码中使用的接口。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ImplementIStreamProvider-ExportStreamProviderClass.cs" >}}

