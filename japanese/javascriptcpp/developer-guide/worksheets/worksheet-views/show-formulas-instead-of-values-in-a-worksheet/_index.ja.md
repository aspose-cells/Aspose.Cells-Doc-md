---
title: JavaScriptを介してC++でワークシートの値の代わりに数式を表示します
linktitle: ワークシートで値の代わりに数式を表示する
type: docs
weight: 20
url: /ja/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: この記事は、C++を介したJavaScript APIを使用して、Excelワークシートやスプレッドシートで数式を値の代わりにプログラム的に表示する方法のサンプルコードを提供します。
---

{{% alert color="primary" %}}

Microsoft Excelで計算値の代わりに数式を表示するには、**数式** リボンのオプションを使用します。数式を表示しているとき、Microsoft Excelはワークシートに数式を表示します。これと同じことは、Aspose.Cells for JavaScriptをC++で使用して実現可能です。

{{% /alert %}}

Aspose.Cellsは[**Worksheet.showFormulas**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#showFormulas--)プロパティを提供しています。これを**true**に設定すると、Microsoft Excelに数式を表示させることができます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Show Formulas Example</title>
    </head>
    <body>
        <h1>Show Formulas Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Show formulas of the worksheet
            worksheet.showFormulas = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'source.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas are now visible. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
