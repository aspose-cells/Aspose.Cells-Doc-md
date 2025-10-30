---
title: Arbeiten mit dem Schatteneffekt von Form oder Diagramm mit JavaScript über C++
linktitle: Arbeiten mit dem Schatten Effekt von Form oder Diagramm
type: docs
weight: 220
url: /de/javascript-cpp/working-with-the-shadow-effect-of-shape-or-chart/
description: Lernen Sie, wie Sie mit dem Schatteneffekt von Formen oder Diagrammen mithilfe von Aspose.Cells for JavaScript via C++ arbeiten.
---

## **Mögliche Verwendungsszenarien**  
Aspose.Cells for JavaScript via C++ bietet die Eigenschaft [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) zusammen mit der Klasse [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect), um mit dem Schatteneffekt von Formen oder Diagrammen zu arbeiten. Die Klasse [ShadowEffect](https://reference.aspose.com/cells/javascript-cpp/shadoweffect) enthält die folgenden Eigenschaften, die je nach Anwendungsanforderungen eingestellt werden können, um unterschiedliche Ergebnisse zu erzielen.  

- [ShadowEffect.angle](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#angle--)  
- [ShadowEffect.blur](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#blur--)  
- [ShadowEffect.color](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#color--)  
- [ShadowEffect.distance](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#distance--)  
- [ShadowEffect.presetType](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#presetType--)  
- [ShadowEffect.size](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#size--)  
- [ShadowEffect.transparency](https://reference.aspose.com/cells/javascript-cpp/shadoweffect/#transparency--)  

## **Arbeiten mit dem Schatten-Effekt von Form oder Diagramm**  
Der folgende Beispielcode lädt die [Quel-Excel-Datei](5115425.xlsx) und greift auf die erste Form im ersten Arbeitsblatt zu, setzt die Untereigenschaften der Eigenschaft [Shape.shadowEffect](https://reference.aspose.com/cells/javascript-cpp/shape/#shadowEffect--) und speichert dann die Arbeitsmappe in der [Ausgabedatei für Excel](5115411.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Shape Shadow Effect Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            const shadowEffect = shape.shadowEffect;
            shadowEffect.angle = 150;
            shadowEffect.blur = 4;
            shadowEffect.distance = 45;
            shadowEffect.transparency = 0.3;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shadow effect applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
