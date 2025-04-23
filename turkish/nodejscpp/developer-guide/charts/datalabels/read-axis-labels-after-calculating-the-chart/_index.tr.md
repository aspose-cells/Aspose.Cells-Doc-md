---  
title: Node.js ve C++ kullanarak Çizelge ile Grafik Çizgileri Sonra Eksensel Etiketleri Okuma  
linktitle: Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma  
description: Aspose.Cells for Node.js via C++ teki grafikteki eksen etiketlerini, hesaplamadan sonra nasıl okuyacağınızı öğrenin. Rehberimiz, eksen etiketlerine erişim ve retrieval, biçimlendirme ve konumlandırma gibi detayları gösterecek.  
keywords: Aspose.Cells for Node.js, grafik, eksen etiketleri, hesaplama, okuma, erişim, retrieval, biçimlendirme, konumlandırma, Node.js ve C++  
type: docs  
weight: 90  
url: /tr/nodejs-cpp/read-axis-labels-after-calculating-the-chart/  
---  

## **Olası Kullanım Senaryoları**

Grafiğin değerlerini hesapladıktan sonra eksen etiketlerini [**Chart.calculate()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#calculate--) yöntemiyle okuyabilirsiniz. Bu amaçla [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getAxisTexts--) yöntemini kullanın, bu yöntem eksen etiketlerinin listesini döndürür.

## **Grafik Hesaplandıktan Sonra Eksen Etiketlerini Okuma**

Lütfen aşağıdaki örnek kodu inceleyin; bu örnek Excel dosyasını yükler ve çalışma sayfasındaki grafiğin kategori eksen etiketlerini okur. Ardından eksen etiketlerinin değerlerini konsolda yazdırır. Referans için aşağıdaki örnek kodun konsol çıktısına bakınız.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "ReadAxisLabels_new.xlsx");

// Load the Excel file containing chart
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart
const chart = worksheet.getCharts().get(0);

// Calculate the chart
chart.calculate();

// Read axis labels of category axis
const lstLabels = chart.getCategoryAxis().getAxisTexts();

// Print axis labels on console
console.log("Category Axis Labels: ");
console.log("---------------------");

// Iterate axis labels and print them one by one
for (let i = 0; i < lstLabels.length; i++) {
console.log(lstLabels[i]);
}
```

## **Konsol Çıktısı**

{{< highlight javascript >}}  
 Category Axis Labels:  

\---------------------  

Iran  

China  

USA  

Brazil  

England  
{{< /highlight >}}  

