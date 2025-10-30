---
title: CellsFactory sınıfını kullanarak Stil nesnesi oluşturma
linktitle: CellsFactory sınıfını kullanarak Stil nesnesi oluşturma
description: CellsFactory sınıfını kullanarak Aspose.Cells for JavaScript ile bir hücre stili nesnesi oluşturmayı öğrenin. Elektronik tablo hücrelerinin görünümünü ihtiyacınıza göre özelleştirin.
keywords: Aspose.Cells, JavaScript via C++, elektronik elektronik tablo, stil nesnesi, hücre stili, özelleştirme
type: docs
weight: 70
url: /tr/javascript-cpp/create-style-object-using-cellsfactory-class/
---

## **CellsFactory sınıfını kullanarak Stil nesnesi oluşturma**
Aşağıdaki örnek kod, CellsFactory sınıfını kullanarak [Style](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi oluşturur ve ardından çalışma kitabının Varsayılan Stilini ayarlar. Bu kodun sonuçlarını görmek için lütfen [çıktı excel dosyasını](5115153.xlsx) indirin.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook with Default Style</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsFactory, BackgroundType, Color, Utils } = AsposeCells;

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
            // Create a Style object using CellsFactory class
            const cf = new CellsFactory();
            const st = cf.createStyle();

            // Set the Style fill color to Yellow
            st.pattern = BackgroundType.Solid;
            st.foregroundColor = Color.Yellow;

            // Create a workbook and set its default style using the created Style object
            const wb = new Workbook();
            wb.defaultStyle = st;

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
