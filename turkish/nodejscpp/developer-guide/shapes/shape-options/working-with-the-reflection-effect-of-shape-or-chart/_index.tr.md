---
title: Şekil veya Grafiklerin Yansıma Efekti ile Node.js ve C++ kullanarak çalışma
linktitle: Şekil veya Grafik Yansıma Efekti Çalışmak
type: docs
weight: 210
url: /tr/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Aspose.Cells for Node.js via C++ kullanarak şekiller veya grafiklerin yansıma etkisi ile nasıl çalışılır, çeşitli yansıma özellikleri ayarlayarak istenilen sonuçlara ulaşın.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells for Node.js via C++, [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) özelliği ve [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) sınıfı ile şekil veya grafiklerin yansıma efektleri üzerinde çalışmanıza olanak tanır. [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) sınıfı, uygulama gereksinimlerine göre farklı sonuçlar elde etmek için ayarlanabilen aşağıdaki özellikleri içerir.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **Şekil veya Grafik Yansıma Efekti Çalışmak**
Aşağıdaki örnek kod, [orijinal excel dosyasını](5115424.xlsx) yükler ve varsayılan çalışma sayfasındaki ilk şekle erişir. [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) sınıfının farklı özelliklerini ayarlar ve ardından çalışma kitabını [çıktı excel dosyasına](5115423.xlsx) kaydeder.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
const reflectionEffect = shape.getReflection();
reflectionEffect.setBlur(30);
reflectionEffect.setSize(90);
reflectionEffect.setTransparency(0);
reflectionEffect.setDistance(80);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
