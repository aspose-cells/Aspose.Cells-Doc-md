---  
title: Node.js経由でC++を使用してURLからWeb画像をExcelワークシートに読み込む  
linktitle: ExcelワークシートにURLからのWeb画像をロードする  
type: docs  
weight: 30  
url: /ja/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/  
description: Aspose.Cells for Node.js via C++を使用してURLから画像を実際のExcel画像に変換する方法。  
keywords: ExcelでURLから画像を表示、ExcelのURLから画像へ、URLからExcelに画像を挿入、URLを画像に変換、ExcelのURLから画像をロード、Node.js、Excel  
---  

## ExcelワークシートにURLからの画像をロードする  

Aspose.Cells for Node.js via C++は、URLから画像を容易にExcelワークシートに読み込むためのシンプルで便利な方法を提供します。この記事では、画像データをストリームにダウンロードし、その後Aspose.Cells APIを使用してワークシートに挿入する方法を説明します。この方法では、画像はExcelファイルの一部となり、スプレッドシートを開くたびにダウンロードされません。  

## サンプルコード  

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const https = require("https");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "webimagebook.out.xlsx");
const url = "https://www.aspose.com/Images/aspose-logo.jpg"; // Changed http to https

let objImage;

https.get(url, (res) => {
const chunks = [];

res.on("data", (chunk) => {
chunks.push(chunk);
```  

{{% alert color="primary" %}}  
常にURLから更新された画像を取得したい場合があります。その場合には、[ウェブアドレスからリンクされた画像を挿入](/cells/ja/nodejs-cpp/insert-a-linked-picture-from-web-address/)の記事の指示に従うことができます。この方法を実行すると、スプレッドシートを開くたびにURLから画像が読み込まれます。  
{{% /alert %}}  


{{< app/cells/assistant language="nodejs-cpp" >}}
