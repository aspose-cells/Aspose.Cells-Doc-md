---
title: 使用Node.js通过C++更改HTML链接的目标类型
linktitle: 更改HTML链接的目标类型
type: docs
weight: 320
url: /zh/nodejs-cpp/change-the-html-link-target-type/
description: 学习如何使用Aspose.Cells for Node.js via C++更改HTML链接的目标类型。控制你的HTML链接中的目标属性。
---

{{% alert color="primary" %}}

Aspose.Cells 允许您更改 HTML 链接的目标类型。 HTML 链接看起来像这样

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

如你所见，上述HTML链接中的target属性是**_self**。你可以使用[**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--)属性控制这个target属性。此属性接受具有以下值的[**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype)枚举。

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

以下代码说明了[**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--)属性的用法。它将链接目标类型更改为**blank**。默认值是**parent**。

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
