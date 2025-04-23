---
title: 电子表格编辑器知识库
type: docs
weight: 30
url: /zh/java/spreadsheet-editor-knowledge-base/
---

## **在任何地方嵌入HTML5电子表格编辑器**

HTML5电子表格编辑器可嵌入到任何网站、博客和论坛中，以在互联网上共享电子表格。它可以作为独立的编辑器嵌入，也可以加载带有电子表格文件的编辑器。

**作为独立的编辑器嵌入**

要作为独立的编辑器嵌入，使用HTML IFRAME标签添加到网站中。例如：

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**使用电子表格嵌入**

要将电子表格加载到嵌入式编辑器中，使用**url**参数。例如：

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
