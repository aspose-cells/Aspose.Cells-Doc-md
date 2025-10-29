---
title: Визуализировать надстройки Office при преобразовании Excel в PDF с помощью JavaScript через C++
linktitle: Рендеринг офисных надстроек при преобразовании Excel в PDF
type: docs
weight: 100
url: /ru/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Возможные сценарии использования**

 Ранее Aspose.Cells не мог рендерить офисные дополнения при сохранении файла Excel в формат PDF. Теперь Aspose.Cells делает это правильно. Вам не нужно использовать никаких специальных методов или свойств для рендеринга офисных дополнений в итоговом PDF. Просто сохраните файл Excel в формат PDF, и он автоматически отобразит офисные дополнения.

## **Рендеринг офисных надстроек при преобразовании Excel в PDF**

Следующий пример кода сохраняет [образец файла Excel](60489769.xlsx), содержащий офисные дополнения. Посмотрите [выводной PDF, созданный с предыдущей версии, то есть 17.11](60489770.pdf) и [выводной PDF, созданный с новой версии, то есть 17.12 и последующие](60489771.pdf). Вывод предыдущей версии — пустой PDF, а новая версия показывает офисное дополнение.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Office Add-Ins to PDF Example</title>
    </head>
    <body>
        <h1>Render Office Add-Ins to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Aspose.Cells version (converted from getVersion())
            const version = AsposeCells.CellsHelper.version;

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `output-${version}.pdf`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Saved to PDF successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
