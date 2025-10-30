---
title: C++ üzerinden Node.js ile Akıllı Sanatı Grup Şekline Dönüştür
linktitle: Akıllı Sanatı Grup Şekline Dönüştür
type: docs
weight: 200
url: /tr/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **Olası Kullanım Senaryoları**

[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--) yöntemi kullanılarak Akıllı Sanat Şekli Grup Şekline dönüştürülebilir. Bu, akıllı sanat şekliyle bir grup şekli gibi ilgilenmenizi sağlar. Sonuç olarak, grup şeklinin bireysel parçalarına veya şekillerine erişebilirsiniz.

## **Akıllı Sanatı Grup Şekline Dönüştür**

Aşağıdaki örnek kod, bu ekran görüntüsünde gösterildiği gibi bir akıllı sanat şekli içeren [örnek Excel dosyasını](55541793.xlsx) yükler. Ardından, akıllı sanat şeklini grup şekline dönüştürür ve Shape.isGroup özelliğini yazdırır. Lütfen aşağıda verilen örnek kodun çıktılarını konsolda inceleyiniz.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **Konsol Çıktısı**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
