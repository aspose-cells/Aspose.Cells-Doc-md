---  
title: Şekil veya Grafiklerin Gölgelendirme Efekti ile Node.js ve C++ kullanarak çalışma  
linktitle: Şekil veya Grafik Gölgelendirme Efekti Çalışmak  
type: docs  
weight: 220  
url: /tr/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Aspose.Cells for Node.js via C++ kullanarak şekil veya grafiklerin gölgelendirme efektleriyle çalışma yöntemini öğrenin.  
---  

## **Olası Kullanım Senaryoları**  
Aspose.Cells for Node.js via C++, [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) özelliği ve [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) sınıfı ile şekil veya grafiklerin gölgelendirme efektleri üzerinde çalışmanıza olanak tanır. [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) sınıfı, uygulama gereksinimlerine göre farklı sonuçlar elde etmek için ayarlanabilen aşağıdaki özellikleri içerir.  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **Şekil veya Grafik Gölgelenme Efekti ile Çalışma**  
Aşağıdaki örnek kod, [orijinal excel dosyasını](5115425.xlsx) yükler ve ilk çalışma sayfasındaki ilk şekle erişir. [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) özelliğinin alt özelliklerini ayarlar ve ardından çalışma kitabını [çıktı excel dosyasına](5115411.xlsx) kaydeder.  

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

// Set the shadow effect of the shape, set its Angle, Blur, Distance and Transparency properties
const shadowEffect = shape.getShadowEffect();
shadowEffect.setAngle(150);
shadowEffect.setBlur(4);
shadowEffect.setDistance(45);
shadowEffect.setTransparency(0.3);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

