---
title: JavaScriptを使用したワークシートからシナリオを作成、操作、削除（C++）
linktitle: シナリオの管理
type: docs
weight: 190
url: /ja/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: JavaScriptをC++ APIで使用してExcelワークシートのシナリオをプログラム的に作成、操作、削除する方法を学びます。
keywords: シナリオワークシートの作成（JavaScript/C++）、シナリオの削除（JavaScript/C++）、ワークシートシナリオの操作（JavaScript/C++）
---

{{% alert color="primary" %}}

時折、スプレッドシートでシナリオを作成、操作、または削除する必要があります。シナリオとは、1つ以上の数式によってリンクされた可変の入力セルを含む名前付きの'仮定'モデルです。シナリオを作成する前に、異なる値が挿入できるセルに依存する1つ以上の数式を含むワークシートの設計を行います。以下の例は、Aspose.CellsのAPIを使用してワークシートからシナリオを作成および削除する方法を示しています。

{{% /alert %}}

Aspose.Cellsは、便利なクラス[**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection)、[**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection)、および[**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell)クラスを提供します。また、[**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--)プロパティもあります。以下のサンプルコードは、シナリオを含むExcelファイル（XLSX）を開き、既存のシナリオを削除し、新しいシナリオをワークシートに追加してからExcelファイルを保存します。例は非常に単純なテンプレートファイルを使用しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Scenarios Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Scenarios Example</h1>
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

            // Instantiate the Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            if (worksheet.scenarios.count > 0) {
                // Remove the existing first scenario from the sheet
                worksheet.scenarios.removeAt(0);
            }

            // Create a scenario
            const i = worksheet.scenarios.add("MyScenario");
            // Get the scenario
            const scenario = worksheet.scenarios.get(i);
            // Add comment to it
            scenario.comment = "Test scenario is created.";
            // Get the input cells for the scenario
            const sic = scenario.inputCells;
            // Add the scenario on B4 (as changing cell) with default value
            sic.add(3, 1, "1100000");

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outBk_scenarios1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Process completed successfully. File ready for download.</p>';
        });
    </script>
</html>
```
