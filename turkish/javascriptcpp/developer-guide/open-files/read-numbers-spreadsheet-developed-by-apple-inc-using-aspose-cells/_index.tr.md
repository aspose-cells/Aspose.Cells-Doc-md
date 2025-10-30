---
title: Aspose.Cells for JavaScript kullanarak Apple Inc. tarafından geliştirilmiş Numbers Elektronik Tablosu Oku
linktitle: Aspose.Cells tarafından geliştirilen Numbers Elektronik Tablo Uygulamasını Oku ve Apple Inc. tarafından geliştirildi.
type: docs
weight: 140
url: /tr/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Apple Inc. tarafından geliştirilen Numbers elektronik tablosunu Aspose.Cells for JavaScript kullanarak nasıl okunacağını öğrenin. 
---

## **Olası Kullanım Senaryoları**

Numbers, Apple Inc. tarafından geliştirilen bir elektronik tablo uygulamasıdır. Aspose.Cells, Numbers tablolarını okuyabilir, fakat yazma desteği yoktur. Numbers tablolarının Veri, Stil ve Formüllerini okuyabilir.

## ** Apple Inc. tarafından geliştirilen Numbers elektronik tablosunu Aspose.Cells for JavaScript kullanarak okutun**

Aşağıdaki örnek kod, [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) dosyasını yükler ve onu [Output PDF Format](outputNumbersByAppleInc.pdf) biçimine dönüştürür. Başarılı yükleme için [**LoadOptions**](https://reference.aspose.com/cells/javascript-cpp/loadoptions) sınıfını kullanmalı ve yapıcısında [**LoadFormat.Numbers**](https://reference.aspose.com/cells/javascript-cpp/loadformat) parametresini belirtmelisiniz. İki dosyayı da verilen bağlantılardan indirmeniz gerekir. Kodu herhangi bir Numbers elektronik tablosu ile deneyebilirsiniz. Daha fazla yardım için kodun yorumlarını okuyun.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Numbers to PDF Example</title>
    </head>
    <body>
        <h1>Convert Apple Numbers to PDF</h1>
        <input type="file" id="fileInput" accept=".numbers" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .numbers file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Specify load options to load Numbers spreadsheet
            const opts = new LoadOptions(LoadFormat.Numbers);

            // Load the Numbers spreadsheet in workbook with above load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save the workbook to PDF format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputNumbersByAppleInc.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
