---
title: 在将电子表格呈现为 HTML 时设置默认字体
type: docs
weight: 830
url: /zh/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells 允许在将电子表格呈现为 HTML 时设置默认字体。请使用 [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) 来实现此目的。如果电子表格中有一些单元格具有无效或不存在的字体，则这些单元格将以 [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) 属性指定的字体呈现。

{{% /alert %}} 
## **在将电子表格呈现为HTML时设置默认字体**
以下示例代码创建一个工作簿，并向第一个工作表的 B4 单元格添加一些文本，并将其字体设置为某些未知/不存在的字体。然后，通过设置不同的默认字体名称（如 Courier New、Arial、Times New Roman 等）将工作簿保存为 HTML 格式。

屏幕截图显示了通过 [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) 属性设置不同默认字体名称的效果。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成了使用 Courier New 的[输出 HTML 文件](5472568)，使用 Arial 的[输出 HTML](5472567)和使用 Times New Roman 的[输出 HTML 文件](5472565)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
