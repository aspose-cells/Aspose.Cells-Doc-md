---
title: Modifier la direction des étiquettes de graduation avec JavaScript via C++
linktitle: Modifier la direction des étiquettes de graduation
description: Apprenez à changer la direction des étiquettes de graduation en Aspose.Cells for JavaScript via C++. Notre guide vous aidera à comprendre comment ajuster l orientation des étiquettes de graduation sur les axes, y compris horizontal, vertical, et angulé.
keywords: Aspose.Cells for JavaScript via C++, étiquettes de graduation, direction, orientation, axes, horizontal, vertical, angulé.
type: docs
weight: 170
url: /fr/javascript-cpp/change-tick-label-direction/
---

## **Changer la direction des étiquettes des graduations**

Aspose.Cells vous offre la possibilité de changer la direction des étiquettes de graduation du graphique en utilisant la propriété [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--). La propriété [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) accepte la valeur d'énumération [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype). L'énumération [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) fournit les membres suivants :

- Horizontale
- Verticale
- Rotation90
- Rotation270
- Empilée

L'image suivante compare les fichiers source et de sortie

### **Image du fichier source**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Image du fichier de sortie**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Le snippet de code suivant change la direction des étiquettes de graduation de Rotation90 à Horizontale.

## **Code d'exemple**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Tick Label Direction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartTextDirectionType } = AsposeCells;

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
            const result = document.getElementById('result');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const chart = worksheet.charts.get(0);

            chart.categoryAxis.tickLabels.directionType = ChartTextDirectionType.Horizontal;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeChartDataLableDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Les fichiers source et de sortie peuvent être téléchargés à partir des liens suivants.

[Fichier source](105480221.xlsx)

[Fichier de sortie](105480223.xlsx)
