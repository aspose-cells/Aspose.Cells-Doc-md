---
title: C++を介したAspose.Cells for JavaScriptを使用したIFNA関数の計算
description: JavaScriptを介したC++でAspose.Cellsライブラリを使用してIFNA関数を計算する方法。既存のExcelファイルを読み込むか、新規作成し、IFNA関数を計算して結果を取得します。最後に変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、IFNA関数、計算、JavaScriptを介したC++
type: docs
weight: 40
url: /ja/javascript-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.CellsはExcelのIFNA関数の計算をサポートしています。IFNA関数は、式が#N/Aエラーを返した場合に指定した値を返し、それ以外の場合は式の結果を返します。

{{% /alert %}} 
## **Aspose.Cells for JavaScriptを使ったC++によるIFNA関数の計算**
以下のサンプルコードは、C++を介したAspose.Cells for JavaScriptを使用したIFNA関数の計算例を示しています。 


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VLOOKUP IFNA Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which may contain hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add data for VLOOKUP
            worksheet.cells.get("A1").value = "Apple";
            worksheet.cells.get("A2").value = "Orange";
            worksheet.cells.get("A3").value = "Banana";

            // Access cell A5 and A6
            const cellA5 = worksheet.cells.get("A5");
            const cellA6 = worksheet.cells.get("A6");

            // Assign IFNA formula to A5 and A6
            cellA5.formula = '=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")';
            cellA6.formula = '=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")';

            // Calculate the formula of workbook
            workbook.calculateFormula();

            // Get the string values of A5 and A6
            const valueA5 = cellA5.stringValue;
            const valueA6 = cellA6.stringValue;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = `<p style="color: green;">A5: ${valueA5}</p><p style="color: green;">A6: ${valueA6}</p>`;
        });
    </script>
</html>
```
## **コンソール出力**


{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
