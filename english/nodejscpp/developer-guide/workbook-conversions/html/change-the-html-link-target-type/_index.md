---
title: Change the HTML Link Target Type with Node.js via C++
linktitle: Change the HTML Link Target Type
type: docs
weight: 320
url: /nodejs-cpp/change-the-html-link-target-type/
description: Learn how to change the HTML link target type using Aspose.Cells for Node.js via C++. Control the target attribute in your HTML links.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to change the HTML link target type. **The** HTML link looks like this

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

As you can see, the target attribute in the above HTML link is **_self**. You can control this target attribute using the [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) property. This property takes the [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype) enum which has the following values.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

The following code illustrates the usage of [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) property. It changes the link target type to **Self**. By default, it is **Parent**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

 // The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Sample1.xlsx");
const outputPath = path.join(dataDir, "Output.out.html");

const workbook = new AsposeCells.Workbook(inputPath);

const opts = new AsposeCells.HtmlSaveOptions();
opts.setLinkTargetType(AsposeCells.HtmlLinkTargetType.Self);

workbook.save(outputPath, opts);
console.log(`File saved: ${outputPath}`);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
