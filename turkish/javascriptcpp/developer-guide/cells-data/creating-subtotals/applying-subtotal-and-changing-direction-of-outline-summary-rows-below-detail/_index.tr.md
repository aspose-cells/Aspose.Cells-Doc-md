---
title: Alt Detay Altında Toplam Uygulama ve Özet Satırların Yönünü Değiştirme
type: docs
weight: 100
url: /tr/javascript-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Özet satırlarını alt toplam uygulama ve Outline özeti Satırlarının yönünü değiştirme hakkında bilgi edinin, aşağıdaki Detay alanını kullanarak Aspose.Cells for JavaScript via C++ API.
keywords: Alt detay altında toplam uygulama, toplam ekleme, özet detay altında özet satırların yönünü değiştirme, özet detay altında özet sütunlarını sağa değiştirme, toplam oluşturma ve özet detay altında özet satırlarının yönünü değiştirme
---

{{% alert color="primary" %}}

Bu makale, verilere toplam uygulamanın nasıl yapılacağını ve özet detay altında yönün nasıl değiştirileceğini açıklayacaktır.

Verilere [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-boolean-boolean-boolean-) yöntemini kullanarak toplam uygulayabilirsiniz. Aşağıdaki parametreleri alır.

- **CellArea** - Toplam uygulanacak aralık
- **GroupBy** - Sıfıra dayalı bir tamsayı kaydırmak için alan
- **Function** - Toplam işlevi
- **TotalList** - Toplam eklenen sıfıra dayalı alan kaydırmaları dizisi
- **Replace** - Mevcut toplamı değiştirip değiştirmeyeceğini gösterir
- **PageBreaks** - Gruplar arasına sayfa sonu ekleyip eklemediğini gösterir
- **SummaryBelowData** - Verilerin altına özet ekleyip eklemediğini gösterir

Ayrıca, Şekil5'te gösterildiği gibi Çalışsayı.Outline.SummaryRowBelow özelliğini kullanarak Özet satırların altındaki detay yönünü kontrol edebilirsiniz. Bu ayarı **Veri > Özet > Ayarlar** kullanarak Microsoft Excel'de açabilirsiniz.

![todo:image_alt_text](1.png)

{{% /alert %}}

## Kaynak ve çıktı dosyalarının görüntüleri

Aşağıdaki ekran görüntüsü, aşağıda yer alan örnek kodda kullanılan kaynak Excel dosyasını göstermektedir ve içinde A ve B sütunlarında bazı veriler içermektedir.

![todo:image_alt_text](2.png)

Aşağıdaki ekran görüntüsü, örnek kod tarafından oluşturulan çıktı Excel dosyasını göstermektedir. Görebileceğiniz gibi, toplam A2:B11 aralığına uygulanmış ve özetin yönü detayın altında bulunmaktadır.

![todo:image_alt_text](3.png)

## JavaScript ile alt toplamlar uygulama ve outline özet satırlarının yönünü değiştirme



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Subtotal Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ConsolidationFunction, Utils } = AsposeCells;

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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the Cells collection in the first worksheet
            const cells = worksheet.cells;

            // Create a cellarea i.e., A2:B11
            const ca = CellArea.createCellArea("A2", "B11");

            // Apply subtotal, the consolidation function is Sum and it will applied to Second column (B) in the list
            cells.subtotal(ca, 0, ConsolidationFunction.Sum, [1], true, false, true);

            // Set the direction of outline summary
            worksheet.outline.summaryRowBelow = true;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
