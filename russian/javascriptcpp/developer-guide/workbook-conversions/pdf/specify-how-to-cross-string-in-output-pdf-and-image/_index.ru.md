---
title: Задайте параметры перехода строки в выходном PDF и изображении с помощью JavaScript на C++
linktitle: Указание того, как пересекать строку в выходном PDF и изображении
type: docs
weight: 120
url: /ru/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Научитесь управлять переполнением текста в выходном PDF/Изображении, задавая тип перехода строки с помощью Script Aspose.Cells for Java на C++.
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, строка переполняется, если следующая ячейка в следующем столбце равна null или пустая. При сохранении файла Excel в PDF/изображение вы можете контролировать это переполнение, задавая тип перекрестка с помощью перечисления [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). Оно имеет следующие значения:

- **TextCrossType.Default**: отображение текста как в MS Excel, зависящее от следующей ячейки. Если следующая ячейка равна null, строка переполняется или обрезается.

- **TextCrossType.CrossKeep**: отображать строку как в MS Excel при экспорте в PDF/изображение.

- **TextCrossType.CrossOverride**: отображать весь текст, пересекающий другие ячейки, и переопределять содержимое пересекаемых ячеек.

- **TextCrossType.StrictInCell**: Отображать только строку в пределах ширины ячейки.

## **Указание того, как пересекать строку в выходном PDF/изображении с использованием TextCrossType**

Следующий пример загружает пример файла Excel и сохраняет его в формате PDF/изображение, задавая разные [**TextCrossType**](https://reference.aspose.com/cells/javascript-cpp/textcrosstype). Образец файла Excel и выходные файлы можно скачать по ссылкам ниже:

[sampleCrossType.xlsx](81920905.xlsx)  

[outputCrossType.pdf](81920903.pdf)  

[outputCrossType.png](81920904.png)  

### Образец кода

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Cross Text Type to PDF and Image</title>
    </head>
    <body>
        <h1>Convert Excel to PDF and PNG (Text Cross Type)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkPdf" style="display: none; margin-right: 10px;">Download PDF</a>
            <a id="downloadLinkPng" style="display: none;">Download PNG</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, ImageOrPrintOptions, SheetRender, TextCrossType, Utils } = AsposeCells;

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
            const downloadLinkPdf = document.getElementById('downloadLinkPdf');
            const downloadLinkPng = document.getElementById('downloadLinkPng');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Clear previous links/messages
            downloadLinkPdf.style.display = 'none';
            downloadLinkPng.style.display = 'none';
            resultDiv.innerHTML = '';

            // Read file from input
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Initialize PDF save options
            const pdfSaveOptions = new PdfSaveOptions();
            // Set text cross type (converted setter -> property)
            pdfSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Save PDF file data
            const pdfData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            downloadLinkPdf.href = URL.createObjectURL(pdfBlob);
            downloadLinkPdf.download = 'outputCrosssType.pdf';
            downloadLinkPdf.style.display = 'inline-block';
            downloadLinkPdf.textContent = 'Download PDF File';

            // Initialize image or print options
            const imageSaveOptions = new ImageOrPrintOptions();
            // Set text cross type (converted setter -> property)
            imageSaveOptions.textCrossType = TextCrossType.StrictInCell;

            // Initialize sheet renderer for first worksheet
            const sheetRenderer = new SheetRender(workbook.worksheets.get(0), imageSaveOptions);

            // Render the first page/image of the sheet to image data
            const imageData = sheetRenderer.toImage(0);
            const imageBlob = new Blob([imageData], { type: 'image/png' });
            downloadLinkPng.href = URL.createObjectURL(imageBlob);
            downloadLinkPng.download = 'outputCrosssType.png';
            downloadLinkPng.style.display = 'inline-block';
            downloadLinkPng.textContent = 'Download PNG File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Download links are ready.</p>';
        });
    </script>
</html>
```
