---
title: 电子表格编辑器知识库
type: docs
weight: 30
url: /zh/java/spreadsheet-editor-knowledge-base/
---

## **在任何地方嵌入HTML5电子表格编辑器**

HTML5电子表格编辑器可嵌入到任何网站、博客和论坛，用于在互联网上共享电子表格。它可以作为独立编辑器嵌入，也可以加载电子表格文件。

**嵌入为独立编辑器**

要作为独立编辑器嵌入，可以使用HTML IFRAME标签添加到网站中。例如:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**加载电子表格**

要在嵌入的编辑器中加载电子表格**url**参数。例如:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
