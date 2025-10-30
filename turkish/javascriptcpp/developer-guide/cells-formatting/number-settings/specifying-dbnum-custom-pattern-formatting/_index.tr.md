---
title: DBNum Özel Desen Biçimlendirmesi Belirt
linktitle: DBNum Özel Desen Biçimlendirmesi Belirt
description: Aspose.Cells, C++ üzerinden JavaScript için bir kütüphane olup, özel biçimlendirme desenleri kullanarak tarihleri ve sayıları biçimlendirmeye olanak tanır. Bu makale, sayı görüntüleme üzerinde daha iyi kontrol sağlamak için dbnum özel biçim desenini nasıl belirleyeceğinizi gösterir.
keywords: Aspose.Cells, JavaScript via C++, elektronik elektronik tablo, özel biçim deseni, biçimlendirme, dbnum , görüntüleme kontrolü
type: docs
weight: 110
url: /tr/javascript-cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for JavaScript kullanarak C++ *DBNum* özel desen biçimlendirmeyi destekler. Örneğin, hücre değeri 123 ise ve özel biçimlendirmeyi [DBNum2][$-804]General olarak belirtirseniz, 壹佰贰拾叁 olarak görüntülenir. Hücrenin özel biçimlendirmesini [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) ve [**Style.custom(string)**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) yöntemiyle belirleyebilirsiniz.

## **Örnek Kod**

Aşağıdaki örnek kod, *DBNum* özel desen biçimlendirmeyi nasıl belirleyeceğinizi gösterir. Daha fazla yardım için [çıktı PDF](43352081.pdf) dosyasına bakınız.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - DBNum Custom Formatting Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Access cell A1 and put value 123.
            const cell = ws.cells.get("A1");
            cell.value = 123;

            // Access cell style.
            const st = cell.style;

            // Specifying DBNum custom pattern formatting.
            st.custom = "[DBNum2][$-804]General";

            // Set the cell style.
            cell.style = st;

            // Set the first column width.
            ws.cells.columns.get(0).width = 30;

            // Save the workbook in output pdf format.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDBNumCustomFormatting.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
