---
title: Aspose.Cells for Node.js via C++ kullanarak PivotGrafik Ekleme Yöntemi
linktitle: Pivot Grafik
type: docs
weight: 100
url: /tr/nodejs-cpp/how-to-add-pivot-chart/
description: Aspose.Cells for Node.js via C++ kullanarak PivotGrafik nasıl eklenir.
keywords: PivotGrafik Node.js ile C++
---
## PivotChart Nedir

Bir pivot grafiği, pivot tablodaki verilerin görsel temsilidir. Pivot grafikler, özet verileri özetleme, analiz etme, keşfetme ve sunma imkanı sağlar. İşte pivot grafiklerin bazı temel özellikleri ve yönleri:

1. Dinamik Veri Temsili: Pivot grafikleri, pivot tablodaki değişiklikleri otomatik olarak yansıtır. Pivot tablodaki alanları ekleyip çıkarırsanız, pivot grafik de buna göre güncellenir.

1. İnteraktif: Pivot grafikleri etkileşimlidir, kullanıcıların filtreleme, sıralama ve veri detayına inmesine izin verir. Bu, verilerin farklı yönlerini keşfetmeyi kolaylaştırır.

1. Esnek Düzen: Kullanıcılar alanları sürükleyip bırakarak pivot grafiğin düzenini değiştirebilir, bu da nasıl görselleştirileceğinde esneklik sağlar.

1. Çeşitli Grafik Türleri: Pivot grafikler çeşitli grafik türleri kullanılarak oluşturulabilir; çubuk grafikleri, çizgi grafikleri, pasta grafikleri ve daha fazlası, verinin doğasına ve elde etmek istediğiniz içgörülere bağlı olarak.

1. Özetleme: Pivot grafikleri büyük miktarda veriyi özetler ve toplamlar, ortalamalar, sayımlar veya diğer özet istatistikleri gösterebilir.

1. Filtreleme: Filtreleme özellikleri sağlar, belirli kriterleri karşılayan verileri görüntülemenize olanak tanır.

<br>
Pivot grafikler, karmaşık veri setlerinin net ve öz bir görsel özetini sağlamak için iş zekası ve veri analizinde yaygın olarak kullanılır. Veri odaklı kararlar almak için güçlü bir araçtır.

## Aspose.Cells for Node.js via C++ kullanarak PivotChart nasıl eklenir

### **Pivot Tablo Ekleme**

Aspose.Cells for Node.js via C++ kullanarak pivot tablo oluşturmak için:

1. Bir hücre nesnesinin `putValue` metodunu kullanarak bir çalışma sayfasına veri ekleyin. Ayrıca, zaten veriyle doldurulmuş bir şablon dosyası da kullanabilirsiniz. Veriler, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. `PivotTables` koleksiyonunun `add` metodunu çağırarak çalışma sayfasına bir pivot tablo ekleyin.
1. `PivotTables` koleksiyonundan yeni PivotTable nesnesine erişmek için indeksini kullanın. PivotTable nesnesine kapsüllenmiş herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

const namesAndValues = [
["David", 1, "Maxilaku", "Asia", "China", 2000],
["David", 2, "Maxilaku", "Asia", "India", 500],
["David", 3, "Chai", "Asia", "Korea", 1200],
["David", 4, "Maxilaku", "Asia", "India", 1500],
["James", 1, "Chang", "Europe", "France", 500],
["James", 2, "Chang", "Europe", "France", 1500],
["James", 3, "Chang", "Europe", "Germany", 800],
["James", 4, "Chang", "Europe", "Italy", 900],
["James", 4, "Chang", "Europe", "France", 500],
["Miya", 1, "Geitost", "America", "U.S.", 1600],
["Miya", 2, "Chai", "America", "U.S.", 600],
["Miya", 3, "Geitost", "America", "Brazil", 2000],
["Miya", 2, "Geitost", "America", "U.S.", 500],
["Miya", 3, "Maxilaku", "America", "Canada", 900],
["Miya", 4, "Geitost", "America", "U.S.", 700],
["Miya", 5, "Geitost", "America", "U.S.", 1400],
["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
["Miya", 7, "Ikuru", "Europe", "France", 300],
["Miya", 8, "Ikuru", "Europe", "Italy", 500],
["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
];

namesAndValues.forEach((item, index) => {
const rowIndex = index + 2;
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **Pivot Grafik Ekleme**

Aspose.Cells for Node.js via C++ kullanarak PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafiğin `PivotSource` özelliğini, mevcut bir pivot tabloya referans olacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

