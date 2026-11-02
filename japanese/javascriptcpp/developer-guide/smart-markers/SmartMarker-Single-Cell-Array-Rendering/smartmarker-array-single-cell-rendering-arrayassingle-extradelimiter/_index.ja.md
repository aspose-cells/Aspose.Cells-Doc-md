---
title: SmartMarker による配列の単一セルレンダリング | Aspose.Cells for JavaScript via C++
linktitle: SmartMarker による配列の単一セルレンダリング | Aspose.Cells for JavaScript via C++
description: Aspose.Cells for JavaScript via C++ のスマートマーカーで ArrayAsSingle 属性と ExtraDelimiter 属性を使用し、配列データを単一セルにレンダリングする方法を学びます。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ ライブラリ, スプレッドシート, スマートマーカー, ArrayAsSingle, ExtraDelimiter, 配列の単一セルレンダリング, 配列レンダリング, テンプレート
type: docs
weight: 195
url: /ja/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、スマートマーカーを使用して配列データを単一セルにレンダリングできます。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を併用することで、開発者は単一セル内で配列要素を区切る方法を制御し、レポートやテンプレートの書式を柔軟に設定できます。
{{% /alert %}}

## **はじめに**
Aspose.Cells のスマートマーカーは、`&=DataSource.Field` などのマーカー式を使用してスプレッドシートにデータを動的に入力できる、テンプレートベースの強力な機能です。マーカーをデザイナー用ワークブックに配置し、テンプレートを `WorkbookDesigner` で処理すると、マーカーは指定したデータソースの値に置き換えられます。
既定では、スマートマーカーが配列プロパティ（例: `&=DataSource.Numbers`）を参照すると、エンジンは配列を展開し、各要素を横方向または縦方向に配置して、それぞれ別の隣接セルに格納します。この動作は多くのシナリオで便利です。しかし、配列要素を連結し、任意の区切り文字で区切って配列全体を1つのセルにレンダリングしたい場合は、この動作が適さない場合があります。
`ArrayAsSingle` 属性と `ExtraDelimiter` 属性をスマートマーカータグ内で併用すると、この要件を満たせます。レポートのレイアウトをコンパクトかつ予測可能な状態に保ちながら、配列データソースをネイティブに処理できます。

## **この機能が必要な理由**

### **既定の配列展開動作**
スマートマーカーが配列プロパティを参照すると、Aspose.Cells は既定で配列を複数のセルに展開します。たとえば、4 個の文字列からなる配列に対する `&=Product.Tags` のようなマーカーは、各値を個別のセルに配置します。これにより、隣接するテンプレート内容が押し出され、慎重に設計されたレポートのレイアウトが崩れる可能性があります。

### **ユースケースの制限**
既定の展開動作が望ましくない実際的なシナリオは多数あります。
- **サマリー形式のレポート** — レコードごとに1行のコンパクトなレイアウトが必要な場合。
- **タグ、ラベル、またはキーワードのリスト** — 値をカンマ区切りまたはパイプ区切りの単一セル内に表示する場合。
- **フィルターチップまたはステータス表示** — 可読性のために複数の値を1か所にまとめて表示する場合。
- **下流のパイプライン**（CSVエクスポート、PDFレンダリング、メールマージ）— 展開された範囲ではなく、セルごとに1つの結合された値を必要とする場合。
- **クロスプラットフォーム互換性** — 一部のコンシューマーが複数セルにまたがる配列を扱えない場合。

### **解決される課題**
組み込みのメカニズムがなければ、開発者は JavaScript でデータを前処理し、配列を区切り文字付き文字列に結合してから `WorkbookDesigner` にバインドする必要があります。この回避策ではロジックが重複し、データモデルが複雑になり、エラーが発生する可能性が高まります。`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、スマートマーカー内で書式設定を宣言的に処理できるため、この回避策が不要になります。

## **機能の利点**
スマートマーカーで `ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用すると、いくつかの利点が得られます。
- **単一セルへの格納** — すべての配列要素を1つのセルにレンダリングし、レイアウトをコンパクトかつ予測可能な状態に保ちます。
- **カスタム区切り文字の制御** — カンマ、セミコロン、ハイフン、パイプ、改行、または任意のカスタムテキストなど、任意の区切り文字を指定できます。
- **テンプレートによる書式設定** — データを前処理するための追加コードは不要で、書式設定のルールはスマートマーカータグ内に記述されます。
- **より整ったレポート** — 配列データによって隣接するテンプレート内容が別の行や列へ押し出されることがなくなります。
- **多様なデータ型** — 文字列、数値、日付、および区切り文字で結合できるその他のデータ型に対応します。
- **後方互換性** — 属性を省略すると元の展開動作が維持されるため、既存のテンプレートは変更なしで動作し続けます。

## **この機能の使用方法**

### **スマートマーカーの構文**
`ArrayAsSingle` 属性と `ExtraDelimiter` 属性は、標準のスマートマーカーの括弧内にキーと値のペアとして指定します。一般的な構文は次のとおりです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

マーカーは次の要素で構成されます。
- `&=DataSource.ArrayProperty` — バインドされたデータソースの配列プロパティを参照する標準のスマートマーカーです。
- `arrayasSingle=true` — 配列全体を単一セルにレンダリングするようエンジンに指示します。値が `true` の場合のみ、単一セルへのレンダリングが有効になります。
- `extraDelimiter=", "` — 配列要素間に挿入する区切り文字を定義します。値は文字列リテラルであり、空文字、単一文字、または複数文字の文字列を指定できます。

{{% alert color="primary" %}}
`extraDelimiter` 属性には、任意の文字列リテラルを指定できます。複数文字の区切り文字、カスタムテキスト、改行区切り出力用の `\n` などのエスケープシーケンスも使用できます。配列が空の場合、生成されるセルは空のままになります。
{{% /alert %}}

### **段階的なワークフロー**
次のワークフローは、スマートマーカーを使用して配列を単一セルにレンダリングする方法を説明します。
1. **データソースの準備** — 配列を返すプロパティを持つオブジェクト（またはデータ構造）を作成します。このプロパティは、文字列、数値、またはサポートされているその他の値型の配列を返すことができます。
2. **デザイナー用ワークブックの作成** — 新しい `Workbook` を作成し、ヘッダー行を追加します。次に、配列プロパティを参照し、`arrayasSingle` 属性と `extraDelimiter` 属性を指定したスマートマーカーセルを配置します。
3. **`WorkbookDesigner` のインスタンス化** — `WorkbookDesigner` オブジェクトを作成し、デザイナー用ワークブックを関連付け、`setDataSource` メソッドを使用してデータソースをバインドします。
4. **マーカーの処理** — `workbookDesigner.process()` メソッドを呼び出してスマートマーカーを展開し、実際のデータでワークブックの内容を入力します。
5. **結果の保存** — 結果のワークブックを XLSX またはサポートされているその他のファイル形式でディスクに保存します。

### **コード例 1 — 基本的な文字列配列のレンダリング**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **コード例 2 — カスタム区切り文字を指定した数値配列**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // セクション1: デフォルトのスマートマーカー - 値をセル横向 Ethics展开
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // セクション2: arrayasSingleとextraDelimiterを使用した新しい単一セルレンダリング
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // データソースをバインドしてスマートマーカーを処理
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // 結果のワークブックを保存
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **コード例 3 — 既定動作と ArrayAsSingle 動作の比較**

### **注記とベストプラクティス**
`ArrayAsSingle` 属性と `ExtraDelimiter` 属性を使用する際は、次の点に注意してください。
- `extraDelimiter` の値は文字列リテラルとして扱われます。テンプレートプロセッサーが解釈する可能性がある特殊文字はエスケープしてください。
- `arrayasSingle` 属性はブール値（`true` / `false`）を受け取ります。`true` の場合のみ単一セル動作が有効になり、それ以外の値では既定の展開動作にフォールバックします。
- 配列が空または `null` の場合、セルは空のままになります（データ型によっては空の文字列が含まれます）。
- この機能は、オブジェクトデータソースのほか、列を配列に分割できる表形式データソースでも機能します。
- 改行区切りの出力には、区切り文字として `\n` を使用します。

## 関連記事
- [Aspose.Cells for JavaScript via C++ でピボットテーブルにフィルター フィールドを追加する](/cells/ja/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ でピボットテーブルにスタイルを適用する](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルのページ フィールド レイアウトを変更する](/cells/ja/javascript-cpp/change-page-field-layout/)
- [Aspose.Cells for JavaScript via C++ でスパークラインを画像および HTML に変換する](/cells/ja/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Excel を OFD 形式に変換する](/cells/ja/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}