---
title: 将呈现电子表格时的默认字体设置为 HTML
type: docs
weight: 370
url: /zh/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 Aspose.Cells 允许您在将电子表格呈现为 HTML 时设置默认字体。请使用[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)以此目的。当电子表格中的某些单元格具有无效或不存在的字体时，此属性很有用。然后这些单元格将以指定的字体呈现[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)财产。

{{% /alert %}}

## 将呈现电子表格时的默认字体设置为 HTML

以下示例代码创建一个工作簿并在第一个工作表的单元格 B4 中添加一些文本，并将其字体设置为某种未知/不存在的字体。然后通过设置不同的默认字体名称（如 Courier New、Arial、Times New Roman 等）将工作簿保存在 HTML 中。

截图显示了通过设置不同的默认字体名称的效果[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)财产。

![待办事项：图片_替代_文本](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成[使用 Courier New 输出 HTML 文件](5115516) ， 这[用 Arial 输出 HTML](5115518) 和[使用 Times New Roman 输出 HTML 文件](5115517).

## 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
