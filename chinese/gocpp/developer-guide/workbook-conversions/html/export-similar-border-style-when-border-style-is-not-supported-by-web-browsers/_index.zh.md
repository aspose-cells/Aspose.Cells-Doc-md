---
title: 在Web浏览器不支持边框样式时，使用Golang通过C++导出类似的边框样式
linktitle: 在Web浏览器不支持边框样式时导出类似的边框样式
type: docs
weight: 70
url: /zh/go-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/
description: 学习如何使用Aspose.Cells通过C++与Golang导出在Web浏览器不支持的情况下的类似边框样式
---

## **可能的使用场景**

微软Excel支持一些虚线边框类型，但Web浏览器不支持。当你用Aspose.Cells将此类Excel文件转为HTML时，这些边框会被移除。除了移除，Aspose.Cells还支持显示这些边框，通过设置[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)属性为**true**，支持显示未支持的边框，导出到HTML。

## **在Web浏览器不支持边框样式时导出相似的边框样式**

以下示例加载了包含一些不支持边框的【示例Excel文件】(64716806.xlsx)，调用效果如截图所示。截图进一步展示了[**HtmlSaveOptions.GetExportSimilarBorderStyle()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportsimilarborderstyle/)属性在【输出HTML】(64716804.zip)中的效果。

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportSimilarBorderStyleWhenBorderStyleIsNotSupportedByWebBrowsers.go" >}}
