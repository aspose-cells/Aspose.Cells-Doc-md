---
title: Использование функции FormulaText в Aspose.Cells for JavaScript через C++
linktitle: Использование функции FormulaText в Aspose.Cells
description: В этой статье рассматривается, как использовать функцию FormulaText в библиотеке Aspose.Cells для обработки формул в Microsoft Excel. Узнайте, как получать и устанавливать текст формулы ячейки и сохранять изменённые файлы Excel с помощью JavaScript через C++.
keywords: Aspose.Cells, Excel, функции FormulaText JavaScript через C++
type: docs
weight: 60
url: /ru/javascript-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText — это функция Excel 2013 и новее. Она не поддерживается более ранними версиями, такими как Excel 2010 или 2007 и др. Как следует из названия, она выводит текст формулы, содержащейся в указанной ячейке. В этой статье покажем, как использовать эту функцию с помощью Aspose.Cells for JavaScript через C++.

{{% /alert %}} 

Следующий пример кода демонстрирует использование FormulaText с Aspose.Cells for JavaScript через C++. Сначала в ячейку A1 записывается формула, а затем в ячейке A2 выводится текст формулы с помощью FormulaText.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - FormulaText</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some formula in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.formula = "=Sum(B1:B10)";

            // Get the text of the formula in cell A2 using FORMULATEXT function
            const cellA2 = worksheet.cells.get("A2");
            cellA2.formula = "=FormulaText(A1)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Print the results of A2, It will now print the text of the formula inside cell A1
            console.log(cellA2.stringValue);

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully! Formula text: ${cellA2.stringValue}</p>`;
        });
    </script>
</html>
```
## **Вывод в консоль**


{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
