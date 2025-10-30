---
title: Excel e Arka Plan Resmi Ekleme C++ aracılığıyla JavaScript kullanarak
linktitle: Excel e Arka Plan Görüntüsü Ekleme
type: docs
weight: 90
url: /tr/javascript-cpp/insert-background-image-to-excel/
description: "Excel e arka plan resmi nasıl eklenir? C++ aracılığıyla Aspose.Cells for JavaScript ile."
---

{{% alert color="primary" %}} 

Bir çalışma sayfasına resim ekleyerek çalışma sayfasını daha çekici hale getirebilirsiniz. Bu özellik, çalışma sayfasındaki verileri engellemeden arka plana hafif bir ipucu ekleyen özel bir kurumsal grafik veya resminiz varsa oldukça etkili olabilir. Aspose.Cells API'sini kullanarak bir sayfa için arka plan resmi ayarlayabilirsiniz.

{{% /alert %}} 

## **Microsoft Excel'de Sayfa Arka Planını Ayarlama**

Microsoft Excel'de bir sayfanın arka plan görüntüsünü ayarlamak için (örneğin, Microsoft Excel 2019 için):

1. **Sayfa Düzeni** menüsünden **Sayfa Ayarı** seçeneğini bulun ve ardından **Arka Plan** seçeneğine tıklayın.
1. Tablonun arka plan resmini ayarlamak için bir resim seçin.

   **Tablo arka planı ayarlama**

![todo:image_alt_text](insert-background-to-excel.jpg)

## ** Sayfa Arka Planını C++ aracılığıyla Aspose.Cells for JavaScript kullanarak ayarlama**

Aşağıdaki kod, bir akıştaki bir resim kullanarak arka plan resmini ayarlar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Worksheet Background Image</title>
    </head>
    <body>
        <h1>Set Worksheet Background Image Example</h1>
        <p>
            Select a background image to apply to a new workbook's first worksheet,
            then click "Apply Background & Save" to generate XLSX and HTML files.
        </p>
        <input type="file" id="bgInput" accept="image/*" />
        <button id="runExample">Apply Background & Save</button>
        <a id="downloadXlsx" style="display: none; margin-left: 10px;"></a>
        <a id="downloadHtml" style="display: none; margin-left: 10px;"></a>
        <div id="result" style="margin-top: 1em;"></div>
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
            const bgInput = document.getElementById('bgInput');
            const resultDiv = document.getElementById('result');

            if (!bgInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a background image file.</p>';
                return;
            }

            const bgFile = bgInput.files[0];
            const arrayBuffer = await bgFile.arrayBuffer();
            const imgBytes = new Uint8Array(arrayBuffer);

            // Create a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Set the background image for the worksheet.
            sheet.backgroundImage = imgBytes;

            // Save the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([xlsxData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadXlsx = document.getElementById('downloadXlsx');
            downloadXlsx.href = URL.createObjectURL(blobXlsx);
            downloadXlsx.download = 'outputBackImageSheet.xlsx';
            downloadXlsx.style.display = 'inline';
            downloadXlsx.textContent = 'Download Excel File';

            // Save the HTML file
            const htmlData = workbook.save(SaveFormat.Html);
            const blobHtml = new Blob([htmlData], { type: 'text/html' });
            const downloadHtml = document.getElementById('downloadHtml');
            downloadHtml.href = URL.createObjectURL(blobHtml);
            downloadHtml.download = 'outputBackImageSheet.html';
            downloadHtml.style.display = 'inline';
            downloadHtml.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Background image applied. Download links are ready.</p>';
        });
    </script>
</html>
```

## İlgili Makaleler

- [ODS Dosyalarında Arkaplanla Çalışma](/cells/tr/javascript-cpp/working-with-background-in-ods-files/)
