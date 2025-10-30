---
title: Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın 
type: docs  
weight: 320  
url: /tr/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: AutoFilter’ı yeniledikten sonra tüm gizlenmiş satırların indekslerini almak için Aspose.Cells for JavaScript kullanmayı öğrenin, C++ API.  
keywords: AutoFilter’ı Yeniledikten Sonra Tüm Gizli Satırların İndekslerini Al JavaScript ve C++ ile, Tüm Gizli Satırları Yenileme Sonrası İndeksleri Al JavaScript ve C++ ile, AutoFilter yenileme sonrası tüm gizlenmiş satırların indekslerini al JavaScript ve C++ ile  
---

## **Olası Kullanım Senaryoları**  

Çalışma sayfası hücrelerine otomatik filtre uyguladığınızda, bazı satırlar otomatik olarak gizlenir. Ancak, bazı satırlar Excel kullanıcısı tarafından manuel olarak gizlenmiş olabilir ve otomatik filtre ile gizlenmemiş olabilir. Bu nedenle, otomatik filtrenin hangi satırları gizlediği ve hangilerinin manuel olarak gizlendiği hakkında bilgi sahibi olmak zordur. Aspose.Cells for JavaScript C++ kullanılarak, bu sorunu [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-) dizisi ile çözer. Bu yöntem, otomatik filtre tarafından gizlenen ve manuel olarak gizlenmeyen tüm satırların satır indekslerini döndürür.  

## **Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın**  

Lütfen aşağıdaki örnek kodu inceleyin; bu kod, bazı satırların Excel kullanıcıları tarafından manuel olarak gizlendiği [örnek Excel dosyasını](64716909.xlsx) yükler. Kod, otomatik filtre uygular ve `[**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-)` yöntemi kullanarak tüm gizlenmiş satırların satır dizinlerini döndürür. Ardından, gizlenmiş satırların dizinlerini, hücre isimleri ve değerleriyle birlikte konsola yazdırır.  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **Konsol Çıktısı**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
