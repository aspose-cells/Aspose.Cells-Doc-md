---
title: ヘッダーとフッターのスマートマーカー | Aspose.Cells for Node.js via Java
linktitle: ヘッダー・フッターのスマートマーカー | Aspose.Cells for Node.js via Java
description: ページのヘッダーとフッターにダブルアングルブラケット構文と WorkbookDesigner.setEnableHeaderFooterMarkers スイッチを使用して JSON データソースから Smart Marker プレースホルダーを配置し、データ URI を使用して画像をバインドします。Aspose.Cells for Node.js via Java 用です。
keywords: Aspose.Cells for Node.js via Java, スマートマーカー, ヘッダー, フッター, ヘッダー フッターマーカー, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, JSON 行, データ バインディング, 画像, データ URI, JavaScript
type: docs
weight: 196
url: /ja/nodejs-java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
ページのヘッダーとフッターには、レポートのタイトル、報告期間、作成者、部門などのレポートメタデータが一般的に含まれます。この情報がワークブックの作成に使用されるデータソースにすでに存在している場合、手動で繰り返し入力すると不要な重複が生じます。
従来のスマートマーカー構文 `&=Source.Field` はワークシートの本体セルで処理されます。`PageSetup.setHeader` や `PageSetup.setFooter` を使用してヘッダーまたはフッターに従来のマーカーを配置すると、`WorkbookDesigner.process()` がスキャンするワークシートセルグリッドの対象外であるため、文字列のまま残ります。
**Aspose.Cells for Node.js via Java 26.11** 以降、デフォルトで `false` の `WorkbookDesigner.setEnableHeaderFooterMarkers` 設定により、`process()` はヘッダーおよびフッターのセクション文字列に記述された `<<Source.Field>>` プレースホルダーを解決します。`process()` を呼び出す前に `designer.setEnableHeaderFooterMarkers(true)` を実行してください。ヘッダーとフッターのプレースホルダーは本体マーカーと同じデータソースを使用します。
各ヘッダーとフッターにはアドレス指定可能な 3 つのセクションがあります。
- Section `0` は左側のセクションです。
- Section `1` は中央のセクションです。
- Section `2` は右側のセクションです。
`PageSetup.setHeader(int section, String value)` と `PageSetup.setFooter(int section, String value)` を使用してこれらのセクションに書き込みます。処理後は `PageSetup.getHeader(int section)` と `PageSetup.getFooter(int section)` を使用して完成したテキストを取得します。

{{% alert color="primary" %}}
`<<Source.Field>>` のようなプレースホルダーは、フィールド値をテキストとしてセクション文字列に挿入します。画像は `(picture)` サフィックスとデータ URI の値でバインドされます。
{{% /alert %}}

## **JSON 行データでヘッダー/フッターマーカーを有効化**
**Aspose.Cells for Node.js via Java 26.11** で JSON 行データを使用してヘッダーおよびフッターのプレースホルダーを解決する手順は次のとおりです。
1. `Workbook` を作成し、`workbook.getWorksheets().get(0)` で最初の `Worksheet` を取得します。
2. `PageSetup.setHeader` と `PageSetup.setFooter` を使用して、目的のヘッダーおよびフッターセクションに `<<Source.Field>>` プレースホルダーを書き込みます。
3. 行データを行オブジェクトの JSON 配列として準備し、プレースホルダーで使用されるソースプレフィックスと一致するソース名を選択します。たとえば、`node` という名前のソースは `<<node.Name>>` のようなプレースホルダーに対応します。`setDataSource` に渡すプレーンな JavaScript オブジェクトや配列はこのプラットフォームではバインドされません。サポートされている表形式は JSON です。
4. ワークブック用に `WorkbookDesigner` を作成します。
5. 処理前に `designer.setEnableHeaderFooterMarkers(true)` を呼び出します。
6. `designer.setJsonDataSource("node", '[{"Name":"...","Author":"..."}]')` で JSON を添付します。
7. `designer.process()` を呼び出します。
8. 処理後、ヘッダーまたはフッターテキストにプレースホルダーは残りません。`getHeader` と `getFooter` を使用して完成したセクション文字列を取得します。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource(
  "node",
  '[{"Name":"Q4 2026","Author":"Aspose.Cells"}]'
);
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
console.log("Footer: " + worksheet.getPageSetup().getFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.save("HeaderFooterSmartMarkers.xlsx");
```

## **JSON データソースの使用**
レポートデータが既に JSON で利用可能な場合、1 回の `setJsonDataSource` 呼び出しで全てのマーカースタイルに供給できます。`WorkbookDesigner.setJsonDataSource(String name, String json)` を呼び出してソースを添付します。
`name` 引数はプレースホルダーで使用されるソース名です。たとえば、`node` という名前は `<<node.Company>>` や `<<node.Title>>` のプレースホルダーに対応します。
`setJsonDataSource` に行データを直接渡します：
- 行配列（1 つ以上の行オブジェクトを含む JSON 配列）はサポートされます。
- 単一の行オブジェクトも直接渡すことができます。
- `{"rows":[...]}` のように名前付きトップレベルキーで行をラップしないでください。このラッパーはこのワークフローで期待される行指向の入力形状ではありません。
1 つの JSON ソースは、同じ `process()` 呼び出しで両方のマーカースタイルに供給できます。ワークシート本体セルの従来の `&=` マーカーと、ヘッダー・フッターセクションのダブルアングルブラケット `<<>>` プレースホルダーの両方を解決できます。ヘッダーおよびフッターのプレースホルダーを解決するには、引き続き `designer.setEnableHeaderFooterMarkers(true)` を呼び出す必要があります。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
worksheet.getCells().get("A1").putValue("&=node.Company");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", '[{"Company":"Aspose Pty Ltd","Title":"Half-Year Report"}]');
designer.process();
console.log("Left: " + worksheet.getPageSetup().getHeader(0));
console.log("Right: " + worksheet.getPageSetup().getHeader(2));
console.log("Body: " + worksheet.getCells().get("A1").getStringValue());
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.save("HeaderFooterJsonMarkers.xlsx");
```

## **スイッチとマルチ行ソースのセマンティクス**
`setEnableHeaderFooterMarkers` はデフォルトで `false` で、ヘッダーとフッターの `<<Source.Field>>` プレースホルダーのみを制御します。スイッチがオフの場合、`process()` は従来の `&=` 本体マーカーは解決しますが、ヘッダーまたはフッターの `<<Source.Field>>` プレースホルダーは文字列のまま残ります。
ヘッダーまたはフッターのセクションは単一の文字列であり、繰り返し領域ではありません。データソースに複数行が含まれている場合、最初の行がヘッダーとフッターの値を提供します。解決後、その値は通常のヘッダーまたはフッターのテキストとなります。`save` を呼び出した後もワークブックに残り、保存されたワークブックを再度ロードした際にも存在します。
以下の例は、同じマルチ行 JSON ソースを使用して 2 つのワークブックを作成し、無効化と有効化の動作を比較します。`plainDesigner` はプレースホルダーを変更せずに残し、`enabledDesigner` は最初の行を使用して解決します。

```javascript
const AsposeCells = require("aspose.cells");
const table = '[{"Name":"First Row"},{"Name":"Second Row"}]';
// Without the switch the placeholder stays literal text
const plainWorkbook = new AsposeCells.Workbook();
const plainSheet = plainWorkbook.getWorksheets().get(0);
plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const plainDesigner = new AsposeCells.WorkbookDesigner(plainWorkbook);
plainDesigner.setJsonDataSource("node", table);
plainDesigner.process();
// With the switch on, the FIRST row of a multi-row source wins
const enabledWorkbook = new AsposeCells.Workbook();
const enabledSheet = enabledWorkbook.getWorksheets().get(0);
enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
const enabledDesigner = new AsposeCells.WorkbookDesigner(enabledWorkbook);
enabledDesigner.setEnableHeaderFooterMarkers(true);
enabledDesigner.setJsonDataSource("node", table);
enabledDesigner.process();
console.log("Without switch: " + plainSheet.getPageSetup().getHeader(1));
console.log("With switch: " + enabledSheet.getPageSetup().getHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
```

## **ヘッダーまたはフッターに画像をバインドする**
`(picture)` サフィックスはヘッダーまたはフッターのセクションに画像をバインドします。画像を表示させたい位置に `<<node.logo(picture)>>` と記述し、フィールド値としてデータ URI を提供します。プレフィックスは `data:image/png;base64,` で、その後に画像バイトの Base64 文字列を続けます。`data:` プレフィックスがない単なる Base64 文字列は画像を埋め込みません。
`process()` 後：
1. プレースホルダーは標準のヘッダー・フッター画像コードである `&G` に置き換えられます。マーカーがセクション文字列内のコードになるため、`Logo: <<node.logo(picture)>>` のような長いテキストの中に配置できます。
2. 画像バイトはワークブック内にメディアパートとして埋め込まれ、対象ワークシートのヘッダー/フッタードローイングレイヤーに付随するため、ヘッダーまたはフッターとともに画像が印刷されます。

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
const table = [
    {
        logo: "data:image/png;base64," + fs.readFileSync("logo.png").toString("base64")
    }
];
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setEnableHeaderFooterMarkers(true);
designer.setJsonDataSource("node", JSON.stringify(table));
designer.process();
console.log("Header: " + worksheet.getPageSetup().getHeader(1));
// This prints:
// Header: Logo: &G
workbook.save("HeaderFooterPicture.xlsx");
```

印刷された `&G` は、Excel がヘッダーを描画する際に解釈する画像コードです。`logo.png` のバイトは `HeaderFooterPicture.xlsx` 内に格納され、コードの代わりに画像が印刷されます。
ヘッダーおよびフッターのスマートマーカーを使用するには、`setHeader` と `setFooter` を使用して左・中央・右のヘッダーまたはフッターセクションに `<<Source.Field>>` プレースホルダーを書き込みます。`process()` を呼び出す前に `designer.setEnableHeaderFooterMarkers(true)` を実行し、`designer.setJsonDataSource(name, json)` で値を提供します。完成したセクションは `getHeader` と `getFooter` で取得します。同じデータソースで本体マーカーとヘッダー・フッターのプレースホルダーを 1 回の処理で供給できます。画像をセクションにバインドするには、データ URI の値とともに `(picture)` サフィックスを追加します。

## 関連記事
- [SmartMarker 単一セル配列レンダリング](/cells/ja/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="nodejs-java" >}}