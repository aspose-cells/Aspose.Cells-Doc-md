---
title: Задайте версию документа Excel, используя встроенные свойства документа с помощью JavaScript через C++
linktitle: Указание версии документа Excel с использованием встроенных свойств документа
type: docs
weight: 20
url: /ru/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: Узнайте, как программно задать версию документа Excel с помощью встроенных свойств документа с использованием JavaScript через C++.
---

## **Возможные сценарии использования**  

Вы можете изменить **номер версии** файла Excel, щелкнув правой кнопкой мыши по файлу и выбрав Свойства > Детали, затем отредактировав поле **Номер версии**. Пожалуйста, используйте свойство [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--) для выбора этого программно через API Aspose.Cells.  

## **Указание версии документа Excel с использованием встроенных свойств документа**  

Следующий пример кода создает книгу и изменяет её встроенные свойства документа, включая название, авторов и номер версии. Посмотрите сгенерированный этим кодом [выходной файл Excel](64716811.xlsx) и скриншот, показывающий изменённый номер версии с помощью свойства [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
