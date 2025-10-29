---
title: 在用Golang通过C++将电子表格渲染为HTML时设置默认字体
linktitle: 在将电子表格渲染为HTML时设置默认字体
type: docs
weight: 370
url: /zh/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: 学习如何使用Aspose.Cells for C++在渲染电子表格为HTML时设置默认字体。
---

{{% alert color="primary" %}}

Aspose.Cells允许在将电子表格渲染为HTML时设置默认字体。请使用[**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/)实现此功能。当电子表格中的某些单元格字体无效或不存在时，这些单元格将以由[**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/)属性指定的字体呈现。

{{% /alert %}}

## 在将电子表格渲染为HTML时设置默认字体

以下示例代码创建一个工作簿，并在第一个工作表的B4单元格中添加了一些文本，并将其字体设置为某个未知/不存在的字体。然后，它通过设置不同的默认字体名称，如Courier New、Arial、Times New Roman等，将工作簿保存为HTML。

截图显示通过[**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/)属性设置不同默认字体名的效果。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成了使用Courier New的[output HTML文件](5115516), 使用Arial的[output HTML文件](5115518), 以及使用Times New Roman的[output HTML文件](5115517).

## 示例代码

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
