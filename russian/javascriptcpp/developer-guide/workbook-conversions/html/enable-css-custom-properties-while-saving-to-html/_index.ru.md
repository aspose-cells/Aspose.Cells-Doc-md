---
title: Включить свойства CSS при сохранении в HTML с помощью JavaScript через C++
linktitle: Включить пользовательские CSS свойства при сохранении в HTML
type: docs
weight: 320
url: /ru/javascript-cpp/enable-css-custom-properties-while-saving-to-html/
description: Узнайте, как включить пользовательские свойства CSS при сохранении Excel файлов в HTML с помощью Aspose.Cells for JavaScript через C++. 
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, при наличии нескольких случаев одной базовой64 изображения, с пользовательским свойством данных изображения необходимо сохранять только один раз, чтобы повысить производительность итогового HTML. Пожалуйста, используйте свойство [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--) и установите его **true** при сохранении в HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Включить пользовательские свойства CSS при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--). Скриншот демонстрирует эффект этого свойства, когда оно не установлено в **true**. Пожалуйста, скачайте [пример файла Excel](50528260.xlsx), использованный в этом примере, и [выходной HTML файл](50528261.zip), сгенерированный им, для справки.



## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Enable CSS Custom Properties Example</title>
    </head>
    <body>
        <h1>Enable CSS Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and set properties (converted from setters to property assignments)
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.exportImagesAsBase64 = true;
            opts.enableCssCustomProperties = true;

            // Save the workbook to HTML using SaveFormat.Html and provided options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEnableCssCustomProperties.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
