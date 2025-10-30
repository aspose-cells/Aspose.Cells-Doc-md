---
title: JavaScript ile C++ kullanarak 1904 Tarih Sistemini Uygula
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir JavaScript kütüphanesidir. 1904 tarih sisteminin uygulanmasını destekler, kullanıcıların 1 Ocak 1904 tarihine göre hesaplama ve biçimlendirme yapmasına olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak 1904 tarih sisteminin nasıl uygulanacağını açıklar.
keywords: Aspose.Cells, 1904 tarih sistemi, elektronik tablo, hesaplama, biçimlendirme, JavaScript via C++
type: docs
weight: 7000
url: /tr/javascript-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

Microsoft Excel, iki tarih sistemini destekler: 1900 tarih sistemi (Windows için Excel'de varsayılan tarih sistemi) ve 1904 tarih sistemi. 1904 tarih sistemi genellikle Macintosh Excel dosyalarıyla uyumluluğu sağlamak için kullanılır ve Mac için Excel kullanıyorsanız varsayılan sistemdir. 1904 tarih sistemini Excel dosyaları için {Aspose.Cells for Java} komut dosyası ile ayarlayabilirsiniz. 

{{% /alert %}} 

Microsoft Excel'de (örneğin, Microsoft Excel 2003) 1904 tarih sistemini uygulamak için:

1. **Araçlar** menüsünden **Seçenekler**'i seçin ve **Hesaplama** sekmesini seçin.
1. **1904 tarih sistemi** seçeneğini belirleyin.
1. **Tamam**'a tıklayın.

|**Microsoft Excel'de 1904 tarih sistemini seçme**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

Bunu, Aspose.Cells API'lerini kullanarak nasıl başarılır gösteren örnek kodu görün.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Enable 1904 Date System</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement 1904 date system
            workbook.settings.date1904 = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">1904 date system enabled. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
