---  
title: Node.js ile C++ üzerinden Excel 2016 Grafiklerini Oku ve Manipüle Et  
linktitle: Excel 2016 Grafiklerini Okuma ve Değiştirme  
description: Aspose.Cells for Node.js via C++ kullanarak Excel 2016 grafiklerini nasıl okuyup manipüle edeceğinizi öğrenin. Bu kılavuz, çeşitli grafik özelliklerine nasıl erişileceğini ve bunların nasıl değiştirileceğini gösterecek.  
keywords: Aspose.Cells for Node.js, Excel 2016 grafikler, okuma, manipüle etme, veri etiketleri, seri renkleri, düzen, hiyerarşik grafikleme, dairesel grafik.  
type: docs  
weight: 48  
url: /tr/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **Olası Kullanım Senaryoları**  
Aspose.Cells artık Microsoft Excel 2016 grafiklerini okuma ve değiştirme desteği sunmaktadır, bu özellik Microsoft Excel 2013 veya daha önceki sürümlerde bulunmamaktadır.  
## **Excel 2016 Grafiklerini Okuma ve Değiştirme**  
Aşağıdaki örnek kod, ilk çalışma sayfasında Excel 2016 grafiklerini içeren kaynak Excel dosyasını yükler. Tüm grafikleri tek tek okur ve tipi doğrultusunda başlıklarını değiştirir. Aşağıdaki ekran görüntüsü, kod çalıştırılmadan önceki kaynak Excel dosyasını gösterir. Gördüğünüz gibi, tüm grafikler için başlık aynıdır.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Aşağıdaki ekran görüntüsü, kodun çalıştırılması sonrası [çıktı excel dosyasını](22774104.xlsx) göstermektedir. Görebileceğiniz gibi, grafik başlığı türüne göre değişmiştir.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Örnek Kod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "excel2016Charts.xlsx");

// Load source excel file containing excel 2016 charts
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet which contains the charts
const sheet = workbook.getWorksheets().get(0);

// Access all charts one by one and read their types
for (let i = 0; i < sheet.getCharts().getCount(); i++) {
// Access the chart
const ch = sheet.getCharts().get(i);

// Print chart type
console.log(ch.getType());

// Change the title of the charts as per their types
ch.getTitle().setText("Chart Type is " + ch.getType().toString());
}

// Save the workbook
workbook.save(path.join(dataDir, "out_excel2016Charts.xlsx"));
```  
## **Konsol Çıktısı**  
Yukarıdaki örnek kodun [kaynak excel dosyası](22774101.xlsx) ile çalıştırılması sonucu konsol çıktısı

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Gelişmiş Konular**  
- [Su Düşen Grafik Oluşturma](/cells/tr/nodejs-cpp/creating-waterfall-chart/)  
- [Ağaç Haritası Grafik Oluşturma](/cells/tr/nodejs-cpp/creating-treemap-chart/)  
- [Güneş Patlaması Grafik Oluşturma](/cells/tr/nodejs-cpp/creating-sunburst-chart/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
