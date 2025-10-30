---
title: Dropdownlist kullanarak Dinamik Grafik Oluşturma Nasıl Yapılır
linktitle: Dropdownlist ile Dinamik Grafik Nasıl Oluşturulur
description: Aspose.Cells for JavaScript ile C++ kullanarak, seçim listesine göre güncellenen dinamik grafik oluşturmayı öğrenin. Adım adım rehberimiz, grafiklerinize esnek veri görselleştirmesi için bir açılır liste entegre etmenizi gösterecek.
keywords: Aspose.Cells for JavaScript ile C++, Dinamik Grafik, Açılır Liste, Veri Görselleştirme, Entegrasyon, Esnek Görselleştirme.
type: docs
weight: 76
url: /tr/javascript-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Olası Kullanım Senaryoları**
Excel'de Açılır listede Dinamik Grafik, seçilen verilere göre dinamik olarak güncellenebilen etkileşimli grafikler oluşturmayı sağlayan güçlü bir araçtır. Bu özellik özellikle birden fazla veri setini analiz etme veya çeşitli senaryoları karşılaştırma ihtiyacı duyulan durumlarda kullanışlıdır.

Açılır listede Dinamik Grafik'in yaygın bir uygulaması finansal analizde gerçekleşir. Örneğin, bir şirket farklı yıllar veya departmanlar için birden fazla finansal veri setine sahip olabilir. Açılır listeden kullanıcılar istedikleri belirli veri setini seçebilirler ve grafik otomatik olarak ilgili bilgileri görüntülemek için güncellenir. Bu, kolay karşılaştırma ve trend veya desenlerin belirlenmesine olanak tanır.

Başka bir uygulama ise satış ve pazarlamada gerçekleşir. Bir şirket farklı ürünler veya bölgeler için satış verilerine sahip olabilir. Açılır listede Dinamik Grafik ile kullanıcılar belirli bir ürün veya bölge seçebilir ve grafik seçilen seçenek için satış performansını dinamik olarak güncelleyebilir. Bu, en iyi performans gösteren alanları veya ürünleri belirlemede ve veriye dayalı kararlar almada yardımcı olur.

Özetle, Excel'de Açılır listede Dinamik Grafik, veriyi görselleştirmek ve analiz etmek için esnek ve etkileşimli bir yol sağlar. Birden fazla veri setini karşılaştırma veya farklı senaryoları keşfetme ihtiyacı duyulan durumlarda finansal analiz, satış ve pazarlama ve birçok farklı uygulama için çok yönlü bir araçtır.

## **Dinamik Grafik ve Açılır Liste oluşturmak için Aspose Cells'i kullanın**
 Bir sonraki paragraflarda, Aspose.Cells for JavaScript ile C++ kullanarak Dropdownlist ile dinamik grafik oluşturmayı göstereceğiz. Örneğin kodunu ve bu kodla oluşturulan Excel dosyasını da sunacağız.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Grafik ve Açılır Listeli Dosyayı](DynamicChartWithDropdownlist.xlsx) oluşturacaktır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Dynamic Chart with Dropdown List Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, ValidationType, BackgroundType, Color, ChartType } = AsposeCells;

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
            // Create a new workbook and access the first worksheet.
            const workbook = new Workbook();
            const sheets = workbook.worksheets;
            const sheet = sheets.get(0);

            // Populate the data for the chart. Add values to cells and set series names.
            sheet.cells.get("A3").putValue("Tea");
            sheet.cells.get("A4").putValue("Coffee");
            sheet.cells.get("A5").putValue("Sugar");

            // In this example, we will add 12 months of data
            sheet.cells.get("B2").putValue("Jan");
            sheet.cells.get("C2").putValue("Feb");
            sheet.cells.get("D2").putValue("Mar");
            sheet.cells.get("E2").putValue("Apr");
            sheet.cells.get("F2").putValue("May");
            sheet.cells.get("G2").putValue("Jun");
            sheet.cells.get("H2").putValue("Jul");
            sheet.cells.get("I2").putValue("Aug");
            sheet.cells.get("J2").putValue("Sep");
            sheet.cells.get("K2").putValue("Oct");
            sheet.cells.get("L2").putValue("Nov");
            sheet.cells.get("M2").putValue("Dec");
            const allMonths = 12;
            const iCount = 3;
            for (let i = 0; i < iCount; i++) {
                for (let j = 0; j < allMonths; j++) {
                    const _row = i + 2;
                    const _column = j + 1; 
                    sheet.cells.get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
                }
            }

            // This is the Dropdownlist for Dynamic Data
            const ca = CellArea.createCellArea(9, 0, 9, 0);
            const _index = sheet.validations.add(ca);
            const _va = sheet.validations.get(_index);
            _va.type = ValidationType.List;
            _va.inCellDropDown = true;
            _va.formula1 = "=$B$2:$M$2";
            sheet.cells.get("A9").putValue("Current Month");
            sheet.cells.get("A10").putValue("Jan");
            const _style = sheet.cells.get("A10").style;
            _style.font.isBold = true;
            _style.pattern = BackgroundType.Solid;
            _style.foregroundColor = Color.Yellow;
            sheet.cells.get("A10").style = _style;

            // Set the dynamic range for the chart's data source. 
            let index = sheets.names.add("Sheet1!ChtMonthData");
            sheets.names.get(index).refersTo = "=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)";

            // Set the dynamic range for the chart's data labels. 
            index = sheets.names.add("Sheet1!ChtXLabels");
            sheets.names.get(index).refersTo = "=Sheet1!$A$3:$A$5";

            // Create a chart object and set its data source.
            const chartIndex = sheet.charts.add(ChartType.Column, 8, 2, 20, 8);
            const chart = sheet.charts.get(chartIndex);
            chart.nSeries.add("month", true);
            chart.nSeries.get(0).name = "=Sheet1!$A$10";
            chart.nSeries.get(0).values = "Sheet1!ChtMonthData";
            chart.nSeries.get(0).xValues = "Sheet1!ChtXLabels";

            // Save the workbook as an Excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DynamicChartWithDropdownlist.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

## **Notlar**
Oluşturulan dosyada, grafik seçilen ay için verileri dinamik olarak sayacaktır. Bu, örneğin kodundaki 'OFFSET' formülü kullanılarak gerçekleşir:
