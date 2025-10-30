---
title: 組み込みスタイルの使用
linktitle: 組み込みスタイルの使用
type: docs
weight: 80
url: /ja/javascript-cpp/using-built-in-styles/
description: C++を使用したAspose.Cells for JavaScriptによるExcelの組み込みスタイルを使用するJavaScriptコード。
keywords: JavaScriptでExcelの組み込みスタイルを使用し、ワークブックにプログラム的にスタイルを適用し、Excelの組み込みスタイルを適用するJavaScriptコード
---

{{% alert color="primary" %}}  
Aspose.Cellsは、スプレッドシートドキュメントのセルを書式設定するための多くの再利用可能なスタイルを提供しています。ワークブックで組み込みのスタイルを使用したり、カスタムスタイルを作成したりすることができます。  
{{% /alert %}}  

## **組み込みスタイルの使用方法**  

[**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-)メソッドと[**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype)列挙型を使用すると、組み込みスタイルを簡単に使用できます。以下にすべての可能な組み込みスタイルのリストがあります:  

- TwentyPercentAccent1
- TwentyPercentAccent2
- TwentyPercentAccent3
- TwentyPercentAccent4
- TwentyPercentAccent5
- TwentyPercentAccent6
- FortyPercentAccent1
- FortyPercentAccent2
- FortyPercentAccent3
- FortyPercentAccent4
- FortyPercentAccent5
- FortyPercentAccent6
- SixtyPercentAccent1
- SixtyPercentAccent2
- SixtyPercentAccent3
- SixtyPercentAccent4
- SixtyPercentAccent5
- SixtyPercentAccent6
- Accent1
- Accent2
- Accent3
- Accent4
- Accent5
- Accent6
- 良くない
- 計算
- セルを確認
- カンマ
- カンマ1
- 通貨
- 通貨1
- 説明テキスト
- 良い
- ヘッダー1
- ヘッダー2
- ヘッダー3
- ヘッダー4
- ハイパーリンク
- 追跡用リンク
- 入力
- 連結セル
- ニュートラル
- 標準
- メモ
- 出力
- パーセント
- タイトル
- 合計
- 警告テキスト
- 行レベル
- 列レベル


## 組み込みスタイルを使用したJavaScriptコード  
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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();

            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;

            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);

            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';

            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```
