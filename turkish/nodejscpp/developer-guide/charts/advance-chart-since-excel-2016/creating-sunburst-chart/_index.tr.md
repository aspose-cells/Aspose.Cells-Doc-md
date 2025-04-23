---
title: Node.js ile Güneş Patlaması Grafiği Nasıl Oluşturulur C++ üzerinden
linktitle: Güneş patlaması grafiği nasıl oluşturulur
description: Kılavuzumuz, verileri daire şeklinde sunan bir grafik olan Aspose.Cells for Node.js via C++ dür. Bu kılavuz, grafiklerinizin çeşitli özelliklerini ve biçimlendirmesini, veri etiketleri, efsaneler, renkler ve daha fazlasını ayarlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for Node.js via C++, güneş patlaması grafiği, oluşturma, özellikleri ayarla, veri etiketleri, efsane, biçim, renk, daire, veri görselleştirme.
type: docs
weight: 162
url: /tr/nodejs-cpp/creating-sunburst-chart/
---

## **Olası Kullanım Senaryoları**
Ağaçharitası grafikleri, hiyerarşi içindeki oranları karşılaştırmak için iyidir; ancak, ağaçharitası grafikleri en büyük kategoriler ile her veri noktası arasındaki hiyerarşi seviyelerini gösterirken iyi değildir. Bunun yerine, güneş patlaması grafiği çok daha iyi bir görsel grafiktir. Güneş patlaması grafiği, hiyerarşik verileri göstermek için idealdir. Hiyerarşinin her seviyesi, en içteki daire hiyerarşinin en üstü olarak temsil edilen bir halka veya daireyle gösterilir. Hiyerarşik verisi olmayan (bir seviye kategorisi olan) güneş patlaması grafiği, bir halka dilimine benzer görünür. Ancak, birden fazla kategori seviyesiyle güneş patlaması grafiği, dış halkaların iç halkalara nasıl bağlı olduğunu gösterir. Güneş patlaması grafiği, bir halkanın nasıl katkıda bulunduğunu göstermek açısından en etkilidir; diğer hiyerarşik grafik türü olan ağaçharitası, göreceli boyutları karşılaştırmak için idealdir.

![todo:image_alt_text](sample.png)
## **Güneş Patlaması Grafiği**
Aşağıdaki kodu çalıştırdıktan sonra, aşağıdaki gibi Güneş patlaması grafiğini göreceksiniz.

![todo:image_alt_text](result.png)
## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](sunburst.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
