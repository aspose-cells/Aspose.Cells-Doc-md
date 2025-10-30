---  
title: Node.js üzerinden C++ kullanarak çalışma kitabını önizleyin  
linktitle: Çalışma kitabını önizle 
type: docs  
weight: 70  
url: /tr/nodejs-cpp/workbook-and-worksheet-preview/  
description: Aspose.Cells, Microsoft Excel kurulumuna gerek kalmadan Node.js üzerinden C++ kullanarak Excel dosyalarını yazdırmayı ve önizlemeyi destekler.  
---  

## **Yazdırma Önizlemesi**  

Milyonlarca sayfaya sahip Excel dosyalarının PDF veya resimlere dönüştürülmesi gereken durumlar olabilir. Bu tür dosyaları işlemek çok zaman ve kaynak tüketir. Bu durumda, Çalışma Kitabı ve Çalışma Sayfası Yazdırma Önizleme özelliği faydalı olabilir. Bu dosyaları dönüştürmeden önce toplam sayfa sayısını kontrol ederek dosyanın dönüştürülüp dönüştürülmeyeceğine karar verebilir. Bu makale, toplam sayfa sayısını öğrenmek için [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) sınıflarının kullanılmasına odaklanır.  

Aspose.Cells, yazdırma önizleme özelliği sağlar. API, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) ve [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) sınıflarını içerir. Tüm çalışma kitabının yazdırma önizlemesini oluşturmak için, [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) sınıfından bir örnek oluşturun ve yapıcıya [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) nesnelerini geçirin. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) sınıfı, oluşturulan önizlemedeki sayfa sayısını döndüren bir [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) metot sağlar. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) sınıfına benzer şekilde, [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) sınıfı belirli bir çalışma sayfası için yazdırma önizlemesi oluşturmak için kullanılır. Bir çalışma sayfasının yazdırma önizlemesini oluşturmak için [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) sınıfından bir örnek oluşturun ve yapıcıya [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) nesnelerini geçirin. [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) sınıfı ayrıca, oluşturulan önizlemede sayfa sayısını döndüren [**getEvaluatedPageCount**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/#getEvaluatedPageCount--) metodunu sağlar.  

Aşağıdaki kod parçacığı, [örnek excel dosyası](94896177.xlsx) kullanılarak hem [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/workbookprintingpreview/) hem de [**SheetPrintingPreview**](https://reference.aspose.com/cells/nodejs-cpp/sheetprintingpreview/) sınıflarının kullanımını gösterir.  

### **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

const filePath = path.join(sourceDir, "Book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const imgOptions = new AsposeCells.ImageOrPrintOptions();
const preview = new AsposeCells.WorkbookPrintingPreview(workbook, imgOptions);
console.log("Workbook page count: " + preview.getEvaluatedPageCount());

const preview2 = new AsposeCells.SheetPrintingPreview(workbook.getWorksheets().get(0), imgOptions);
console.log("Worksheet page count: " + preview2.getEvaluatedPageCount());
```  

Yukarıdaki kodun yürütülmesiyle oluşturulan çıktı aşağıdaki gibidir.  

### **Konsol Çıktısı**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **Gelişmiş Konular**  
- [Elektronik Tabloları Görüntüleme Yazı Tiplerini Yapılandırma](/cells/tr/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [Çalışma Sayfasını Görüntüye Dönüştür - Veri etrafındaki boşlukları kaldır](/cells/tr/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [Çalışsayısı veya Sayfa Görseline ve Sayfa Sayfasına Çalışsayısı Dönüştürme](/cells/tr/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [ImageOrPrint Seçenekleri Kullanarak Çalışma Sayfasını Görüntüye Dönüştürme](/cells/tr/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar](/cells/tr/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [Belirtilen Genişlik ve Yükseklikte Çalışsayısı veya Tabloyu Resme Dışa Aktarma](/cells/tr/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [ImageOrPrintOptions Kullanarak Çalışma Sayfalarından Resimleri Çıkarma](/cells/tr/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [Çalışma Sayfasının Önizlemesini Oluşturun](/cells/tr/nodejs-cpp/generate-thumbnail-of-the-worksheet/)  
- [Hiçbir şey Yazdırılacak Değilken Boş Sayfa Çıktısı](/cells/tr/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [Sayfa Ayarları ve Yazdırma Seçenekleri](/cells/tr/nodejs-cpp/page-setup-and-printing-options/)  
- [Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma](/cells/tr/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [Çalışsayısını Grafiksel Ortama Dönüştürme](/cells/tr/nodejs-cpp/render-worksheet-to-graphic-context/)  
- [Çalışma Kitabı Rendeleme İçin Bireysel veya Özel Font Kümesini Belirtin](/cells/tr/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)   

{{< app/cells/assistant language="nodejs-cpp" >}}
