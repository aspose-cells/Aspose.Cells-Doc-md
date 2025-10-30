---  
title: Grafikte hangi Eksenin olduğunu Node.js ve C++ kullanarak belirleyin  
linktitle: Grafiğin hangi Eksenin varolduğunu belirle.  
description: Aspose.Cells for Node.js via C++ kullanılarak oluşturulan bir grafikte hangi eksenin var olduğunu nasıl belirleyeceğinizi öğrenin. Kılavuzumuz, kategori, değer ve ikincil eksenler dahil olmak üzere çeşitli eksenleri tanımlamanıza ve erişmenize yardımcı olur.  
keywords: Aspose.Cells for Node.js, grafik, eksen, varlık, kategori, değer, ikincil.  
type: docs  
weight: 140  
url: /tr/nodejs-cpp/determine-which-axis-exists-in-the-chart/  
---  

{{% alert color="primary" %}}  
Bazen, kullanıcıların belirli bir eksenin grafikte var olup olmadığını bilmeleri gerekir. Örneğin, bir İkincil Değer Ekseninin grafikte olup olmadığını öğrenmek isteyebilirler. Bazı grafikler, örneğin Pasta, Exploded Pasta, PastaPasta, Çubuk Pasta, 3D Pasta, 3D Exploded Pasta, Daire, Daireyle Patlatılmış vb. eksenleri içermez.  

Aspose.Cells, belirli bir eksenin grafikte var olup olmadığını belirlemek için [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) methodunu sağlar.  
{{% /alert %}}  

Aşağıdaki örnek kod, [**Chart.hasAxis(axisType, isPrimary)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#hasAxis-AxisType-boolean-) kullanarak örnek diyagramın Birincil ve İkincil Kategori ve Değer Ekseni olup olmadığını gösterir.  

## Çizelgede hangi eksenin mevcut olduğunu belirlemek için Node.js kodu  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
// Create workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Check if there are any charts before accessing
const charts = worksheet.getCharts();
if (charts.getCount() === 0) {
console.log("No charts found in the worksheet.");
return;
}

// Access the chart
const chart = charts.get(0);

// Determine which axis exists in chart
let ret = chart.hasAxis(AsposeCells.AxisType.Category, true);
console.log("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Category, false);
console.log("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, true);
console.log("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AsposeCells.AxisType.Value, false);
console.log("Has Secondary Value Axis: " + ret);
```  

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı  

Kodun konsol çıktısı aşağıda gösterilmiştir, Bu çıktı Birincil Kategori ve Değer Eksenleri için doğru, İkincil Kategori ve Değer Eksenleri için yanlış gösterir.  

{{< highlight java >}}  
Has Primary Category Axis: True  
Has Secondary Category Axis: False  
Has Primary Value Axis: True  
Has Secondary Value Axis: False  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
