---
title: JavaScript kullanarak Dosya Birleştirme ile C++
linktitle: Dosyaları Birleştirme
type: docs
weight: 20
url: /tr/javascript-cpp/merge-files/
---

## **Giriş**

Aspose.Cells, dosya birleştirme için farklı yollar sunar. Veri, biçimlendirme ve formüller içeren basit dosyalar için [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) yöntemi birkaç çalışma kitabını birleştirmek; ve [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-) yöntemi, çalışma sayfalarını yeni bir çalışma kitabına kopyalamak için kullanılabilir. Bu yöntemler kullanımı kolay ve etkilidir, ancak çok sayıda dosya birleştiriyorsanız, sistem kaynaklarınızın yoğun kullanıldığını fark edebilirsiniz. Bunu önlemek için, birkaç dosyayı birleştirmenin daha verimli yolu olan [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-) statik yöntemini kullanın.

## **C++ kullanarak Aspose.Cells for JavaScript ile Dosya Birleştirme**

Aşağıdaki örnek kod, büyük dosyaları [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-) yöntemi ile birleştirme yöntemini gösterir. İki basit ve büyük dosya olan Book1.xls ve Book2.xls kullanır. Dosyalar sadece biçimlendirilmiş veri ve formüller içerir.

{{% alert color="primary" %}}

Metod yalnızca veri, stiller, biçimlendirme ve formülleri birleştirmeyi destekler. Grafikler, resimler, yorumlar veya diğer nesneler gibi objeler, bu yöntemi kullanarak birleştirilmeyebilir. Ayrıca, işlem için geçici verileri saklamak için önbellek dosyası kullanılır.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Excel Files and Rename Sheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" multiple />
        <button id="runExample">Merge and Rename Sheets</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length || fileInput.files.length < 2) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least two Excel files to merge.</p>';
                return;
            }

            // Read selected files into Uint8Array array
            const files = [];
            for (let i = 0; i < fileInput.files.length; i++) {
                const file = fileInput.files[i];
                const arrayBuffer = await file.arrayBuffer();
                files.push(new Uint8Array(arrayBuffer));
            }

            // Create cacheFile name and destination name (virtual in browser)
            const cacheFile = "test.txt";
            const dest = "output.xlsx";

            // Call CellsHelper.mergeFiles with file byte arrays, cacheFile name and destination name
            // Note: In the browser environment mergeFiles is expected to accept file byte arrays and return merged file bytes.
            const mergedData = CellsHelper.mergeFiles(files, cacheFile, dest);

            // Log cacheFile as in original code
            console.log(cacheFile);

            // Load the merged workbook from returned bytes
            const workbook = new Workbook(new Uint8Array(mergedData));

            // Rename sheets sequentially starting at 1
            let i = 1;
            const worksheets = workbook.worksheets;
            for (let j = 0; j < worksheets.count; j++) {
                worksheets.get(j).name = `Sheet1${i}`;
                i++;
            }

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Merged and Renamed Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Files merged and sheets renamed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
