---
title: Задайте язык файла Excel, используя встроенные свойства документа с помощью JavaScript через C++
linktitle: Указание языка документа Excel с использованием встроенных свойств документа
type: docs
weight: 30
url: /ru/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **Возможные сценарии использования**

Вы можете изменить язык файла Excel, щёлкнув правой кнопкой по файлу и выбрав Свойства > Подробности, затем отредактировать поле Язык. Пожалуйста, используйте свойство [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--), чтобы изменить его программно с помощью API Aspose.Cells for JavaScript через C++.

## **Указание языка файла Excel с использованием встроенных свойств документа**

Следующий пример кода создает книгу и изменяет её встроенное свойство документа с именем язык. Посмотрите сгенерированный этим кодом [выходной файл Excel](64716891.xlsx) и скриншот, показывающий изменённое поле Язык с помощью свойства [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
