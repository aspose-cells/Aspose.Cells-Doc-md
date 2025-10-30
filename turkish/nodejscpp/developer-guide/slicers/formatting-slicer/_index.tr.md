---  
title: Node.js ve C++ kullanarak Dilimleyiciyi Biçimlendirme  
linktitle: Dilimleyici Biçimlendirme  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/formatting-slicer/  
---  

## **Olası Kullanım Senaryoları**  

 Microsoft Excel'de dilimleyiciyi, kolon sayısını ayarlayarak veya stilini belirleyerek biçimlendirebilirsiniz. Aspose.Cells for Node.js via C++ aynı zamanda bunu [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) ve [**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--) özellikleriyle yapmanıza izin verir.  

## **Dilimleyici Biçimlendirme**  

Lütfen aşağıdaki kodu görün. İçinde bir dilimleyici içeren [örnek Excel dosyasını](67338473.xlsx) yükler. Dilimleyiciye erişir ve sütun sayısını ve stil türünü ayarlar ve bu şekilde [çıkış Excel dosyasını](67338474.xlsx) kaydeder. Ekran görüntüsü, örnek kodun çalıştırılmasından sonra dilimleyicinin nasıl göründüğünü gösterir.  

![todo:image_alt_text](formatting-slicer_1.png)  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
