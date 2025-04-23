---  
title: Microsoft Excel gibi Otomatik Birimlerini Node.js ve C++ kullanarak Çizelge Eksenleriyle ele alınması  
linktitle: Microsoft Excel gibi Grafik Ekseni Otomatik Birimleri ile Başa Çık  
description: Aspose.Cells for Node.js via C++ üzerinde otomatik birimleri nasıl idare edeceğinizi öğrenin. Rehberimiz, otomatik birimleri bir çizelge ekseninde yapılandırma ve özelleştirme, bilimsel gösterim ve ölçek ayarını da içermektedir.  
keywords: Aspose.Cells for Node.js via C++, çizelge eksenleri, otomatik birimler, Microsoft Excel, yapılandırma, özelleştirme, bilimsel gösterim, ölçekleme.  
type: docs  
weight: 120  
url: /tr/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **Olası Kullanım Senaryoları**  
Aspose.Cells for Node.js via C++'ün erken sürümleri, görüntü veya PDF'ye çizelge render edildiğinde çizelge ekseninin otomatik birimlerini düzgün şekilde idare edemiyordu. Artık Aspose.Cells for Node.js via C++ otomatik birimlerin idaresini destekliyor. Kod değişikliği gerekmez. Sadece çizelgenizi bir resim veya PDF'ye dönüştürün ve Microsoft Excel gibi çizelge eksenlerini render edecektir.  

## **Grafik Ekseni Otomatik Birimleri ile Başa Çık**  
Aşağıdaki örnek kod, [örnek Excel dosyasını](61767755.xlsx) yükler ve [çıktı PDF çizelgesi](61767752.pdf) üretir. Ekran görüntüsü, çizelge ekseninin otomatik birimlerini kırmızı dikdörtgenlerde gösterirken, örnek Excel dosyasındaki çizelge ile çıktı PDF'sini karşılaştırır. Her ikisi de tam olarak aynıdır.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Örnek Kod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
