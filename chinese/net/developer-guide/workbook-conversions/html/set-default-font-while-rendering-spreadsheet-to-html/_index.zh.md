---
title: 在将电子表格呈现为 HTML 时设置默认字体
type: docs
weight: 370
url: /zh/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells 允许您在将电子表格呈现为 HTML 时设置默认字体。请使用 [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) 进行此设置。当电子表格中有一些单元格包含无效或不存在的字体时，通过该属性规定的字体将用于呈现这些单元格。

{{% /alert %}}

## 在将电子表格呈现为 HTML 时设置默认字体

以下示例代码创建一个工作簿，并向第一个工作表的 B4 单元格添加一些文本，并将其字体设置为某些未知/不存在的字体。然后，通过设置不同的默认字体名称（如 Courier New、Arial、Times New Roman 等）将工作簿保存为 HTML 格式。

屏幕截图显示通过 [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) 属性设置不同默认字体名称的效果。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成了带有 Courier New 的[HTML 文件](5115516)，带有 Arial 的 [HTML 文件](5115518)，以及带有 Times New Roman 的 [HTML 文件](5115517)。

## 示例代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
