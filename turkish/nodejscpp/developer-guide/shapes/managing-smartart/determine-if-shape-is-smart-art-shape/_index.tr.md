---  
title: Node.js ile C++ üzerinden Şeklin Smart Art Şekli olup olmadığını belirle  
linktitle: Şekil Akıllı Sanat Şekli mi Belirle  
type: docs  
weight: 400  
url: /tr/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: Excel deki bir şeklin Smart Art şekli olup olmadığını Aspose.Cells for Node.js via C++ kullanarak nasıl belirleyeceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Smart Art Şekilleri, Microsoft Excel'de otomatik olarak karmaşık diyagramlar oluşturmanıza olanak tanıyan özel şekillerdir. Bir şeklin smart art şekli olup olmadığını veya normal şekil olduğunu [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) özelliği kullanarak bulabilirsiniz.  

## **Şekil Akıllı Sanat Şekli mi Belirle**  

Aşağıdaki örnek kod, bu ekran görüntüsünde gösterildiği gibi bir smart art şekli içeren [örnek Excel dosyasını](55541792.xlsx) yükler. Ardından, ilk şeklin [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) özelliğinin değerini yazdırır. Lütfen aşağıda verilen örnek kodun çıktılarını konsolda inceleyiniz.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **Konsol Çıktısı**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
