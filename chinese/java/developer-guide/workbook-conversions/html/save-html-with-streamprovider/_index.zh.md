---
title: 使用 StreamProvider 保存 Html
type: docs
weight: 120
url: /zh/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

在将包含图像和形状的Excel文件转换为HTML文件时，我们通常会遇到以下两个问题:
1. 将 Excel 文件保存为 HTML 流时应将图像和形状保存在何处。
1. 将默认路径替换为期望的路径。

本文介绍了如何实现 [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) 属性的 [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) 接口。通过实现此接口，您将能够将生成的资源保存到特定位置或内存流中以备用于 HTML 生成。

{{% /alert %}}

## 示例代码

这是显示 [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider) 属性用法的主代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

以下是*ExportStreamProvider*类的代码，该类实现了以上代码中使用的 [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) 接口。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

