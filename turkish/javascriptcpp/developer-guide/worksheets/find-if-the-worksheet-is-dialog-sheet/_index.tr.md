---
title: JavaScript ile C++ kullanarak Çalışma Sayfasının Diyalog Sayfası olup olmadığını bulun
linktitle: Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma
type: docs
weight: 90
url: /tr/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Bu makale, C++ ile Aspose.Cells for JavaScript kullanarak programlı olarak bir Excel çalışma sayfasının Diyalog Sayfası olup olmadığını belirlemek için talimatlar ve örnek kodlar sağlar.
keywords: C++ ile JavaScript kullanarak Excel çalışma sayfası diyaloğu türünü bulun, Diyalog JavaScript ile C++
---

## **Olası Kullanım Senaryoları**

Diyalog Sayfası, bir diyalog kutusu içeren eski format bir sayfadır. Bu tür sayfa, eski Microsoft Excel sürümleri (örneğin 2003) tarafından eklenebilir ve ekran görüntüsüyle gösterilir. Ayrıca, yeni sürümlerde VBA kullanılarak da eklenebilir (örneğin Microsoft Excel 2016).

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

 Sayfanın diyalog sayfası veya başka bir türde olup olmadığını [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) özelliği ile Aspose.Cells for JavaScript kullanarak C++ ile bulabilirsiniz. Eğer dönen değer [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype) ise, bu durumda diyalog sayfasıyla ilgilendiğiniz anlamına gelir.

## **Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma**

Aşağıdaki örnek kod, diyalog sayfası içeren [örnek Excel dosyasını](64716820.xlsx) yükler. [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) özelliğini kontrol eder, [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype) ile karşılaştırır ve mesajı yazdırır. Daha fazla yardım için aşağıdaki örnek kodun konsol çıktılarına bakabilirsiniz.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
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

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **Konsol Çıktısı**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
