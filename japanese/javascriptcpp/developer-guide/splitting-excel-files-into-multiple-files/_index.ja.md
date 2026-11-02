---
title: Excel ファイルを複数のファイルに分割する
linktitle: Excel ファイルを複数のファイルに分割する
description: Aspose.Cells for JavaScript via C++ は、スプレッドシートファイルの操作を行う JavaScript via C++ ライブラリで、単一の Excel ファイルを複数のファイルに分割することをサポートします。この記事では、各ワークシートを個別のワークブックにコピーする方法と、特定のセル範囲を別のワークブックにコピーする方法について紹介します。
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ library, スプレッドシート, Excel ファイルの分割, ワークシートのコピー, 範囲のコピー, 複数のワークブック, 別々のファイルとして保存
type: docs
weight: 195
url: /ja/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ は、単一の Excel ファイルを複数のファイルに分割する機能を提供します。主な方法は 2 つあり、(1) ソース ワークブックの各ワークシートを新しいワークブックにコピーして個別のファイルとして保存する方法、(2) ワークシート内の特定のセル範囲を新しいワークブックにコピーする方法です。データのサブセットを配布したり、受取人ごとに小さなレポートを作成したり、個別に処理するデータを分離したりする場合に便利です。
{{% /alert %}}

## **概要**
開発者が単一の Excel ファイルを複数の小さなファイルに分割する必要があるシナリオは多数あります。たとえば、ワークブックに部門ごとのワークシートがあり、各部門長が自分のシートだけを受け取りたい場合があります。また、ワークシートから特定の表やデータブロックを抽出して、残りのワークブックを公開せずにメールで単体のファイルとして送信したいケースもあります。大規模な統合ワークブックを扱いやすくしたり、読み込み速度を向上させたり、他システムでの下流処理のために分割が必要になることもあります。  
Aspose.Cells for JavaScript via C++ は、このタスクに対して 2 つの柔軟なアプローチを提供します。最初の方法は、ソース ワークブック内のすべてのワークシートを順に処理し、各シートの内容を新規 `Workbook` インスタンスにコピーして別々のファイルとして保存します。2 番目の方法は、ワークシート内の特定のセル範囲にフォーカスし、その範囲のみを新しいワークブックにコピーします。どちらの場合も基本的なフローは同じです。`Workbook` クラスでソース ワークブックを読み込み、`Worksheet` と `Cells` オブジェクトで対象データにアクセスし、目的の `Workbook` に転送してディスクに保存します。

## **ワークシートを新しいワークブックにコピーして Excel ファイルを分割する方法**

### **アプローチ概要**
この方法では、ソース ワークブックを 1 回開き、`Worksheets` コレクション内の各 `Worksheet` に対して新しい宛先 `Workbook` を作成します。ソース ワークシートの内容は宛先ワークブックの最初のワークシートにコピーされ、宛先ワークブックはソース ワークシート名に基づいたファイル名で保存されます。結果として、ワークシートごとに 1 つの出力ファイルが生成され、各ファイルには単一の元シートのデータが含まれます。  
この手法は、ソース ワークブックの各ワークシートが部門、地域、月、製品ラインなど論理的に独立した情報単位を表し、各単位を個別に配布または処理したい場合に適しています。

### **手順**
Excel ファイルを各ワークシートごとに新しいワークブックにコピーして分割する手順は以下の通りです。
1. `Workbook` オブジェクトをインスタンス化し、ファイル パスをコンストラクタに渡してソース Excel ファイルを開きます。
2. `for` または `for...of` ループを使用して `Workbook.Worksheets` コレクションを反復し、ソース ファイル内のすべての `Worksheet` を処理します。
3. ループ内で、現在のワークシート用に空の `Workbook` インスタンス（宛先ワークブック）を作成します。
5. ソース ワークシートの内容を宛先ワークシートにコピーします。これは、ソース ワークシートの `Cells` コレクションを走査して対応するセルに値を書き込むか、`Cells.Copy` メソッドを使用して範囲全体を一括転送することで実行できます。
6. ソース ワークシート名を組み込んだ出力ファイル パスを構築します（例: `dataDir + worksheet.Name + ".xls"`）。これにより、生成される各ファイルに固有の名前が付与されます。
7. 宛先 `Workbook.Save` メソッドを呼び出してディスクにファイルを書き込みます。
8. 次のワークシートに対して手順 3～7 を繰り返し、すべてのワークシートが処理されるまで続けます。

### **コード例**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

期待される出力は、データ ディレクトリ内に作成された新しいファイルの集合で、ソース ワークブックの各ワークシートにつき 1 つのファイルが生成されます。各ファイルは対応する元シートの名前が付けられ、単一シートのデータ（必要に応じて書式設定も含む）が格納されています。

## **セル範囲を新しいワークブックにコピーして Excel ファイルを分割する方法**

### **アプローチ概要**
分割対象のデータがワークシート全体ではなく、`A1:D10` のような特定の矩形領域や、特定のテーブルを表す名前付き範囲である場合があります。このようなケースでは、ワークシート全体をコピーするのは無駄であり、より正確な手法が求められます。ソース範囲を特定し、その範囲だけを新しいワークブックにコピーしてファイルとして保存します。  
この手法は、大きなワークシートから単一のテーブル、レポートブロック、またはデータ領域を抽出し、無関係なコンテンツを除外したい場合に最適です。また、ユーザーが選択したシート領域をスタンドアロン ファイルとしてエクスポートする際にも有用です。

### **手順**
Excel ファイルを特定の範囲を新しいワークブックにコピーして分割する手順は以下の通りです。
1. ファイル パスを指定して `Workbook` オブジェクトをインスタンス化し、ソース Excel ファイルを開きます。
2. コピー対象の範囲を含む `Worksheet` をインデックス（例: 最初のシート）または名前で `Worksheets` コレクションから取得します。
3. コピーする範囲を特定します。ハードコードされたセル範囲（例: `A1:C10`）や、`Worksheet.Cells` コレクションから取得した名前付き範囲、または `Worksheet.Cells.CreateRange` で作成した範囲が対象となります。
4. 新しい宛先 `Workbook` インスタンスを作成します。
5. 宛先ワークブックの最初の `Worksheet`（デフォルト シート）にアクセスします。
6. ソース範囲を宛先ワークシートにコピーします。通常はセル `A1` から開始します。宛先 `Cells` コレクションの `Cells.Copy` メソッドを使用して範囲全体をコピーするか、ソース範囲のセルを走査して `PutValue` で値を書き込むことができます。`CopyOptions` を指定すれば、値のみ、値と書式、数式など転送内容を制御できます。
7. `Workbook.Save` メソッドを使用して、宛先ワークブックをディスク上の新しいファイル パスに保存します。

### **コード例**
期待される出力は、データ ディレクトリ内に作成された単一の新規ファイルで、ソース ワークブックから抽出した指定範囲の値（必要に応じて書式設定も含む）だけが含まれます。宛先ファイルはソース ファイルの他のデータとは無関係で、抽出した範囲が最初のワークシートのセル `A1` から始まります。

## Related Articles
- [Aspose.Cells for JavaScript via C++ のピボットテーブルにフィルタ フィールドを追加](/cells/ja/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ のピボットテーブルにスタイルを適用](/cells/ja/javascript-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルのページ フィールド レイアウトを変更](/cells/ja/javascript-cpp/change-page-field-layout/)
- [Aspose.Cells for JavaScript via C++ でスパークラインを画像と HTML に変換](/cells/ja/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Excel を OFD 形式に変換](/cells/ja/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}