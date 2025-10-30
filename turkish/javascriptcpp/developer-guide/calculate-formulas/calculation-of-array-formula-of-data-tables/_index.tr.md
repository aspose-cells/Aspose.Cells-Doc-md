---
title: JavaScript aracılığıyla C++ ile Veri Tablolarının Dizi Formülünü Hesaplama
linktitle: Veri Tablolarının Dizilerini Hesaplama
description: Aspose.Cells kütüphanesini kullanarak JavaScript aracılığıyla C++ ile Microsoft Excel de veri tablosu için dizi formüllerini nasıl hesaplayacağınızı gösterir. Bir Excel dosyasını yükleyin veya oluşturun, dizi formülünü hesaplayın ve değiştirilen dosyayı kaydedin.
keywords: Aspose.Cells, Excel, veri tabloları, dizi formülleri, hesaplamalar JavaScript aracılığıyla C++
type: docs
weight: 70
url: /tr/javascript-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Microsoft Excel'de Veri > Varsayılan Analiz > Veri Tablosu.... kullanarak bir Veri Tablosu oluşturabilirsiniz. Aspose.Cells artık veri tablosunun dizi formüllerini hesaplamanıza izin veriyor. Herhangi bir formülü hesaplamak için normalde [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) kullanın.

{{% /alert %}}

Aşağıdaki örnek kodda, [kaynak excel dosyası](5115535.xlsx)'ı kullandık. Eğer B1 hücresinin değerini 100 olarak değiştirirseniz, Sarı renkle doldurulan Veri Tablosu değerleri 120 olarak değişir ve [çıktı PDF'sini](5115538.pdf) oluşturur. Daha fazla bilgi için yorumları okuyunuz.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>DataTable Calculation Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
            const cell = worksheet.cells.get("B1");
            cell.putValue(100);

            // Calculate formula, now it also calculates Data Table array formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
