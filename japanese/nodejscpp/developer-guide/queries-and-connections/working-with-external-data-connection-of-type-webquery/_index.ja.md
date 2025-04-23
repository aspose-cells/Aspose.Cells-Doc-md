---
title: Node.jsとC++を使用したWebQueryタイプの外部データ接続の扱い方
linktitle: WebQueryタイプの外部データ接続の操作
type: docs
weight: 30
url: /ja/nodejs-cpp/working-with-external-data-connection-of-type-webquery/
description: Aspose.Cells for Node.js via C++を使用してWebQueryタイプの外部データ接続の操作方法を学ぶ。 
---

{{% alert color="primary" %}}

Workbook.DataConnectionsコレクションを使用して、任意の種類の外部データ接続にアクセスできます。そのようなデータ接続の1つはWebQueryです。この記事では、WebQueryデータ接続の操作方法を示します。Microsoft Excelで**Data** > **From Web** メニューを使用してWebQueryデータ接続を作成できます。

{{% /alert %}}

## WebQueryの外部データ接続を操作する

次のコードは、**WebQuery**タイプの外部データ接続を扱う方法を示しています。提供されたリンクからダウンロードできる[サンプルエクセルファイル](5112365.xlsx)を使用しています。コンソールには、このコードの出力も示されています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "WebQuerySample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const connections = workbook.getDataConnections();
if (connections.getCount() > 0) {
const connection = connections.get(0);

if (connection instanceof AsposeCells.WebQueryConnection) {
const webQuery = connection;
console.log("Web Query URL: " + webQuery.getUrl());
}
}
```

## コンソール出力

上記コードのコンソール出力は、この[サンプルエクセルファイル](5112365.xlsx)とともに以下に示されています。

{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/nodejs-cpp/

{{< /highlight >}}
