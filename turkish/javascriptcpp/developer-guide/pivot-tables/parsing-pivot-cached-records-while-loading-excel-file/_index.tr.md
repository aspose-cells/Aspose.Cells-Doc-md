---
title: Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırın
type: docs
weight: 70
url: /tr/javascript-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Olası Kullanım Senaryoları**

Bir Pivot Tablosu oluşturduğunuzda, Microsoft Excel kaynak verinin bir kopyasını alır ve Pivot Önbelleğine saklar. Pivot Önbelleği, Microsoft Excel'in belleğinin içinde bulunur. Onu göremezsiniz, ancak bu, Pivot Tablonuzu oluştururken veya bir Dilim Seçimi değiştirdiğinizde veya satırlar/sütunlar etrafında hareket ettiğinizde Pivot Tablosunun başvurduğu veridir. Bu, Microsoft Excel'in Pivot Tablosundaki değişikliklere çok duyarlı olmasını sağlar, ancak dosya boyutunun potansiyel olarak iki kat artmasına neden olabilir.

Excel dosyanızı Workbook nesnesi içine yüklerken, Pivot Önbellek kayıtlarını da yüklemek isteyip istemediğinize karar verebilirsiniz, [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-) özelliğini kullanarak. Bu özelliğin varsayılan değeri **false**'dur. Pivot Önbelleği oldukça büyükse, performansı artırabilir. Ancak, Pivot Önbelleği'nin kayıtlarını da yüklemek istiyorsanız, bu özelliği **true** olarak ayarlamalısınız.

## **Excel dosyasını yüklerken Pivot Önbellek Kayıtlarını Ayrıştırın**

Aşağıdaki örnek kod, [**LoadOptions.parsingPivotCachedRecords**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#parsingPivotCachedRecords-boolean-) özelliğinin kullanımını açıklar. Pivot önbellek kayıtlarını ayrıştırırken [örnek Excel dosyasını](61767773.xlsx) yükler. Ardından pivot tablosunu yeniler ve [çıktı Excel dosyası](61767774.xlsx) olarak kaydeder.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Parsing Pivot Cached Records While Loading Example</title>
    </head>
    <body>
        <h1>Parsing Pivot Cached Records While Loading Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options
            const options = new LoadOptions();
            // Set ParsingPivotCachedRecords true, default value is false
            options.parsingPivotCachedRecords = true;

            // Load the Excel file with load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), options);

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first pivot table
            const pt = ws.pivotTables.get(0);

            // Set refresh data flag true
            pt.refreshDataFlag = true;

            // Refresh and calculate pivot table
            pt.refreshData();
            pt.calculateData();

            // Set refresh data flag false
            pt.refreshDataFlag = false;

            // Save the output Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
