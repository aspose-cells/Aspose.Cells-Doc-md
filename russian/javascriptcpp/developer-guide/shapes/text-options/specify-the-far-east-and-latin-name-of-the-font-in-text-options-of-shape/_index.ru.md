---
title: Укажите название шрифта на Востоке и в Латинице в настройках текста фигуры с помощью JavaScript через C++
linktitle: Укажите Дальний Восток и латинское название шрифта в опциях текста формы
type: docs
weight: 1600
url: /ru/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Узнайте, как указать имена шрифтов на Востоке и в Латинице в настройках текста фигур с помощью Script Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**  

Иногда вам нужно отображать текст на Восточных языках, например японский, китайский, тайский и др. Script Aspose.Cells for JavaScript через C++ предоставляет свойство [**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--), которое можно использовать для указания имени шрифта для Восточноязычных шрифтов. Также вы можете указать латинский шрифт, используя свойство [**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--).  

## **Укажите Дальний Восток и латинское название шрифта в опциях текста формы**  

Следующий пример создает текстовое поле и добавляет внутри него японский текст. Затем указывается латинское и Восточноазиатское название шрифтов для текста и сохраняется рабочая книга как [выходной файл Excel](67338274.xlsx). Следующий скриншот показывает латинские и Восточноазиатские названия шрифтов выходного текстового поля в Microsoft Excel.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Far East and Latin Name of Font in TextOptions of Shape</h1>
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
            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Add textbox inside the worksheet.
            const idx = ws.textBoxes.add(5, 5, 50, 200);
            const tb = ws.textBoxes.get(idx);

            // Set the text of the textbox.
            tb.text = "こんにちは世界";

            // Specify the Far East and Latin name of the font.
            tb.textOptions.latinName = "Comic Sans MS";
            tb.textOptions.farEastName = "KaiTi";

            // Save the output Excel file.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
