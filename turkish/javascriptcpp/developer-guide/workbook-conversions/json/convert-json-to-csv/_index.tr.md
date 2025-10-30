---
title: JSON u C++ ile JavaScript kullanarak CSV ye Dönüştürme
linktitle: JSON u CSV ye dönüştür
type: docs
weight: 210
url: /tr/javascript-cpp/convert-json-to-csv/
description: JSON verisini CSV ye dönüştürmenin nasıl yapılacağını Aspose.Cells for JavaScript C++ ile öğrenin.
---

## **JSON'ı CSV'ye dönüştür**

Aspose.Cells for JavaScript C++ temel ve iç içe JSON'u CSV'ye dönüştürmeyi destekler. Bunun için API [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) sınıflarını sağlar. [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) sınıfı, [**JsonLayoutOptions.arrayAsTable**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions/#arrayAsTable--) (diziyi tablo olarak işler) gibi JSON düzeni seçenekleri sunar. [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) sınıfı, JSON'u [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) sınıfı ile ayarlanan düzen seçenekleri kullanarak işler.

Aşağıdaki kod örneği, [kaynak JSON dosyasını](104398869.json) yüklemek ve [çıktı CSV dosyasını](104398870.csv) oluşturmak için [**JsonLayoutOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonlayoutoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility) sınıflarını kullanmayı gösterir.

### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells JSON to CSV Example</title>
    </head>
    <body>
        <h1>Import JSON to CSV Example</h1>
        <input type="file" id="fileInput" accept=".json" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLayoutOptions, JsonUtility, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const jsonText = await file.text();

            // Create empty workbook
            const workbook = new Workbook();

            // Get Cells from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Set JsonLayoutOptions
            const importOptions = new JsonLayoutOptions();
            importOptions.convertNumericOrDate = true;
            importOptions.arrayAsTable = true;
            importOptions.ignoreTitle = true;

            // Import JSON data into worksheet cells starting at A1 (0,0)
            JsonUtility.importData(jsonText, cells, 0, 0, importOptions);

            // Save Workbook as CSV
            const outputData = workbook.save(SaveFormat.Csv);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleJson_out.csv';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CSV File';

            resultDiv.innerHTML = '<p style="color: green;">JSON imported and CSV prepared. Click the download link to get the CSV file.</p>';
        });
    </script>
</html>
```
