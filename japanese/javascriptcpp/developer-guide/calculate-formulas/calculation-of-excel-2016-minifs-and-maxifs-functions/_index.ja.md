---
title: JavaScriptを介したC++によるExcel 2016のMINIFSとMAXIFS関数の計算
description: この記事は、Aspose.Cellsライブラリを使用してJavaScriptを介したC++でMicrosoft Excel 2016のMINIFSとMAXIFS関数を計算する方法を紹介します。既存のExcelファイルを読み込むか、新規作成し、これらの関数を計算して結果をディスクに保存します。
keywords: Aspose.Cells、Excel、2016、MINIFS関数、MAXIFS関数、計算、JavaScriptを介したC++
type: docs
weight: 300
url: /ja/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **可能な使用シナリオ**
Microsoft Excel 2016はMINIFSとMAXIFS関数をサポートしています。これらの関数はExcel 2013以前ではサポートされていません。C++を介したAspose.Cells for JavaScriptもこれらの関数の計算をサポートしています。以下のスクリーンショットはこれらの関数の使用例を示しています。スクリーンショット内の赤いコメントを読めば、これらの関数の動作を理解できます。

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Excel 2016のMINIFSおよびMAXIFS関数の計算**
次のサンプルコードは[sample excel file](5115149.xlsx)を読み込み、[Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)メソッドを呼び出してAspose.Cells for JavaScriptを介したC++での数式計算を実行し、その結果を [output PDF](5115154.pdf)に保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
