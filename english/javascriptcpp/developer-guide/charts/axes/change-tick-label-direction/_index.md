---
title: Change Tick Label Direction with JavaScript via C++
linktitle: Change Tick Label Direction
description: Learn how to change the direction of tick labels in Aspose.Cells for JavaScript via C++. Our guide will help you understand how to adjust the orientation of tick labels on axes, including horizontal, vertical, and angled orientations.
keywords: Aspose.Cells for JavaScript via C++, tick labels, direction, orientation, axes, horizontal, vertical, angled.
type: docs
weight: 170
url: /javascript-cpp/change-tick-label-direction/
---

## **Change Tick Label Direction**

Aspose.Cells provides you with the ability to change the chart tick label direction by using the [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) property. The [**TickLabels.directionType**](https://reference.aspose.com/cells/javascript-cpp/ticklabels/#directionType--) property accepts the [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) enumeration value. The [**ChartTextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/charttextdirectiontype) enumeration provides the following members:

- Horizontal
- Vertical
- Rotate90
- Rotate270
- Stacked

The following image compares the source and output files.

### **Source file image**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Output file image**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

The following code snippet changes the tick label direction from Rotate90 to Horizontal.

## **Sample Code**

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
            downloadLink.download = 'outputChangeChartDataLabelDirection.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Tick label direction changed. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

The source and output files can be downloaded from the following links.

[Source File](105480221.xlsx)

[Output File](105480223.xlsx)