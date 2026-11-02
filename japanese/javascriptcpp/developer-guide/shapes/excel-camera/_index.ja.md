---
title: Aspose.Cells for JavaScript via C++ の Excel カメラ
linktitle: Aspose.Cells for JavaScript via C++ の Excel カメラ
description: Aspose.Cells for JavaScript via C++ で Excel カメラの使用方法を学び、セル範囲にリンクされてソースデータに応じて更新され、ソースのすべての書式設定を保持する動的画像を作成します。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, Excel カメラ, 動的画像, リンクされた画像, picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /ja/javascript-cpp/excel-camera/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel カメラは、セル範囲の画像をリアルタイムにレンダリングし、通常の画像と同様に描画レイヤーに浮遊するワークシートオブジェクトです。Aspose.Cells は、ソースデータが変わるたびに自動更新される動的画像と、範囲の一度限りのスナップショットをキャプチャする静的画像の 2 つの作成モードをサポートしています。このSebastien-shaでは両方のアプローチを紹介するので、レイアウトに適した方法を選択できます。

## Excel カメラとは？
Excel カメラは、本質的には、ワークシートの描画レイヤーに特定の行と列にアンカーされた画像オブジェクトです。通常の挿入画像とは異なり、Excel カメラは `"A1:F10"` などの A1 形式の数式を通じてソース範囲にリンクされます。その範囲内のセルが変更されるたびに、カメラの画像が自動的に更新され、新しい内容を反映します。Excel カメラは、罫線、背景色、フォント、数値形式など、ソース範囲の書式設定をすべて保持します。そのため、セル内で表示される内容もすべてカメラの画像に反映されます。この機能は、スクロールやデータの重複を行わずに、ワークシート内の離れた領域を可視化したいダッシュボード、要約、サイドパネル、レポートレイアウトに特にUsefulです。留意点が 2 つあります。ワークブックを保存する前に `updateSelectedValue()` を呼び出す必要があります。また、これらの形式はライブの再計算ではなく埋め込み画像データに依存するため、ファイルは HTML または PDF にエクスポートされます。

## 方法 1 — 動的カメラ画像を追加する
動的カメラは最も一般的な方法であり、Excel の組み込みカメラ ツールに最も近い動作をします。初期状態の画像内容を持たない画像を追加し、ソース範囲を参照する `formula` を割り当てることによって機能します。数式を割り当てた後、`updateSelectedValue()` を呼び出すと、埋め込み画像データが更新され、参照元セルと同期します。Excel カメラは専用クラスを使って実装されているわけではなく、標準の `Picture` 型のみで構成されています。
主な API は次のとおりです。
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, null)` — 指定した行と列にアンカーされた画像を追加します。画像パラメーターに `null` を渡すと、動的カメラのプレースホルダーとなる空の画像が作成されます。このメソッドは新しい画像のインデックスを返します。
- `worksheet.getPictures().get(index)` — コレクションから特定の `Picture` を取得します。
- `picture.formula` — Excel カメラが同期するソース範囲の A1 形式の参照を保持する文字列プロパティです。例として `"A1:F10"` があります。
- `picture.updateSelectedValue()` — `formula` で参照されているセルから埋め込み画像データを更新する、戻り値のないメソッドです。

{{% alert color="primary" %}}
出力が HTML または PDF の場合、保存する前に `updateSelectedValue()` を必ず呼び出す必要があります。呼び出さないと、エクスポートされたファイルに画像データが含まれず、レンダリングされた出力で Excel カメラが空白表示になります。
次のコードは、ワークブックを作成し、10 行目、6 列目にアンカーされた空の画像を追加し、`formula` プロパティを通じてソース範囲 `A1:F10` にリンクし、埋め込み画像データを更新して、ワークブックを保存します。
{{% /alert %}}

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // ダイナミックカメラ：空の画像を追加し、FormulaでA1:F10にリンクしてから更新する
            const pictures = worksheet.pictures;
            const index = pictures.add(10, 6, null);
            const picture = pictures.get(0);
            picture.formula = "A1:F10";
            picture.updateSelectedValue();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_dynamic.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## 方法 2 — 静的カメラ画像を追加する
静的カメラは、本質的には、セル範囲を一度レンダリングしたプレビューです。常に更新されるリンクを維持する代わりに、範囲を画像バイト列に一度だけレンダリングし、そのバイト列を `Buffer` でラップして通常の画像として追加します。画像の内容は作成時の状態に固定され、ソースセルが変更されても自動更新されません。
主な API は次のとおりです。
- `cells.createRange(address)` — `"A1:F10"` などの A1 形式のアドレスから `Range` オブジェクトを構築します。
- `range.toImage(options)` — 範囲を画像バイト列にレンダリングします。`null` を渡すと既定の描画オプションを使用し、出力をより細かく制御できるオーバーロードもあります。
- `Buffer.from(imageBytes)` — レンダリングされた画像バイト列を `Buffer` でラップし、`worksheet.getPictures().add` に渡せるようにします。
- `worksheet.getPictures().add(upperLeftRow, upperLeftColumn, imageBuffer)` — 指定した行と列にアンカーされた画像を追加します。この場合は、レンダリングによって生成された `Buffer` を渡します。
次のコードは、ワークブックを作成し、`A1:F10` の `Range` を構築し、`range.toImage(null)` で画像バイト列にレンダリングし、そのバイト列を `Buffer` でラップして、10 行目、6 列目にアンカーされた画像を追加し、ワークブックを保存します。

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
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "CameraDemo";
            // 静的カメラ: Range を構築し、バイト列にレンダリングして、MemoryStream でラップし、画像として追加
            const range = worksheet.cells.createRange("A1:F10");
            const imageData = range.toImage();
            const pictures = worksheet.pictures;
            pictures.add(10, 6, imageData);
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_static.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## 動的カメラと静的カメラの選択
- **動的カメラ:** 再計算ごとに更新されます。`updateSelectedValue()` を呼び出した後は HTML または PDF にエクスポートでき、ファイル有効期間中もライブリンクの動作を維持します。
- **静的カメラ:** 一度だけレンダリングされ、更新されません。データのライブミラーではなく、ビルド時に埋め込む固定のスナップショットが必要な場合に適しています。
Aspose.Cells は、`picture.formula` と `updateSelectedValue()` に基づく動的で自動更新されるカメラと、`range.toImage` と `Buffer` に基づく静的で一度限りのカメラの両方をサポートしています。出力がソースセルと同期する必要がある場合は動的アプローチを、ビルド時に必要な固定のスナップショットだけが必要な場合は静的アプローチを選択してください。

## 関連記事
- [Aspose.Cells for JavaScript via C++ でスパークラインを画像と HTML に変換](/cells/ja/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Aspose.Cells for JavaScript via C++ でピボットテーブルにフィルター フィールドを追加](/cells/ja/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ でピボットテーブルにスタイルを適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}