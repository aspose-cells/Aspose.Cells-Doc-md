---  
title: Node.js ve C++ kullanarak toplam olarak nokta belirlemeyi nasıl ayarlarsınız?  
linktitle: Noktayı toplam olarak ayarlama nasıl yapılır  
description: Aspose.Cells for Node.js via C++ kullanarak Waterfall grafiklerde noktaları toplam olarak ayarlamayı öğrenin.  
keywords: Waterfall Grafiği, Nokta, Toplam olarak ayarla, Node.js ve C++ kullanımı  
type: docs  
weight: 72  
url: /tr/nodejs-cpp/how-to-set-point-as-total/  
---  

## Excel Grafiklerinde "Noktayı toplam olarak ayarla" nedir?

Bazı Excel grafiklerinde, örneğin Waterfall grafikte, bazı nokta verileri önceki noktaların toplamıdır ve "noktayı toplam yap" gerekebilir. Aşağıda örnek kodu ve açıklamayı göreceksiniz.

## Bir WaterFall Grafik "Noktayı toplam yap" gerektirir 

![todo:image_alt_text](set-as-total1.png)

Bu resim Excel'de bir WaterFall grafiği gösterir. "Toplam" ile başlayan dört veri noktası görebiliyoruz ve bunlar önceki tüm verileri saymak için kullanılır. Bu resimde ayarlar tam doğru değildir. "Toplam 2024" noktasını seçtiğinizde, Excel'de "Toplam olarak ayarla" seçeneğinin işaretli olmadığını görebilirsiniz. Aşağıda değiştirilmesi gereken örnek Excel dosyası ([SampleSheet.xlsx](SampleSheet.xlsx)) ve Aspose.Cells for Node.js via C++ kullanılarak doğru ayar yapılacaktır.

## Aspose.Cells for Node.js via C++ kullanarak "Noktayı toplam yap" 

Dosyanın doğru şekilde ayarlanması için aşağıdaki kodu kullanıyoruz:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Aşağıdaki doğru [çıktı dosyasını](output.xlsx) edinebilirsiniz

Aşağıdaki şekilde gösterildiği gibi, dört "Toplam" veri noktası doğru şekilde ayarlandı ve önceki grafikten farkı görebilirsiniz.

![todo:image_alt_text](set-as-total2.png)  
{{< app/cells/assistant language="nodejs-cpp" >}}
