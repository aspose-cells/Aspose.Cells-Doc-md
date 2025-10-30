---
title: Node.js aracılığıyla C++ kullanarak Excel in TIFF e Dönüşüm Progresini Takip Etme
linktitle: Excel den TIFF e Dönüşüm İlerlemesini İzle
type: docs
weight: 190
url: /tr/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarının TIFF e dönüşüm ilerlemesini nasıl takip edeceğinizi öğrenin. Dönüşüm sırasında kullanıcı deneyimini artırın.
---

## **Olası Kullanım Senaryoları**

Bazen büyük Excel dosyalarını dönüştürmek zaman alabilir. Bu süre zarfında, uygulamanızın kullanılabilirliğini artırmak için yalnızca yükleme ekranı yerine belge dönüştürme ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells for Node.js via C++, [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) arayüzü sağlayarak belge dönüştürme sürecini takip etmeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) arayüzü, kendi sınıfınızda uygulayabileceğiniz [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) ve [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) yöntemleri sağlar. Ayrıca, *TestPageSavingCallback* özelleştirilmiş sınıfında gösterildiği gibi hangi sayfaların görüntüleneceğini de kontrol edebilirsiniz.

## **Excel'den TIFF'e Dönüşüm İlerlemesini İzle**

Aşağıdaki kod örneği, [kaynak excel dosyasını](95584311.xlsx) yükler ve *TestPageSavingCallback* özel sınıfını kullanarak dönüşüm ilerlemesini konsolda gösterir. Oluşturulan çıktı dosyası referans için ektedir.

[Output File](95584312.tiff)

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();

// Define TestTiffPageSavingCallback
class TestTiffPageSavingCallback {
// Implement required methods for the callback here
}

opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

Aşağıda, *TestTiffPageSavingCallback* özel sınıfının kodu yer almaktadır.

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages before page index 2.
if (args.pageIndex < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages after page index 8.
if (args.pageIndex >= 8) {
args.setHasMorePages(false);
}
}
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
