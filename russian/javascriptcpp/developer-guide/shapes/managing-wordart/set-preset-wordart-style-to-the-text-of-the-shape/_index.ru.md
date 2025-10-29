---
title: Устанавливайте предустановленный стиль WordArt для текста фигуры с помощью JavaScript через C++
linktitle: Установить предварительный стиль WordArt для текста формы
type: docs
weight: 280
url: /ru/javascript-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Узнайте, как установить предустановленный стиль WordArt для текста фигуры с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**
Вы можете установить предустановленный стиль WordArt для текста фигуры с помощью Aspose.Cells for JavaScript через C++. Пожалуйста, используйте методы [FontSetting.wordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/javascript-cpp/fontsetting/#wordArtStyle-presetwordartstyle-) или [FontSettingCollection.wordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/javascript-cpp/fontsettingcollection/#wordArtStyle-presetwordartstyle-) для этой цели.

## **Установить предварительный стиль WordArt для текста формы**
Следующий пример кода создает текстовое поле с текстом и затем устанавливает его предустановленный стиль WordArt с помощью метода [FontSetting.wordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/javascript-cpp/fontsetting/#wordArtStyle-presetwordartstyle-). Вот как выглядит [выходной excel-файл](5115445.xlsx) в Microsoft Excel.

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Preset WordArt Style</title>
    </head>
    <body>
        <h1>Set Preset WordArt Style Example</h1>
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
            const resultDiv = document.getElementById('result');

            // Create a new workbook (original JavaScript code created a new Workbook without reading a file)
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a textbox with some text
            const textbox = worksheet.shapes.addTextBox(0, 0, 0, 0, 100, 700);
            textbox.text = "Aspose File Format APIs";
            textbox.font.size = 44;

            // Sets preset WordArt style to the text of the shape.
            const fntSetting = textbox.richFormattings[0];
            fntSetting.wordArtStyle = AsposeCells.PresetWordArtStyle.WordArtStyle3;

            // Save the workbook in xlsx format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSetPresetWordArtStyle.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with WordArt';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```
