---
title: Node.js ile C++ üzerinden Sparklines ve Ayarları 3D Format Kullanımı
linktitle: Sparklines ve 3D Format Ayarlarını Kullanma
type: docs
weight: 40
url: /tr/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: Aspose.Cells for Node.js via C++ kullanarak sparklines ları nasıl kullanacağınızı ve Excel dosyalarında 3D biçimlendirme uygulayacağınızı öğrenin. 
---

## **Sparklines Kullanma**
Microsoft Excel 2010, bilgileri daha önce hiç olmadığı kadar fazla şekilde analiz etmenizi sağlar. Kullanıcıların yeni veri analiz ve görselleştirme araçlarıyla önemli veri eğilimlerini takip etmesine ve vurgulamasına izin verir. Sparklines, veriyi ve tabloyu aynı anda görüntüleyebileceğiniz mini grafiklerdir. Sparklines uygun şekilde kullanıldığında, veri analizi daha hızlı ve daha anlaşılır olur. Ayrıca, aşırı kalabalık çalışma tablolarını çok fazla meşgul grafiklerle önler. Onlar, aynı tabloda veriyi görmek için basit bir görünüm sağlar. Ayrıca, Aspose.Cells, elektronik tablolardaki sparklines'ı manipüle etmek için bir API sağlar.

Aspose.Cells for Node.js via C++, tablolar üzerinde sparklines'ları manipüle etmek için API sağlar.
### **Microsoft Excel'de Sparklines Kullanma**
Microsoft Excel 2010'da Sparklines eklemek için:

1. Sparklines'ların görünmesini istediğiniz hücreleri seçin. Onları görüntülemeyi kolaylaştırmak için, verinin yanındaki hücreleri seçin.
1. Menü şeridinde **Ekle**'yi tıklayın, ardından **Sparklines** grubunda **Sütun**'u seçin.
1. Kaynak verinin bulunduğu çalışma sayfasındaki hücre aralığını seçin veya girin. Grafikler görünecektir.

Sparklines, örneğin, bir bayan voleybol ligi için kazanma veya kaybetme kaydını görmek için size yardımcı olur. Sparklines, ligdeki her takımın tüm sezonlarının toplamını dahi verebilir.
### **Aspose.Cells for Node.js via C++ kullanılarak sparklines'lar**
Geliştiriciler, Aspose.Cells for Node.js via C++ tarafından sağlanan API'yi kullanarak şablon dosyasında sparklines oluşturabilir, silebilir veya okuyabilirler. Sparklines'ları yöneten sınıflar [SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/) modülünde bulunur, bu yüzden bu özellikleri kullanmadan önce bu modülü dahil etmeniz gerekir.

Belirli bir veri aralığı için özel grafikler ekleyerek, geliştiriciler seçili hücre alanlarına farklı türde küçük grafikler eklemek özgürlüğüne sahiptir.

Aşağıdaki örnek, Sparklines özelliğini sergiler. Örnek, şunları gösterir:

1. Basit bir şablon dosyasını açın.
1. Bir çalışma sayfası için sparklines bilgilerini okuyun.
1. Belirli bir veri aralığı için yeni sparklines ekleyin.
1. Excel dosyasını diske kaydedin.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Use the following lines if you need to read the Sparklines
// Read the Sparklines from the template file (if it has)
const sparklinesCount = sheet.getSparklineGroups().getCount();

for (let i = 0; i < sparklinesCount; i++)
{
const group = sheet.getSparklineGroups().get(i);
// Display the Sparklines group information e.g type, number of sparklines items
console.log(`sparkline group: type:${group.getType()}, sparkline items count:${group.getSparklines().getCount()}`);
const sparklineCount = sparklineGroup.getSparklines().getCount();
for (let j = 0; j < sparklineCount; j++) 
{
const sparkline = sparklineGroup.getSparklines().get(j);
// Display the individual Sparkines and the data ranges
console.log(`sparkline: row:${sparkline.getRow()}, col:${sparkline.getColumn()}, dataRange:${sparkline.getDataRange()}`);
}
}


// Add Sparklines
// Define the CellArea D2:D10
const ca = AsposeCells.CellArea.createCellArea(1, 4, 7, 4);
// Add new Sparklines for a data range to a cell area
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "Sheet1!B2:D8", false, ca);
const group = sheet.getSparklineGroups().get(idx);
// Create CellsColor
const clr = workbook.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Save the excel file
workbook.save(path.join(dataDir, "Book1.out.xlsx"));
```
## **3B Formatını Ayarlama**
Senaryonuz için sonuçlar alabilmek adına 3D grafik stillerine ihtiyaç duyabilirsiniz. Aspose.Cells for Node.js via C++, Microsoft Excel 2007 3D biçimlendirmesini uygulamak için ilgili API'yi sağlar.

Aşağıda, bir grafik oluşturmayı ve Microsoft Excel 2007 3B biçimlendirmesini uygulamayı sergilemek için tam bir örnek verilmiştir. Örnek kodu çalıştırdıktan sonra bir sütun grafiği (3B efektleri ile) çalışma sayfasına eklenecektir.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "3d_format.out.xlsx");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Add a Data Worksheet
const dataSheet = book.getWorksheets().add("DataSheet");

// Add Chart Worksheet
const sheet = book.getWorksheets().add("MyChart");

// Put some values into the cells in the data worksheet
dataSheet.getCells().get("B1").putValue(1);
dataSheet.getCells().get("B2").putValue(2);
dataSheet.getCells().get("B3").putValue(3);
dataSheet.getCells().get("A1").putValue("A");
dataSheet.getCells().get("A2").putValue("B");
dataSheet.getCells().get("A3").putValue("C");

// Define the Chart Collection
const charts = sheet.getCharts();
// Add a Column chart to the Chart Worksheet
const chartSheetIdx = charts.add(AsposeCells.ChartType.Column, 5, 0, 25, 15);

// Get the newly added Chart
const chart = book.getWorksheets().get(2).getCharts().get(0);

// Set the background/foreground color for PlotArea/ChartArea
chart.getPlotArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Hide the Legend
chart.setShowLegend(false);

// Add Data Series for the Chart
chart.getNSeries().add("DataSheet!B1:B3", true);
// Specify the Category Data
chart.getNSeries().setCategoryData("DataSheet!A1:A3");

// Get the Data Series
const ser = chart.getNSeries().get(0);

// Apply the 3-D formatting
const spPr = ser.getShapeProperties();
const fmt3d = spPr.getFormat3D();

// Specify Bevel with its height/width
const bevel = fmt3d.getTopBevel();
bevel.setType(AsposeCells.BevelPresetType.Circle);
bevel.setHeight(2);
bevel.setWidth(5);

// Specify Surface material type
fmt3d.setSurfaceMaterialType(AsposeCells.PresetMaterialType.WarmMatte);

// Specify surface lighting type
fmt3d.setSurfaceLightingType(AsposeCells.LightRigType.ThreePoint);

// Specify lighting angle
fmt3d.setLightingAngle(20);

// Specify Series background/foreground and line color
ser.getArea().setBackgroundColor(AsposeCells.Color.Maroon);
ser.getArea().setForegroundColor(AsposeCells.Color.Maroon);
ser.getBorder().setColor(AsposeCells.Color.Maroon);

// Save the Excel file
book.save(filePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
