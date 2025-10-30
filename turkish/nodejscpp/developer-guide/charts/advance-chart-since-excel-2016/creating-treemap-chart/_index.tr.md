---  
title: Node.js ile C++ üzerinden TreeMap grafiği nasıl oluşturulur  
linktitle: Ağaç Haritası Grafiği Nasıl Oluşturulur  
description: Aspose.Cells for Node.js via C++ te bir Ağaç Haritası grafiği nasıl oluşturulur öğrenin. Kılavuzumuz, renkler, etiketler ve veri gösterimi dahil olmak üzere Ağaç Haritası grafikleri için mevcut olan çeşitli özellikleri ve biçimlendirme seçeneklerini anlamanıza yardımcı olacaktır.  
keywords: Aspose.Cells for Node.js, Ağaç Haritası grafiği, oluşturma, özellikler, biçimlendirme, renkler, etiketler, veri gösterimi, daire grafik, hiyerarşik grafik.  
type: docs  
weight: 161  
url: /tr/nodejs-cpp/creating-treemap-chart/  
---  

## **Olası Kullanım Senaryoları**  
Ağaç haritası grafiği verilerinizin hiyerarşik bir görünümünü sağlar ve hangi ürünlerin bir mağazanın en çok satanları olduğunu görmek gibi desenleri kolayca belirlemenize olanak tanır. Ağaç dalları dikdörtgenlerle temsil edilir ve her alt dal daha küçük bir dikdörtgen olarak gösterilir. Ağaç haritası grafikleri kategorileri renk ve yakınlıkla gösterir ve diğer grafik türleri ile zor olacak birçok veriyi kolayca gösterebilir.  

![todo:image_alt_text](sample.png)  
## **Ağaç Haritası Grafiği**  
Aşağıdaki kodu çalıştırdıktan sonra, aşağıdaki gibi Ağaç Haritası grafiğini göreceksiniz.  

![todo:image_alt_text](result.png)  
## **Örnek Kod**  
Aşağıdaki örnek kod [örnek Excel dosyasını](treemap.xlsx) yükler ve [çıktı Excel dosyasını](out.xlsx) oluşturur.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
