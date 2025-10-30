---
title: Konsolidasyon Fonksiyonu
type: docs
weight: 20
url: /tr/javascript-cpp/consolidation-function/
description: Aspose.Cells for JavaScript kullanarak Pivot Tablo nun Veri Alanlarına KonsolidasyonFonksiyonu nasıl uygulanır?
keywords: Aspose.Cells for JavaScript kullanarak Excel, Excel JavaScript kütüphanesi, Pivot Tablo Veri Alanlarına KonsolidasyonFonksiyonu Uygulama
---

## **Konsolidasyon fonksiyonu**

Aspose.Cells for JavaScript kullanarak Pivot Tablo'nun veri alanlarına (veya değer alanlarına) KonsolidasyonFonksiyonu uygulayabilirsiniz. Microsoft Excel'de, değer alanına sağ tıklayıp **Değer Alanı Ayarları...** seçeneğini seçebilir ve ardından **Değerleri Özetle** sekmesini kullanabilirsiniz. Oradan Sum, Count, Average, Max, Min, Product, Distinct Count vb. herhangi bir KonsolidasyonFonksiyonu seçebilirsiniz.

Aspose.Cells for JavaScript kullanarak [**ConsolidationFunction**](https://reference.aspose.com/cells/javascript-cpp/consolidationfunction/) sıralaması, aşağıdaki konsolidasyon fonksiyonlarını desteklemek için sağlar.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Aspose.Cells for JavaScript kullanarak Pivot Tablo'nun Veri Alanlarına KonsolidasyonFonksiyonu nasıl uygulanır?**

Aşağıdaki kod **Ortalama** konsolidasyon fonksiyonunu birinci veri alanına (veya değer alanına) ve ikinci veri alanına (veya değer alanına) **FarklıSayıyıSay** konsolidasyon fonksiyonunu uygular.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PivotTable Consolidation Function</title>
    </head>
    <body>
        <h1>Apply Consolidation Function to PivotTable</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet of the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table of the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Apply Average consolidation function to first data field
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Average;

            // Apply DistinctCount consolidation function to second data field
            pivotTable.dataFields.get(1).function = AsposeCells.ConsolidationFunction.DistinctCount;

            // Calculate the data to make changes affect
            pivotTable.calculateData();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable consolidation functions applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

BENZERSİZ_SAYIM birleştirme fonksiyonu yalnızca Microsoft Excel 2013 tarafından desteklenmektedir.

{{% /alert %}}
