---
title: Ändra tick etikettens riktning med JavaScript via C++
linktitle: Ändra riktning för ticketiketter
description: Lär dig hur du ändrar riktningen på tick etiketter i Aspose.Cells for JavaScript via C++. Vår guide hjälper dig att förstå hur du justerar orienteringen av tick etiketter på axlar, inklusive horisontell, vertikal och vinklad orientering.
keywords: Aspose.Cells for JavaScript via C++, tickmarkeringar, riktning, orientering, axlar, horisontell, vertikal, vinklad.
type: docs
weight: 170
url: /sv/javascript-cpp/change-tick-label-direction/
---

## **Ändra riktning för ticketiketter**

Aspose.Cells ger dig möjlighet att ändra riktningen på diagrammets ticketiketter genom att använda egenskapen [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--). Egenskapen [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) accepterar värdet för [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) ENUMERATION. ENUMERATION [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) innehåller följande medlemmar:

- Horisontell
- Vertikal
- Rotera 90
- Rotera 270
- Staplad

Följande bild jämför käll- och utdatafilerna

### **Källfilens bild**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Utdatasfilens bild**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Följande kodsnutt ändrar ticketikettens riktning från Rotera 90 till Horisontell.

## **Exempelkod**

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

Käll- och utdatafilerna kan laddas ned från följande länkar.

[Källfil](105480221.xlsx)

[Utdatasfil](105480223.xlsx)
