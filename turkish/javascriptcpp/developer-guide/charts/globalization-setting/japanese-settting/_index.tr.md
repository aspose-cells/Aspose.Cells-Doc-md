---
title: Japon bölgesi için Grafik Dönüştürme için JavaScript ile C++ kullanımı
description: C++ ile Aspose.Cells for JavaScript kullanarak grafiklerinizde Japon yapılandırmasını nasıl ayarlayacağınızı öğrenin. Rehberimiz, grafiklerin Japon karakterleri ve biçimlendirmeyi destekleyecek şekilde yapılandırılmasını gösterecek, bu da yazı tipleri, boyut, metin yönü ve daha fazlasını içerecek.  
keywords: Aspose.Cells for JavaScript ile C++, Grafikler, Japon yapılandırması, yazı tipi, yazı tipi boyutu, metin yönü, destek.  
linktitle: Japon Bölgesi Belirle  
type: docs  
weight: 10  
url: /tr/javascript-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/javascript-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
Bu konuda, bir grafik için Japon Bölgesi nasıl belirleneceğini göstereceğiz.  
{{% /alert %}}  

## **Bir miras sınıfı tanımlar**  

İlk adım olarak, [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/chartglobalizationsettings/) sınıfından türeyen "ChartJapaneseSettings" adında bir sınıf tanımlamanız gerekir.  
Ardından ilgili işlevleri yeniden yazarak grafik öğelerinin metnini kendi dilinize göre belirleyebilirsiniz.  
Kod örneği:  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Chart Globalization - Japanese Example</h1>
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

        // Converted class from JavaScript to browser-compatible JavaScript
        class ChartJapaneseSettings extends AsposeCells.ChartGlobalizationSettings {
            constructor() {
                super();
                // Parameterless getters converted to properties
                this.axisTitleName = "軸タイトル";
                this.chartTitleName = "グラフ タイトル";
                this.legendDecreaseName = "削減";
                this.legendIncreaseName = "ぞうか";
                this.legendTotalName = "すべての";
                this.otherName = "その他";
                this.seriesName = "シリーズ";
            }

            // Getter with parameter converted to a method with lowercase first letter (no 'get' prefix)
            axisUnitName(type) {
                switch (type) {
                    case AsposeCells.DisplayUnitType.None:
                        return '';
                    case AsposeCells.DisplayUnitType.Hundreds:
                        return "百";
                    case AsposeCells.DisplayUnitType.Thousands:
                        return "千";
                    case AsposeCells.DisplayUnitType.TenThousands:
                        return "万";
                    case AsposeCells.DisplayUnitType.HundredThousands:
                        return "10万";
                    case AsposeCells.DisplayUnitType.Millions:
                        return "百万";
                    case AsposeCells.DisplayUnitType.TenMillions:
                        return "千万";
                    case AsposeCells.DisplayUnitType.HundredMillions:
                        return "億";
                    case AsposeCells.DisplayUnitType.Billions:
                        return "10億";
                    case AsposeCells.DisplayUnitType.Trillions:
                        return "兆";
                    default:
                        return '';
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (optional for this demo).</p>';
                return;
            }

            // No try-catch per instructions; let errors propagate
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Example usage: instantiate the ChartJapaneseSettings and demonstrate properties/methods
            const settings = new ChartJapaneseSettings();

            // Example: show axis title name and chart title name and a sample axis unit name
            const axisTitle = settings.axisTitleName;
            const chartTitle = settings.chartTitleName;
            const sampleUnit = settings.axisUnitName(AsposeCells.DisplayUnitType.Thousands);

            document.getElementById('result').innerHTML = `
                <p><strong>axisTitleName:</strong> ${axisTitle}</p>
                <p><strong>chartTitleName:</strong> ${chartTitle}</p>
                <p><strong>axisUnitName(DisplayUnitType.Thousands):</strong> ${sampleUnit}</p>
                <p style="color: green;">ChartJapaneseSettings instantiated successfully.</p>
            `;

            // Additionally, demonstrate opening the provided file as a Workbook (no modifications)
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare a simple save to allow downloading the opened file back (unchanged)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```  

## **Grafik için Japon Yapılandırmasını Yapın**  

Bu adımda, önceki adımda tanımladığınız "ChartJapaneseSettings" sınıfını kullanacaksınız.  
Kod örneği:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Chart to Image</title>
    </head>
    <body>
        <h1>Chart to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils, ChartJapaneseSettings } = AsposeCells;

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

            // Apply Japanese chart settings
            workbook.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();

            // Access the first chart in the first worksheet
            const chart0 = workbook.worksheets.get(0).charts.get(0);

            // Convert chart to image (PNG)
            const imageData = chart0.toImage(SaveFormat.Png);
            const blob = new Blob([imageData], { type: 'image/png' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```

Ardından çıktı görüntüsünde etkiyi görebilirsiniz, grafikteki unsurlar ayarlarınıza göre yeniden oluşturulur.  

## **Sonuç**  

Bu örnekte, bir grafik için Japon Bölgesi belirlemezseniz, aşağıdaki grafik unsurları varsayılan dilde, yani İngilizce olarak oluşturulabilir.  
Yukarıdaki işlemden sonra, Japon Bölgesi ile çıktı grafik resmi alabiliriz.  

|**Desteklenen unsurlar**|**Bu örnekteki değer**|**İngilizce ortamındaki varsayılan değer**|  
| :- | :- | :- |  
|Eksen Başlığı Adı|軸タイトル|Eksen Başlığı|  
|Eksen Birimi Adı|百,千...|Yüz, Bin...|  
|Grafik Başlığı Adı|グラフ タイトル|Grafik Başlığı|  
|Legend Artış Adı|ぞうか|Artış|  
|Legend Azalma Adı|削減|Azalma|  
|Legend Total Adı|すべての|Toplam|  
|Diğer Adı|その他|Diğer|  
|Seri Adı|シリーズ|Seri|
