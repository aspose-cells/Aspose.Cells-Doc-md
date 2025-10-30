---
title: Shape veya Metin Kutusu nun Metin Efektleri Gölgesini JavaScript ve C++ kullanarak ayarlama
linktitle: Şekil veya Metin Kutusunun Metin Efektlerinin Gölgesini Ayarlama
type: docs
weight: 250
url: /tr/javascript-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Herhangi bir şekil veya Metin Kutusu için metin efektleri gölgesini nasıl ayarlayacağınızı Aspose.Cells for JavaScript ile C++ kullanarak öğrenin.
---

{{% alert color="primary" %}}  

Herhangi bir Şekil veya Metin Kutusu'nun **Metin Efektleri** gölgesini ayarlayabilirsiniz. Lütfen [**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--) özelliğini kullanın. Bu özellik şeklin metninin ayarını gösterir ve [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) nesnelerini döner. Ona eriştikten sonra, lütfen **Gölge**yi [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--) özelliği aracılığıyla ayarlayın. Bu özellik [**PresetShadowType**](https://reference.aspose.com/cells/javascript-cpp/presetshadowtype) türündedir ve birkaç değere sahiptir, bunlardan bazıları  

- Dikey Sağa Ofset  
- Alt Ofset  
- OffsetDiagonalTopRight  
- InsideLeft  
- InsideCenter  
- PerspectiveDiagonalUpperLeft  
- PerspectiveDiagonalLowerRight  

{{% /alert %}}  

Aşağıdaki kod parçası, Shape veya TextBox'un metin efektleri gölgesini ayarlamak için [**FontSetting.presetType**](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--) özelliğinin kullanımını gösterir.  

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
