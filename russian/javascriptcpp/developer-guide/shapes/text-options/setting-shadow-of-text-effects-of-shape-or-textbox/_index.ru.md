---
title: Настройка тени эффектов текста фигуры или текстового поля с помощью JavaScript через C++
linktitle: Установка тени текстовых эффектов формы или текстового поля
type: docs
weight: 250
url: /ru/javascript-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Узнайте, как задать тень эффектов текста для любой фигуры или текстового поля с помощью Script Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  

Вы можете установить **Тень** эффекта **Текстовых эффектов** любой фигуры или текстового поля. Пожалуйста, используйте свойство [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--). Оно представляет настройку текста фигуры и возвращает объекты [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting). После получения доступа установите **Тень** через свойство [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--). Это свойство типа [**PresetShadowType**](https://reference.aspose.com/cells/javascript-cpp/presetshadowtype), которое имеет несколько значений. Некоторые из них  

- Смещение по диагонали вниз и вправо  
- Смещение вниз  
- Смещение по диагонали вверх и вправо  
- Слева внутри  
- По центру внутри  
- Диагональная перспектива вверху слева  
- ПерспективаДиагональНижнийПравый  

{{% /alert %}}  

Следующий фрагмент кода демонстрирует использование свойства [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--) для установки тени эффектов текста фигуры или текстового поля.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Text Effects Shadow of Shape or Textbox</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PresetShadowType, Color } = AsposeCells;

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

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Add text box with these dimensions
            const tb = ws.shapes.addTextBox(2, 0, 2, 0, 100, 400);

            // Set the text of the textbox
            tb.text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

            // Set all the text runs shadow to preset offset bottom
            const textBody = tb.textBody;
            for (let i = 0; i < textBody.count; i++) {
                const textRun = textBody.get(i);
                textRun.textOptions.shadow.presetType = PresetShadowType.OffsetBottom;
            }

            // Set the font color and size of the textbox
            tb.font.color = Color.Red;
            tb.font.size = 16;

            // Save the output file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSettingTextEffectsShadowOfShapeOrTextbox.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
