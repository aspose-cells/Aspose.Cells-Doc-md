---
title: Node.js ile C++ kullanarak Grafik Seri Değer Format Kodu Ayarlama
description: Aspose.Cells for Node.js via C++ te grafik serisinin değer format kodunu nasıl ayarlayacağınızı öğrenin. Bu kılavuz, verilerinizi doğru ve profesyonel bir şekilde sunmanıza olanak tanıyacak uygun format kodu kullanarak grafik serisi verilerinizi biçimlendirme konusunda size yardımcı olacaktır.
keywords: Aspose.Cells for Node.js, grafik serisi, değer format kodu, biçimlendirme, veri sunumu, doğruluk, profesyonellik.
linktitle: Sayı Biçimi
type: docs
weight: 100
url: /tr/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **Olası Kullanım Senaryoları**
 [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) özelliğini kullanarak grafik serisinin değer biçim kodunu ayarlayabilirsiniz. Bu özellik, yalnızca çalışma sayfası içindeki aralığa dayalı seriler için değil, aynı zamanda değer dizisi kullanılarak oluşturulan seriler için de uygundur.

## **Grafik Serisinin Değer Biçim Kodunu Ayarlayın**
 Aşağıdaki örnek kod, boş grafiğe seri ekler ve bu seriyi daha önce serisi olmayan nesneye ekler. Seriyi değer dizisi kullanarak ekler ve ardından [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) özelliği ile biçimlendirir, ve sayı 10.000 olan gösterim $#,##0 olur. Ekran görüntüsü, kodun etkisini örnek Excel dosyasında gösterir.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Örnek Kod**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
