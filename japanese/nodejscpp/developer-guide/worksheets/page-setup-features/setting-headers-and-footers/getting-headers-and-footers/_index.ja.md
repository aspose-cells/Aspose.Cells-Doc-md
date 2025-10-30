---
title: Node.jsを利用してC++経由でヘッダーやフッターを取得する方法
linktitle: ヘッダーまたはフッターの取得
type: docs
weight: 30
url: /ja/nodejs-cpp/get-headers-or-footers/
description: この資料では、Node.jsをC++ API経由で使ってExcelやOpenOfficeのファイルからヘッダーとフッターをプログラム的に取得する方法について解説します。
---

{{% alert color="primary" %}}

ヘッダーとフッターは、ページレイアウトビュー、印刷プレビュー、および印刷されたページでのみ表示されます。 

複数のワークシートでヘッダーやフッターを表示する場合は、ページ設定ダイアログボックスも使用できます。 

チャートシートやチャートなどの他のシートタイプでは、ページ設定ダイアログボックスを使用してのみヘッダーやフッターを挿入できます。

{{% /alert %}}

## **MS Excelでのヘッダーとフッターの取得**
1. ヘッダーやフッターを表示または変更したいワークシートをクリックします。
2. 表示タブの「ワークブックビュー」グループで、「ページレイアウト」をクリックします。
   Excelはワークシートをページレイアウトビューで表示します。
3. ヘッダーやフッターを表示または編集するには、ワークシートページの上（ヘッダーの下）または下（フッターの上）にある左、中央、または右のヘッダーまたはフッターテキストボックスをクリックします。


## **Aspose.Cells for Node.js via C++を使ってヘッダーとフッターを取得する方法**
[**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-)と[**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-)メソッドを使えば、Node.js開発者は簡単にファイルからヘッダーやフッターを取得できます。

1. ブックを作成してファイルを開く。
2. ヘッダーまたはフッターを取得したいワークシートを取得します。
3. 特定のセクションIDを持つヘッダーまたはフッターを取得します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **ヘッダーとフッターをコマンドリストに解析する**
ヘッダーまたはフッターテキストには、ページ番号や現在の日付、テキストの書式設定属性などの特殊コマンドを含めることができます。

特殊コマンドは、先頭にアンパサンド（"&"）を付けた1つの文字で表されます。

ヘッダーとフッターの文字列は、ABNF文法を用いて構築されています。ビューアなしでは理解しにくいです。

Aspose.Cells for Node.js via C++は、ヘッダーとフッターをコマンドリストとして解析するための[**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-)メソッドを提供します。

次のコードは、ヘッダーまたはフッターをコマンドリストとして解析し、コマンドを処理する方法を示しています：

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
