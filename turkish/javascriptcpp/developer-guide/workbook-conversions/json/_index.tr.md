---
title: Javascript ile C++ aracılığıyla JSON ile JavaScript kullanarak
linktitle: Json
type: docs
weight: 300
url: /tr/javascript-cpp/convert-workbook-to-json/
description: Excel Çalışma Kitabını JSON a dönüştürmeyi Aspose.Cells for JavaScript ile C++ kullanarak nasıl yapacağınızı öğrenin.
---

{{% alert color="primary" %}}
Aspose.Cells, bir çalışma kitabını Json (JavaScript Nesne Notasyonu) dosyasına dönüştürmeyi destekler.
{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Aspose.Cells API, elektronik tabloyu JSON formatına dönüştürmeyi destekler. Çalışma kitabını JSON'a aktarmak için, [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat) parametresini [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) metodunun ikinci parametresi olarak geçirin. Ayrıca, JSON'a dışa aktarım ayarlarını belirlemek için [**JsonSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonsaveoptions) sınıfını kullanabilirsiniz.

Aşağıdaki kod örneği, aktif çalışma sayfasını JSON'a dışa aktarmayı, [**SaveFormat.Json**](https://reference.aspose.com/cells/javascript-cpp/saveformat/#json) enum üyesi kullanarak gösterir. Lütfen kaynak dosya (book1.xlsx) ve kod tarafından üretilen çıktı Json dosyası (book1.Json) arasındaki dönüşüm örneğine bakın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Workbook to JSON</title>
    </head>
    <body>
        <h1>Convert Workbook to JSON Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to JSON</button>
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

            // Save workbook as JSON
            const outputData = workbook.save(SaveFormat.Json);
            const blob = new Blob([outputData], { type: 'application/json' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.json';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download JSON File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook converted to JSON successfully! Click the download link to get the JSON file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [CSV'yi JSON'a dönüştür](/cells/tr/javascript-cpp/convert-csv-to-json/)
- [Excel'i JSON'a dönüştür](/cells/tr/javascript-cpp/convert-excel-to-json/)
- [JSON'ı CSV'ye dönüştür](/cells/tr/javascript-cpp/convert-json-to-csv/)
- [JSON'ı Excel'e dönüştür](/cells/tr/javascript-cpp/convert-json-to-excel/)
