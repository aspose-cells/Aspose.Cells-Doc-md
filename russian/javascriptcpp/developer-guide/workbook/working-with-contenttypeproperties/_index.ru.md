---
title: Работа с свойствами ContentTypeProperties с помощью JavaScript через C++
linktitle: Работа с ContentTypeProperties
type: docs
weight: 150
url: /ru/javascript-cpp/working-with-contenttypeproperties/
description: Узнайте, как работать с пользовательскими свойствами ContentTypeProperties в файлах Excel с использованием Aspose.Cells for JavaScript через C++.
---

Aspose.Cells предоставляет метод [**Workbook.contentTypeProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#contentTypeProperties--) для добавления пользовательских ContentTypeProperties в Excel файл. Также вы можете сделать свойство необязательным, установив свойство [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/javascript-cpp/contenttypeproperty/#isNillable--) в значение **true**. Следующий фрагмент кода демонстрирует добавление необязательных пользовательских ContentTypeProperties в Excel файл. На изображении показаны оба свойства, добавленных примером кода.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

Выходной файл, сгенерированный образцов кода, прикреплен в качестве справки.

[Выходной файл](95584314.xlsx)

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Working With Content Type Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');

            // Creating a new Workbook with Xlsx format
            const workbook = new Workbook(FileFormatType.Xlsx);

            // Adding content type properties
            let index = workbook.contentTypeProperties.add("MK31", "Simple Data");
            workbook.contentTypeProperties.get(index).isNillable = false;

            index = workbook.contentTypeProperties.add("MK32", new Date().toISOString(), "DateTime");
            workbook.contentTypeProperties.get(index).isNillable = true;

            // Saving the workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkingWithContentTypeProperties_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
