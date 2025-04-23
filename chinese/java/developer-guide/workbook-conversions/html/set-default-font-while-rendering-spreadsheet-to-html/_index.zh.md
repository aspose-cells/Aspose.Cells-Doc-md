---
title: 在将电子表格渲染为HTML时设置默认字体
type: docs
weight: 830
url: /zh/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells允许您在将电子表格渲染为HTML时设置默认字体。请使用[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)进行设置。当电子表格中存在一些单元格具有无效或不存在的字体时，此属性非常有用。那些单元格将以[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)属性指定的字体呈现。

{{% /alert %}} 
## **在将电子表格渲染为HTML时设置默认字体**
以下示例代码创建一个工作簿，并在第一个工作表的B4单元格中添加了一些文本，并将其字体设置为某个未知/不存在的字体。然后，它通过设置不同的默认字体名称，如Courier New、Arial、Times New Roman等，将工作簿保存为HTML。

截图显示通过[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)属性设置不同默认字体名称的效果。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

该代码生成带Courier New的[输出HTML文件](5472568)，带Arial的[输出HTML文件](5472567)和带Times New Roman的[输出HTML文件](5472565)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
