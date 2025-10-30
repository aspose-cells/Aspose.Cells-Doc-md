---
title: Schatten der Text Effekte von Shape oder TextBox mit JavaScript über C++ festlegen
linktitle: Einstellen des Schattens von Texteffekten von Form oder TextBox
type: docs
weight: 250
url: /de/javascript-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Erfahren Sie, wie Sie den Schatten der Texteffekte für jedes Shape oder TextBox mit Aspose.Cells for JavaScript über C++ festlegen.
---

{{% alert color="primary" %}}  

Sie können den **Schatten** der **Texteffekte** jeder Form oder Textbox festlegen. Bitte verwenden Sie die [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--)-Eigenschaft. Sie zeigt die Einstellung des Texts der Form an und gibt [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting)-Objekte zurück. Nach dem Zugriff legen Sie den **Schatten** über die [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)-Eigenschaft fest. Diese Eigenschaft ist vom Typ [**PresetShadowType**](https://reference.aspose.com/cells/javascript-cpp/presetshadowtype) und hat mehrere Werte. Einige davon sind  

- OffsetDiagonal-unten-rechts  
- OffsetBottom  
- OffsetDiagonal-oben-rechts  
- Innen-links  
- Innen-mitte  
- PerspektiveDiagonalObenLinks  
- PerspektiveDiagonalUntenRechts  

{{% /alert %}}  

Das folgende Codesnippet zeigt die Verwendung der [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)-Eigenschaft zum Festlegen des Schattens der Texteffekte von Shape oder TextBox.  

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
