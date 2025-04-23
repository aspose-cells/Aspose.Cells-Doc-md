---
title: Node.js経由のC++でヘッダーとフッターを設定する方法
linktitle: ヘッダーとフッターの設定
type: docs
weight: 30
url: /ja/nodejs-cpp/setting-headers-and-footers/
description: この記事では、Aspose.Cells for Node.js via C++を使用してExcelのワークシートのヘッダーとフッターに画像をプログラム的に挿入する方法について説明します。 
keywords: Excelのヘッダーやフッターに画像を挿入する Node.js経由のC++スクリプトコマンド設定
---

{{% alert color="primary" %}}

ヘッダーとフッターはそれぞれ上部の余白の下に表示されるテキスト行です。ワークシートにもヘッダーやフッターを追加することができます。ヘッダーやフッターには、ページ番号、著者名、トピック名、または日付と時刻などの有用な情報を表示することができます。ヘッダーとフッターはページ設定の設定を使用して管理されます。

{{% /alert %}}

## **ヘッダーとフッタの設定**

Aspose.Cells for Node.js via C++では、実行時にワークシートにヘッダーとフッターを追加できますが、印刷のためには事前にデザインされたファイルに手動で設定することを推奨します。Microsoft ExcelをGUIツールとして使用し、ヘッダーとフッターの設定を行えば、労力と開発時間を節約できます。Aspose.Cellsはファイルをインポートして設定を保存できます。

ヘッダーやフッターをランタイムで追加するために、Aspose.Cells は特別な API 呼び出しとスクリプトコマンドを提供しています。

### **スクリプトコマンド**

スクリプトコマンドは、ヘッダーやフッターのフォーマットを設定する特別なコマンドです。

|**スクリプトコマンド**|**説明**|
| :- | :- |
|&P|現在のページ番号
|&G|画像
|&N|ページの総数
|&D|現在の日付
|&T|現在の時刻
|&A|ワークシート名
|&F|パスを除いたファイル名
|&&Text|は &Text を表示します。例： &&WO は &WO と表示されます|
|&"\<FontName>"|フォント名を表します。例: &"Arial"
|&"\<FontName>, \<FontStyle>"|スタイル付きのフォント名を表します。例: &"Arial,Bold"
|&\<FontSize>|フォントサイズを表します。例：「&14abc」。ただし、このコマンドの後にヘッダーに印刷されるプレーンな数字が続く場合、その数字はフォントサイズとスペースで区切る必要があります。例：「&14 123」。|

### **ヘッダーやフッタの設定**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)クラスは、ワークシートにヘッダーとフッターを追加するための[**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-)と[**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-)の2つのメソッドを提供します。これらのメソッドは2つのパラメータだけを受け取ります：

- **Section** – ヘッダーやフッターを配置するセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **Script** – ヘッダーやフッターのために使用するスクリプト。このスクリプトにはヘッダーやフッターをフォーマットするためのスクリプトコマンドが含まれます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **ヘッダーやフッターに画像を挿入**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)クラスには、ヘッダーとフッターに画像を追加するための[**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-)と[**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-)の追加メソッドがあります。これらのメソッドは次のパラメータを受け取ります：

- **Section** – 画像が配置されるヘッダーやフッターセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **バイト配列** – グラフィカルデータ（バイナリデータはバイト配列のバッファに書き込む必要があります）。

以下のコードを実行し、ファイルを開いた後、ワークシートのヘッダーを確認してください。

1. **ファイル** メニューから **ページ設定** を選択します。ダイアログが表示されます。
1. **ヘッダー/フッター** タブを選択します。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
