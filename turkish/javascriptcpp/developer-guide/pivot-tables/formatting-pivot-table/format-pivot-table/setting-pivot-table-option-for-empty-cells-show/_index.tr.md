---
title: Boş Hücreler İçin pivot tablo seçeneğini ayarlayın
type: docs
weight: 40
url: /tr/javascript-cpp/setting-pivot-table-option-for-empty-cells-show/
---

{{% alert color="primary" %}}

Farklı pivot tablo seçenekleri ayarlamak için Aspose.Cells for JavaC++ betiğini kullanabilirsiniz. Bu seçeneklerden biri de "Boş hücrelerde göster"dır. Bu seçeneği ayarlayarak, pivot tablosundaki tüm boş hücreler belirli bir dize olarak gösterilir.

{{% /alert %}}

## **Boş Hücreler İçin Göster Pivot Tablo Seçeneği Ayarlama**

Bu seçeneği bulup Microsoft Excel'de ayarlamak için:

1. Bir pivot tablo seçin ve sağ tıklayın.
1. **PivotTablo Seçenekleri**'ni seçin.
1. **Düzen ve Biçim** sekmesini seçin.
1. **Boş hücreler için göster** seçeneğini seçin ve bir dize belirtin.

## **Aspose.Cells for JavaC++ ile Pivot Tablo Seçeneği Ayarlama**

Aspose.Cells for JavaC++ betiği, "Boş hücrelerde göster" pivot tablo seçeneğini ayarlamak için [**PivotTable.displayNullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#displayNullString-boolean-) ve [**PivotTable.nullString**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#nullString-string-) özelliklerini sağlar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Update Example</title>
    </head>
    <body>
        <h1>Update PivotTable Null Display Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            await AsposeCells.onReady();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its first pivot table
            const worksheet = workbook.worksheets.get(0);
            const pt = worksheet.pivotTables.get(0);

            // Indicating if or not display the empty cell value
            pt.displayNullString = true;
            // Indicating the null string
            pt.nullString = "null";

            // Recalculate pivot table data
            pt.calculateData();

            // Do not refresh data on opening file
            pt.refreshDataOnOpeningFile = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## İlgili Makaleler

- [Pivot Tablosu Biçimlendirme](/cells/tr/javascript-cpp/formatting-pivot-table/)
