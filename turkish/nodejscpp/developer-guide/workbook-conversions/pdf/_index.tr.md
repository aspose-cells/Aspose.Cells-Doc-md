---
title: Node.js kullanarak C++ ile PDF
linktitle: Pdf
type: docs
weight: 220
url: /tr/nodejs-cpp/convert-excel-to-pdf/
description: Aspose.Cells for Node.js via C++ kullanarak Excel Çalışma Kitabını PDF ye nasıl dönüştüreceğinizi öğrenin. 
---

{{% alert color="primary" %}}
Aspose.Cells, Excel Çalışma Kitabını PDF'ye dönüştürmeyi destekler. Bu örnekte, bir Excel Çalışma Kitabının tam dönüşümünü göreceğiz.
{{% /alert %}}

## **Excel Çalışma Kitabını PDF'e Dönüştürme**

PDF dosyaları, kuruluşlar, devlet kurumları ve bireyler arasında belge değişiminde geniş ölçüde kullanılır. Standart bir belge biçimidir ve yazılım geliştiriciler genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmek için bir yol bulmaları istenir.

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++, çıkış belgelerinde API ve Sürüm Numarası hakkında bilgileri doğrudan yazar. Örneğin, belgeyi PDF'e dönüştürürken, Aspose.Cells for Node.js via C++ **PDF Üretici** alanını 'Aspose.Cells v23.2' gibi bir değerle doldurur.

Lütfen bu bilgileri çıktı Belgelerinde [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--) özelliği ile değiştirebileceğinizi unutmayın.
{{% /alert %}}

### **Doğrudan Dönüşüm**

Aspose.Cells for Node.js via C++, elektronik tablo dosyalarından PDF'e dönüştürmeyi diğer yazılımlara bağlı kalmadan destekler. Bir Excel dosyasını [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) yöntemiyle PDF olarak kaydedin. [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) yöntemi, yerel Excel dosyalarını PDF formatına dönüştüren [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum üyesini sağlar.

Doğrudan Excel elektronik tablolarını PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1. Boş kurucuyu çağırarak [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının nesnesini örnekleyin.
1. Varolan bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
3. Aspose.Cells'in API'lerini kullanarak elektronik tabloda herhangi bir işlem yapın (giriş verileri, biçimlendirme uygulama, formüller belirleme, resimler veya diğer çizim nesneleri ekleme vb.).
1. Elektronik tablo kodu tamamlandığında, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) yöntemini çağırarak elektronik tabloyu kaydedin.

Dosya biçimi PDF olmalı, bu nedenle nihai PDF belgesini oluşturmak için *Pdf* (önceden tanımlanmış bir değer) olarak [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) sınıfının numaralandırmasından seçim yapın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **Gelişmiş Dönüşüm**

Dönüşüm için farklı özellikleri ayarlamak için [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) sınıfını kullanabilirsiniz. [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) sınıfının farklı özelliklerini ayarlamak, çıktı PDF'nin yazdırma, font, güvenlik ve sıkıştırma ayarları üzerinde kontrol sahibi olmanızı sağlar. 

En önemli özellik [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--), PDF standartları uyumluluk seviyesini ayarlamanıza olanak tanır. Şu anda PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u formatlarına kaydedebilirsiniz. PDF/A formatı ile, çıktı dosyasının boyutu düzenli PDF dosyasının boyutundan daha büyüktür.

#### **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**

Aşağıdaki kod parçacığı, Excel dosyalarını PDF/A uyumlu PDF biçimine kaydetmek için [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) sınıfının nasıl kullanılacağını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
Lütfen, [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) özelliğinin Aspose.Cells for Node.js via C++ 5.3.0 sürümünde eklendiğini unutmayın.
{{% /alert %}}

#### **PDF Oluşturma Saatini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) sınıfı ile PDF oluşturma saatinizi alabilir veya ayarlayabilirsiniz. Aşağıdaki kod, PDF dosyasının oluşturma zamanını belirlemek için [**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) özelliğin kullanımını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **İçerik Erişilebilirlik Kopyalama seçeneğini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) sınıfı ile dönüştürülen PDF'de içerik erişimini kontrol etmek için PDF [**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--) seçeneğini alabilir veya ayarlayabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **Özel özellikleri PDF'ye aktar**

[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) sınıfı ile kaynak elektronik tablodaki özel özellikleri PDF'ye aktarabilirsiniz. Özellikleri nasıl aktarılacağını belirtmek için [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/) numaralama sağlanmaktadır. Bu özellikler, aşağıdaki resimde gösterildiği gibi Adobe Acrobat Reader'da Dosya'ya tıklayarak ardından özellikler seçeneğini tıklayarak görüntülenebilir. Şablon dosyası "sourceWithCustProps.xlsx" test etmek için [buradan](sourceWithCustProps.xlsx) indirilebilir ve çıktı PDF dosyası "outSourceWithCustProps" analiz için [buradan](outSourceWithCustProps.pdf) temin edilebilir.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **Dönüşüm Özellikleri**

Her yeni sürümle dönüşüm özelliklerini geliştirmeye çalışıyoruz. Aspose.Cell'in Excel'den PDF'ye dönüştürme hala birkaç kısıtlamaya sahiptir. HaritaÇizelgesi, PDF biçimine dönüştürülürken desteklenmez. Ayrıca, bazı çizim nesneleri iyi desteklenmez.

Aşağıdaki tablo, Aspose.Cells kullanarak PDF'ye dışa aktarırken tamamen veya kısmen desteklenen tüm özellikleri listeleyen bir tablodur. Bu tablo son değildir ve tüm elektronik tablo özniteliklerini kapsamaz, ancak dışa aktarmak için tamamen veya kısmen desteklenmeyen özellikleri tanımlar.

|**Belge Öğesi**|**Özellik**|**Desteklenen**|**Notlar**|
| :- | :- | :- | :- |
|Hizalama| |Evet| |
|Arka plan Ayarları| |Evet| |
|Kenarlık|Renk|Evet| |
|Kenarlık|Çizgi stili|Evet| |
|Kenarlık|Çizgi genişliği|Evet| |
|Hücre Verisi| |Evet| |
|Yorumlar| |Evet| |
|Koşullu Biçimlendirme| |Evet| |
|Döküman Özellikleri| |Evet| |
|Çizim Nesneleri| |Kısmen|Çizim nesneleri için gölge ve 3-B efektleri iyi desteklenmez; WordArt ve SmartArt kısmen desteklenir.|
|Yazı Tipi|Boyut|Evet| |
|Yazı Tipi|Rengi|Evet| |
|Yazı Tipi|Stili|Evet| |
|Yazı Tipi|Altı çizili|Evet| |
|Yazı Tipi|Efektleri|Evet||
|Resimler| |Evet| |
|Hyperlink| |Evet| |
|Grafikler| |Kısmen|Harita Grafikleri desteklenmiyor.|
|Birleştirilmiş Hücreler| |Evet| |
|Sayfa Sonu| |Evet| |
|Sayfa Ayarı|Üstbilgi/Altbilgi|Evet| |
|Sayfa Ayarı|Kenar Boşlukları|Evet| |
|Sayfa Ayarı|Sayfa Yönü|Evet| |
|Sayfa Ayarı|Sayfa Boyutu|Evet| |
|Sayfa Ayarı|Yazdırma Alanı|Evet| |
|Sayfa Ayarı|Yazdırma Başlıkları|Evet| |
|Sayfa Ayarı|Ölçekleme|Evet| |
|Satır Yüksekliği/Sütun Genişliği| |Evet| |
|RTL (Sağdan Sola) Dil| |Evet| |

{{% alert color="primary" %}}
Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.
{{% /alert %}}

## **Gelişmiş Konular**
- [Adlandırılmış Yer İmleriyle PDF Yer İmi Ekleyin](/cells/tr/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle](/cells/tr/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDF'ye Kaydederken Yalnızca Belirli Unicode Karakterlerin Yazı Tipini Değiştirme](/cells/tr/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [XLSX Dosyasını PDF Biçimine Dönüştür](/cells/tr/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [PDFA-1a uyumlu PDF biçimine Excel dosyasını dönüştür](/cells/tr/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Resim veya Grafiklerle XLS Dosyasını PDF Biçimine Dönüştür](/cells/tr/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Grafik Tablosu için PdfBookmarkEntry Oluştur](/cells/tr/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır](/cells/tr/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandler sınıfını kullanarak PDF'ye dönüştürürken DrawObject ve Sınırlı Alın](/cells/tr/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excel Dosyasını PDF'e Dönüştürürken Yazı Tipi Yedeği İçin Uyarıları Al](/cells/tr/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay](/cells/tr/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Oluşturulan Sayfa Sayısını Sınırla - Excel'den PDF'e Dönüştürme](/cells/tr/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF'ye kaydederken yorumları yazdır](/cells/tr/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [Excel'i PDF'e dönüştürürken Office Eklentilerini renderla](/cells/tr/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excel'den PDF'ye Dönüşümde Her Excel Çalışsayarı İçin Bir PDF Sayfası Oluştur](/cells/tr/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cells ile çıktı PDF'inde Unicode Ek Karakterlerini renderla](/cells/tr/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Eklenti Görüntülerini Yeniden Örnekle](/cells/tr/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet](/cells/tr/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Excel'i Standart veya Minimum Boyutta PDF olarak kaydet](/cells/tr/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Belirtilen Çalışsayfalarını PDF olarak kaydet](/cells/tr/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [Güvenli PDF Belgeleri](/cells/tr/nodejs-cpp/secure-pdf-documents/)
- [Çıktı PDF ve görüntülerde metin geçişini belirle](/cells/tr/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
