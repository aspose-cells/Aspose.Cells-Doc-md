---  
title: Şekil veya Grafiklerin Parlaklık Efekti ile Çalışmak Node.js üzerinden C++  
linktitle: Şekil veya Grafik Gölgelendirme Efekti Çalışmak  
type: docs  
weight: 240  
url: /tr/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Aspose.Cells for Node.js via C++ kullanarak şekil veya grafiklerin parlaklık efektleriyle çalışmayı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  
Aspose.Cells, şekil veya grafiğin parlaklık efektleri ile çalışmak için [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) özelliği ve [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) sınıfını sağlar. [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) sınıfı, uygulama gereksinimlerine göre farklı sonuçlar elde etmek için ayarlanabilen aşağıdaki özellikleri içerir.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **Şekil veya Grafik Gölgelendirme Efekti Çalışmak**  
Aşağıdaki örnek kod, [source excel dosyasını](5115407.xlsx) yükler, ilk çalışma sayfasındaki ilk şekli erişir ve [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) özellik alt özelliklerini ayarlar, ardından çalışma kitabını [çıktı excel dosyasına](5115414.xlsx) kaydeder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
