---  
title: Excel i Pdf, Görüntü ve diğer biçimlere dönüştürün  
linktitle: Çalışma Kitabı Dönüşümleri  
type: docs  
weight: 65  
url: /tr/nodejs-cpp/convert-workbook-to-different-formats/  
description: Excel dosyalarını Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML ve daha fazlasına dönüştürmek için Node.js i C++ ile kullanın.  
---  

{{% alert color="primary" %}}  
Aspose.Cells, birçok biçim arasında dönüşümü destekler. Teknik olarak, dönüştürme, bir elektronik tabloyu bir dosya biçiminde yüklemek ve başka bir biçimde kaydetmek anlamına gelir.  
{{% /alert %}}  

## **Excel Çalışma Kitabını PDF'e Dönüştür**  
PDF dosyaları, kuruluşlar, devlet kurumları ve bireyler arasında belge değişiminde geniş ölçüde kullanılır. Standart bir belge biçimidir ve yazılım geliştiriciler genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmek için bir yol bulmaları istenir.  

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **Excel Çalışma Kitabını JPG'e Dönüştür**  
Aspose.Cells, Excel dosyalarını JPG'ye dönüştürmeyi destekler. Aşağıdaki kod örneği, çalışma kitabını JPG olarak nasıl kaydedeceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **Excel Çalışma Kitabını Görüntüye Dönüştür**  
Aspose.Cells, Excel dosyalarını görüntüye dönüştürmeyi destekler. Aşağıdaki kod örneği, çalışma kitabını görüntü olarak nasıl kaydedeceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **Excel Çalışma Kitabını XPS'ye Dönüştürme**  
XPS belge formatı, her bir sayfanın düzenini ve her bir sayfanın görsel görünümünü tanımlayan yapılandırılmış XML işaretleme ve belgelerin dağıtımı, arşivleme, işleme ve yazdırma kurallarıyla birlikte renderleme kurallarından oluşur.  

XPS için işaretleme dili, XAML'nin bir alt kümesi olup Windows Presentation Foundation (WPF) temel yapı taşlarını kullanarak belgelere vektör grafik öğelerini dahil etmesine izin verir. Kullanılan öğeler, yol ve diğer geometrik temel yapı taşları terimleriyle tanımlanır.  

Bir XPS dosyası aslında belgeyi oluşturan dosyaları içeren Open Packaging Conventions kullanan bir Unicode ZIP arşividir. Bunlar, her sayfa için bir XML işaretleme dosyasını, metni, gömülü yazı tiplerini, rastgele görüntüleri ve 2D vektör grafikleri yanı sıra dijital hak yönetimi bilgilerini içerir. Bir XPS dosyasının içeriği, ZIP dosyalarını destekleyen bir uygulamada açılarak kolayca incelenebilir.  

Aspose.Cells 6.0.0'dan itibaren Microsoft Excel'den XPS dönüşümü desteklenmektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **Excel'i Ods, Sxc ve Fods (OpenOffice / LibreOffice Calc) formatlarına dönüştür**  
Aspose.Cells, Excel dosyalarını Ods, Sxc ve Fods dosyalarına dönüştürmeyi destekler. Aşağıdaki kod örneği, [şablon](book1.xlsx) dosyasını Ods, Sxc ve Fods dosyasına nasıl dönüştüreceğinizi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **Excel Çalışma Kitabını MHTML Dosyalarına Dönüştürme**  
MHTML, normal HTML'yi dış kaynaklarla (genellikle bağlantılı olarak bulunan, resimler, animasyonlar, sesler vb.) tek bir dosyaya birleştirir. Bunlar, .mht dosya uzantılı e-postalar için kullanılır.  

Aspose.Cells, MHTML dosyalarını okuma ve yazma desteği sağlamaktadır.  

Aşağıdaki kod örneği, bir çalışma kitabını MHTML dosyası olarak kaydetmenin nasıl yapıldığını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **Excel Çalışma Kitabını HTML'ye Dönüştürme**  
Aspose.Cells API, elektronik tabloyu HTML formatına aktarmayı destekler. Bu amaçla, Aspose.Cells [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) sınıfını kullanarak çıktı HTML'sinin çeşitli yönlerini kontrol etme esnekliği sağlar.  

Aşağıdaki kod örneği, bir çalışma kitabını HTML dosyası olarak kaydetme yöntemini gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **HTML için Görüntü Tercihlerini Ayarlama**  
8.0.2 sürümünden itibaren, Aspose.Cells [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) sınıfı için [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) sınıfını açtı ve geliştiricilerin, elektronik tabloları HTML formatına kaydederken resim tercihini belirtmelerine olanak tanıdı.  

Uygulanabilecek bazı görüntü ayarlarının detayları aşağıda verilmiştir.  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): Görüntü türünü belirtir. Lütfen not edin, tüm şekiller, grafikler de dahil olmak üzere çıktı HTML'de resim olarak oluşturulur.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--): JPG olarak belirtildiğinde, [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) parametresi kullanıldığında görüntü kalitesini 0 ile 100 arasında belirler.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): Görselin dikey düzeyde inç başına nokta cinsinden çözünürlüğünü alır veya ayarlar.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): Görselin yatay düzeyde inç başına nokta cinsinden çözünürlüğünü alır veya ayarlar.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/): [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) parametresi TIFF olarak belirtildiğinde, görüntülerin sıkıştırma türünü alır veya ayarlar.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): Görüntü biçimi Png olarak belirtildiğinde bir görüntünün arka planının saydam olup olmayacağını belirtir.  

## **Excel Çalışma Kitabını Markdown'a Dönüştür**  
Aspose.Cells API, elektronik tabloları Markdown formatına da dışa aktarma desteği sağlar. Aktif sayfayı Markdown'a aktarmak için [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) metodunun ikinci parametresi olarak [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) kullanın. Ayrıca, sayfayı Markdown'a dışa aktarma için ek ayarlar belirlemek amacıyla [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) sınıfını kullanabilirsiniz.  

Aşağıdaki kod örneği, [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum üyesi kullanılarak aktif sayfayı Markdown'e dışa aktarmayı göstermektedir. Lütfen kod tarafından oluşturulan [çıktı Markdown dosyasını](md_sample.txt) inceleyin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **Excel Çalışma Kitabını JSON'a Dönüştür**  
Aspose.Cells, bir çalışma kitabını Json (JavaScript Nesne Notasyonu) dosyasına dönüştürmeyi destekler.  

Aşağıdaki kod örneği, [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum üyesi kullanılarak aktif sayfayı Json'a dışa aktarmayı göstermektedir. Lütfen kodu, [kaynak dosyasını](Book1.xlsx) Json çıktısına dönüştürmek için kullanın.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Excel'i XML'e Dönüştür**  
Aspose.Cells, bir çalışma kitabını Excel 2003 Elektronik Tablo XML ve düz XML veriye dönüştürmeyi destekler.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **Excel Çalışma Kitabını TIFF'e Dönüştür**  
Aspose.Cells, bir çalışma kitabını TIFF dosyasına dönüştürmeyi destekler.  

Aşağıdaki kod parçası, Excel'i TIFF'e dönüştürmeyi göstermektedir:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **Excel Çalışma Kitabını DOCX'e Dönüştür**  
Aspose.Cells API, elektronik tabloları DOCX formatına dönüştürme desteği sağlar. Çalışma kitabını DOCX'e aktarmak için [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) parametresi ile [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) metodunu kullanın. Ayrıca, sayfayı DOCX'e aktarmak için ek ayarları belirlemek amacıyla [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) sınıfını kullanabilirsiniz.  

Aşağıdaki kod örneği, [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum üyesi kullanılarak aktif sayfayı DOCX'e aktarmayı göstermektedir. Lütfen kod tarafından oluşturulan [çıktı DOCX dosyasını](Book1.docx) inceleyin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **Excel Çalışma Kitabını PPTX'e Dönüştür**  
Aspose.Cells API, elektronik tabloları PPTX formatına dönüştürme desteği sağlar. Çalışma kitabını PPTX'e aktarmak için [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) parametresi ile [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) metodunu kullanın. Ayrıca, sayfayı PPTX'e aktarmak için [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) sınıfını kullanabilirsiniz.  

Aşağıdaki kod örneği, [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum üyesi kullanılarak aktif sayfayı PPTX'e aktarmayı göstermektedir. Lütfen kod tarafından oluşturulan [çıktı PPTX dosyasını](Book1.pptx) inceleyin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **Excel Çalışma Kitabını EPUB'a dönüştür**  
Aspose.Cells API, elektronik tabloları EPUB formatına dönüştürme desteği sağlar. Çalışma kitabını EPUB'a aktarmak için [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) parametresi ile [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) metodunu kullanın. Ayrıca, sayfayı EPUB'a aktarmak için [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) sınıfını kullanabilirsiniz.  

Aşağıdaki kod örneği, aktif sayfayı EPUB'a aktarmayı [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum üyesi kullanarak göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **Excel Çalışma Dosyasını AZW3'e dönüştür**  
Aspose.Cells API, elektronik tabloları AZW3 formatına dönüştürmeyi destekler. Çalışma kitabını AZW3'e aktarmak için [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) parametresi ile [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) metodunu kullanın. Ayrıca, sayfayı AZW3'e aktarmak için [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) sınıfını kullanabilirsiniz.  

Aşağıdaki kod örneği, aktif sayfayı AZW3'e [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum üyesi kullanarak aktarmayı göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **Gelişmiş Konular**  
- [XLSB Revizyonunu XLSM'ye Dönüştür](/cells/tr/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/tr/nodejs-cpp/convert-excel-to-html/)  
- [Görüntü](/cells/tr/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/tr/nodejs-cpp/convert-workbook-to-json/)  
- [Excel çalışma kitabını Ods, Sxc ve Fods (OpenOffice / LibreOffice calc) formatlarına dönüştür.](/cells/tr/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/tr/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [Excel'i CSV, TSV ve Txt'e dönüştür](/cells/tr/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [Belge Dönüşüm İlerlemesini İzle](/cells/tr/nodejs-cpp/track-document-conversion-progress/)  
- [CSV, TSV ve TXT'yi Excel'e Dönüştür](/cells/tr/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
