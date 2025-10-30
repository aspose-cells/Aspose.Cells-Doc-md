---
title: JavaScriptを使用してC++で印刷範囲を設定する方法
linktitle: 印刷範囲の設定方法
type: docs
weight: 200
url: /ja/javascript-cpp/how-to-set-print-area/
description: このコードは、C++用のJavaScriptライブラリAspose.Cellsを使用して印刷範囲を設定する方法を示しています。
keywords: 印刷範囲の制限、設定、クリア、設定とクリアの方法（JavaScript via C++）、印刷範囲の設定とクリア（JavaScript経由C++）、JavaScriptを使用した印刷範囲のクリア方法、JavaScript経由C++を使用した印刷範囲の追加方法、JavaScriptを使用した印刷範囲の削除方法、Excelでの印刷範囲設定とクリア方法
---

## **可能な使用シナリオ**

Excelなどの文書で印刷範囲を設定することで、印刷時に含める内容を制御できます。設定の理由は次の通りです：

1. 特定のデータに集中：必要な部分だけを印刷し、不必要なコンテンツを避けることができます。
1. レイアウトの改善：内容を整然と配置し、ページ分割や不必要な改ページを防ぎます。
1. リソースの節約：印刷範囲を制限することで、紙とインクの使用量を削減できます。
1. プロフェッショナルなプレゼンテーション：最終的なデータのみを印刷することにより、レポートやプレゼンテーションの品質を向上させます。
1. 一貫性：複数回同じ文書を印刷する場合、一貫した出力が保証されます。

<br>
より多くのドキュメントの一部だけを共有または印刷する必要がある場合に特に役立ちます。

## **Excelで印刷範囲を設定する方法**

Excelで印刷範囲を設定するには、次の手順に従います：

1. セルの選択：印刷範囲に設定したいセル範囲をクリックしてドラッグします。
1. ページレイアウトタブを開く：Excelウィンドウ上部のリボンの「ページレイアウト」タブに移動します。
1. 印刷範囲の設定：「ページ設定」グループ内の「印刷範囲」をクリックします。ドロップダウンメニューから「印刷範囲の設定」を選択します。
<br>
<img src="3.png" width=60% />

1. 印刷範囲への追加：既存の印刷範囲にセルを追加したい場合は、追加のセルを選択し、「ページレイアウト」タブの「印刷範囲」から「印刷範囲に追加」を選択します。

<br>
この操作により、選択したセルが印刷範囲として定義されます。ワークシートを印刷すると、この定義された範囲のみが印刷されます。

## **Excelで印刷範囲をクリアする方法**

Excelで印刷範囲をクリアするには、次の手順に従います：

1. ページレイアウトタブを開く：Excelウィンドウのリボンの「ページレイアウト」タブをクリックします。
1. 印刷範囲のクリア：「ページ設定」グループ内の「印刷範囲」をクリックし、ドロップダウンから「印刷範囲のクリア」を選択します。
<br>
<img src="4.png" width=60% />

<br>
この操作により、以前設定された印刷範囲が解除され、ワークシート全体の印刷が可能になります。

## **印刷範囲をクリアした後に何が起こるか**

ExcelのようなスプレッドシートアプリケーションでAspose.Cellsを使用して印刷範囲をクリアすると、ドキュメントを印刷したときにワークシート全体が含まれます。印刷範囲が設定されている場合は、その範囲のみが印刷されます。印刷範囲をクリアすると、特定の範囲が設定されていない状態になり、デフォルトの動作（シート全体の印刷）が適用されることになります。

1. デフォルトの印刷動作：ワークシート全体が印刷対象となります。データや書式設定があるすべてのセルが印刷されます。
1. 印刷範囲の制限なし：以前に定義された印刷範囲の制限は解除されます。特定の行や列に印刷指定があった場合でも、その制約はなくなります。
1. 全内容印刷：ヘッダー、フッター、その他のデータを含めて、すべての内容が印刷されます。

## **Aspose.Cells for JavaScriptをC++で使用して印刷範囲を設定する方法**

指定したワークシートの印刷範囲を設定するには、最初に[サンプルファイル](input.xlsx)を読み込み、その後に目的のワークシートの [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) オブジェクトの [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) プロパティを変更します。このプロパティに範囲文字列を設定すると印刷範囲が設定されます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Area</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xlsx,.xls" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet (first worksheet)
            const worksheet = workbook.worksheets.get(0);

            // Set the print area - specify the range you want to print
            worksheet.pageSetup.printArea = "A1:D10";

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

出力結果：
<br>
<img src="1.png" width=60% />

## **C++でAspose.Cells for JavaScriptを使用した印刷範囲のクリア方法**

指定されたワークシートの印刷範囲をクリアするには：最初に[サンプルファイル](input.xlsx)を読み込み、その後目的のワークシートに対して[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)オブジェクトの[**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--)プロパティを変更する必要があります。このプロパティを空の文字列に設定すると、印刷範囲がクリアされます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Clear Print Area</title>
    </head>
    <body>
        <h1>Clear Print Area Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the print area
            worksheet.pageSetup.printArea = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_area.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultEl.innerHTML = '<p style="color: green;">Print area cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```

出力結果：
<br>
<img src="2.png" width=60% />
