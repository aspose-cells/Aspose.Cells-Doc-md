---  
title: Node.js ve C++ kullanarak Hücre Aralığını Veri Etiketi Olarak Gösterme  
linktitle: Veri Etiketleri olarak Hücre Aralığını Gösterme  
description: Aspose.Cells for Node.js via C++ kullanarak grafiklerde hücre aralığını veri etiketi olarak gösterme yöntemini öğrenin. Rehberimiz, etiketleri veri kaynağınıza nasıl bağlayacağınızı ve doğru ve anlamlı bilgiler sunmak için nasıl biçimlendireceğinizi gösterecektir.  
keywords: Aspose.Cells for Node.js via C++, grafik çizimi, veri etiketleri, hücre aralığı, veri kaynağı, biçimlendirme, doğruluk, anlamlı bilgi.  
type: docs  
weight: 130  
url: /tr/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
Microsoft Excel 2013'te, veri etiketleri için hücre aralığını görüntüleyebilirsiniz. Aspose.Cells for Node.js bu özelliği destekler.  
{{% /alert %}}  

## **Hücre Aralığını Veri Etiketleri Olarak Göster'i seçenek kutusu**  

Microsoft Excel'de hücre aralığını veri etiketleri olarak göstermek için:  

1. Seri veri etiketlerini seçin ve bağlam menüsünü açmak için sağ tıklayın.  
1. **Veri Etiketlerini Biçimlendir**'i seçin. Etiket seçenekleri görüntülenir.  
1. **Etiket İçeriği - Hücrelerden Değer İçerir** seçeneğini işaretleyin veya temizleyin.  

Aşağıdaki örnek kod, bir grafik serisi veri etiketlerine erişir ve [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) özelliğini **true** olarak ayarlayarak **Etiket İçerir - Hücrelerden Değer** seçeneğini seçer.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

