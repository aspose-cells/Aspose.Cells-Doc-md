---
title: JavaScript ve C++ kullanarak Çalışma Sayfası için Özelleştirilmiş Kağıt Boyutu Uygula
linktitle: Otomatik Olarak Çalışma Sayfası Kağıt Boyutunun Oluşturulması için Özelleştirilmiş Kağıt Boyutunun Uygulanması
type: docs
weight: 70
url: /tr/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Bu makale, JavaScript API sini C++ üzerinden kullanarak, bir Excel dosyasını PDF formatına dönüştürürken istenilen sayfalar için özelleştirilmiş kağıt boyutu ayarlamanın nasıl yapılacağını açıklar.
keywords: Excel i PDF ye dönüştürürken özel kağıt boyutu ayarla C++ üzerinden JavaScript ile
---

## **Olası Kullanım Senaryoları**  

MS Excel'de doğrudan özel kağıt boyutları oluşturmak için bir seçenek olmamasına rağmen, Excel dosyasını PDF'ye dönüştürürken istediğiniz çalışma sayfalarının özel kağıt boyutunu ayarlayabilirsiniz. Bu belge, Aspose.Cells API'leri kullanarak çalışma sayfasının özel kağıt boyutunun nasıl ayarlanacağını açıklar.  

## **Otomatik Olarak Çalışma Sayfası için Özel Kağıt Boyutunun Uygulanması**  

Aspose.Cells, çalışma sayfasının istediğiniz kağıt boyutunu uygulamanıza olanak tanır. [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-) metodunu kullanarak özel bir sayfa boyutu belirtebilirsiniz. Aşağıdaki örnek kod, çalışma kitabının ilk çalışma sayfası için özel bir kağıt boyutunun nasıl belirtileceğini gösterir. Ayrıca, aşağıdaki kodla oluşturulan [çıktı PDF](45056028.pdf) örneği de referans alınabilir.  

## **Ekran Görüntüsü**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
