---
title: Excel de Dondurulmuş Durumu JavaScript kullanarak ve C++ olmadan nasıl kontrol edilir
linktitle: Dondurulmuş Durum
type: docs
weight: 190
url: /tr/javascript-cpp/how-to-check-frozen-state-of-excel-worksheet
description: Bu yazıda, JavaScript ve C++ kütüphanesi kullanarak bir Excel çalışma sayfasının dondurulmuş durumunu programatik olarak nasıl kontrol edeceğinizi öğrenacaksınız.
---

## **Giriş**

Bu makalede, bir Excel çalışma sayfasının programatik olarak dondurulma durumunu nasıl kontrol edeceğimizi öğreneceğiz. MS Excel'de çalışma sayfasının donuk veya bölünmüş olup olmadığını basitçe bulabiliriz. Ama JavaScript ile dondurulmuş mu yoksa bölünmüş mü olduğunu bulmanın bir yolu var mı? Bunu basitçe C++ ve Aspose.Cells for JavaScript kullanarak yapabiliriz.

## **Pencereler Dondurulmuş mu**
C++ ile Aspose.Cells for JavaScript kullanarak pencerenin dondurulup ılmadığını ve hangi satır ve sütunların kilitlendiğini kontrol edebiliriz.

Lütfen pencere panolarının durumunu kontrol etmek ve kilitli satır ve sütunları almak için [**Worksheet.paneState**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#paneState--) özelliğini, ve [**Worksheet.freezedPanes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezedPanes--) özelliğini kullanın.
1. Dosyayı açmak için Workbook'u oluşturun.
2. Çalışma sayfasının dondurulup dondurulmadığını kontrol edin.
3. Kilitli satır ve sütunları alın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check Frozen Panes Example</title>
    </head>
    <body>
        <h1>Check Frozen Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PaneStateType, Utils } = AsposeCells;

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

            // Loading the workbook which contains frozen panes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Check whether worksheet is frozen.
            const paneState = sheet.paneState;
            if (paneState === PaneStateType.Frozen || paneState === PaneStateType.FrozenSplit) {
                // Gets locked rows and columns.
                const panes = sheet.freezedPanes;
                let html = '<p style="color: green;">Worksheet has frozen panes. Details:</p><ul>';
                panes.forEach((value) => {
                    const row = value[0];
                    const column = value[1];
                    const rows = value[2];
                    const columns = value[3];
                    html += `<li>row: ${row}, column: ${column}, rows: ${rows}, columns: ${columns}</li>`;
                });
                html += '</ul>';
                document.getElementById('result').innerHTML = html;
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is not frozen.</p>';
            }
        });
    </script>
</html>
```
