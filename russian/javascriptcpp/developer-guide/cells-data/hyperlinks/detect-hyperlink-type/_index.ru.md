---
title: Обнаружение типа гиперссылки
type: docs
weight: 160
url: /ru/javascript-cpp/detect-hyperlink-type/
description: Узнайте, как обнаруживать тип гиперссылки через Aspose.Cells for JavaScript через C++ API.
keywords: Обнаружение типа гиперссылки JavaScript через C++, Определить тип гиперссылки JavaScript через C++, Получить тип гиперссылки JavaScript через C++
---

## **Определение типа гиперссылки**

Файл Excel может иметь разные типы гиперссылок, такие как внешние, ссылка на ячейку, путь к файлу и др. Aspose.Cells for JavaScript через C++ поддерживает функцию определения типа гиперссылки. Типы гиперссылок представлены перечислением [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). Перечисление [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype) содержит следующие элементы.

- Внешний: Внешняя ссылка
- FilePath: Локальный и полный путь к файлам/папкам.
- Email: Электронная почта
- CellReference: Ссылка на ячейку или именованный диапазон.

Чтобы проверить тип гиперссылки, класс [**Hyperlink**](https://reference.aspose.com/cells/javascript-cpp/hyperlink) предоставляет свойство [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) с возвращаемым типом [**TargetModeType**](https://reference.aspose.com/cells/javascript-cpp/targetmodetype). Следующий фрагмент кода демонстрирует использование свойства [**linkType**](https://reference.aspose.com/cells/javascript-cpp/hyperlink/#linkType--) с помощью этого [исходного файла Excel](94896195.xlsx).

### Исходный код

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Link Types Example</title>
    </head>
    <body>
        <h1>Link Types Example</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                const resultDiv = document.getElementById('result');

                if (!fileInput.files.length) {
                    resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object from the uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Get the first (default) worksheet
                const worksheet = workbook.worksheets.get(0);

                // Create a range A1:A7 (original code created A1:B7 but used A1 to A7 in parameters)
                const range = worksheet.cells.createRange("A1", "A7");

                // Get Hyperlinks in range
                const hyperlinks = range.hyperlinks;

                let outputHtml = '<p>Hyperlinks found:</p><ul>';
                if (typeof hyperlinks.forEach === 'function') {
                    hyperlinks.forEach(link => {
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    });
                } else {
                    for (let i = 0; i < hyperlinks.count; i++) {
                        const link = hyperlinks.get(i);
                        outputHtml += `<li>${link.textToDisplay}: ${link.linkType}</li>`;
                    }
                }
                outputHtml += '</ul>';

                resultDiv.innerHTML = outputHtml;
            });
        });
    </script>
</html>
```


Ниже приведен вывод, сгенерированный указанным выше фрагментом кода.

### Вывод в консоли
