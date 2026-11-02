---
title: Aspose.Cells for JavaScript via C++ を使用してスパークラインを画像と HTML に変換
linktitle: Aspose.Cells for JavaScript via C++ を使用してスパークラインを画像と HTML に変換
description: HtmlSaveOptions を使用して、セルに埋め込む独立した画像として Aspose.Cells のスパークラインをレンダリングする方法と、スパークラインを多数含むワークシートを HTML にエクスポートする方法を学習します。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, スパークライン, sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, スパークラインをレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/javascript-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインは、ワークシートのセル内に配置される小型グラフです。Aspose.Cells を使用すると、各スパークラインを独立した画像として抽出し、別のセルや外部レポートに埋め込むことができます。また、スパークラインを多数含むワークシート全体を、ブラウザーで配布するための HTML としてエクスポートできます。この記事で使用する `cell.embeddedImage` プロパティは、**Aspose.Cells 26.5 以降**で使用できます。
{{% /alert %}}

## **概要**
スパークラインは、ワークシート内で直接トレンドを可視化するためのコンパクトな手段です。Excel ユーザーにはセル内でそのまま表示されますが、実際の使用シーンでは、スパークラインをセルから外す必要がある場合があります。たとえば、別のセルに静的画像として埋め込む、自動生成されたメールに添付する、または Web に公開する HTML レポートの一部としてレンダリングする場合です。
Aspose.Cells は、この 2 つの操作をいずれもサポートしています。`sparkline.toImage` メソッドは個々のスパークラインを `Buffer` としてレンダリングします。生成されたバイト列を `cell.embeddedImage` に代入すると、画像をワークブック内の 1 つのセルに格納できます。また、`HtmlSaveOptions` を使用すると、スパークラインを含むワークブック全体を自己完結型の HTML ファイルに変換できます。このチュートリアルでは、両方のワークフローを手順を追って説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**
このワークフローでは、少量のデータ値を含むワークシートを作成し、その範囲に 3 種類の異なるスパークライングループ（Line、Column、Stacked／Win-Loss）を追加します。各グループを PNG としてレンダリングし、その PNG バイト列を隣接するセルに埋め込み画像として書き込みます。最終的な結果は、ネイティブのスパークラインと画像としてレンダリングされた対応物を含む、1 つの `.xlsx` ファイルになります。

### **手順**
1. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
2. セル `A1` から `E1` まで、5 つのサンプルの数値（例：日次売上高や温度測定値）を入力します。
3. `worksheet.getSparklineGroups().add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します。
   - アンカーが `F1`、データ範囲が `A1:E1` の `SparklineType.Line` グループ。
   - アンカーが `G1`、データ範囲が `A1:E1` の `SparklineType.Column` グループ。
   - アンカーが `H1`、データ範囲が `A1:E1` の `SparklineType.Stacked`（勝敗）グループ。
4. `ImageOrPrintOptions` インスタンスを作成し、`imageType` プロパティを `ImageType.Png` に設定して、各スパークラインを PNG 画像としてレンダリングします。
5. ワークブックを `output_with_sparklines.xlsx` として保存します。

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
        const { Workbook, CellArea, ImageOrPrintOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // 新しいワークブックを作成し、最初のワークシートにアクセスする
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // A1:E1のセルにサンプルデータを入力する
            cells.get("A1").value = 5;
            cells.get("B1").value = -3;
            cells.get("C1").value = 8;
            cells.get("D1").value = -2;
            cells.get("E1").value = 6;
            // F1（列5、行0）を基準位置にLineスパークライングループを追加する
            const lineArea = new CellArea();
            lineArea.startColumn = 5;
            lineArea.endColumn = 5;
            lineArea.startRow = 0;
            lineArea.endRow = 0;
            const lineIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Line,
                "A1:E1",
                false,
                lineArea
            );
            // G1（列6、行0）を基準位置にColumnスパークライングループを追加する
            const columnArea = new CellArea();
            columnArea.startColumn = 6;
            columnArea.endColumn = 6;
            columnArea.startRow = 0;
            columnArea.endRow = 0;
            const columnIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Column,
                "A1:E1",
                false,
                columnArea
            );
            // H1（列7、行0）を基準位置にWin/Loss（Stacked）スパークライングループを追加する
            const stackedArea = new CellArea();
            stackedArea.startColumn = 7;
            stackedArea.endColumn = 7;
            stackedArea.startRow = 0;
            stackedArea.endRow = 0;
            const stackedIdx = worksheet.sparklineGroups.add(
                AsposeCells.SparklineType.Stacked,
                "A1:E1",
                false,
                stackedArea
            );
            // PNG出力用の画像オプションを構成する
            const imageOptions = new ImageOrPrintOptions();
            imageOptions.imageType = AsposeCells.ImageType.Png;
            // Lineスパークラインを画像に変換し、F2セルに埋め込む
            const lineSp = worksheet.sparklineGroups.get(lineIdx).sparklines.get(0);
            cells.get("F2").embeddedImage = lineSp.toImage(imageOptions);
            // Columnスパークラインを画像に変換し、G2セルに埋め込む
            const columnSp = worksheet.sparklineGroups.get(columnIdx).sparklines.get(0);
            cells.get("G2").embeddedImage = columnSp.toImage(imageOptions);
            // Win/Lossスパークラインを画像に変換し、H2セルに埋め込む
            const stackedSp = worksheet.sparklineGroups.get(stackedIdx).sparklines.get(0);
            cells.get("H2").embeddedImage = stackedSp.toImage(imageOptions);
            // ワークブックをディスクに保存する
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_with_sparklines.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

上のコードにより、各スパークラインの視覚表現が 2 つの形式で存在するワークブックが生成されます。1 行目にアンカーされたネイティブのスパークラインと、2 行目の隣接セルに直接埋め込まれた静的な PNG 画像です。画像がファイル自体に格納されているため、ワークブックは単一の自己完結型ファイルとしてメール送信やアーカイブ保存ができ、埋め込み画像の参照が切れ、关于容ではありません。

{{% alert color="primary" %}}
各スパークライングループは 1 つのセルにアンカー付けされているため、コレクションを列挙する代わりに、インデクサー `group.getSparklines()[0]` で参照できます。これによりレンダリングコードを簡潔に保ち、「アンカーセルごとに 1 つのスパークライン」という一般的なパターンに対応できます。`cell.embeddedImage` を使用して画像バイト列を格納するには、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインを含むワークシートを HTML にエクスポート**
ワークブックにネイティブのスパークライン（および必要に応じて埋め込み画像）が含まれている場合、ワークシート全体を HTML として保存して Web に公開できます。`HtmlSaveOptions` クラスは、このエクスポートを制御するために必要な設定項目を提供します。このワークフローでは、ワークフロー 1 で作成した `output_with_sparklines.xlsx` ファイルを再利用し、簡潔な 1 ページの HTML ドキュメントに変換します。

### **手順**
1. ワークフロー 1 で作成した `output_with_sparklines.xlsx` ファイルが、作業ディレクトリに保存されていることを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、`exportActiveWorksheetOnly` プロパティを `true` に設定します。これにより、生成される HTML ファイルにはワークブック全体ではなく、アクティブワークシートのみが含まれます。
4. `workbook.save("sparklines.html", htmlOptions)` を呼び出して、HTML 出力をディスクに書き込みます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const htmlOptions = new HtmlSaveOptions();
                htmlOptions.exportActiveWorksheetOnly = true;
                const outputData = workbook.save(AsposeCells.SaveFormat.Html, htmlOptions);
                const blob = new Blob([outputData], { type: "text/html" });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "sparklines.html";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

上のコードは、ワークフロー 1 で作成したスパークラインを多数含むワークブックを、ポータブルな HTML ファイルに変換します。スパークライングループは、生成された HTML テーブル内のインライン画像としてレンダリングされるため、利用者は Excel をインストールしていなくても、最新のブラウザーでトレンドを確認できます。`exportActiveWorksheetOnly` を `true` に設定すると、非表示シートや補助データが誤って公開されるのを防ぎ、ユーザーに現在表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、`exportHiddenWorksheet`、`exportImagesAsBase64`、`encoding` など、出力を微調整するための追加プロパティがあります。必要に応じて、展開先の環境に合うよう調整してください。
{{% /alert %}}

## **API の概要**
上記のワークフローでは、いくつかの Aspose.Cells API を組み合わせて使用します。
- `SparklineGroup` とコレクションアクセサーの `worksheet.getSparklineGroups()` を使用し、各スパークライングループのタイプ（Line、Column、Stacked）、データ範囲、アンカーセルを宣言します。この state's 各グループを 1 つのセルにアンカー付けしているため、各グループには `worksheet.getSparklineGroups()[i]` でアクセスできます。
- `Sparkline` とインデクサー `group.getSparklines()[0]` を使用すると、グループ内の個々のスパークラインを取得できます。例では各グループにスパークラインが 1 つだけ含まれるため、反復ループは不要です。
- `sparkline.toImage(imageOrPrintOptions)` は、スパークラインの画像を `Buffer` として返すレンダリングメソッドです。返されたバイト列は `cell.embeddedImage` に直接代入できます。
- `HtmlSaveOptions.exportActiveWorksheetOnly`（ブール型）は、HTML エクスポートをアクティブワークシートに制限します。単一ページのレポートを生成する際、`HtmlSaveOptions` で最もよく使用されるプロパティーの 1 つです。
- `ImageOrPrintOptions.imageType` は、`toImage` によるレンダリングやワークシートを画像として印刷するときに使用する画像形式（例：`ImageType.Png`）を選択します。

{{< app/cells/assistant language="javascript-cpp" >}}