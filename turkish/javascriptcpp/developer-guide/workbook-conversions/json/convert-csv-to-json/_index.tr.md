---
title: CSV’yi JavaScript ile JSON’a Dönüştürün, C++ kullanarak
linktitle: CSV den JSON a Dönüştürme
type: docs
weight: 220
url: /tr/javascript-cpp/convert-csv-to-json/
description: Kolay kullanımlı Aspose.Cells for JavaScript ile CSV dosyasını JSON’a dönüştürün, C++ API kullanarak.
keywords: CSV’yi JSON’a Dönüştür, CSV’den JSON’a dönüştür, CSV, JSON, CSV’yi JSON’a dönüştürmek için C++ ile JavaScript kullanın, CSV’den JSON’a dönüştürmek için C++ kodu
---

## **CSV'yi JSON'a dönüştür**

Aspose.Cells, CSV'yi JSON'a dönüştürmeyi destekler. Bunun için API [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) sınıflarını sağlar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) sınıfı, JSON'e dışa aktarım için aralık seçenekleri sunar. [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) sınıfının aşağıdaki özellikleri vardır.

- [**ExportRangeToJsonOptions.exportAsString**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#exportAsString--): Bu, hücrelerin dize değerlerini JSON'a dışa aktarır.
- [**ExportRangeToJsonOptions.hasHeaderRow**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#hasHeaderRow--): Bu, aralığın başlık satırı içerip içermediğini belirtir.
- [**ExportRangeToJsonOptions.indent**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/#indent--): Girintiyi gösterir.

[**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) sınıfı, JSON'u [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) sınıfıyla belirlenen dışa aktarma seçeneklerini kullanarak dışa aktarır.

Aşağıdaki kod örneği, [kaynak CSV dosyasını](104398879.csv) yüklemek için [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/javascript-cpp/exportrangetojsonoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/javascript-cpp/jsonutility/) sınıflarını kullanmayı ve JSON çıkışını konsolda yazdırmayı göstermektedir.

### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Export CSV Range to JSON Example</title>
    </head>
    <body>
        <h1>Export CSV Range to JSON Example</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Export to JSON</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFormat, JsonSaveOptions, JsonUtility } = AsposeCells;

        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            runButton.disabled = false;
        });

        function escapeHtml(unsafe) {
            return unsafe
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            downloadLink.href = '';
            downloadLink.textContent = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const loadOptions = new LoadOptions(LoadFormat.Csv);
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            const worksheet = workbook.worksheets.get(0);
            const lastCell = worksheet.cells.lastCell;

            const jsonSaveOptions = new JsonSaveOptions();
            const range = worksheet.cells.createRange(0, 0, lastCell.row + 1, lastCell.column + 1);
            const data = JsonUtility.exportRangeToJson(range, jsonSaveOptions);

            // Display JSON in the result div
            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully!</p><pre>' + escapeHtml(data) + '</pre>';

            // Create a downloadable JSON file
            const blob = new Blob([data], { type: 'application/json' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'exported_range.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';
        });
    </script>
</html>
```

### **Konsol Çıktısı**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
