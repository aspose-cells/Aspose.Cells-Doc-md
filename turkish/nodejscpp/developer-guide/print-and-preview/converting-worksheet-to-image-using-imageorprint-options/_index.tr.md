---  
title: Node.js kullanarak C++ ile Görüntü veya Yazdırma Seçenekleriyle Çalışma Sayfasını Görüntüye Dönüştürme  
linktitle: Resim veya Yazdır Seçeneklerini Kullanarak Çalışma Sayfasını Resme Dönüştürme  
type: docs  
weight: 90  
url: /tr/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Aspose.Cells for Node.js via C++ kullanarak çalışma sayfasını görüntü dosyasına dönüştürmeyi ve çeşitli görüntü ve yazdırma seçenekleri uygulamayı öğrenin.   
---  

{{% alert color="primary" %}}  
Bu belge, bir çalışma sayfasını bir resim dosyasına dönüştürme ve resim için farklı resim ve yazdır seçeneklerini (çözünürlük, TIFF sıkıştırma, resim formatı ve sayfa kalitesi gibi) uygulama konusunda ayrıntılı bir anlayış sağlamak amacıyla tasarlanmıştır.  
{{% /alert %}}  

## **Çalışma Sayfalarını Resim Olarak Kaydetme - Farklı Yaklaşımlar**  

Bazen çalışsayılarınızı resimsel bir temsil olarak sunmanız gerekebilir. Çalışsayı resimlerini uygulamalarınıza veya web sayfalarınıza eklemeniz veya kullanmanız gerekebilir. Resimlerini bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemeniz veya bunları başka bir senaryoda kullanmanız gerekebilir. Basitçe başka bir yerde kullanabilmek için çalışsayısının bir resim olarak görüntülenmesini istersiniz. Aspose.Cells, Excel dosyalarındaki çalışsayıları resme dönüştürmeyi destekler. Ayrıca, Aspose.Cells, resim formatı, çözünürlük (dikey ve yatay), resim kalitesi ve diğer resim ve yazdırma seçenekleri belirleme gibi farklı seçenekleri destekler.  

Office Otomasyonu deneyebilirsiniz, ancak Office otomasyonunun kendi zayıf noktaları vardır. Güvenlik, kararlılık, ölçeklenebilirlik ve hız, fiyat ve özellikler gibi birkaç nedeni ve sorun içerir. Kısacası, birçok nedeni vardır ve en önemlisi Microsoft'un kendisinin yazılım çözümlerinden Office otomasyonuna karşı şiddetle tavsiye etmemesidir.  

Bu makale, Visual Studio .NET'te bir konsol uygulaması oluşturmayı, Aspose.Cells API'sını kullanarak bir çalışma sayfasını farklı resim ve yazdır seçenekleriyle bir resme dönüştürmeyi ve bunu birkaç basit satır kodla gerçekleştirmeyi gösteriyor.  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) sınıfı, çalışma sayfası için görüntüler oluşturmak amacıyla bir çalışma sayfasını temsil eder, doğrudan çalışma sayfasını belirttiğiniz özelliklerle veya seçeneklerle görüntü dosyasına dönüştürebilen aşırı yüklenmiş [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) yöntemine sahiptir. Bir nesne döndürebilir ve bu nesneye görüntü dosyasını disk/akışa kaydedebilirsiniz. Desteklenen birkaç görüntü formatı vardır, örn BMP, PNG, GIFF, JPEG, TIFF, EMF ve diğerleri.  

## **Aspose.Cells'ı Kullanarak Resme Dönüştürme İçin Resim veya Yazdır Seçeneklerini Kullanma**  

### **Microsoft Excel'de şablon çalışma kitabı oluşturma**  

MS Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim. Şimdi, şablon dosyasının "Sheet1" adlı çalışma sayfasını "SheetImage.tiff" adlı bir görüntü dosyasına dönüştüreceğim ve yatay ve dikey çözünürlük, TiffCompression vb. gibi farklı görüntü seçenekleri uygulayacağım.  

### **Aspose.Cells'i İndirin ve Yükleyin**  

İlk olarak, [indir](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. Bunu geliştirme bilgisayarınıza yükleyin. Tüm [Aspose](http://www.aspose.com/) bileşenleri kurulduğunda değerlendirme modunda çalışır. Değerlendirme modu zaman sınırı olmayan ve yalnızca üretilen belgelere filigran ekleyen bir moddur.  

### **Bir Proje Oluşturun**  

Tercih ettiğiniz geliştirme ortamınızı (örneğin, Visual Studio) başlatın. Yeni bir konsol uygulaması oluşturun.  

### **Referanslar Ekle**  

Bu proje Aspose.Cells kullanacaktır. Bu yüzden, projenize Aspose.Cells bileşenine referans eklemeniz gerekir. Örneğin, ….\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node referansı ekleyin.  

### **Çalışma Sayfasını Bir Görüntü Dosyasına Dönüştürme**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **Dönüşüm Seçenekleri**  

Belirli sayfaları resme kaydetmek mümkündür. Aşağıdaki kod, bir çalışma kitabındaki ilk ve ikinci çalışsayılarını JPG resimlerine dönüştürür.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **WorkbookRender kullanarak Görüntü dönüşümü**  

Bir TIFF görüntüsü birden fazla çerçeve içerebilir. Tüm çalışma kitabını tek bir TIFF görüntüsüne çoklu çerçeve veya sayfa olarak kaydedebilirsiniz:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
