---
title: Отображение дополнительных символов Юникода в итоговом PDF с помощью Script Aspose.Cells for Java через C++
linktitle: Отображайте дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells
type: docs
weight: 350
url: /ru/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Узнайте, как отображать дополнительные символы Юникода в итоговом PDF с использованием Script Aspose.Cells for Java через C++. 
---

{{% alert color="primary" %}}

Обычные символы Юникода имеют длину 2 байта, а дополнительные символы Юникода - 4 байта. Aspose.Cells теперь поддерживает отображение этих дополнительных символов Юникода длиной 4 байта.

В стандарте символов Юникода дополнительные символы - это символы, которым назначены кодовые точки от U+10000 до U+10FFFF. Другими словами, это символы Юникода, большие чем U+FFFF.

- В UTF-8 каждый из этих символов имеет длину 4 байта.
- В UTF-16 для этих символов требуются 2 заместителя (16-битные единицы).

{{% /alert %}}

## Визуализация дополнительных символов Юникода в итоговом PDF с помощью Script Aspose.Cells for Java через C++

Следующий скриншот показывает, как Aspose.Cells преобразовал [исходный excel-файл](5115563.xlsx) в [выходной PDF](5115564.pdf). Как видите, все три дополненных юникодных символа были отображены точно так же, как в Microsoft Excel.

![todo:image_alt_text](output.png)

## Образец кода

Вы можете использовать этот образец кода для преобразования [исходного файла Excel](5115563.xlsx) в [выходной PDF](5115564.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Unicode Supplementary Characters to PDF</title>
    </head>
    <body>
        <h1>Render Unicode Supplementary Characters to PDF</h1>
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

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenderUnicodeInOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
