---  
title: Node.js ile C++ kullanarak Dinamik Grafikler Oluşturma  
linktitle: Dinamik Grafikler Oluşturma  
description: Aspose.Cells for Node.js via C++ te dinamik grafikler oluşturmayı öğrenin. Bu kılavuz, grafik verilerini, serilerini ve biçimlendirmeyi ihtiyaçlarınıza göre nasıl dinamik olarak güncelleyeceğinizi gösterecek ve değişen verileri görsel olarak sunmanıza olanak tanıyacaktır.  
keywords: Aspose.Cells for Node.js, grafik çizimi, dinamik grafikler, veri, seri, biçimlendirme, çalışma sayfaları, güncelleme.  
type: docs  
weight: 240  
url: /tr/nodejs-cpp/create-dynamic-charts/  
---  

{{% alert color="primary" %}}  
Dinamik (veya etkileşimli) grafikler, veri kapsamını değiştirdiğinizde değişme yeteneğine sahiptir. Diğer bir deyişle, dinamik grafikler, veri kaynağı değiştiğinde otomatik olarak değişiklikleri yansıtabilir. Veri kaynağında değişikliği tetiklemek için, Excel Tablolarının filtreleme seçeneğini veya ComboBox veya Dropdown listesi gibi bir kontrolü kullanabilirsiniz.

Bu makale, yukarıda bahsedilen iki yaklaşımı kullanarak dinamik grafikler oluşturmak için Aspose.Cells for Node.js via C++ API'lerinin kullanımını gösterir.  
{{% /alert %}}  

## **Excel Tablolarını Kullanma**  

{{% alert color="primary" %}}  
Excel tabloları Aspose.Cells perspektifinde ListObject olarak adlandırılır, bu nedenle açıklık için "Tablo" yerine "ListObject" terimini kullanacağız. Lütfen, Aspose.Cells for Node.js via C++ ile [ListObject oluşturma](/cells/tr/nodejs-cpp/create-and-format-table/) hakkında detaylı bilgi edinin.  
{{% /alert %}}  

ListObject, kullanıcı etkileşimi üzerine sıralama ve filtreleme yapmak için yerleşik fonksiyonlar sağlar. Her iki sıralama ve filtreleme seçeneği, [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) başlık satırına otomatik olarak eklenen açılır listeler aracılığıyla sağlanır. Bu özellikler (sıralama ve filtreleme) nedeniyle, [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) dinamik grafik için veri kaynağı olarak mükemmel aday olur çünkü sıralama veya filtreleme değiştiğinde, grafikteki veri gösterimi güncellenecek ve [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)nin mevcut durumunu yansıtacaktır.

Demoyu basit tutmak amacıyla, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)'ı sıfırdan oluşturacağız ve aşağıda belirtilen adımlarla ilerleyeceğiz.

1. Boş bir [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) oluşturun.
1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) içinde ilk [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) in [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) erişimi.
1. Hücrelere bazı veriler ekleyin.
1. Eklenen verilere dayanarak [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) oluşturun.
1. [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject) nin veri aralığına göre [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) oluşturun.
1. Sonucu diske kaydedin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const book = new AsposeCells.Workbook();
// Access first worksheet from the collection
const sheet = book.getWorksheets().get(0);
// Access cells collection of the first worksheet
const cells = sheet.getCells();

// Insert data column-wise
cells.get("A1").putValue("Category");
cells.get("A2").putValue("Fruit");
cells.get("A3").putValue("Fruit");
cells.get("A4").putValue("Fruit");
cells.get("A5").putValue("Fruit");
cells.get("A6").putValue("Vegetables");
cells.get("A7").putValue("Vegetables");
cells.get("A8").putValue("Vegetables");
cells.get("A9").putValue("Vegetables");
cells.get("A10").putValue("Beverages");
cells.get("A11").putValue("Beverages");
cells.get("A12").putValue("Beverages");

cells.get("B1").putValue("Food");
cells.get("B2").putValue("Apple");
cells.get("B3").putValue("Banana");
cells.get("B4").putValue("Apricot");
cells.get("B5").putValue("Grapes");
cells.get("B6").putValue("Carrot");
cells.get("B7").putValue("Onion");
cells.get("B8").putValue("Cabbage");
cells.get("B9").putValue("Potato");
cells.get("B10").putValue("Coke");
cells.get("B11").putValue("Coladas");
cells.get("B12").putValue("Fizz");

cells.get("C1").putValue("Cost");
cells.get("C2").putValue(2.2);
cells.get("C3").putValue(3.1);
cells.get("C4").putValue(4.1);
cells.get("C5").putValue(5.1);
cells.get("C6").putValue(4.4);
cells.get("C7").putValue(5.4);
cells.get("C8").putValue(6.5);
cells.get("C9").putValue(5.3);
cells.get("C10").putValue(3.2);
cells.get("C11").putValue(3.6);
cells.get("C12").putValue(5.2);

cells.get("D1").putValue("Profit");
cells.get("D2").putValue(0.1);
cells.get("D3").putValue(0.4);
cells.get("D4").putValue(0.5);
cells.get("D5").putValue(0.6);
cells.get("D6").putValue(0.7);
cells.get("D7").putValue(1.3);
cells.get("D8").putValue(0.8);
cells.get("D9").putValue(1.3);
cells.get("D10").putValue(2.2);
cells.get("D11").putValue(2.4);
cells.get("D12").putValue(3.3);

// Create ListObject, Get the List objects collection in the first worksheet
const listObjects = sheet.getListObjects();

// Add a List based on the data source range with headers on
let index = listObjects.add(0, 0, 11, 3, true);

sheet.autoFitColumns();

// Create chart based on ListObject
index = sheet.getCharts().add(AsposeCells.ChartType.Column, 21, 1, 35, 18);
const chart = sheet.getCharts().get(index);
chart.setChartDataRange("A1:D12", true);
chart.getNSeries().setCategoryData("A2:B12");

// Save spreadsheet
book.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Dinamik Formüller Kullanma**  

Eğer [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject)’ı dinamik grafik için veri kaynağı olarak kullanmak istemiyorsanız, diğer seçenek Excel fonksiyonlarını (veya formülleri) kullanmak ve veriyi değiştiren bir kontrol (örneğin, ComboBox) oluşturmaktır. Bu senaryoda, seçim yapıldığında VLOOKUP fonksiyonu uygun değerleri getirecek şekilde kullanılır. Seçim değiştirildiğinde, VLOOKUP fonksiyonu hücre değeri yenilenir. Bir hücre aralığı VLOOKUP fonksiyonu kullanıyorsa, tüm aralık kullanıcı etkileşimiyle yenilenebilir ve bu nedenle dinamik grafikte veri kaynağı olarak kullanılabilir.

Demonstrasyonu anlaşılır tutmak için Workbook'ı sıfırdan oluşturacağız ve aşağıda belirtilen adımları adım adım ilerleteceğiz.

1. Boş bir [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) oluşturun.
1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) içinde ilk [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) in [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) erişimi.
1. Hücrelere Adlandırılmış Aralık oluşturarak bazı veriler ekleyin. Bu veriler, dinamik grafik için seri olarak hizmet edecektir.
1. Önceki adımda oluşturulan Adlandırılmış Aralık kullanılarak [**ComboBox**](https://reference.aspose.com/cells/nodejs-cpp/combobox) oluştur.
1. VLOOKUP işlevine veri kaynağı olacak hücrelere başka veriler ekleyin.
1. Uygun parametrelerle VLOOKUP fonksiyonunu hücre aralığına ekleyin. Bu aralık, dinamik grafik için veri kaynağı olarak kullanılacaktır.
1. Önceki adımda oluşturulan aralığa göre [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) oluştur.
1. Sonucu diske kaydedin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range in the second worksheet
const range = worksheet.getCells().createRange("C21", "C24");

// Name the range
range.setName("MyRange");

// Fill different cells with data in the range
range.get(0, 0).putValue("North");
range.get(1, 0).putValue("South");
range.get(2, 0).putValue("East");
range.get(3, 0).putValue("West");

const comboBox = worksheet.getShapes().addComboBox(15, 0, 2, 0, 17, 64);
comboBox.setInputRange("=MyRange");
comboBox.setLinkedCell("=B16");
comboBox.setSelectedIndex(0);
const cell = worksheet.getCells().get("B16");
const style = cell.getStyle();
style.getFont().setColor(AsposeCells.Color.White);
cell.setStyle(style);

worksheet.getCells().get("C16").setFormula("=INDEX(Sheet1!$C$21:$C$24,$B$16,1)");

// Put some data for chart source
// Data Headers
worksheet.getCells().get("D15").putValue("Jan");
worksheet.getCells().get("D20").putValue("Jan");

worksheet.getCells().get("E15").putValue("Feb");
worksheet.getCells().get("E20").putValue("Feb");

worksheet.getCells().get("F15").putValue("Mar");
worksheet.getCells().get("F20").putValue("Mar");

worksheet.getCells().get("G15").putValue("Apr");
worksheet.getCells().get("G20").putValue("Apr");

worksheet.getCells().get("H15").putValue("May");
worksheet.getCells().get("H20").putValue("May");

worksheet.getCells().get("I15").putValue("Jun");
worksheet.getCells().get("I20").putValue("Jun");

// Data
worksheet.getCells().get("D21").putValue(304);
worksheet.getCells().get("D22").putValue(402);
worksheet.getCells().get("D23").putValue(321);
worksheet.getCells().get("D24").putValue(123);

worksheet.getCells().get("E21").putValue(300);
worksheet.getCells().get("E22").putValue(500);
worksheet.getCells().get("E23").putValue(219);
worksheet.getCells().get("E24").putValue(422);

worksheet.getCells().get("F21").putValue(222);
worksheet.getCells().get("F22").putValue(331);
worksheet.getCells().get("F23").putValue(112);
worksheet.getCells().get("F24").putValue(350);

worksheet.getCells().get("G21").putValue(100);
worksheet.getCells().get("G22").putValue(200);
worksheet.getCells().get("G23").putValue(300);
worksheet.getCells().get("G24").putValue(400);

worksheet.getCells().get("H21").putValue(200);
worksheet.getCells().get("H22").putValue(300);
worksheet.getCells().get("H23").putValue(400);
worksheet.getCells().get("H24").putValue(500);

worksheet.getCells().get("I21").putValue(400);
worksheet.getCells().get("I22").putValue(200);
worksheet.getCells().get("I23").putValue(200);
worksheet.getCells().get("I24").putValue(100);

// Dynamically load data on selection of Dropdown value
worksheet.getCells().get("D16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,2,FALSE),0)");
worksheet.getCells().get("E16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,3,FALSE),0)");
worksheet.getCells().get("F16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,4,FALSE),0)");
worksheet.getCells().get("G16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,5,FALSE),0)");
worksheet.getCells().get("H16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,6,FALSE),0)");
worksheet.getCells().get("I16").setFormula("=IFERROR(VLOOKUP($C$16,$C$21:$I$24,7,FALSE),0)");

// Create Chart
const index = worksheet.getCharts().add(AsposeCells.ChartType.Column, 0, 3, 12, 9);
const chart = worksheet.getCharts().get(index);
chart.getNSeries().add("='Sheet1'!$D$16:$I$16", false);
chart.getNSeries().get(0).setName("=C16");
chart.getNSeries().setCategoryData("=$D$15:$I$15");

// Save result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
