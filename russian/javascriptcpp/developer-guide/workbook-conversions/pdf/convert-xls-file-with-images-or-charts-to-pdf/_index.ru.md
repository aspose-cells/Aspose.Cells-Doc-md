---
title: Преобразование XLS файла с изображениями или графиками в PDF с помощью JavaScript через C++
linktitle: Преобразование XLS файла с изображениями или диаграммами в PDF
type: docs
weight: 50
url: /ru/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование XLS файлов, содержащих изображения и графики, в PDF документы. Script Aspose.Cells for Java через C++ может работать независимо для преобразования таблицы в PDF: для этого не требуется Aspose.PDF для JavaScript через C++. Процесс можно выполнить в памяти, так как он не зависит от временных или промежуточных XML файлов. Это означает, что большие файлы Excel, например содержащие изображения, графики и другие объекты рисования, можно преобразовать быстро и эффективно.

{{% /alert %}} 
## **Образец кода**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}} 

Если в таблице есть формулы, рекомендуется вызвать метод [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) сразу перед преобразованием в PDF. Это гарантирует пересчет значений, зависящих от формул, и правильное отображение их в PDF.

{{% /alert %}}
