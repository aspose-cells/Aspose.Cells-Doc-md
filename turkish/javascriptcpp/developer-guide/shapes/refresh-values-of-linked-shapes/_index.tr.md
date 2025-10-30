---
title: Bağlantılı Şekillerin Değerlerini JavaScript C++ ile Yenile
linktitle: Bağlı Şekillerin Değerlerini Yenile
type: docs
weight: 3200
url: /tr/javascript-cpp/refresh-values-of-linked-shapes/
description: C++ ile Aspose.Cells for JavaScript kullanarak Excel deki bağlantılı şekillerin değerlerini nasıl yenileyeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bazen, Excel dosyanızda bir bağlantılı şekil bulunur ve bu şekil bazı hücrelere bağlıdır. Microsoft Excel'de, bağlı hücrenin değeri değiştirildiğinde bağlı şeklinin de değeri değişir. Ayrıca, bu Aspose.Cells for JavaScript ile C++ kullanarak XLS veya XLSX formatında dosyanızı kaydetmekle de çalışır. Ancak, dosyanızı PDF veya HTML formatında kaydetmek isterseniz, bağlı şeklin değerini yenilemek için [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) yöntemini çağırmanız gerekir.

{{% /alert %}}

## Örnek

Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodda kullanılan kaynak Excel dosyasını gösterir. Bu dosyada A1 ile E4 hücreleri arasında bağlantılı bir resim vardır. Aspose.Cells ile B4 hücresinin değerini değiştirecek ve ardından [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#updateSelectedValue--) metodunu çağırarak resmin değerini yenileyecek ve PDF formatında kaydedeceğiz.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Sağlanan bağlantılardan [ kaynak Excel dosyasını](95584291.xlsx) ve [çıktı PDF'sini](95584292.pdf) indirebilirsiniz.

### Bağlantılı şekillerin değerlerini yenilemek için JavaScript kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh Value Of Linked Shapes Example</title>
    </head>
    <body>
        <h1>Refresh Value Of Linked Shapes Example</h1>
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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Change the value of cell B4
            const cell = worksheet.cells.get("B4");
            cell.value = 100;

            // Update the value of the Linked Picture which is linked to cell B4
            worksheet.shapes.updateSelectedValue();

            // Save the workbook in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRefreshValueOfLinkedShapes.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
