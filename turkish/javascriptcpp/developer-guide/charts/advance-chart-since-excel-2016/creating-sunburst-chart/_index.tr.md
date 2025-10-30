---
title: JavaScript ile Sunburst grafiği nasıl oluşturulur (C++ aracılığıyla)
linktitle: Güneş patlaması grafiği nasıl oluşturulur
description: Aspose.Cells for JavaScript aracılığıyla JavaScript ile güneşpatlaması grafiği nasıl oluşturulur, veriyi bir daire içinde gösteren bir grafik. Kılavuzumuz grafik özellikleri ve biçimlendirmesi, veri etiketleri, lejantlar, renkler ve daha fazlasını yapılandırmanıza yardımcı olacak.
keywords: Aspose.Cells for JavaScript ile C++ aracılığıyla güneşpatlaması grafiği, oluşturma, özellikleri ayarlama, veri etiketleri, lejant, biçim, renk, daire, veri işleme.
type: docs
weight: 162
url: /tr/javascript-cpp/creating-sunburst-chart/
---

## **Olası Kullanım Senaryoları**
Ağaçharitası grafikleri, hiyerarşi içindeki oranları karşılaştırmak için iyidir; ancak, ağaçharitası grafikleri en büyük kategoriler ile her veri noktası arasındaki hiyerarşi seviyelerini gösterirken iyi değildir. Bunun yerine, güneş patlaması grafiği çok daha iyi bir görsel grafiktir. Güneş patlaması grafiği, hiyerarşik verileri göstermek için idealdir. Hiyerarşinin her seviyesi, en içteki daire hiyerarşinin en üstü olarak temsil edilen bir halka veya daireyle gösterilir. Hiyerarşik verisi olmayan (bir seviye kategorisi olan) güneş patlaması grafiği, bir halka dilimine benzer görünür. Ancak, birden fazla kategori seviyesiyle güneş patlaması grafiği, dış halkaların iç halkalara nasıl bağlı olduğunu gösterir. Güneş patlaması grafiği, bir halkanın nasıl katkıda bulunduğunu göstermek açısından en etkilidir; diğer hiyerarşik grafik türü olan ağaçharitası, göreceli boyutları karşılaştırmak için idealdir.

![todo:image_alt_text](sample.png)
## **Güneş Patlaması Grafiği**
Aşağıdaki kodu çalıştırdıktan sonra, aşağıdaki gibi Güneş patlaması grafiğini göreceksiniz.

![todo:image_alt_text](result.png)
## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](sunburst.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sunburst Chart Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sunburst Chart Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            const pieIdx = worksheet.charts.add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
            const chart = worksheet.charts.get(pieIdx);

            chart.showLegend = true;
            chart.title.text = "Sunburst Chart";
            chart.nSeries.add("D2:D16", true);
            chart.nSeries.categoryData = "A2:C16";
            chart.nSeries.get(0).dataLabels.showCategoryName = true;
            chart.plotArea.area.fillFormat.fillType = AsposeCells.FillType.None;

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sunburst chart created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
