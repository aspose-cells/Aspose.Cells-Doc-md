---
title: JavaScript ile C++ aracılığıyla şablon dosyasından çalışma kitabı yüklerken veri türünü filtreleme
linktitle: Şablon dosyasından çalışma kitabını yüklerken veri türünü filtreleme
type: docs
weight: 400
url: /tr/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}
B sometimes, şablon dosyasından çalışma kitabını oluştururken hangi tür verilerin yükleneceğini belirtmek isteyebilirsiniz. Yüklenen veriyi filtrelemek, özellikle [LightCells API'leri](/cells/tr/javascript-cpp/using-lightcells-api/) kullanırken performansı artırabilir. Bu amaçla [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) özelliğini kullanın.
{{% /alert %}}

Aşağıdaki örnek kod, yükleme sırasında yalnızca şekil nesnelerini yükleyen ve indirilebilecek [şablon dosyasından](5115552.xlsx) yükler. Aşağıdaki ekran görüntüsü, [şablon dosyasını](5115552.xlsx) gösterir ve Kırmızı renk ve Sarı arka plan içeren verilerin yüklenmeyeceğini açıklar; çünkü [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) özelliği [**Shape**](https://reference.aspose.com/cells/javascript-cpp/shape/) olarak ayarlanmıştır.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Aşağıdaki ekran görüntüsü, verilerin kırmızı renkli ve sarı arka planlı olmadığını, ancak tüm şekillerin olduğunu gösterir.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Set the load options, we only want to load shapes and do not want to load data
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Create workbook object from uploaded excel file using load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleFilterChars_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
