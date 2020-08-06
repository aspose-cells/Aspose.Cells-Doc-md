---
title: Spreadsheet Editor Knowledge Base
type: docs
weight: 30
url: /java/spreadsheet-editor-knowledge-base/
---

**Table of Contents**

- [Embed HTML5 Spreadsheet Editor Anywhere](#SpreadsheetEditorKnowledgeBase-EmbedHTML5SpreadsheetEditorAnywhere)
### **Embed HTML5 Spreadsheet Editor Anywhere**
HTML5 Spreadsheet Editor can be embedded into any website, blog and forums to share spreadsheets across the internet. It can be embedded as a standalone editor or you can load it with a spreadsheet file.

**Embed as standalone editor**

To embed as a standalone editor, use the HTML IFRAME tag to add into the website. For example:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**Embed with a spreadsheet**

To load a spreadsheet into an embedded editor **url** parameter as described in [Open from URL](/pages/createpage.action?spaceKey=cellsjava&title=1.2.1.4+Open+from+URL&linkCreation=true&fromPageId=5275663). For example:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
