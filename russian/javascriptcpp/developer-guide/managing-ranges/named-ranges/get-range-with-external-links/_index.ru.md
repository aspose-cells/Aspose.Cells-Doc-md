---
title: Получение диапазона с внешними ссылками с помощью JavaScript через C++
linktitle: Получить диапазон с внешними ссылками
type: docs
weight: 120
url: /ru/javascript-cpp/get-range-with-external-links/
description: Узнайте, как получать диапазоны с внешними ссылками, используя Script через C++. Эффективно извлекайте данные из различных файлов Excel.
---

## **Получить диапазон с внешними ссылками**

Многие файлы Excel обращаются к данным из других файлов Excel через внешние ссылки. Script через C++ предоставляет возможность получать эти внешние ссылки с помощью метода [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-). Метод [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) возвращает массив типа [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea). Класс [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) содержит свойство [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--), которое возвращает имя внешнего файла. Класс [**ReferredArea**](https://reference.aspose.com/cells/javascript-cpp/referredarea) раскрывает следующие члены.

- [**ReferredArea.endColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endColumn--): Конечный столб области
- [**ReferredArea.endRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#endRow--): Конечная строка области
- [**ReferredArea.externalFileName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#externalFileName--): Получить имя внешнего файла, если это внешний ссылка
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isArea--): Указывает, является ли это областью
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#isExternalLink--): Указывает, является ли это внешней ссылкой
- [**ReferredArea.sheetName**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#sheetName--): Указывает, в каком листе находится эта ссылка
- [**ReferredArea.startColumn**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startColumn--): Начальный столб области
- [**ReferredArea.startRow**](https://reference.aspose.com/cells/javascript-cpp/referredarea/#startRow--): Начальная строка области

Пример кода, приведенный ниже, демонстрирует использование метода [**Name.referredAreas(boolean)**](https://reference.aspose.com/cells/javascript-cpp/name/#referredAreas-boolean-) для получения диапазонов с внешними ссылками.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - External References</title>
    </head>
    <body>
        <h1>Sample External References</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (SampleExternalReferences.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing named ranges via worksheets.names
            const names = workbook.worksheets.names;
            const namesCount = names.count;
            const outputLines = [];
            outputLines.push(`<p>Processing file: ${file.name}</p>`);
            outputLines.push(`<p>Named Ranges Count: ${namesCount}</p>`);

            for (let i = 0; i < namesCount; i++) {
                const namedRange = names.get(i);
                outputLines.push(`<h3>Named Range ${i}: ${namedRange.name || ('Index ' + i)}</h3>`);

                // Get referred areas (including external references)
                const referredAreas = namedRange.referredAreas(true);
                if (referredAreas) {
                    referredAreas.forEach((referredArea, idx) => {
                        outputLines.push(`<h4>Referred Area ${idx}</h4>`);
                        outputLines.push(`<ul>`);
                        outputLines.push(`<li>IsExternalLink: ${referredArea.isExternalLink}</li>`);
                        outputLines.push(`<li>IsArea: ${referredArea.isArea}</li>`);
                        outputLines.push(`<li>SheetName: ${referredArea.sheetName}</li>`);
                        outputLines.push(`<li>ExternalFileName: ${referredArea.externalFileName}</li>`);
                        outputLines.push(`<li>StartColumn: ${referredArea.startColumn}</li>`);
                        outputLines.push(`<li>StartRow: ${referredArea.startRow}</li>`);
                        outputLines.push(`<li>EndColumn: ${referredArea.endColumn}</li>`);
                        outputLines.push(`<li>EndRow: ${referredArea.endRow}</li>`);
                        outputLines.push(`</ul>`);
                    });
                } else {
                    outputLines.push(`<p>No referred areas for this named range.</p>`);
                }
            }

            resultDiv.innerHTML = outputLines.join('');
        });
    </script>
</html>
```
