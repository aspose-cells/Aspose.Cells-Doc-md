---
title: Bir Çalışma Sayfasından Pivot Tablosunu Sil
type: docs
weight: 60
url: /tr/javascript-cpp/delete-pivot-table-from-a-worksheet/
description: Excel Sayfalarında PivotTable’ı Kaldırmak için Aspose.Cells for JavaScript C++ kodu
keywords: Aspose.Cells for JavaScript C++ Excel, Excel JavaScript kütüphanesi ile pivot tabloyu sayfadan kaldırma, pivot tabloyu silme, pivot tabloyu kaldırma, nasıl silinir, kaldırılır, c++ ile pivot tabloyu silme, pivot tabloyu kaldırma, silme
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript C++ ile Pivot Tabloyu silme veya kaldırma özelliği sağlar. Pivot tabloyu, pivot tablo nesnesini veya konumunu kullanarak silebilirsiniz. Lütfen [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) metodunu kullanarak pivot tablo nesnesini, [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) metodunu ise koleksiyon içindeki konumunu kullanarak silin.

{{% /alert %}}

## **Çalışma Sayfasından Pivot Tablo Nasıl Silinir Aspose.Cells for JavaScript ile C++ Kullanılarak**

Aşağıdaki örnek kod, çalışma sayfasından iki pivot tablosunu siler. İlk önce [**Worksheet.pivotTables.remove(pivotTable)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#remove-pivottable-) yöntemini kullanarak pivot tablosunu kaldırır, ardından [**Worksheet.pivotTables.removeAt(index, keepData)**](https://reference.aspose.com/cells/javascript-cpp/pivottablecollection/#removeAt-number-boolean-) yöntemini kullanarak pivot tablosunu kaldırır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Table</title>
    </head>
    <body>
        <h1>Remove Pivot Table Example</h1>
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
            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table object
            const pivotTable = worksheet.pivotTables.get(0);

            // Remove pivot table using pivot table object
            worksheet.pivotTables.remove(pivotTable);
            // OR remove by index:
            // worksheet.pivotTables.removeAt(0);

            // Saving the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
