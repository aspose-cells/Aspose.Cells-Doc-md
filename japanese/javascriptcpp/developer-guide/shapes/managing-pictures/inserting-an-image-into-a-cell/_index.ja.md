---
title: セルに画像を挿入する
linktitle: セルに画像を挿入する
description: Aspose.Cells for JavaScript via C++ は、スプレッドシートファイルを操作するためのライブラリです。このProvisioningでは、浮動画像をセル上に配置するか、画像をセルに直接埋め込むことで、画像を 1 つのセルに正確に合わせる方法を説明します。
keywords: Aspose.Cells, JavaScript via C++ ライブラリ, スプレッドシート, 画像の挿入, 画像の埋め込み, セル内の画像, 画像をセルに合わせる, Pictures, EmbeddedImage
type: docs
weight: 80
url: /ja/javascript-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells には、画像を 1 つのセルに関連付ける方法として、異なる 2 つの方法があります。浮動画像は、セル範囲に視覚的に重なるワークシートの描画レイヤー上のシェイプです。一方、埋め込み画像はセル自体に格納され、セルの表示領域に合わせて自動的にスケールします。レイアウト要件に最もよく合う方法を選択してください。
{{% /alert %}}

## **導入**
画像を 1 つのセルに正確に合わせることは、視覚的なレポート、商品カタログ、従業員ディレクトリ、ダッシュボード、または在庫リストとして機能するスプレッドシートを設計する場合によくある要件です。画像を多数のセルにまたがって引き伸ばしたり、ワークシート上に緩く配置するよりも、その画像が属するセルと常に整列し、セルに明確に紐づく画像が望ましい場合があります。
Aspose.Cells では、この要件を相補的な 2 つの方法で実現できます。
- **方法 1 — セル上に浮動画像を配置する。** `Picture` をワークシートに追加し、`picture.setPlacement(PlacementType.MoveAndSize)` で配置動作を設定します。続いて、`picture.setUpperLeftRow()`、`picture.setUpperLeftColumn()`、`picture.setLowerRightRow()`、`picture.setLowerRightColumn()` でアンカーセルを調整し、画像が 1 つのセルだけを覆うようにします。
- **方法 2 — 画像をセルに直接埋め込む。** `cell.setEmbeddedImage(imageBuffer)` を使って、画像データを含む `Buffer` をセルに割り当てます。画像は自動的にセルの表示領域に合わせてスケールし、セルとともに移動します。
以降では、両方の方法、関連 API、およびコードでの使用例について説明します。

## **方法 1: セル上に画像を配置する**
浮動画像は、ワークシートの描画レイヤーに存在する `Picture` オブジェクトです。どの単一セルにも属しませんが、セル範囲にアンカーされます。画像のアンカーセル（左上端と右下端のコーナー）は、ワークシート上で画像が表示される範囲を決定します。既定では、新しく追加した画像は複数のセルにまたがります。
浮動画像が**1 つのセルだけ**を覆うようにするには、次の操作が必要です。
1. `worksheet.getPictures().add(row, column, imageBuffer)` を使って画像を追加します。`imageBuffer` は画像データを含む `Buffer` です。この操作により、新しい画像が指定したセルにアンカーされます。
2. 画像の境界矩形が対象セルと一致するよう、4 つのアンカー値を設定します。
3. `picture.setPlacement(PlacementType.MoveAndSize)` を呼び出します。これにより、ユーザーが列幅または行高を変更しても、対象のセルとともに画像が移動およびサイズ変更されます。

### **画像を 1 つのセルにアンカーする**
画像のアンカーは、4 つの 0 始まりのインデックス用アクセサーで定義されます。
- `picture.getUpperLeftRow()` と `picture.setUpperLeftRow(value)` — 画像の上端の行インデックス。
- `picture.getUpperLeftColumn()` と `picture.setUpperLeftColumn(value)` — 画像の左端の列インデックス。
- `picture.getLowerRightRow()` と `picture.setLowerRightRow(value)` — 画像の下端の行インデックス。画像の下端が行 `r` の下端と一致するようにする場合は、`r + 1` に設定します。
- `picture.getLowerRightColumn()` と `picture.setLowerRightColumn(value)` — 画像の右端の列インデックス。画像の右端が列 `c` の右端と一致するようにする場合は、`c + 1` に設定します。

{{% alert color="primary" %}}
Aspose.Cells の行インデックスと列インデックスは**0 ベース**です。セル C6 の行インデックスは 5、列インデックスは 2 です。右下側のアンカーに 1 のずれが生じると、画像が隣接するセルに重なって見える主な原因となります。
{{% /alert %}}

### **配置動作の制御**
`picture.getPlacement()` と `picture.setPlacement(value)` は `PlacementType` 列挙型を使用し、ユーザーが画像の下にある行または列のサイズを変更したときの動作を制御します。1 つのセルに収める画像では、`PlacementType.MoveAndSize` が推奨されます。この値により、画像が対象のセルとともに移動およびサイズ変更されるため、セルにぴったり合った状態が維持されます。

### **手順**
1. 新しい `Workbook` を作成するか、既存のワークブックを開きます。
2. `workbook.getWorksheets().getAt(0)` で対象の `Worksheet` にアクセスします。
3. Node.js の `fs.readFileSync` を使用するなどして、画像ファイルをディスクから `Buffer` に読み込みます。
4. `worksheet.getPictures().add(5, 2, imageBuffer)` を呼び出して、セル C6 にアンカーされた画像を追加します。このメソッドは `Pictures` コレクション内の新しい画像のインデックスを返します。そのインデックスを使用して、対応する `Picture` を取得します。
5. 画像がセル C6 だけを覆うよう、4 つのアンカー座標を設定します。`picture.setUpperLeftRow(5)`、`picture.setUpperLeftColumn(2)`、`picture.setLowerRightRow(6)`、`picture.setLowerRightColumn(3)` を使用します。
6. 列幅または行高を変更しても画像が C6 に整列した状態を保つため、`picture.setPlacement(PlacementType.MoveAndSize)` を呼び出します。
7. 必要に応じて、周囲のセルにサンプルテキストを追加し、画像がセル C6 だけに表示されることを示します。
8. ワークブックを `.xlsx` ファイルとしてディスクに保存します。
以下のコードは、この方法の実装例全体を示します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,image/png" />
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
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];
            if (!file) {
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Please select a PNG image.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const imageData = new Uint8Array(await file.arrayBuffer());
            const picIndex = worksheet.pictures.add(5, 2, imageData);
            const picture = worksheet.pictures.get(picIndex);
            picture.upperLeftRow = 5;
            picture.upperLeftColumn = 2;
            picture.lowerRightRow = 6;
            picture.lowerRightColumn = 3;
            picture.placement = AsposeCells.Drawing.PlacementType.MoveAndSize;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **方法 2: 画像をセルに直接埋め込む**
Aspose.Cells には、セルに紐づく画像のためのよりシンプルなメカニズムとして、`cell.setEmbeddedImage(imageBuffer)` メソッドも提供されています。このメソッドで画像データを割り当てると、インラインコンテンツであるかのように、画像がセル自体に添付されます。

### **埋め込み画像のしくみ**
- 画像は、描画レイヤー上のシェイプではなく、セル内容の一部として格納されます。
- 画像は、セルの表示領域内に収まるよう自動的にスケールされます。アンカー座標や配置設定は必要ありません。
- セルは引き続き実際のセルであり、実際のアドレスを持つため、数式で参照したり、行の一部としてソートしたり、他のセル単位の操作で利用したりできます。
したがって、目的が単に「このセルの中に存在する画像」である場合、`cell.setEmbeddedImage(imageBuffer)` が最も簡潔な選択肢です。

### **手順**
1. 新しい `Workbook` を作成するか、既存のワークブックを開きます。
2. `workbook.getWorksheets().getAt(0)` で対象の `Worksheet` にアクセスします。
3. Node.js の `fs.readFileSync` を使用するなどして、画像ファイルをディスクから `Buffer` に読み込みます。
4. `worksheet.getCells().get("C6")` または `worksheet.getCells().get(5, 2)` を通じて、対象セルへの参照を取得します。
5. `cell.setEmbeddedImage(imageBuffer)` を使って `Buffer` をセルに渡します。
6. 必要に応じて、対象行の高さおよび対象列の幅を調整し、埋め込み画像をより目立つ表示にします。
7. ワークブックを `.xlsx` ファイルとしてディスクに保存します。
以下のコードは、この方法の実装例全体を示します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".png,.jpg,.jpeg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const asposeReady = AsposeCells.onReady({
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
            if (!fileInput.files || fileInput.files.length === 0) {
                result.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // 対象のセル C6 を取得
            const cell = worksheet.cells.get("C6");
            // 画像ファイルをバイト配列に読み込む
            const imageData = new Uint8Array(await fileInput.files[0].arrayBuffer());
            // 画像をセルに直接埋め込む
            cell.embeddedImage = imageData;
            // 埋め込んだ画像が見えやすくなるように、行の高さと列の幅をオプションで調整する
            worksheet.cells.setColumnWidth(2, 30); // 列 C（インデックス 2）
            worksheet.cells.setRowHeight(5, 100); // 行 6（インデックス 5）
            // 結果のワークブックを .xlsx ファイルとして保存する
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **適切な方法を選択する**
どちらの方法も 1 つのセル内に収まる画像を作成しますが、画像の保存方法と動作が異なります。
- **浮動画像（方法 1）を使用する場合：**
  - 配置、重ね順、または他の描画オブジェクトとの整列を細かく制御する必要がある場合。
  - 画像を選択、並べ替え、または他のシェイプとグループ化できるシェイプとして扱いたい場合。
  - `worksheet.getPictures()` で取得できる `Pictures` コレクションを操作する既存コードとの互換性が必要な場合。
  - ワークシートのレイアウトに基づいて、アンカー座標を動的に計算する必要がある場合。
- **埋め込み画像（方法 2）を使用する場合：**
  - 画像をセルに挿入する最も簡単な方法を使用したい場合。
  - 画像が他のセル内容と同じように、セルとともに移動するようにしたい場合。

## 関連記事
- [Aspose.Cells for JavaScript via C++ の Excel カメラ](/cells/ja/javascript-cpp/excel-camera/)
- [Aspose.Cells for JavaScript via C++ でピボットテーブルにフィルター項目を追加](/cells/ja/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ でピボットテーブルにスタイルを適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)
- [Aspose.Cells for JavaScript via C++ でスパークラインを画像および HTML に変換](/cells/ja/javascript-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript-cpp" >}}