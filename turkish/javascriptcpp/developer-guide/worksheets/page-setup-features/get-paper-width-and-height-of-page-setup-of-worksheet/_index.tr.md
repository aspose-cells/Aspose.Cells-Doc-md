---
title: Worksheet in Sayfa Kurulumu Kağıt Genişliği ve Yüksekliğini JavaScript ve C++ kullanarak alın
linktitle: Çalışma Sayfası Sayfa Ayarları Kağıt Genişliğini ve Yüksekliğini Alma
type: docs
weight: 50
url: /tr/javascript-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Excel Çalışma Sayfası Sayfa Kurulumu Kağıt Genişliği ve Yüksekliğini JavaScript ve C++ ile programlı olarak nasıl alacağınızı keşfedin.
keywords: Excel sayfa kurulumu kağıt genişliği JavaScript ve C++, Excel sayfa kurulumu kağıt yüksekliği JavaScript ve C++
---

## **Olası Kullanım Senaryoları**

Bazen, çalışma sayfasının sayfa kurulumu içinde ayarlanmış olan kağıt boyutunun genişliğini ve yüksekliğini bilmeniz gerekir. Bu amaçla [**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--) ve [**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--) özelliklerini kullanın.

## **Çalışma Sayfası Sayfa Ayarları Kağıt Genişliği ve Yüksekliğini Alma**

Aşağıdaki örnek kod, [**PageSetup.paperWidth**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperWidth--) ve [**PageSetup.paperHeight**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperHeight--) özelliklerinin kullanımını açıklar. Önce kağıt boyutunu *A2* olarak değiştirir, ardından kağıdın genişlik ve yüksekliğini bulur, sonra sırasıyla *A3*, *A4*, *Letter* yapar ve kağıdın genişlik ve yüksekliğini bulur.

### **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Paper Size Example</h1>
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

            // If a file is selected, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set paper size to A2 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA2;
            console.log("PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A3 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA3;
            console.log("PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to A4 and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
            console.log("PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            // Set paper size to Letter and print paper width and height in inches
            sheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperLetter;
            console.log("PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight);

            const outputLines = [
                "PaperA2: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA3: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperA4: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight,
                "PaperLetter: " + sheet.pageSetup.paperWidth + "x" + sheet.pageSetup.paperHeight
            ];

            document.getElementById('result').innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```

### **Konsol Çıktısı**



{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
