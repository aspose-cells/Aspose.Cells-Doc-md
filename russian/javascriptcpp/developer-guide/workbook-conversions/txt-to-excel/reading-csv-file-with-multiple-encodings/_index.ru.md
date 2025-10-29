---
title: Чтение CSV файла с несколькими кодировками с помощью JavaScript на C++
linktitle: Чтение CSV файла с несколькими кодировками
type: docs
weight: 200
url: /ru/javascript-cpp/reading-csv-file-with-multiple-encodings/
description: Узнайте, как читать CSV файлы с несколькими кодировками, используя Script Aspose.Cells for Java на C++.
---

{{% alert color="primary" %}}

 Иногда ваши CSV-файлы содержат несколько кодировок (Unicode, ANSI, UTF8, UTF7 и т. д.). Aspose.Cells позволяет загружать такие CSV-файлы и преобразовывать их в другие форматы, например, PDF или XLSX.

{{% /alert %}}

Для этого используйте свойство [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--), установив его в значение **true** для правильной загрузки CSV с несколькими кодировками.

На следующем скриншоте показан пример CSV-файла, который содержит две строки. Первая строка в кодировке **ANSI**, а вторая строка в кодировке **Unicode**.

|**Входной файл**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Следующий снимок показывает файл XLSX, преобразованный из вышеуказанного CSV-файла без установки свойства [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) в **true**. Как видите, Unicode-текст был преобразован неправильно.

|**Файл вывода 1: не предусмотрены множественные кодировки**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 Следующий скриншот показывает XLSX-файл, преобразованный из указанного CSV-файла после установки свойства [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#isMultiEncoded--) в **true**. Теперь Unicode-текст отображается правильно.

|**Файл вывода 2: IsMultiEncoded установлен в true**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Ниже приведен образец кода, преобразующий вышеуказанный файл CSV в формат XLSX правильно.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Multi-Encoded CSV to XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create TxtLoadOptions and set isMultiEncoded property
            const options = new TxtLoadOptions();
            options.isMultiEncoded = true;

            // Load the CSV into a Workbook using the options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const outName = file.name.replace(/(\.[^/.]+)$/, '$1.out.xlsx');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = outName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to save the XLSX file.</p>';
        });
    </script>
</html>
```

## Связанные статьи

- [Открытие файлов CSV](/cells/ru/javascript-cpp/opening-files-with-different-formats/#opening-csv-files)
