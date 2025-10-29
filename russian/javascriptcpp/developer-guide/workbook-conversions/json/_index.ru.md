---
title: JSON с JavaScript через C++
linktitle: Json
type: docs
weight: 300
url: /ru/javascript-cpp/convert-workbook-to-json/
description: Узнайте, как конвертировать рабочую книгу Excel в JSON с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}
API Aspose.Cells поддерживает преобразование книги в Json (JavaScript Object Notation).
{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

API Aspose.Cells поддерживает преобразование таблиц в формат JSON. Для экспорта рабочей книги в JSON передайте [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) в качестве второго параметра метода [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-). Также можно использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions) для задания дополнительных настроек при экспорте рабочего листа в JSON.

Следующий пример демонстрирует экспорт активного листа в JSON с использованием члена перечисления [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json). Проверьте код преобразования [исходного файла](book1.xlsx) в [выходной Json](book1.Json), сгенерированный кодом.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Преобразовать CSV в JSON](/cells/ru/javascript-cpp/convert-csv-to-json/)
- [Преобразовать Excel в JSON](/cells/ru/javascript-cpp/convert-excel-to-json/)
- [Преобразовать JSON в CSV](/cells/ru/javascript-cpp/convert-json-to-csv/)
- [Преобразовать JSON в Excel](/cells/ru/javascript-cpp/convert-json-to-excel/)
