---
title: Node.js ile Dropdown list kullanarak Dinamik Grafik oluşturma nasıl yapılır?
linktitle: Dropdownlist ile Dinamik Grafik Nasıl Oluşturulur
description: Aspose.Cells for Node.js via C++ kullanarak, seçimlere göre güncellenen dinamik bir grafik nasıl oluşturulacağını öğrenin. Adım adım rehberimiz, grafiklerinize esnek veri görselleştirme için bir drop down listesi entegre etmenin yollarını gösterecektir.
keywords: Aspose.Cells for Node.js via C++, Dinamik Grafik, Drop Down Listesi, Veri Görselleştirme, Entegrasyon, Esnek Görselleştirme.
type: docs
weight: 76
url: /tr/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Olası Kullanım Senaryoları**
Excel'de Açılır listede Dinamik Grafik, seçilen verilere göre dinamik olarak güncellenebilen etkileşimli grafikler oluşturmayı sağlayan güçlü bir araçtır. Bu özellik özellikle birden fazla veri setini analiz etme veya çeşitli senaryoları karşılaştırma ihtiyacı duyulan durumlarda kullanışlıdır.

Açılır listede Dinamik Grafik'in yaygın bir uygulaması finansal analizde gerçekleşir. Örneğin, bir şirket farklı yıllar veya departmanlar için birden fazla finansal veri setine sahip olabilir. Açılır listeden kullanıcılar istedikleri belirli veri setini seçebilirler ve grafik otomatik olarak ilgili bilgileri görüntülemek için güncellenir. Bu, kolay karşılaştırma ve trend veya desenlerin belirlenmesine olanak tanır.

Başka bir uygulama ise satış ve pazarlamada gerçekleşir. Bir şirket farklı ürünler veya bölgeler için satış verilerine sahip olabilir. Açılır listede Dinamik Grafik ile kullanıcılar belirli bir ürün veya bölge seçebilir ve grafik seçilen seçenek için satış performansını dinamik olarak güncelleyebilir. Bu, en iyi performans gösteren alanları veya ürünleri belirlemede ve veriye dayalı kararlar almada yardımcı olur.

Özetle, Excel'de Açılır listede Dinamik Grafik, veriyi görselleştirmek ve analiz etmek için esnek ve etkileşimli bir yol sağlar. Birden fazla veri setini karşılaştırma veya farklı senaryoları keşfetme ihtiyacı duyulan durumlarda finansal analiz, satış ve pazarlama ve birçok farklı uygulama için çok yönlü bir araçtır.

## **Dinamik Grafik ve Açılır Liste oluşturmak için Aspose Cells'i kullanın**
Aşağıdaki paragraflarda, Aspose.Cells for Node.js via C++ kullanarak Dönen Dinamik Grafik oluşturmayı göstereceğiz. Örnek kodu ve bu kodla oluşturulan Excel dosyasını da göstereceğiz.

## **Örnek Kod**
Aşağıdaki örnek kod, [Dinamik Grafik ve Açılır Listeli Dosyayı](DynamicChartWithDropdownlist.xlsx) oluşturacaktır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **Notlar**
Oluşturulan dosyada, grafik seçilen ay için verileri dinamik olarak sayacaktır. Bu, örneğin kodundaki 'OFFSET' formülü kullanılarak gerçekleşir:

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

A2'de açılır listedeki değeri değiştirmeyi deneyin ve grafik dinamik olarak değişecektir. Aspose.Cells'i kullanarak başarılı bir şekilde dinamik bir grafik ve açılır liste oluşturduk.
