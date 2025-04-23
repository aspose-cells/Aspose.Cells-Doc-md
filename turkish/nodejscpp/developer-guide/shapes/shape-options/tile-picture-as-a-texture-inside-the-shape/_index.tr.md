---  
title: Node.js ile C++ kullanarak Çerçeve İçinde Küçük Bir Resmi Doku Olarak Döşeyin  
linktitle: Resmin Bir Desen Olarak Şeklin İçine Yerleştirilmesi  
type: docs  
weight: 1700  
url: /tr/nodejs-cpp/tile-picture-as-a-texture-inside-the-shape/  
description: Aspose.Cells for Node.js via C++ kullanarak şekil içinde küçük bir resmi doku olarak döşemeyi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Resim küçükse ve kalitesini kaybetmeden şeklin tüm yüzeyini kaplamıyorsa, koyulma seçeneğiniz vardır. Koyulma, küçük bir resmi tekrarlayarak şekil yüzeyini doldurur.  

## **Resmin Bir Desen Olarak Şeklin İçine Yerleştirilmesi**  

Şekil yüzeyini bazı görüntülerle doldurabilir ve [**Shape.isTiling()**](https://reference.aspose.com/cells/nodejs-cpp/texturefill/#isTiling--) özelliği kullanarak döşeyebilir ve **true** ayarını yapabilirsiniz. Lütfen aşağıdaki örnek kodu, örnek Excel dosyasını ([46465050.xlsx](46465050.xlsx)) ve ekran görüntüsünü inceleyin.  

## **Ekran Görüntüsü**  

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleTextureFill_IsTiling.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape inside the worksheet
const shape = worksheet.getShapes().get(0);

// Tile Picture as a Texture inside the Shape 
shape.getFill().getTextureFill().setIsTiling(true);

// Save the output Excel file
workbook.save(path.join(outputDir, "outputTextureFill_IsTiling.xlsx"));
```  

