---
title: JavaScript ile Çizelgede Hangi Eksenin Var Olduğunu Belirleme ve C++ ile JavaScript kullanarak Eksenlerin Var olup olmadığını belirleme
linktitle: Grafiğin hangi Eksenin varolduğunu belirle.
description: Aspose.Cells for JavaScript kullanarak C++ ile bir çizelgede hangi eksenin olduğunu belirlemeyi öğrenin. Kılavuzumuz, kategori, değer ve ikinci eksenler dahil olmak üzere bir çizelgedeki farklı eksenleri tanımlamanıza ve erişmenize yardımcı olacaktır.
keywords: Aspose.Cells for JavaScript kullanarak C++, çizelge, eksen, varlığı, kategori, değer, ikinci.
type: docs
weight: 140
url: /tr/javascript-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}  
Bazen, kullanıcıların belirli bir eksenin grafikte var olup olmadığını bilmeleri gerekir. Örneğin, bir İkincil Değer Ekseninin grafikte olup olmadığını öğrenmek isteyebilirler. Bazı grafikler, örneğin Pasta, Exploded Pasta, PastaPasta, Çubuk Pasta, 3D Pasta, 3D Exploded Pasta, Daire, Daireyle Patlatılmış vb. eksenleri içermez.  

Aspose.Cells, belirli bir eksenin grafikte var olup olmadığını belirlemek için [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) methodunu sağlar.  
{{% /alert %}}  

Aşağıdaki örnek kod, [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/javascript-cpp/chart/#hasAxis-AxisType-boolean-) kullanarak örnek diyagramın Birincil ve İkincil Kategori ve Değer Ekseni olup olmadığını gösterir.  

## Çizelgede hangi eksenin olduğunu belirlemek için JavaScript kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Chart Axes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Check if there are any charts before accessing
            const charts = worksheet.charts;
            if (charts.count === 0) {
                resultDiv.innerHTML = '<p>No charts found in the worksheet.</p>';
                return;
            }

            // Access the chart
            const chart = charts.get(0);

            // Determine which axis exists in chart
            let outputs = [];
            let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
            outputs.push("Has Primary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
            outputs.push("Has Secondary Category Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
            outputs.push("Has Primary Value Axis: " + ret);

            ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
            outputs.push("Has Secondary Value Axis: " + ret);

            resultDiv.innerHTML = '<p>' + outputs.join('</p><p>') + '</p>';
        });
    </script>
</html>
```

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Kodun konsol çıktısı aşağıda gösterilmiştir, Bu çıktı Birincil Kategori ve Değer Eksenleri için doğru, İkincil Kategori ve Değer Eksenleri için yanlış gösterir.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}
