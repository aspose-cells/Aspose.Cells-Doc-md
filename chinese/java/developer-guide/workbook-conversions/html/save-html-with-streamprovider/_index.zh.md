---
title: 使用StreamProvider保存HTML
type: docs
weight: 120
url: /zh/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

在将包含图像和形状的Excel文件转换为HTML文件时，我们经常会面临以下两个问题：
1. 将Excel文件保存为HTML流时，应该保存图像和形状的位置。
1. 用期望的路径替换默认路径。

本文说明了如何为设置特定位置或内存流保存在HTML生成期间创建的资源提供[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)接口的实现。通过实现此接口，您将能够将创建的资源保存到指定的位置或内存流。

{{% /alert %}}

## 示例代码

这是展示[**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)属性的主要代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

以下是*ExportStreamProvider*类的代码，该类实现了在上述代码中使用的[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)接口。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

{{< app/cells/assistant language="java" >}}
