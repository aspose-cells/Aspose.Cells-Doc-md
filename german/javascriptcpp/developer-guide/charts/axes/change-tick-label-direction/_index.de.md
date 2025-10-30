---
title: Ändern Sie die Richtung der Tick Beschriftung mit JavaScript via C++
linktitle: Ändern Sie die Ausrichtung der Tickbeschriftung
description: Lernen Sie, wie man die Richtung der Tick Beschriftungen in Aspose.Cells for JavaScript mit C++ ändert. Unser Leitfaden hilft Ihnen, die Ausrichtung der Tick Beschriftungen auf Achsen zu verstehen, einschließlich horizontaler, vertikaler und schräger Ausrichtungen.
keywords: Aspose.Cells for JavaScript mit C++, Tick Beschriftungen, Richtung, Ausrichtung, Achsen, horizontal, vertikal, schräg.
type: docs
weight: 170
url: /de/javascript-cpp/change-tick-label-direction/
---

## **Ändern der Richtung der Markierungstexte**

Aspose.Cells bietet die Möglichkeit, die Richtung der Diagramm-Tick-Labels mit der [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) Eigenschaft zu ändern. Die [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) Eigenschaft akzeptiert den [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) Enumeration-Wert. Das [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) Enumeration bietet die folgenden Mitglieder:

- Horizontal
- Vertikal
- Drehen90
- Drehen270
- Gestapelt

Das folgende Bild vergleicht die Quell- und Ausgabedateien

### **Quelldateibild**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Ausgabedateibild**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Der folgende Code-Schnipsel ändert die Richtung der Tickbeschriftung von Rotate90 auf Horizontal.

## **Beispielcode**

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

Die Quell- und Ausgabedateien können von den folgenden Links heruntergeladen werden.

[Quelldatei](105480221.xlsx)

[Ausgabedatei](105480223.xlsx)
