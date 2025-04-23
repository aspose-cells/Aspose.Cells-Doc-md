---  
title: Bir Sayfa Aralığını Node.js ile C++ kullanarak Görüntüye Dışa Aktarma  
linktitle: Çalışma Sayfasındaki Hücre Aralığını Bir Görüntüye Aktarma  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **Olası Kullanım Senaryoları**  

Aspose.Cells for Node.js via C++ kullanarak bir sayfa veya alanın görüntüsünü çıkarabilirsiniz. Ancak bazen, yalnızca bir hücre aralığını görüntüye aktarmanız gerekebilir. Bu makale, bunu nasıl yapacağınızı açıklar.  

## **Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar**  

Bir alanın görüntüsünü almak için, yazdırma alanını istediğiniz aralığa ayarlayın ve tüm kenar boşluklarını 0 yapın. Ayrıca [**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--) değerini **true** olarak ayarlayın. Aşağıdaki kod D8:G16 aralığının görüntüsünü alır. Aşağıda, kodda kullanılan [örnek Excel dosyasının](47153160.xlsx) ekran görüntüsü bulunmaktadır. Kodu herhangi bir Excel dosyasıyla deneyebilirsiniz.  

## **Örnek Excel Dosyası ve Dışa Aktarılan Görüntü Ekran Görüntüsü**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Kod çalıştırıldığında yalnızca D8:G16 aralığının bir görüntüsü oluşturulur.  

**![todo:image_alt_text](Output-Image.png)**  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  

