---
title: Configuración de sombra de efectos de texto de forma o cuadro de texto con JavaScript a través de C++
linktitle: Establecer sombra de efectos de texto de forma o cuadro de texto
type: docs
weight: 250
url: /es/javascript-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Aprenda cómo establecer la sombra de los efectos de texto para cualquier forma o cuadro de texto usando Aspose.Cells for JavaScript a través de C++.
---

{{% alert color="primary" %}}  

Puedes establecer la **Sombra** de los **Efectos de texto** de cualquier forma o cuadro de texto. Por favor, usa la propiedad [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--). Esta presenta la configuración del texto de la forma y devuelve objetos [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting). Después de acceder a ella, configura la **Sombra** mediante la propiedad [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--). Esta propiedad es del tipo [**PresetShadowType**](https://reference.aspose.com/cells/javascript-cpp/presetshadowtype) y tiene varios valores. Algunos de ellos son  

- Diagonal inferior derecha  
- Inferior  
- Diagonal superior derecha  
- Interior izquierdo  
- Centro interior  
PerspectiveDiagonalUpperLeft  
PerspectiveDiagonalLowerRight  

{{% /alert %}}  

El siguiente fragmento de código demuestra el uso de la propiedad [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--) para establecer la sombra de efectos de texto de Forma o Cuadro de texto.  

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
