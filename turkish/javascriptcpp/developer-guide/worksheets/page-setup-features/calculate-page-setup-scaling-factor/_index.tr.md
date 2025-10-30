---
title: JavaScript kullanarak C++ ile Sayfa Ayarı Ölçeklendirme Faktörünü Hesapla
linktitle: Sayfa Ayarı Ölçek Faktörünü Hesaplayın
type: docs
weight: 300
url: /tr/javascript-cpp/calculate-page-setup-scaling-factor/
description: Bu makale, C++ kullanarak JavaScript API sini nasıl kullanacağınızı, Excel çalışma sayfasındaki Fit to n sayfa genişliği ve m yüksekliğinde seçeneklerini programlı olarak kullanarak Sayfa Ayarı ölçeklendirme faktörünü hesaplamayı açıklayan örnek kodlar sağlar.
keywords: Excel JavaScript ile m yüksekliğinde n sayfaya sığdırmak, sayfa ayarını ölçeklendirme faktörünü C++ ile hesapla
---

{{% alert color="primary" %}}

Sayfa Ayarlarını kullanırken **N sayfa genişliğinde ve M sayfa yüksekliğinde** seçeneği, Microsoft Excel'in Sayfa Ayarlarını Hesaplama Faktörünü otomatik olarak hesaplar. Bunu [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--) özelliği kullanarak da yapabilirsiniz. Bu özellik bir çift değer döndürür ve yüzde değere dönüştürülebilir. Örneğin, döndürdüğü değer 0.5 ise, ölçekleme faktörü %50 anlamına gelir.

{{% /alert %}}

Aşağıdaki örnek kod, [**SheetRender.pageScale**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#pageScale--) özelliğini kullanarak sayfa ayarı ölçek faktörünü hesaplamanın örneklerini göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Scale</title>
    </head>
    <body>
        <h1>Page Scale Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, SheetRender, ImageOrPrintOptions, PaperSizeType, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put some data in these cells
            worksheet.cells.get("A4").putValue("Test");
            worksheet.cells.get("S4").putValue("Test");

            // Set paper size
            worksheet.pageSetup.paperSize = PaperSizeType.PaperA4;

            // Set fit to pages wide as 1
            worksheet.pageSetup.fitToPagesWide = 1;

            // Calculate page scale via sheet render
            const sr = new SheetRender(worksheet, new ImageOrPrintOptions());

            // Convert page scale double value to percentage
            const strPageScale = (sr.pageScale * 100).toFixed(0) + "%";

            // Write the page scale value
            document.getElementById('result').innerHTML = `<p>Page Scale: ${strPageScale}</p>`;
            console.log(strPageScale);
        });
    </script>
</html>
```
