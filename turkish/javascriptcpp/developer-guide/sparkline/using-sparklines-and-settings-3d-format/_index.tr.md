---
title: JavaScript ile C++ kullanarak Sparkline ve 3D Format Ayarları
linktitle: Sparklines ve 3D Format Ayarlarını Kullanma
type: docs
weight: 40
url: /tr/javascript-cpp/using-sparklines-and-settings-3d-format/
description: Excel dosyalarında sparkline kullanmayı ve 3D biçimlendirmeyi nasıl uygulayacağınızı öğrenin, Aspose.Cells for JavaScript ile C++ kullanarak. 
---

## **Sparklines Kullanma**
Microsoft Excel 2010, bilgileri daha önce hiç olmadığı kadar fazla şekilde analiz etmenizi sağlar. Kullanıcıların yeni veri analiz ve görselleştirme araçlarıyla önemli veri eğilimlerini takip etmesine ve vurgulamasına izin verir. Sparklines, veriyi ve tabloyu aynı anda görüntüleyebileceğiniz mini grafiklerdir. Sparklines uygun şekilde kullanıldığında, veri analizi daha hızlı ve daha anlaşılır olur. Ayrıca, aşırı kalabalık çalışma tablolarını çok fazla meşgul grafiklerle önler. Onlar, aynı tabloda veriyi görmek için basit bir görünüm sağlar. Ayrıca, Aspose.Cells, elektronik tablolardaki sparklines'ı manipüle etmek için bir API sağlar.

C++ ile Aspose.Cells for JavaScript, elektronik tablolarındaki sparkline'ları manipüle etmek için bir API sağlar.
### **Microsoft Excel'de Sparklines Kullanma**
Microsoft Excel 2010'da Sparklines eklemek için:

1. Sparklines'ların görünmesini istediğiniz hücreleri seçin. Onları görüntülemeyi kolaylaştırmak için, verinin yanındaki hücreleri seçin.
1. Menü şeridinde **Ekle**'yi tıklayın, ardından **Sparklines** grubunda **Sütun**'u seçin.
1. Kaynak verinin bulunduğu çalışma sayfasındaki hücre aralığını seçin veya girin. Grafikler görünecektir.

Sparklines, örneğin, bir bayan voleybol ligi için kazanma veya kaybetme kaydını görmek için size yardımcı olur. Sparklines, ligdeki her takımın tüm sezonlarının toplamını dahi verebilir.
### **C++ ile Aspose.Cells for JavaScript kullanarak Sparkline**
Geliştiriciler, Aspose.Cells for JavaScript ile C++ kullanarak şablon dosyasında sparkline oluşturabilir, silebilir veya okuyabilir. Sparkline'ları yöneten sınıflar [SparklineGroupCollection](https://reference.aspose.com/cells/javascript-cpp/sparklinegroupcollection/) modülünde bulunur, bu yüzden bu özellikleri kullanmadan önce bu modülü dahil etmeniz gerekir.

Belirli bir veri aralığı için özel grafikler ekleyerek, geliştiriciler seçili hücre alanlarına farklı türde küçük grafikler eklemek özgürlüğüne sahiptir.

Aşağıdaki örnek, Sparklines özelliğini sergiler. Örnek, şunları gösterir:

1. Basit bir şablon dosyasını açın.
1. Bir çalışma sayfası için sparklines bilgilerini okuyun.
1. Belirli bir veri aralığı için yeni sparklines ekleyin.
1. Excel dosyasını diske kaydedin.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sparkline Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, SparklineType, Color } = AsposeCells;

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

            // Instantiate a Workbook by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Read the Sparklines from the worksheet (if any)
            const sparklinesCount = sheet.sparklineGroups.count;
            let logHtml = '';
            for (let i = 0; i < sparklinesCount; i++) {
                const group = sheet.sparklineGroups.get(i);
                logHtml += `sparkline group: type:${group.type}, sparkline items count:${group.sparklines.count}<br/>`;
                const sparklineCount = group.sparklines.count;
                for (let j = 0; j < sparklineCount; j++) {
                    const sparkline = group.sparklines.get(j);
                    logHtml += `sparkline: row:${sparkline.row}, col:${sparkline.column}, dataRange:${sparkline.dataRange}<br/>`;
                }
            }

            // Add Sparklines
            // Define the CellArea D2:D10 (rows and columns are zero-based: D is column 4 -> index 4)
            const ca = CellArea.createCellArea(1, 4, 7, 4);
            // Add new Sparklines for a data range to a cell area
            const idx = sheet.sparklineGroups.add(SparklineType.Column, "Sheet1!B2:D8", false, ca);
            const newGroup = sheet.sparklineGroups.get(idx);
            // Create CellsColor and set color
            const clr = workbook.createCellsColor();
            clr.color = Color.Orange;
            newGroup.seriesColor = clr;

            // Save the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><div>' + logHtml + '</div>';
        });
    </script>
</html>
```
## **3B Formatını Ayarlama**
3D grafik stillerine ihtiyaç duyabilirsiniz, böylece yalnızca sizin senaryonuza uygun sonuçları alırsınız. C++ ile Aspose.Cells for JavaScript, Microsoft Excel 2007'nin 3D biçimlendirmesini uygulamak için ilgili API'yi sağlar.

Aşağıda, bir grafik oluşturmayı ve Microsoft Excel 2007 3B biçimlendirmesini uygulamayı sergilemek için tam bir örnek verilmiştir. Örnek kodu çalıştırdıktan sonra bir sütun grafiği (3B efektleri ile) çalışma sayfasına eklenecektir.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>3D Chart Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ChartType, Color, BevelPresetType, PresetMaterialType, LightRigType } = AsposeCells;

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
            // Creating a new workbook
            const book = new Workbook();

            // Add a Data Worksheet
            const dataSheet = book.worksheets.add("DataSheet");

            // Add Chart Worksheet
            const sheet = book.worksheets.add("MyChart");

            // Put some values into the cells in the data worksheet
            dataSheet.cells.get("B1").value = 1;
            dataSheet.cells.get("B2").value = 2;
            dataSheet.cells.get("B3").value = 3;
            dataSheet.cells.get("A1").value = "A";
            dataSheet.cells.get("A2").value = "B";
            dataSheet.cells.get("A3").value = "C";

            // Define the Chart Collection
            const charts = sheet.charts;
            // Add a Column chart to the Chart Worksheet
            const chartSheetIdx = charts.add(ChartType.Column, 5, 0, 25, 15);

            // Get the newly added Chart
            const chart = book.worksheets.get(2).charts.get(0);

            // Set the background/foreground color for PlotArea/ChartArea
            chart.plotArea.area.backgroundColor = Color.White;
            chart.chartArea.area.backgroundColor = Color.White;
            chart.plotArea.area.foregroundColor = Color.White;
            chart.chartArea.area.foregroundColor = Color.White;

            // Hide the Legend
            chart.showLegend = false;

            // Add Data Series for the Chart
            chart.nSeries.add("DataSheet!B1:B3", true);
            // Specify the Category Data
            chart.nSeries.categoryData = "DataSheet!A1:A3";

            // Get the Data Series
            const ser = chart.nSeries.get(0);

            // Apply the 3-D formatting
            const spPr = ser.shapeProperties;
            const fmt3d = spPr.format3D;

            // Specify Bevel with its height/width
            const bevel = fmt3d.topBevel;
            bevel.type = BevelPresetType.Circle;
            bevel.height = 2;
            bevel.width = 5;

            // Specify Surface material type
            fmt3d.surfaceMaterialType = PresetMaterialType.WarmMatte;

            // Specify surface lighting type
            fmt3d.surfaceLightingType = LightRigType.ThreePoint;

            // Specify lighting angle
            fmt3d.lightingAngle = 20;

            // Specify Series background/foreground and line color
            ser.area.backgroundColor = Color.Maroon;
            ser.area.foregroundColor = Color.Maroon;
            ser.border.color = Color.Maroon;

            // Saving the modified Excel file and providing download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = '3d_format.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
