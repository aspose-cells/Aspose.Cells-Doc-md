---
title: JavaScript ile C++ kullanarak Aralıkların Hücre Adresini, Hücre Sayısını, Ofset Tüm Sütun ve Tüm Satır Uygulamasıyla alın
linktitle: Aralığın Adres Hücre Sayısı Ofset Tüm Sütun ve Tüm Sıra Sayısını Al
type: docs
weight: 330
url: /tr/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for JavaScript ile C++ Range nesnesi çeşitli yardımcı metodlar içerir ve kullanıcıların Excel Aralıklarıyla kolayca çalışmasını sağlar. Bu makale, Range nesnesinin aşağıdaki metod veya özelliklerinin kullanımını açıklar.

- **Adres**

Aralığın adresini alır.

- **Hücre Sayısı**

Aralıktaki tüm hücre sayısını alır.

- **Ofset**

Ofset ile aralığı alır.

- **Tüm Sütun**

Belirtilen aralığı içeren tüm sütunu (veya sütunları) temsil eden bir Range nesnesi alır.

- **Tüm Satır**

Belirtilen aralığı içeren tüm satırı (veya satırları) temsil eden bir Range nesnesi alır.

## **Aralığın Adresini, Hücre Sayısını, Kaydırmayı, Tüm Sütunu ve Tüm Satırı Al**
Aşağıda verilen örnek kod, yukarıda tartışılan yöntemlerin ve özelliklerin kullanımını açıklar. Referans için aşağıdaki kodun konsol çıktısını inceleyin.

## **Örnek Kod**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // This example creates ranges on a new empty workbook and prints info to the page.
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Create range A1:B3.
            console.log("Creating Range A1:B3\n");
            let rng = ws.cells.createRange("A1:B3");

            // Print range address and cell count.
            const lines = [];
            lines.push("Range Address: " + rng.address);
            lines.push("Range row Count: " + rng.rowCount);
            lines.push("Range column Count: " + rng.columnCount);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Create range A1.
            console.log("Creating Range A1\n");
            rng = ws.cells.createRange("A1");

            // Print range offset, entire column and entire row.
            lines.push("Offset: " + rng.offset(2, 2).address);
            lines.push("Entire Column: " + rng.entireColumn.address);
            lines.push("Entire Row: " + rng.entireRow.address);

            // Formatting console output.
            lines.push("----------------------");
            lines.push("");

            // Display results
            resultEl.innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

## **Konsol Çıktısı**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
