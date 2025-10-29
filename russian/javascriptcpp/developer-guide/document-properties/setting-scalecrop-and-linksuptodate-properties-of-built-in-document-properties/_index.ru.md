---
title: Установка свойств ScaleCrop и LinksUpToDate встроенных свойств документа с помощью JavaScript через C++
linktitle: Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа
type: docs
weight: 320
url: /ru/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Узнайте, как устанавливать свойства ScaleCrop и LinksUpToDate встроенных свойств документа с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**
[BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) и [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) — это два расширенных встроенных свойства документа, определённых внутри формата OpenXml. Назначение этих свойств следующее.

## **1) ScaleCrop**
Этот элемент указывает режим отображения миниатюры документа. Установите этот элемент в **TRUE**, чтобы включить масштабирование миниатюры документа для отображения. Установите этот элемент в **FALSE**, чтобы обрезать миниатюру документа и показать только секции, которые помещаются на экране.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.

## **2) LinksUpToDate**
Этот элемент указывает, актуальны ли гиперссылки в документе. Установите этот элемент в **TRUE**, чтобы указать, что гиперссылки обновлены. Установите этот элемент в **FALSE**, чтобы указать, что гиперссылки устарели.

Допустимые значения для этого элемента определяются типом данных W3C XML Schema boolean.

## **Снимок экрана, показывающий эти свойства в файле app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Настройка свойств ScaleCrop и LinksUpToDate встроенных свойств документа**
Следующий пример кода устанавливает расширенные встроенные свойства документа [BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) и [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) рабочей книги. Пожалуйста, проверьте [сгенерированный файл Excel](5115500.xlsx), измените его расширение на .zip, распакуйте его содержимое и просмотрите app.xml, как показано на скриншоте выше.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
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
            const fileInput = document.getElementById('fileInput');

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
