---  
title: Node.js kullanarak belge dönüştürme ilerlemesini izleyin ve C++  
linktitle: Belge Dönüşüm İlerlemesini İzle  
type: docs  
weight: 970  
url: /tr/nodejs-cpp/track-document-conversion-progress/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarında belge dönüştürme ilerlemesini nasıl izleyebileceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Bazen büyük Excel dosyalarını dönüştürmek zaman alabilir. Bu süre zarfında, uygulamanızın kullanılabilirliğini artırmak için yalnızca yükleme ekranı yerine belge dönüştürme ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells for Node.js via C++, [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) arayüzü sağlayarak belge dönüştürme sürecini takip etmeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) arayüzü, kendi sınıfınızda uygulayabileceğiniz [**IPageSavingCallback.pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) ve [**IPageSavingCallback.pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) yöntemleri sağlar. Ayrıca, *TestPageSavingCallback* özelleştirilmiş sınıfında gösterildiği gibi hangi sayfaların görüntüleneceğini de kontrol edebilirsiniz.  

## **Belge Dönüşüm İlerlemesini İzle**  

Aşağıdaki kod örneği, [kaynak excel dosyasını](94896151.xlsx) yükler ve *TestPageSavingCallback* özelleştirilmiş sınıfını kullanarak dönüştürme ilerlemesini konsola yazdırır. Bu sınıf, [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) arayüzünü uygular.  

## **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Define TestPageSavingCallback class
class TestPageSavingCallback {
// Implement the required methods of this callback as needed
onPageSaving(pageIndex, fileName) {
console.log(`Saving page ${pageIndex} to ${fileName}`);
}
}

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "PagesBook1.xlsx"));

const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setPageSavingCallback(new TestPageSavingCallback());

workbook.save(path.join(outputDir, "DocumentConversionProgress.pdf"), pdfSaveOptions);
```  

*TestPageSavingCallback* özel sınıfının kodu aşağıdadır.  

```javascript
const AsposeCells = require("aspose.cells.node");

class TestPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages before page index 2.
if (args.getPageIndex() < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.getPageIndex()} of pages ${args.getPageCount()}`);

// don't output pages after page index 8.
if (args.getPageIndex() >= 8) {
args.setHasMorePages(false);
}
}
}
```  

## **Konsol Çıktısı**  

{{< highlight java >}}  

Start saving page index 0 of pages 11</br>  
End saving page index 0 of pages 11</br>  
Start saving page index 1 of pages 11</br>  
End saving page index 1 of pages 11</br>  
Start saving page index 2 of pages 11</br>  
End saving page index 2 of pages 11</br>  
Start saving page index 3 of pages 11</br>  
End saving page index 3 of pages 11</br>  
Start saving page index 4 of pages 11</br>  
End saving page index 4 of pages 11</br>  
Start saving page index 5 of pages 11</br>  
End saving page index 5 of pages 11</br>  
Start saving page index 6 of pages 11</br>  
End saving page index 6 of pages 11</br>  
Start saving page index 7 of pages 11</br>  
End saving page index 7 of pages 11</br>  
Start saving page index 8 of pages 11</br>  
End saving page index 8 of pages 11  

{{< /highlight >}}  

