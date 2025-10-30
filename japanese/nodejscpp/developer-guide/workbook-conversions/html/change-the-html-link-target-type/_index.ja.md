---
title: Node.jsとC++を使用してHTMLのリンクターゲットタイプを変更
linktitle: HTMLリンクのターゲットタイプを変更する
type: docs
weight: 320
url: /ja/nodejs-cpp/change-the-html-link-target-type/
description: Aspose.Cells for Node.js via C++を使ってHTMLリンクのターゲットタイプを変更する方法を学びます。HTMLリンクのターゲット属性を制御します。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、HTMLリンクのターゲットタイプを変更できます。HTMLリンクは以下のようになります。

{{< highlight javascript >}}

 <a href="http://www.aspose.com/" target="_self">

{{< /highlight >}}

上のHTMLリンクのターゲット属性は**_self**です。[**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--)プロパティを使用してこのターゲット属性を制御できます。このプロパティは以下の値を持つ[**HtmlLinkTargetType**](https://reference.aspose.com/cells/nodejs-cpp/htmllinktargettype)列挙型を受け取ります。

- HtmlLinkTargetType.Blank
- HtmlLinkTargetType.Parent
- HtmlLinkTargetType.Self
- HtmlLinkTargetType.Top

{{% /alert %}}

以下のコードは[**HtmlSaveOptions.getLinkTargetType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getLinkTargetType--)プロパティの使用例を示しています。リンクターゲットタイプを**blank**に変更します。デフォルトは**parent**です。

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
