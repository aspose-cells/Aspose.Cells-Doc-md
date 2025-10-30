---
title: JavaScriptを使用したC++での印刷タイトルの設定方法
linktitle: 印刷タイトルの設定方法
type: docs
weight: 200
url: /ja/javascript-cpp/how-to-set-print-titles/
description: この記事では、C++を使ったJavaScript用Aspose.Cellsライブラリを使用して印刷タイトルを設定する方法を紹介します。
keywords: 行と列を繰り返して印刷、JavaScriptで印刷タイトルを設定、JavaScriptを使った印刷タイトルの設定とクリア、JavaScriptで印刷タイトルを非表示にする方法、JavaScriptを使った印刷タイトルの追加と削除、Excelでの印刷タイトルの設定とクリア。  
---

## **可能な使用シナリオ**  

Excelで印刷タイトルを設定すると、特定の行または列がすべてのページで繰り返され、大きなスプレッドシートを複数ページにわたって印刷する場合に特に便利です。設定する理由は次の通りです：  

1. 読みやすさの向上：印刷タイトルは、見出しをすべてのページで表示し続けることで、データの理解を助けます。各ページで情報を解釈しやすくなります。  

1. 専門的な外観：各ページにヘッダーやラベルを一定して表示することで、印刷されたドキュメントに洗練されたプロフェッショナルな印象を与えます。  

1. ナビゲーションの改善：膨大なデータを含むドキュメントでは、各ページでヘッダーを繰り返すことで、迅速にナビゲートおよび参照でき、ページの行き来を減らすことができます。  

1. エラー低減：すべてのページにヘッダーがあると、誤解やデータ入力エラーの可能性が低減され、ユーザーがデータのコンテキストを簡単に理解できるためです。  

1. 一貫性：重要な情報（列見出しや行ラベルなど）が常に表示されることにより、ドキュメント全体の一貫性と明確さが保たれます。  

## **Excelで印刷タイトルを設定する方法**  

Excelで印刷タイトルを設定するには、次の手順に従います：  

1. ページレイアウトタブを開く：Excelウィンドウのリボンの「ページレイアウト」タブをクリックします。  
1. 印刷タイトルにアクセス： "ページ設定" グループ内の "印刷タイトル" をクリックします。  
1. 行の繰り返し設定： "ページ設定" ダイアログボックスの "シート" タブに移動します。 "印刷タイトル" セクションで、 "上部で繰り返す行" の横のボックスをクリックし、繰り返す行を選択します。  
1. 列の繰り返し設定（必要に応じて）：同様に、 "左側で繰り返す列" の横のボックスをクリックし、繰り返す列を選択します。  
<br>  
<img src="3.png" width=60% />  

1. 確認して印刷："OK" をクリックして設定を適用します。ワークシートを印刷すると、指定した行や列がすべてのページに表示されます。  

## **Excelで印刷タイトルをクリアする方法**  

Excelで印刷タイトルをクリアするには、繰り返す設定された行または列を削除する必要があります。次の手順です：  

1. ページレイアウトタブを開く：Excelウィンドウのリボンの「ページレイアウト」タブをクリックします。  
1. 印刷タイトルにアクセス： "ページ設定" グループ内の "印刷タイトル" をクリックします。  
1. 印刷タイトルをクリア：「ページ設定」ダイアログボックスの「シート」タブに移動します。「先頭行を繰り返す」および「左端列を繰り返す」のテキストボックス内の内容を削除してクリアします。  
<br>  
<img src="4.png" width=60% />  

1. 確認して閉じる：「OK」をクリックして変更を適用します。  

## **Aspose.Cells for JavaScriptをC++で使用した印刷タイトルの設定方法**  

指定したシートにプリントタイトルを設定するには、まず[サンプルファイル](input.xlsx)を読み込み、次に望むシートの[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)オブジェクトの[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)と[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)のプロパティを変更します。これらのプロパティに範囲文字列を設定するとプリントタイトルが設定されます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Titles</title>
    </head>
    <body>
        <h1>Set Print Titles Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set rows to repeat at the top (e.g., rows 1 and 2)
            worksheet.pageSetup.printTitleRows = "$1:$2";

            // Set columns to repeat at the left (e.g., columns A and B)
            worksheet.pageSetup.printTitleColumns = "$A:$B";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'set_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles set successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

出力結果：  
<br>  
<img src="1.png" width=60% />  

## **Aspose.Cells for JavaScriptをC++で使用した印刷タイトルのクリア方法**  

指定したシートのプリントタイトルをクリアするには、まず[サンプルファイル](input.xlsx)を読み込み、次に望むシートの[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/)オブジェクトの[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)と[**Worksheet.pageSetup**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#pageSetup--)のプロパティを変更します。これらのプロパティを空文字に設定するとプリントタイトルがクリアされます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Clear Print Titles Example</title>
    </head>
    <body>
        <h1>Clear Print Titles Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the desired worksheet
            const worksheet = workbook.worksheets.get(0);

            // Clear the rows and columns set to repeat
            worksheet.pageSetup.printTitleRows = "";
            worksheet.pageSetup.printTitleColumns = "";

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'clear_print_titles.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print titles cleared successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```  

出力結果：  
<br>  
<img src="2.png" width=60% />
