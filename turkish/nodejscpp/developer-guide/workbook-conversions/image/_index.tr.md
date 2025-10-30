---  
title: Resim ile Node.js kullanımı  
linktitle: Görüntü  
type: docs  
weight: 300  
url: /tr/nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cells, bir çalışma kitabından çalışsayı dışa aktarmanıza ve farklı biçimlere dönüştürmenize olanak tanır. Bu makale, bir çalışsayının farklı biçimlere nasıl dönüştürüleceğini açıklar.  
{{% /alert %}}  

## Çalışma Kitabını TIFF'e Dönüştürme  

Bir Excel dosyası çoklu sayfalar ve çok sayfalı bölümler içerebilir. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender), Excel dosyasını çoklu sayfalı TIFF'e dönüştürmenizi sağlar. Ayrıca, TIFF için çeşitli seçenekleri kontrol edebilirsiniz, örneğin [ImageOrPrintOptions.getTiffCompression()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffCompression--), [ImageOrPrintOptions.getTiffColorDepth()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTiffColorDepth--), Çözünürlük ([ImageOrPrintOptions.getHorizontalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--), [ImageOrPrintOptions.getVerticalResolution()](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)).  

Aşağıdaki kod örneği, birden çok sayfa içeren Excel dosyasını TIFF'e nasıl dönüştüreceğinizi gösterir. [Kaynak Excel dosyası](workbook-to-tiff-with-mulitiple-pages.xlsx) ve [oluşturulan TIFF görüntüsü](workbook-to-tiff-with-mulitiple-pages.tiff) referansınız için ekli.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **Çalışsayıyı Görüntüye Dönüştürme**  

Çalışma sayfaları analiz etmek istediğiniz verileri içerebilir. Örneğin, bir çalışma sayfası parametreleri, toplamları, yüzdeleri, istisnaları ve hesaplamaları içerebilir.  

Bir geliştirici olarak, çalışma sayfalarını görüntü olarak sunmanız gerekebilir. Örneğin, bir çalışma sayfasının bir görüntüsünü bir uygulamada veya web sayfasında kullanmanız gerekebilir. Bir çalışma sayfasını bir Microsoft Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belge türüne eklemek isteyebilirsiniz. Basitçe söylemek gerekirse, bir çalışma sayfasını bir görüntü olarak oluşturmak istiyorsunuz ki başka bir yerde kullanabilesiniz.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender)
[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions)
[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender)

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) sınıfı, bir çalışma sayfasını resim olarak gösteren bir sayfa kümesini temsil eder. Aşırı yüklenmiş bir yöntemi, [**SheetRender.toImage(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-string-) ile, bir çalışma sayfasını farklı özelliklerle veya seçeneklerle resim dosyasına dönüştürebilir. Bu, Buffer nesnesi döner ve bir resmi diske kaydedebilir veya akış olarak kullanabilirsiniz. Birkaç resim formatı desteklenmektedir, örneğin BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

Aşağıdaki kod örneği, bir Excel dosyasındaki bir çalışma sayfasını bir görüntü dosyasına dönüştürmenin nasıl yapıldığını gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
let path = "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif";
sr.toImage(j, path);
}
```  

{{% alert color="primary" %}}  
Şu anda, çalışma sayfalarını görüntülere dönüştürmek için API, 3D kabarcık grafiklerini desteklememektedir.  
{{% /alert %}}  

## **Çalışma Sayfasını SVG'ye Dönüştürme**  

SVG, Ölçeklenebilir Vektör Grafikleri anlamına gelir. SVG, iki boyutlu vektör grafikleri için XML standartlarına dayanan bir spesifikasyondur. 1999'dan beri World Wide Web Consortium (W3C) tarafından geliştirilen açık bir standarttır.  

Aspose.Cells for Node.js via C++, 7.1.0 sürümünden beri çalışma sayfalarını SVG resim dosyasına dönüştürmeyi sağlayabilmektedir. Aşağıdaki kod örneği, bir Excel dosyasındaki çalışma sayfasını SVG resim dosyasına nasıl dönüştüreceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **Gelişmiş Konular**  
- [Bir Excel Grafiğini Görüntüye Dönüştürme](/cells/tr/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [SVG Biçiminde Grafikleri Görüntüye Dönüştürme](/cells/tr/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Excel'den TIFF'e Dönüşüm İlerlemesini İzle](/cells/tr/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
