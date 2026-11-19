---
title: ヘッダーとフッターのスマートマーカー | Aspose.Cells .NET
linktitle: ヘッダー・フッターのスマートマーカー | Aspose.Cells
description: ページのヘッダーとフッターに、二重山かっこ構文と WorkbookDesigner.EnableHeaderFooterMarkers スイッチを使用して、DataTable または JSONデータソースから Smart Marker プレースホルダーを配置し、データURI を介して画像をバインドできます（Aspose.Cells for .NET）。
keywords: Aspose.Cells, スマートマーカー, ヘッダー, フッター, ヘッダー フッター マーカー, EnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, SetHeader, SetFooter, SetJsonDataSource, DataTable, データバインディング, 画像, データURI, C#
type: docs
weight: 196
url: /ja/net/smart-markers-in-headers-and-footers/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **想定利用シナリオ**
ページのヘッダーとフッターには、レポートのタイトル、期間、作成者、部門などのメタデータが含まれることが一般的です。この情報がワークブックのデータソースに既に存在する場合、手動で繰り返し入力すると不要な重複が生じます。  
従来の Smart Marker 構文 `&=Source.Field` はワークシートの本体セルで処理されます。`PageSetup.SetHeader` または `PageSetup.SetFooter` を使用してヘッダーまたはフッターに従来のマーカーを配置した場合、`WorkbookDesigner.Process()` がスキャンするワークシートセルグリッドの対象外であるため、文字列はそのままリテラルテキストとして残ります。  
**Aspose.Cells for .NET 26.11** 以降、デフォルトが `false` の `WorkbookDesigner.EnableHeaderFooterMarkers` スイッチを `true` に設定して `Process()` を呼び出すと、ヘッダーおよびフッターのセクション文字列内に記述された `<<Source.Field>>` プレースホルダーが解決されます。ヘッダーとフッターのプレースホルダーは本体マーカーと同じデータソースを使用します。  
各ヘッダーとフッターは 3 つのアドレス可能なセクションで構成されます：
- セクション `0` は左側セクションです。
- セクション `1` は中央セクションです。
- セクション `2` は右側セクションです。  
`PageSetup.SetHeader(int section, string value)` および `PageSetup.SetFooter(int section, string value)` を使用してこれらのセクションに書き込みます。処理後は `PageSetup.GetHeader(int section)` および `PageSetup.GetFooter(int section)` で完成した文字列を取得します。

{{% alert color="primary" %}}
`<<Source.Field>>` のようなプレースホルダーは、フィールド値をテキストとしてセクション文字列に挿入します。画像は `(picture)` サフィックスとデータURIの値でバインドします。
{{% /alert %}}

## **DataTable を使用したヘッダー/フッターマーカーの有効化**
`DataTable` を使用してヘッダーおよびフッターのプレースホルダーを解決するには、**Aspose.Cells for .NET 26.11** の次の一連の手順に従います：

1. `Workbook` を作成し、インデックス `0` の最初の `Worksheet` を取得します。  
2. `PageSetup.SetHeader` と `PageSetup.SetFooter` を使用して、目的のヘッダーおよびフッターセクションに `<<Source.Field>>` プレースホルダーを書き込みます。  
3. `DataTable` を作成し、プレースホルダーで使用されるソースプレフィックスと同じテーブル名にします。例えば、テーブル名 `node` は `<<node.Name>>` などのプレースホルダーに対応します。  
4. `Workbook` に対して `WorkbookDesigner` を作成します。  
5. 処理前に `designer.EnableHeaderFooterMarkers` を `true` に設定します。  
6. `designer.SetDataSource(table)` でテーブルを添付します。  
7. `designer.Process()` を呼び出します。  
8. 処理後、ヘッダーまたはフッターのテキストからプレースホルダーは削除されます。`GetHeader` と `GetFooter` を使用して完成したセクション文字列を取得します。

```csharp
using System;
using System.Data;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Center header and center footer carry <<Source.Field>> placeholders
worksheet.PageSetup.SetHeader(1, "Quarterly Report - <<node.Name>>");
worksheet.PageSetup.SetFooter(1, "Prepared by <<node.Author>>");
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Columns.Add("Author");
table.Rows.Add("Q4 2026", "Aspose.Cells");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
Console.WriteLine("Footer: " + worksheet.PageSetup.GetFooter(1));
// This prints:
// Header: Quarterly Report - Q4 2026
// Footer: Prepared by Aspose.Cells
workbook.Save("HeaderFooterSmartMarkers.xlsx");
```

## **JSON データソースの使用**
レポートデータが既に JSON 形式で入手可能な場合、`DataTable` の代わりに JSON を使用できます。`WorkbookDesigner.SetJsonDataSource(string name, string json)` を呼び出してソースを添付します。  
`name` 引数は `DataTable` の名前と同じ役割を果たします。たとえば、名前 `node` は `<<node.Company>>` および `<<node.Title>>` といったプレースホルダーに対応します。  
`SetJsonDataSource` には行データを直接渡します。  
- 複数の行オブジェクトを含む JSON 配列など、行配列がサポートされます。  
- 単一の行オブジェクトも直接渡すことができます。  
- `{"rows":[...]}` のように名前付きのトップレベルキーで行をラップしないでください。このラッパーはこのワークフローで期待される行指向の入力形式ではありません。  
1 つの JSON ソースで、同一の `Process()` 呼び出し中に両方のマーカースタイルを設定できます。ワークシート本体セルの従来の `&=` マーカーと、ヘッダーおよびフッターセクションの二重山かっこ `<<>>` プレースホルダーの両方を解決できます。ヘッダーおよびフッターのプレースホルダーを解決するには、引き続き `EnableHeaderFooterMarkers` を有効にする必要があります。

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Left header, right header, and a classic body marker — one JSON source feeds all three
worksheet.PageSetup.SetHeader(0, "<<node.Company>>");
worksheet.PageSetup.SetHeader(2, "Page <<node.Title>>");
worksheet.Cells["A1"].PutValue("&=node.Company");
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
designer.Process();
Console.WriteLine("Left: " + worksheet.PageSetup.GetHeader(0));
Console.WriteLine("Right: " + worksheet.PageSetup.GetHeader(2));
Console.WriteLine("Body: " + worksheet.Cells["A1"].StringValue);
// This prints:
// Left: Aspose Pty Ltd
// Right: Page Half-Year Report
// Body: Aspose Pty Ltd
workbook.Save("HeaderFooterJsonMarkers.xlsx");
```

## **スイッチとマルチ行ソースのセマンティクス**
`EnableHeaderFooterMarkers` のデフォルトは `false` で、このスイッチはヘッダーおよびフッターの `<<Source.Field>>` プレースホルダーのみを制御します。スイッチがオフの場合、`Process()` は従来の `&=` 本体マーカーは引き続き解決しますが、ヘッダーまたはフッター内の `<<Source.Field>>` プレースホルダーはリテラルテキストのままです。  
ヘッダーまたはフッターのセクションは単一の文字列であり、繰り返しバンドではありません。データソースに複数行が含まれている場合、最初の行がヘッダーとフッターの値を供給します。解決された後、これらの値は通常のヘッダー・フッターテキストとなり、`Save` を呼び出した後もワークブックに残り、保存されたワークブックを再度読み込んでも保持されます。  
以下の例は、同じマルチ行 `DataTable` を使用して 2 つのワークブックを作成し、スイッチが無効と有効の場合の動作を比較しています。`plainDesigner` はプレースホルダーを変更せずに残し、`enabledDesigner` は最初の行を使用してプレースホルダーを解決します。

```csharp
using System;
using System.Data;
using Aspose.Cells;
DataTable table = new DataTable("node");
table.Columns.Add("Name");
table.Rows.Add("First Row");
table.Rows.Add("Second Row");
// Without the switch the placeholder stays literal text
Workbook plainWorkbook = new Workbook();
Worksheet plainSheet = plainWorkbook.Worksheets[0];
plainSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
plainDesigner.SetDataSource(table);
plainDesigner.Process();
// With the switch on, the FIRST row of a multi-row source wins
Workbook enabledWorkbook = new Workbook();
Worksheet enabledSheet = enabledWorkbook.Worksheets[0];
enabledSheet.PageSetup.SetHeader(1, "<<node.Name>>");
WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
enabledDesigner.EnableHeaderFooterMarkers = true;
enabledDesigner.SetDataSource(table);
enabledDesigner.Process();
Console.WriteLine("Without switch: " + plainSheet.PageSetup.GetHeader(1));
Console.WriteLine("With switch: " + enabledSheet.PageSetup.GetHeader(1));
// This prints:
// Without switch: <<node.Name>>
// With switch: First Row
enabledWorkbook.Save("HeaderFooterMarkersEnabled.xlsx");
```

## **ヘッダーまたはフッターに画像をバインドする**
`(picture)` サフィックスは画像をヘッダーまたはフッターのセクションにバインドします。画像を表示したい位置に `<<node.logo(picture)>>` と記述し、フィールド値としてデータURIを提供します――プレフィックス `data:image/png;base64,` に続けて画像バイトの Base64 テキストを付加します。`data:` プレフィックスなしの純粋な Base64 文字列だけでは画像は埋め込まれません。  
`Process()` 後:  
1. プレースホルダーは標準のヘッダー・フッタ画像コード `&G` に置き換えられます。マーカーがセクション文字列内のコードになるため、`Logo: <<node.logo(picture)>>` のような長いテキストの中に配置できます。  
2. 画像バイトはワークブック内のメディアパートとして、そのワークシートのヘッダー/フッター描画層に添付されるため、ヘッダーまたはフッターとともに画像が印刷されます。

```csharp
using System;
using System.Data;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// The (picture) suffix binds the image named by the data-URI field into the header
worksheet.PageSetup.SetHeader(1, "Logo: <<node.logo(picture)>>");
DataTable table = new DataTable("node");
table.Columns.Add("logo");
table.Rows.Add("data:image/png;base64," + Convert.ToBase64String(File.ReadAllBytes("logo.png")));
WorkbookDesigner designer = new WorkbookDesigner(workbook);
designer.EnableHeaderFooterMarkers = true;
designer.SetDataSource(table);
designer.Process();
Console.WriteLine("Header: " + worksheet.PageSetup.GetHeader(1));
// This prints:
// Header: Logo: &G
workbook.Save("HeaderFooterPicture.xlsx");
```

印刷時に表示される `&G` は、Excel がヘッダーを描画するときに解釈する画像コードです――`logo.png` バイトは現在 `HeaderFooterPicture.xlsx` に格納されており、コードの代わりに画像が印刷されます。  
ヘッダーやフッターで Smart Markers を使用するには、`SetHeader` および `SetFooter` で左・中央・右の各セクションに `<<Source.Field>>` プレースホルダーを書き込みます。`WorkbookDesigner` の `EnableHeaderFooterMarkers` を `true` に設定してから `Process()` を呼び出し、`SetDataSource(DataTable)` または `SetJsonDataSource` のいずれかで値を供給します。完成したセクションは `GetHeader` と `GetFooter` で取得できます。同じデータソースで本体マーカーとヘッダー・フッタープレースホルダーを 1 回の処理で設定できます。画像をセクションにバインドするには、データURI値と共に `(picture)` サフィックスを付加します。

## **関連記事**
- [SmartMarker シングルセル配列レンダリング](/cells/ja/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="csharp" >}}