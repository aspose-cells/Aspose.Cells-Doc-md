---  
title: Node.js ve C++ kullanarak Çalışma Sayfasını Görsele Dönüştürme ve Sayfa Başına Görsele Dönüştürme  
linktitle: Çalışma Sayfasını Görüntüye Dönüştürme ve Sayfa Başına Çalışma Sayfasını Görüntüye Dönüştürme  
type: docs  
weight: 80  
url: /tr/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
Bu belge, geliştirilicilere bir çalışma sayfasını görsel dosyasına dönüştürme ve çok sayfalı çalışma sayfasını her sayfa için ayrı görsel dosyasına dönüştürme konusunda detaylı bilgi sağlamayı amaçlamaktadır.  

Bazı durumlarda, çalışma sayfalarını örneğin uygulamalarda veya web sayfalarında kullanmak için resim olarak sunmanız gerekebilir. Resimleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemek veya başka bir senaryoda kullanmak gerekebilir. Temel olarak, çalışma sayfasını bir resim olarak oluşturmak istersiniz. Aspose.Cells, Microsoft Excel dosyalarındaki çalışma sayfalarını resimlere dönüştürmeyi destekler. Ayrıca, Aspose.Cells, bir çalışma kitabını birden fazla resim dosyasına, sayfa başına bir tane olmak üzere dönüştürmeyi destekler.  

Bunu başarmak için Office Automation'ı kullanabilirsiniz, ancak Office Automation'ın kendi dezavantajları vardır. Güvenlik, istikrar, ölçeklenebilirlik/hız, fiyat ve özellikler gibi birçok neden ve sorun bulunmaktadır. Kısacası, birçok neden bulunmaktadır, ancak ana nedenlerden biri Microsoft'un Office Automation'u kesinlikle önermemesidir.  
{{% /alert %}}  

## **Aspose.Cells for Node.js via C++ kullanarak Çalışma Sayfasını Görsel Dosyasına Dönüştürme**  

Bu makale, bir konsol uygulaması oluşturmayı, çalışma sayfasını görsele dönüştürmeyi ve Aspose.Cells API kullanarak kod satırlarını en basit ve birkaç adımda çalışma sayfasını her biri ayrı görsel dosyası olacak şekilde dönüştürmeyi gösterir.  

Programınıza veya projenize [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/) gibi render işlevselliğiyle ilgili birkaç değerli sınıfı içe aktarmanız gerekir. [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) sınıfı, görsellerin oluşturulacağı çalışma sayfasını temsil eder ve herhangi bir özellik veya seçenek ayarlayarak doğrudan çalışma sayfasını görsellere dönüştürebilen aşırı yüklenmiş [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) metoduna sahiptir. Bu, bir görsel nesnesi dönebilir ve görsel dosyasını disk/akışa kaydedebilirsiniz. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF ve diğerleri gibi birkaç görsel formatı desteklenmektedir.  

Bu makalede şunları açıklar:  

- Bir çalışma sayfasını bir resme dönüştürme  
- Bir çalışma sayfasındaki her sayfayı bir resme dönüştürme  

Bu görev, Aspose.Cells'ı kullanarak bir şablon çalışma kitabındaki bir çalışma sayfasını bir resim dosyasına dönüştürmenin nasıl yapıldığını gösterir.  

### **Proje Kurulumu**  

1. İlk olarak, [Aspose.Cells for Node.js via C++ İndir](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Geliştirme bilgisayarınıza yükleyin. Tüm [Aspose](http://www.aspose.com/) bileşenleri yüklendiğinde değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere su işaretleri ekler. Şimdi geliştirme ortamınızı başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek Node.js konsol uygulaması kullanır, ancak Node.js ile entegre edebileceğiniz herhangi bir kurulum kullanabilirsiniz. Oluşturulan projeye Aspose.Cells referansı ekleyin.  

### **Çalışma Sayfasını Resim Dosyasına Dönüştürme**  

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook.xlsx** (1 çalışma sayfası). Daha sonra, şablon dosyasının Sheet1 çalışma sayfasını SheetImage.jpg adında bir resim dosyasına dönüştürdüm.  

Bileşen tarafından görevi tamamlamak için kullanılan kod aşağıda verilmiştir. Bu kod, **Testbook.xlsx**'teki Sheet1'i, bu dönüşümün ne kadar kolay olduğunu açıklamak için bir resim dosyasına dönüştürür.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Sayfa Başına Görüntü Dosyasına Dönüştürmek İçin Aspose.Cells for Node.js via C++ Kullanımıyla Çalışma Sayfasını Dönüştürme**  

Bu örnek, birkaç sayfası olan bir şablon çalışma kitabından bir çalışma sayfasını bir resim dosyasına dönüştürmek için Aspose.Cells'ı kullanmanın nasıl yapıldığını göstermektedir.  

### **Sayfa bazında Çalışma Sayfasını Görüntüye Dönüştürme**  

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook2.xlsx** (1 çalışma sayfası).  

Şimdi, şablon dosyasının Sheet1 çalışma sayfasını resim dosyalarına dönüştür (sayfa başına bir dosya). Zaten kopyalama görevini gerçekleştirmek için konsol uygulaması oluşturmuştum, bu nedenle konsol uygulaması oluşturma adımlarını atlayacak ve doğrudan çalışma sayfası dönüşüm adımlarına geçeceğim.  

Bunu gerçekleştirmek için kullanılan kod aşağıdadır. Sheet1 in Testbook2.xlsx dosyasını sayfa başına görüntü dosyalarına dönüştürür.  

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
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


