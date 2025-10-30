---  
title: Resim veya Yazdırma Seçenekleri kullanarak Sayfa Dizisini ImageOrPrintOptions ile C++ kullanarak Yükleme ve Sıralama  
linktitle: ResimOluşturYazdırOptions ın PageIndex ve PageCount Özelliklerini Kullanarak Sayfaların Sıralı Olarak Görüntülenmesi  
type: docs  
weight: 110  
url: /tr/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/  
description: Aspose.Cells for Node.js via C++ kullanarak belirli Excel sayfalarını görüntüye dönüştürmeyi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Excel dosyanızın sayfa dizisini [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) ve [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--) özellikleriyle görüntü formatına dönüştürebilirsiniz. Bu özellikler, çalışma sayfanızda binlerce sayfa gibi çok sayfa olduğunda ve yalnızca bazılarını görüntülemek istediğinizde faydalıdır. Bu işlem hem işlem süresinden tasarruf sağlar hem de render işleminin bellek tüketimini azaltır.  

## **Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma**  

Aşağıdaki örnek kod, [örnek Excel dosyasını](55541781.xlsx) yükler ve sadece 4, 5, 6 ve 7. sayfaları [**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--) ve [**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--) özellikleriyle render eder. İşte kod tarafından üretilen sayfalar.  

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|  
| :- | :- |  
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleImageOrPrintOptions_PageIndexPageCount.xlsx"));
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Specify image or print options
// We want to print pages 4, 5, 6, 7
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setPageIndex(3);
opts.setPageCount(4);
opts.setImageType(AsposeCells.ImageType.Png);
// Create sheet render object
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);
// Print all the pages as images
for (let i = opts.getPageIndex(); i < sheetRender.getPageCount(); i++) {
sheetRender.toImage(i, path.join(outputDir, `outputImage-${i + 1}.png`));
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
