---
title: Создание линии подписи в рабочей книге Excel с помощью Aspose.Cells for JavaScript через C++
linktitle: Создать строку подписи в книге Excel с помощью Aspose.Cells
type: docs
weight: 150
url: /ru/javascript-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: Эта статья описывает, как создать линию подписи в рабочей книге Excel с помощью JavaScript и Aspose.Cells for JavaScript через C++.
keywords: Создание линии подписи в рабочей книге Excel с помощью JavaScript и C++, как создать линию подписи в рабочей книге Excel, как добавить линию подписи, как добавить линию подписи в файл Excel.
---

## **Введение**  

Microsoft Excel предоставляет возможность добавлять **Строку подписи** в рабочие книги Excel. Вы можете добавить строку подписи, нажав на вкладку **Вставка** и затем выбрав **Строка подписи** из группы **Текст**.  

## **Как создать строку подписи для Excel**  

 Aspose.Cells for JavaScript через C++ также предоставляет эту функцию и имеет свойство [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) для этой цели. В этой статье объясняется, как использовать это свойство для добавления линии подписи с помощью Aspose.Cells.  

Следующий пример кода добавляет линию подписи с использованием свойства [**Picture.signatureLine**](https://reference.aspose.com/cells/javascript-cpp/picture/#signatureLine--) и сохраняет рабочую книгу.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Signature Line Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SignatureLine, Utils } = AsposeCells;

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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create signature line object
            const signatureLine = new SignatureLine();
            signatureLine.signer = "John Doe";
            signatureLine.title = "Development Lead";
            signatureLine.email = "john.doe@aspose.com";

            // Adds a Signature Line to the first worksheet.
            workbook.worksheets.get(0).shapes.addSignatureLine(1, 1, signatureLine);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Signature line added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
