---
title: Настройка полей комментария или фигуры внутри листа Excel с помощью JavaScript через C++
linktitle: Установить поля комментария или формы внутри таблицы
type: docs
weight: 1500
url: /ru/javascript-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/
description: Узнайте, как установить поля комментариев или фигур внутри листа Excel с помощью Script Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

Aspose.Cells позволяет вам устанавливать поля любой фигуры или комментария с помощью свойства [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/). Это свойство возвращает объект класса [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment), который имеет различные свойства, например, [**ShapeTextAlignment.topMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#topMarginPt--), [**ShapeTextAlignment.leftMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#leftMarginPt--), [**ShapeTextAlignment.bottomMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#bottomMarginPt--), [**ShapeTextAlignment.rightMarginPt**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rightMarginPt--) и др., которые можно использовать для установки верхних, левых, нижних и правых полей.  

## **Задать поля комментария или формы внутри рабочего листа**  

Пожалуйста, ознакомьтесь со следующим образцом кода. Он загружает [образец Excel файла](61767851.xlsx), содержащий две формы. Код получает доступ к формам поочередно и устанавливает их верхние, левые, нижние и правые поля. Пожалуйста, ознакомьтесь с [файлом вывода Excel](61767852.xlsx), сгенерированным кодом, и снимком экрана, показывающим эффект кода на файл вывода Excel.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Margins of Comment or Shape Example</title>
    </head>
    <body>
        <h1>Set Margins of Comment or Shape Inside The Worksheet</h1>
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

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            const shapes = ws.shapes;
            for (let i = 0; i < shapes.count; i++) {
                const sh = shapes.get(i);
                // Access the text alignment
                const txtAlign = sh.textBody.textAlignment;

                // Set auto margin false
                txtAlign.isAutoMargin = false;

                // Set the top, left, bottom and right margins
                txtAlign.topMarginPt = 10;
                txtAlign.leftMarginPt = 10;
                txtAlign.bottomMarginPt = 10;
                txtAlign.rightMarginPt = 10;
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Margins updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
