---
title: Изменение типа целевой ссылки HTML с помощью Node.js через C++
linktitle: Изменить тип HTML ссылки
type: docs
weight: 320
url: /ru/nodejs-cpp/change-the-html-link-target-type/
description: Узнайте, как изменить тип целевой ссылки HTML, используя Aspose.Cells for Node.js via C++. Управляйте атрибутом target в ваших HTML ссылках.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет вам изменять тип целевой ссылки HTML. HTML-ссылка выглядит так

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

Как видите, атрибут target в указанной HTML-ссылке — **_self**. Вы можете управлять этим атрибутом, используя свойство [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). Это свойство принимает перечисление [**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype), которое имеет следующие значения.

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

Следующий пример кода демонстрирует использование свойства [**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--). Он меняет тип целевой ссылки на **blank**. По умолчанию он **parent**.

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
