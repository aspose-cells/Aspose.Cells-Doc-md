---
title: Farklı Sayfalar için Farklı Başlık ve Altbilgi ayarlama JavaScript ve C++ ile
linktitle: Farklı Sayfalar için Farklı Üstbilgi ve Altbilgileri Ayarlama
type: docs
weight: 35
url: /tr/javascript-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Bu makale, Excel çalışma sayfası Sayfa Düzeni nin başlık ve altbilgilerini programlı olarak ayarlamak için örnek kod sağlar. İlk, garsonlar ve çift sayfa için başlık ve altbilgileri ayarlama. Aspose.Cells for JavaScript ve C++ kullanarak.
keywords: Excel başlık ve altbilgi ayarlama ilk sayfa JavaScript ve C++ ile, diğer sayfalar JavaScript ve C++ ile
---

{{% alert color="primary" %}}

MS Excel, ilk sayfa, tekler ve çiftler sayfalar için farklı başlık ve altbilgi ayarlamayı 2007'den beri desteklemektedir.
Aspose.Cells for JavaScript ve C++ aynı özelliği destekler.

{{% /alert %}}

## **MS Excel'de Farklı Üstbilgi ve Altbilgiler Ayarlama**

**![Farklı Üstbilgi ve Altbilgiler Ayarlama](difpage.png)**

1. **Sayfa Düzeni > Başlık ve Alt Bilgi > Üstbilgi/Altbilgi**'ye tıklayın.
1. **Farklı Tek ve Çift Sayfalar** veya **Farklı ilk sayfa** seçeneklerini kontrol edin.
1. Farklı başlık ve altbilgileri girin.

## ** Farklı Başlık ve Altbilgi ayarlama Aspose.Cells for JavaScript ve C++ ile**

Aspose.Cells, Excel ile aynı davranışı sergiler.
1. [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffOddEven--) ve [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isHFDiffFirst--) bayraklarını ayarlar 
1. Farklı başlık ve altbilgileri girin.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Headers</title>
    </head>
    <body>
        <h1>PageSetup Headers Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Gets the setting of page setup for the first worksheet.
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Sets different odd and even pages
            pageSetup.isHFDiffOddEven = true;

            // Set center header (index 1) for odd pages
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[1] = "I am the header of the Odd page.";

            // Set center header (index 1) for even pages
            pageSetup.evenHeader = pageSetup.evenHeader || [];
            pageSetup.evenHeader[1] = "I am the header of the Even page.";

            // Sets different first page
            pageSetup.isHFDiffFirst = true;

            // Set center header (index 1) for first page
            pageSetup.firstPageHeader = pageSetup.firstPageHeader || [];
            pageSetup.firstPageHeader[1] = "I am the header of the First page.";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page setup headers updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
