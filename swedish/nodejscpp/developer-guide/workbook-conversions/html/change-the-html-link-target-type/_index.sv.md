---
title: Ändra HTML Länk Måltids Typ med Node.js via C++
linktitle: Ändra HTML länkens målknapptype
type: docs
weight: 320
url: /sv/nodejs-cpp/change-the-html-link-target-type/
description: Lär dig hur du ändrar HTML länkens måltyp med Aspose.Cells for Node.js via C++. Kontrollera mål attributet i dina HTML länkar.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att ändra målet för HTML-länken. HTML-länken ser ut så här

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Som du kan se, är mål-attributet i länken ovan **_self**. Du kan kontrollera detta mål-attribut med hjälp av [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) egenskapen. Denna egenskap tar enum-värdet [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype) som har följande värden.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Följande kod illustrerar användningen av [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--) egenskapen. Den ändrar länkens måltyp till **blank**. Som standard är det **parent**.

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
