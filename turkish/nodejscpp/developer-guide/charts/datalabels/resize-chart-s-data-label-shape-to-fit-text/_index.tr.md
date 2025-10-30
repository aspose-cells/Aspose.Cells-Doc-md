---  
title: Node.js ve C++ kullanarak Çizelgenin Veri Etiketi Şeklini Metne Uygun Boyuta Getirme  
linktitle: Veri Etiket Şeklini Metne Sığacak Şekilde Yeniden Boyutlandır  
description: Aspose.Cells for Node.js via C++ teki bir çizelgedeki veri etiketi şeklini metne uygun hale getirmek için yeniden boyutlandırmayı nasıl yapacağınızı öğrenin. Rehberimiz, etiket kutusunun boyutunu ve şeklini ayarlama, metnin düzgün şekilde gösterilmesini sağlama ve kesme veya üst üste binmeyi önleme konusunda rehberlik edecektir.  
keywords: Aspose.Cells for Node.js via C++, çizelgeleme, veri etikeleri, şekil yeniden boyutlandırma, metin uyumu, kesme, üst üste binme  
type: docs  
weight: 220  
url: /tr/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
Excel uygulaması, grafiklerin Veri Etiketleri için **Metni Sığdırmak İçin Şekli Yeniden Boyutlandır** seçeneğini sağlar.  
{{% /alert %}}  

## **Microsoft Excel'de Metni Sığdırmak İçin Grafiğin Veri Etiket Şeklini Yeniden Boyutlandırma**  

Bu seçenek, grafikte herhangi bir veri etiketini seçerek Excel arayüzünden erişilebilir. Sağ tık yapın ve **Veri Etiketlerini Biçimlendir** menüsünü seçin. **Boyut ve Özellikler** sekmesi altında, **Hizalama** genişletildiğinde, ilgili özellikleri ve **Metni Düzeltmek İçin Şekli Yeniden Boyutlandır** seçeneğini göreceksiniz.  

## **Aspose.Cells for Node.js via C++ kullanarak Çizelge Veri Etiketi Şeklini Metne Uygun Boyuta Getirmek**  

Excel'in veri etiketi şekillerini metne göre yeniden boyutlandırma özelliğini taklit etmek için, Aspose.Cells API'leri Boolean türü [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--) özelliğini ortaya çıkardı. Aşağıdaki kod parçası, [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--) özelliğinin basit kullanım senaryosunu göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
