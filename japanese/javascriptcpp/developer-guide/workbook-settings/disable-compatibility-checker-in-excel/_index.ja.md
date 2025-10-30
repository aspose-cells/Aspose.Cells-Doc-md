---
title: C++経由のJavaScriptでExcelの互換性チェッカーを無効にする
linktitle: Excelでの互換性チェッカーを無効にする
type: docs
weight: 170
url: /ja/javascript-cpp/disable-compatibility-checker-in-excel/
description: C++ APIを通じてAspose.Cells for JavaScriptで互換性チェッカーを無効にする方法を学びます。
keywords: JavaScriptで互換性チェッカーを無効にする、C++経由でExcelの互換性チェッカーをJavaScriptで無効にする、ブックの互換性チェッカーを無効にする。
---

## JavaScriptでExcelワークシートの互換性チェッカーを無効にする  

{{% alert color="primary" %}}  
Microsoft Excelの互換性チェッカーは、以前のファイル形式でファイルを保存すると機能の問題や精度の低下が引き起こされる可能性があるとして警告を出します。互換性チェッカーはMicrosoft Office Excel 2007およびMicrosoft Excel 2010の機能です。  

以前のバージョンのワークブックをExcel 2007またはExcel 2010からExcel 97からExcel 2003に保存する場合、互換性チェッカーは、以前のバージョンではサポートされていない機能が含まれていないかどうかをワークブックをスキャンします。互換性の問題についての決定を支援するために、互換性チェッカーはオプションを含むダイアログボックスを表示します。また、ワークブックの問題に関するレポートを作成したり、機能を無効にすることもできます。  

時には、特定のスプレッドシートに対して互換性チェッカーを無効にする必要があります。Aspose.CellsのAPIを使えば、これをプログラムで行うことができ、ユーザーがMicrosoft Excelでファイルを再保存する際に互換性チェッカーのダイアログボックスが表示されて混乱したりイライラしたりしません。  
{{% /alert %}}  

## **Microsoft Excelを使用して互換性チェッカーを無効にする方法**  

Microsoft Excel（例: Microsoft Excel 2007/2010）で互換性チェッカーを無効にする場合:  

- （Excel 2007）[Office] ボタンをクリックし、「準備」、[互換性の確認] をクリックし、「このブックを保存するときに互換性を確認する」オプションをクリアします.  
- (Excel 2010) ファイルタブをクリックし**情報**、**問題の確認**、**互換性を確認**をクリックし、最後に**このブックを保存する場合に互換性をチェック**のチェックを外します。  

## **Aspose.Cells APIを使用して互換性チェッカーを無効にする方法**  

Microsoft Excelの互換性チェッカーを無効にするには、[**Workbook.checkCompatibility**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCompatibility--)プロパティを**false**に設定します。  

### **コード例**  

以下のコード例は、C++経由のAspose.Cells for JavaScriptを使用して互換性チェッカーを無効にする方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Disable Compatibility Checker Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable the compatibility checker
            workbook.settings.checkCompatibility = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_BK_CompCheck.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Compatibility check disabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
