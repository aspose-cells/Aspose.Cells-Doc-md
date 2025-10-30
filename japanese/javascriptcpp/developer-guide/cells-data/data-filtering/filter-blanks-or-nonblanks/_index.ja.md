---
title: 空白または非空白をフィルタリングする方法
type: docs
weight: 85
url: /ja/javascript-cpp/how-to-filter-blanks-and-non-blanks/
description: C++ APIを使用してAspose.Cells for JavaScriptで空白と非空白をフィルタリングする方法を学びます。
keywords: 空白をフィルタリングし、非空白をフィルタリングし、ワークシート内の空白をフィルタリングし、ワークシート内の非空白をフィルタリングし、Excel内の空白をフィルタリングし、Excel内の非空白をフィルタリングし、Excel内の空白および非空白をフィルタリングする
---

## **可能な使用シナリオ**
Excelでのデータのフィルタリングは、ユーザーが基準に基づいて特定のデータサブセットに焦点を当てることを可能にし、全体的なデータの操作および解釈プロセスをより効率的かつ効果的にします。

## **Excelで空白または非空白をフィルタリングする方法**
Excelでは、フィルタリングオプションを使用して簡単に空白または非空白をフィルタリングすることができます。以下にその方法を示します。

### **Excelで空白をフィルタリングする方法**
1. 範囲を選択する: 列ヘッダーの文字をクリックして列全体を選択するか、空白をフィルタリングしたい範囲を選択します。
1. フィルタメニューを開く: リボンの"データ"タブに移動します。
<br>
<image src="1.png" width="70%" />
1. フィルタオプション: "フィルタ"ボタンをクリックします。これにより、選択した範囲にフィルタ矢印が追加されます。
1. 空白をフィルタリング: 空白をフィルタリングしたい列のフィルタ矢印をクリックします。"空白"以外のすべてのオプションを選択解除し、OKをクリックします。これにより、その列の空白のセルのみが表示されます。
<br>
<image src="2.png" width="70%" />
1. 結果は次のとおりです:
<br>
<image src="3.png" width="70%" />

### **Excelで非空白をフィルタリングする方法**
1. 範囲を選択する: 列ヘッダーの文字をクリックして列全体を選択するか、非空白をフィルタリングしたい範囲を選択します。
1. フィルタメニューを開く: リボンの"データ"タブに移動します。
<br>
<image src="1.png" width="70%" />
1. フィルタオプション: "フィルタ"ボタンをクリックします。これにより、選択した範囲にフィルタ矢印が追加されます。
1. ブランク以外をフィルタする: フィルタ矢印をクリックし、非ブランクをフィルタしたい列を選択します。"非ブランク"または"カスタム"以外のすべてのオプションを選択解除または条件を設定し、「OK」をクリックします。これにより、その列のブランクでないセルのみが表示されます。
<br>
<image src="4.png" width="70%" />
1. 結果は次のとおりです:
<br>
<image src="5.png" width="70%" />

## **Aspose.Cells for JavaScriptを使用したC++による空白のフィルタリング方法**
列にテキストが含まれ、一部のセルが空白の場合に、その空白セルを含む行だけを選択するには、[**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#matchBlanks-number-)と[**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#addFilter-number-string-)関数を使用します。 

[サンプルExcelファイル](sample.xlsx)を読み込み、ダミーデータを含むコード例をご覧ください。サンプルコードでは、ブランクをフィルタリングするための3つの方法を使用し、その後ブックを[output Excel file](FilteredBlanks.xlsx)として保存します。 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Filter for Blank Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.autoFilter.addFilter(1, null);
            worksheet.autoFilter.refresh();

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download FilteredBlanks.xlsx';

            resultDiv.innerHTML = '<p style="color: green;">Filter applied and file ready for download.</p>';
        });
    </script>
</html>
```


## **C++を使用したAspose.Cells for JavaScriptで非空白のフィルタリング方法**

ダミーデータを含むサンプルExcelファイル(sample.xlsx)をロードし、その後、[AutoFilter.matchNonBlanks(number)]関数を呼び出して空白でないデータをフィルタリングし、最後に[出力Excelファイル](FilteredNonBlanks.xlsx)として保存するサンプルコードをご覧ください。 

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Filter NonBlanks Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Call MatchNonBlanks function to apply the filter
            worksheet.autoFilter.matchNonBlanks(1);

            // Call refresh function to update the worksheet
            worksheet.autoFilter.refresh();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FilteredNonBlanks.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
