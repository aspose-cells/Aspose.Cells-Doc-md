---
title: 将电子表格呈现为 HTML 时设置默认字体
type: docs
weight: 830
url: /zh/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

Aspose.Cells 允许您在将电子表格呈现为 HTML 时设置默认字体。请使用[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)以此目的。当电子表格中的某些单元格具有无效或不存在的字体时，此属性很有用。然后这些单元格将以指定的字体呈现[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)财产。

{{% /alert %}} 
## **将电子表格呈现为 HTML 时设置默认字体**
以下示例代码创建一个工作簿并在第一个工作表的单元格 B4 中添加一些文本，并将其字体设置为某种未知/不存在的字体。然后它通过设置不同的默认字体名称（如 Courier New、Arial、Times New Roman 等）以 HTML 格式保存工作簿。

截图显示了通过设置不同的默认字体名称的效果[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)财产。

![待办事项：图片_替代_文本](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成[使用 Courier New 输出 HTML 文件](5472568) ， 这[用 Arial 输出 HTML](5472567)和[使用 Times New Roman 输出 HTML 文件](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
