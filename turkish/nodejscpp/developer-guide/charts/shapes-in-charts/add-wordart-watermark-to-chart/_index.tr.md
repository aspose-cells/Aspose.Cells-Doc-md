---  
title: Node.js üzerinden C++ ile Grafiğe WordArt Filigranı Ekle  
linktitle: Grafik e WordArt Filigran Ekle  
description: Microsoft Excel de grafiğe WordArt filigranı eklemek için Aspose.Cells for Node.js via C++ nasıl kullanılacağını öğrenin. Kılavuzumuz, WordArt filigranı oluşturmaya ve konumlandırmaya nasıl yardımcı olacağını gösterecek, böylece grafiğinizin görsel cazibesini ve benzersizliğini artırabilirsiniz.  
keywords: Aspose.Cells for Node.js, WordArt Filigranı, Grafik Filigranı, Microsoft Excel, Görsel Çekicilik, Grafik Eşsizliği.  
type: docs  
weight: 50  
url: /tr/nodejs-cpp/add-wordart-watermark-to-chart/  
---  

{{% alert color="primary" %}}  

WordArt'ı elektronik tablolara özel metin efektleri eklemek için kullanabilirsiniz. Örneğin, başlığı uzatabilir, metni süsleyebilir, metni önceden belirlenmiş bir şekle sığdırabilir veya etkilenen metni bir grafik çizim alanına bir filigran olarak uygulayabilirsiniz. WordArt, elektronik tablolarınızda hareket ettirebileceğiniz veya konumlandırabileceğiniz bir nesne haline gelirken dekorasyon eklemek için.  

Aşağıdaki örnek, bir WordArt şeklinin grafik çizim alanı için bir filigran olarak nasıl ekleneceğini göstermektedir.  

{{% /alert %}}  

Aşağıdaki örnek, varolan bir grafik çizim alanı için bir WordArt şeklinin filigran olarak nasıl ekleneceğini göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Open the existing excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add a WordArt watermark (shape) to the chart's plot area.
const wordart = chart.getShapes().addTextEffectInChart(AsposeCells.MsoPresetTextEffect.TextEffect2,
"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);

// Get the shape's fill format.
const wordArtFormat = wordart.getFill();

// Set the transparency.
wordArtFormat.setTransparency(0.9);

// Get the line format.
const lineFormat = wordart.getLine();

// Set Line format to invisible.
lineFormat.setWeight(0.0);

// Save the excel file.
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
