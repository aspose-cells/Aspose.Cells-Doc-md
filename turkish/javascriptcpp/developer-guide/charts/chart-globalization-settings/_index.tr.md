---
title: JavaScript ile C++ kullanarak ChartGlobalizationSettings Sınıfı ile Grafik Bileşeni için Farklı Bir Dil Ayarlama
linktitle: Farklı Dil için Grafik Bileşeni Olarak ChartGlobalizationSettings Sınıfını Kullanma
description: Aspose.Cells for JavaScript via C++ kullanarak ChartGlobalizationSettings sınıfını nasıl kullanacağınızı öğrenin ve grafik bileşenleri için farklı diller ayarlayın. Kılavuzumuz, grafik öğelerini, etiketleri ve efsaneleri nasıl yerelleştireceğinizi anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for JavaC++ ile Komut Dosyası, grafik çizimi, grafik küreselleştirme, diller, yerelleştirme, ChartGlobalizationSettings, öğeler, etiketler, efsaneler.
type: docs
weight: 2200
url: /tr/javascript-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Olası Kullanım Senaryoları**  

Aspose.Cells API'leri, kullanıcıların grafik bileşenlerini farklı dillere ayarlamak ve bir hesap tablosundaki Alt Toplamlar için özel etiketler belirlemek istedikleri durumları ele almak amacıyla [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) sınıfını ortaya çıkardı.  

## **ChartGlobalizationSettings Sınıfına Giriş**  

Şu anda, [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) sınıfı, farklı dillerdeki Eksen Başlığı adları, Eksen Birimi adları, Grafik Başlığı adları gibi, özelleştirilebilir 8 yöntemi sunar, ve bu yöntemler bir özel sınıfta geçersiz kılınabilir.  
1. [**ChartGlobalizationSettings.axisTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisTitleName--): Eksen için Başlık adını alır.  
1. [**ChartGlobalizationSettings.axisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#axisUnitName-displayunittype-): Eksen Birimi için Adı alır.  
1. [**ChartGlobalizationSettings.chartTitleName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#chartTitleName--): Grafik Başlığının adını alır.  
1. [**ChartGlobalizationSettings.legendDecreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendDecreaseName--): Efsane için Azalma adını alır.  
1. [**ChartGlobalizationSettings.legendIncreaseName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendIncreaseName--): Efsane için Artışın adını alır.  
1. [**ChartGlobalizationSettings.legendTotalName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#legendTotalName--): Efsane için Toplam adını alır.  
1. [**ChartGlobalizationSettings.otherName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#otherName--): Grafikte "Diğer" etiketlerinin adını alır.  
1. [**ChartGlobalizationSettings.seriesName**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/#seriesName--): Grafikteki Serilerin adını alır.  

### **Özel dil çevirisi**  
Burada, aşağıdaki verilere dayalı bir su dalgası grafiği oluşturacağız. Grafik bileşenlerinin adları, İngilizce olarak grafikte gösterilecektir. Grafik Başlığı, Efsane Artış/Azalma adları, Toplam adı ve Eksen Başlığı'nın Türkçe olarak nasıl gösterileceğini göstermek için bir Türkçe dil örneği kullanacağız.  

![todo:image_alt_text](sample.png)  

## **Örnek Kod**  
Aşağıdaki örnek kod, [örnek Excel dosyasını](waterfall.xlsx) yükler.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Chart Globalization Settings Example</title>
    </head>
    <body>
        <h1>Chart Globalization Settings Example (Turkey)</h1>
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

        // Define TurkeyChartGlobalizationSettings by converting getXxx methods to properties
        class TurkeyChartGlobalizationSettings extends AsposeCells.ChartGlobalizationSettings {
            constructor() {
                super();
                this.chartTitleName = "Grafik Başlığı"; // Chart Title
                this.legendIncreaseName = "Artış"; // Increase
                this.legendDecreaseName = "Düşüş"; // Decrease
                this.legendTotalName = "Toplam"; // Total
                this.axisTitleName = "Eksen Başlığı"; // Axis Title
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: let errors propagate
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set custom chartGlobalizationSettings (Turkey)
            workbook.settings.globalizationSettings.chartSettings = new TurkeyChartGlobalizationSettings();

            // Access the first worksheet and its charts
            const worksheet = workbook.worksheets.get(0);
            const chartCollection = worksheet.charts;
            const chart = chartCollection.get(0);

            // Calculate the chart
            chart.calculate();

            // Get the chart title text
            const title = chart.title;
            const titleText = title ? title.text : "(No Title)";

            // Prepare output messages
            const messages = [];
            messages.push('<p style="color: green;">Operation completed successfully!</p>');
            messages.push(`<p>Workbook chart title: ${titleText}</p>`);

            // Get legend labels and output them
            const legendEntriesLabels = chart.legend.legendLabels;
            if (legendEntriesLabels && legendEntriesLabels.forEach) {
                const legendItems = [];
                legendEntriesLabels.forEach(label => {
                    legendItems.push(`<li>${label}</li>`);
                });
                if (legendItems.length) {
                    messages.push('<p>Workbook chart legend:</p>');
                    messages.push(`<ul>${legendItems.join('')}</ul>`);
                } else {
                    messages.push('<p>(No legend labels found)</p>');
                }
            } else {
                messages.push('<p>(No legend or legend labels available)</p>');
            }

            // Save modified workbook to allow download (optional)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = messages.join('');
        });
    </script>
</html>
```  

Örneğin ürettiği çıktı  

Yukarıdaki örnek kodun konsol çıktısı budur.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}
