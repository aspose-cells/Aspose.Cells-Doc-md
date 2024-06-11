---
title: 在将电子表格渲染为HTML时设置默认字体
type: docs
weight: 370
url: /zh/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells允许在将电子表格渲染为HTML时设置默认字体. 请使用[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)来实现此目的. 当电子表格中有一些单元格具有无效或不存在的字体时, 特定于[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)属性指定的字体将进行渲染.

{{% /alert %}}

## 在将电子表格渲染为HTML时设置默认字体

以下示例代码创建一个工作簿，并在第一个工作表的B4单元格中添加了一些文本，并将其字体设置为某个未知/不存在的字体。然后，它通过设置不同的默认字体名称，如Courier New、Arial、Times New Roman等，将工作簿保存为HTML。

截图显示了通过[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)属性设置不同默认字体名称的效果.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成了使用Courier New的[output HTML文件](5115516), 使用Arial的[output HTML文件](5115518), 以及使用Times New Roman的[output HTML文件](5115517).

## 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
