---
title: JavaScript ile C++ kullanarak Sparkline Ekleme
linktitle: Kıvılcımlar
type: docs
weight: 160
url: /tr/javascript-cpp/creating-sparklines/
description: Aspose.Cells for JavaScript ile C++ kullanarak Excel için sparklines oluştur.
---

## **Bir kıvılcım ekleyin**
{{% alert color="primary" %}} 

Sparkline, bir çalışma sayfası hücresinde küçük bir grafiktir ve verilerin görsel temsilini sağlar. Trendleri göstermek için sparklines kullanın, örneğin mevsimsel artışlar veya azalmalar, ekonomik döngüler veya maksimum ve minimum değerleri vurgulamak için. En etkili sonuç için sparklini veriye yakın konumlandırın. Üç tür Sparkline vardır: Çizgi, Sütun ve Yığılmış.

{{% /alert %}} 

Aşağıdaki örnek kodlarla Aspose.Cells for JavaScript ile C++ kullanarak sparklines oluşturmak oldukça basittir:



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sparklines Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, SparklineType, Color } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Put values into cells
            sheet.cells.get("A1").putValue(5);
            sheet.cells.get("B1").putValue(2);
            sheet.cells.get("C1").putValue(1);
            sheet.cells.get("D1").putValue(3);

            // Define the CellArea
            const ca = CellArea.createCellArea(0, 4, 0, 4);

            // Add a sparkline group
            const idx = sheet.sparklineGroups.add(SparklineType.Line, `${sheet.name}!A1:D1`, false, ca);

            const group = sheet.sparklineGroups.get(idx);
            group.sparklines.add(`${sheet.name}!A1:D1`, 0, 4);

            // Customize Sparklines
            const clr = workbook.createCellsColor();
            clr.color = Color.Orange;
            group.seriesColor = clr;

            // Set the high points are colored green and the low points are colored red
            group.showHighPoint = true;
            group.showLowPoint = true;
            group.highPointColor.color = Color.Green;
            group.lowPointColor.color = Color.Red;
            // Set line weight 
            group.lineWeight = 1.0;

            // Saving the Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Sparklines created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Kıvılcımları ve Ayarları 3B Biçimi kullanarak Kullanma](/cells/tr/javascript-cpp/using-sparklines-and-settings-3d-format/)
