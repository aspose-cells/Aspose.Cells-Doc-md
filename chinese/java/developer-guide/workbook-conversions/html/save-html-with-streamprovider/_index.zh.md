---
title: 使用 StreamProvider 保存 HTML
type: docs
weight: 120
url: /zh/java/convert-excel-to-html-with-streamprovider/
---
{{% alert color="primary" %}}

在将包含图像和形状的excel字段转换为html文件时，我们经常会遇到以下两个问题：
1. 将 excel 文件保存到 html 流时，我们应该将图像和形状保存在哪里。
1. 用例外路径替换默认路径。

这篇文章解释了如何实现[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)用于设置的界面[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)财产。通过实现此接口，您将能够将在 HTML 生成期间创建的资源保存到您的特定位置或内存流。

{{% /alert %}}

## 示例代码

这是显示用法的主要代码[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)财产

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

这是代码*导出流提供者*实现的类[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)上面代码中使用的接口。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

