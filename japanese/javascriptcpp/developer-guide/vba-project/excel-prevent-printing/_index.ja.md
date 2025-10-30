---
title: JavaScriptを通じてC++でExcelファイルの印刷を阻止する方法
linktitle: Excelファイルの印刷を防止する方法
type: docs
weight: 600
url: /ja/javascript-cpp/how-to-prevent-printing-excel/
description: Aspose.Cells for JavaScriptを使用して、Excelファイルの印刷をユーザーができないように防ぐ方法を学びます。
keywords: excel印刷、excel印刷を防ぐ、Excelファイルの印刷を防ぐ方法、excel印刷を防ぐ、ブック全体の印刷を防ぐ、VBAでブック全体の印刷を防ぐ。
---

## **可能な使用シナリオ**  
日常の仕事の中で、重要な情報を含むExcelファイルがあります。内部データの拡散を防ぐために、会社は印刷を許可しません。このドキュメントは、他者がExcelファイルを印刷できないようにする方法を説明します。  

## **MS-Excelでファイルの印刷を防ぐ方法**  
次のVBAコードを適用して、特定のファイルの印刷を防ぐことができます。  
1. 印刷を許可しないブックを開きます。  
1. Excelリボンの「開発」タブを選択し、「コントロール」セクションの「コードの表示」ボタンをクリックします。あるいは、ALT + F11キーを押してMicrosoft Visual Basic for Applicationsウィンドウを開きます。  
<br>  
<img src="1.png" width=70% />  
1. 次に、左側のProject ExplorerでThisWorkbookをダブルクリックしてモジュールを開き、VBAコードを追加します。  
<br>  
<img src="2.png" width=70% />  
1. その後、コードを保存して閉じ、ブックに戻ります。次にサンプルファイルを印刷しようとすると、印刷が許可されず、次の警告ボックスが表示されます。  
<br>  
<img src="3.png" width=70% />  

## **Aspose.Cells for JavaScriptを使用してExcelファイルの印刷を防止する方法**  

次のサンプルコードは、Excelファイルの印刷を防ぐ方法を示しています。  

1. [サンプルファイル](sample.xlsx)をロードする。  
1. WorkbookのVbaProjectプロパティからVbaModuleCollectionオブジェクトを取得します。  
1. "ThisWorkbook"名を通じてVbaModuleオブジェクトを取得します。  
1. VbaModuleのcodesプロパティを設定します。  
1. サンプルファイルを[xlsm形式](out.xlsm)で保存します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
