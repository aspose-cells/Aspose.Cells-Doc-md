---
title: Impostare l’ombra degli Effetti di Testo di Forma o Casella di Testo con JavaScript tramite C++
linktitle: Impostazione dell ombra degli effetti di testo della forma o del riquadro di testo
type: docs
weight: 250
url: /it/javascript-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Impara come impostare l’ombra degli effetti di testo per qualsiasi forma o casella di testo usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}  

Puoi impostare l'**Ombra** degli **Effetti di Testo** di qualsiasi Forma o Casella di Testo. Usa la proprietà [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--). Essa rappresenta l'impostazione del testo della forma e ritorna gli oggetti [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting). Dopo averla accessibile, imposta l'**Ombra** tramite la proprietà [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--). Questa proprietà è di tipo [**PresetShadowType**](https://reference.aspose.com/cells/javascript-cpp/presetshadowtype) che ha diversi valori, alcuni dei quali sono  

- DiagonaleOffsetInferioreDestra  
- OffsetInferiore  
- DiagonaleOffsetSuperioreDestra  
- SinistraInterno  
- CentroInterno  
- DiagonaleSuperioreSinistraProspettiva  
- DiagonaleInferioreDestraProspettiva  

{{% /alert %}}  

Il seguente frammento di codice dimostra l'uso della proprietà [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--) per impostare l'ombra sugli effetti di testo di Forma o Casella di Testo.  

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
