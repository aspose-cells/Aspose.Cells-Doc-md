---
title: Microsoft Excel kullanarak OLE nesnesini otomatik yenilemek için Aspose.Cells for JavaScript kullanın.
linktitle: Aspose.Cells kullanarak Microsoft Excel üzerinden OLE nesnesini otomatik olarak yenileyin
type: docs
weight: 270
url: /tr/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Excel de OLE nesnelerini otomatik yenilemenin nasıl yapılacağını öğrenin, Aspose.Cells for JavaScript kullanarak C++ ile.
---

{{% alert color="primary" %}}  
Aspose.Cells, Microsoft Excel'de excel dosyası açıldığında OLE nesnesini yenilemek için [**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--) özelliğini sağlar. Bu özellik sayesinde OLE nesnesi, Microsoft Excel tarafından oluşturulan doğru OLE görüntüsünü gösterecektir.  
{{% /alert %}}  

Aşağıdaki örnek kod, gerçek dışı bir OLE görüntüsüne sahip olan [örnek excel dosyasını](5115231.xlsx) yükler. OLE nesnesi aslında bir Microsoft Word belgesidir ancak örnek excel dosyası, Microsoft Word görüntüsü yerine hayvan görüntüsünü göstermektedir. Ancak [çıktı excel dosyasını](5115225.xlsx) açarsanız, Microsoft Excel'in doğru OLE görüntüsünü gösterdiğini göreceksiniz.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh OLE Objects Example</title>
    </head>
    <body>
        <h1>Refresh OLE Objects Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set auto load property of first ole object to true
            sheet.oleObjects.get(0).autoLoad = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshOLEObjects_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">OLE object autoLoad set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
