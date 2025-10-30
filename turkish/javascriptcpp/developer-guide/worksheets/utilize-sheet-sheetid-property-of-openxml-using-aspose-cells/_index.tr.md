---
title: OpenXml in Sheet.SheetId özelliğini Aspose.Cells for JavaScript ile C++ kullanarak kullanın
linktitle: Aspose.Cells Kullanarak OpenXml in Sayfa Kimliği Özelliğini Kullanın
type: docs
weight: 200
url: /tr/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Bu makale, C++ kullanılarak Excel manipülasyonu ile OpenXml in Sheet.SheetId özelliğinin nasıl kullanılacağını Aspose.Cells for JavaScript aracılığıyla gösterir.
keywords: openxml JavaScript sheet id özelliği C++ ile, C++ ile Excel çalışma sayfası JavaScript sheet id
---

## **Olası Kullanım Senaryoları**

*Sheet.SheetId* özelliği *DocumentFormat.OpenXml.Spreadsheet* modülü içinde mevcuttur ve OpenXml'in bir parçasıdır. Bu özelliği ve değerini *workbook.xml* içinde aşağıdaki ekran görüntüsünde görebilirsiniz. Aspose.Cells, karşılık gelen özelliği [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--) olarak sağlar.

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **OpenXml'in Sheet.SheetId özelliğini Aspose.Cells for JavaScript kullanarak C++ ile kullanın**

Aşağıdaki örnek kod, [örnek Excel dosyasını](51740716.xlsx) yükler, Sayfa veya Sekme Kimliğini okur, ardından yeni Sekme Kimliğini atar ve [çıktı Excel dosyası](51740717.xlsx) olarak kaydeder. Ayrıca, aşağıda verilen kodun konsol çıktısını da inceleyin.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **Konsol Çıktısı**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
