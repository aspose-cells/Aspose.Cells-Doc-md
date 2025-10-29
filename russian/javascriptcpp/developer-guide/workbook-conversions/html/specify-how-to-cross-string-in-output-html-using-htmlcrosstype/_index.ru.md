---
title: Задайте способ пересечения строк в выходном HTML, используя HtmlCrossType с помощью JavaScript через C++
linktitle: Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType
type: docs
weight: 140
url: /ru/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Узнайте, как управлять переполнением строк в HTML выводе, указывая HtmlCrossType в Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, строка выходит за пределы, если следующая ячейка в следующем столбце пустая или отсутствует. При сохранении файла Excel в HTML вы можете управлять этим переполнением, задавая тип переноса через перечисление [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Оно имеет следующие значения:

- **HtmlCrossType.Default**: отображается как в MS Excel; зависит от следующей ячейки. Если следующая ячейка null, строка будет перепрыгивать или обрезаться.

- **HtmlCrossType.MSExport**: Отображение строки как при экспорте HTML из MS Excel.

- **HtmlCrossType.Cross**: отображение HTML-перепрыгивания строки; производительность при создании крупных HTML-файлов будет более чем в десять раз быстрее, чем при установке значения по умолчанию или FitToCell.

- **HtmlCrossType.FitToCell**: отображает строку только внутри ширины ячейки.

## **Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType**

Следующий пример кода загружает [пример файла Excel](51740732.xlsx) и сохраняет его в формате HTML, задавая разные значения [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). Пожалуйста, скачайте [выходные HTML](51740734.zip), созданные этим кодом. Пример файла Excel содержит изображение с красной рамкой, как показано на этом скриншоте, который демонстрирует эффект значений [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) на выводимый HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
