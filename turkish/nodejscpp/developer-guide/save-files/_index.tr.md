---
title: Farklı Dosya Kaydetme Yöntemleri Node.js ve C++ ile
linktitle: Dosyaları Kaydet
type: docs
weight: 40
url: /tr/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++, dosyaları PDF, HTML, DOCX, PPTX, JSON ve MHTML de dahil olmak üzere çeşitli formatlarda kaydedebilir.
keywords: Aspose.Cells, Node.js kullanarak Excel dosyasını PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML ve daha fazlasına kaydetmek için sağlar.
---

{{% alert color="primary" %}}

Aspose.Cells, dosyalar oluşturmayı ve kaydetmeyi mümkün kılar. Bu makalede dosyaların kaydedilebileceği çeşitli yollar açıklanmaktadır.

{{% /alert %}}

## **Dosyaları Kaydetmenin Farklı Yolları**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar ve Excel dosyalarıyla çalışmak için gerekli özellikleri ve yöntemleri içerir. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyalarını kaydetmek için kullanılan [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) adlı yöntemi sağlar. [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) yöntemi, farklı yollarla dosya kaydetmek için çeşitli aşırı yükleme seçeneklerine sahiptir.

Dosyanın kaydedildiği dosya biçimi, [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enumerasyonu tarafından belirlenir

|**Dosya Biçimi Türleri**|**Açıklama**|
| :- | :- |
|CSV|CSV dosyasını temsil eder|
|Excel97To2003|Excel 97 - 2003 dosyasını temsil eder|
|Xlsx|Excel 2007 XLSX dosyasını temsil eder|
|Xlsm|Excel 2007 XLSM dosyasını temsil eder|
|Xltx|Excel 2007 şablonu XLTX dosyasını temsil eder|
|Xltm|Excel 2007 makro etkin XLTM dosyasını temsil eder|
|Xlsb|Excel 2007 ikili XLSB dosyasını temsil eder|
|SpreadsheetML|Yaygın Çalışma Kitabı XML dosyasını temsil eder|
|TSV|Tab boşluklu değerler dosyasını temsil eder|
|TabDelimited|Tab Delimited metin dosyasını temsil eder|
|ODS|ODS dosyasını temsil eder|
|Html|HTML dosya(lar)ını temsil eder|
|MHtml|MHTML dosya(lar)ını temsil eder|
|Pdf|PDF dosyasını temsil eder|
|XPS|XPS belgesini temsil eder|
|TIFF|Etiketli Görüntü Dosya Biçimi (TIFF)ni temsil eder|

## **Farklı Biçimlere Dosya Kaydetme Yöntemleri**

Dosya kaydetmek için bir depolama konumuna, dosya adını (depolama yolu dahil) ve istenen dosya biçimini ([**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) sıralamasından) çağırdığınızda [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) nesnesinin [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) metodunu kullanarak belirtin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **Çalışma Kitabını Pdf'ye Nasıl Kaydedilir**
Taşınabilir Belge Formatı (PDF), Adobe tarafından 1990'larda oluşturulan bir belge türüdür. Bu dosya biçiminin amacı, belgelerin ve diğer referans materyallerinin, uygulama yazılımına, donanımına ve İşletim Sistemine bağımsız bir formatta temsili için bir standart getirmektir. PDF dosya biçimi, metin, resimler, bağlantılar, form alanları, zengin medya, dijital imzalar, ekler, meta veriler, Coğrafi konum özellikleri ve 3D nesneler gibi bilgileri içerebilir ve bunlar kaynak belgeye ait olabilir.

Aşağıdaki kod, çalışma kitabını Aspose.Cells kullanarak PDF dosyası olarak kaydetmenin nasıl yapılacağını gösterir:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **Çalışma Kitabını Metin veya CSV Formatına Nasıl Kaydedilir**

Bazen, birden fazla çalışma sayfası olan bir çalışma kitabını metin formatına dönüştürmek veya kaydetmek isteyebilirsiniz. Metin formatları (örneğin TXT, TabDelim, CSV, vb.) için, varsayılan olarak hem Microsoft Excel hem de Aspose.Cells sadece etkin çalışma sayfasının içeriğini kaydeder.

Aşağıdaki kod örneği, tüm çalışma kitabını metin biçimine kaydetmenin nasıl yapılacağını açıklar. Kaynak çalışma kitabını yükleyin; bu, herhangi bir Microsoft Excel veya OpenOffice elektronik tablosu dosyası (XLS, XLSX, XLSM, XLSB, ODS ve diğerleri) olabilir ve herhangi sayıda çalışma sayfası içerebilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği değiştirerek dosyanızı CSV'ye kaydedebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) virgüldür, bu yüzden CSV formatında kaydederken ayırıcı belirtmeyin. Lütfen dikkat: Eğer değerlendirme sürümünü kullanıyorsanız ve [**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--) özelliği doğru olsa bile, program yalnızca bir çalışma sayfası dışa aktarır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Özel Ayraçlı Metin Dosyalarına Nasıl Kaydedilir**

Metin dosyaları, biçimlendirme olmadan elektronik tablo verisi içerir. Dosya, verileri arasında özelleştirilmiş sınıflandırıcılara sahip bir düz metin dosyası türündedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```

## **Bir Akışa Dosya Nasıl Kaydedilir**

Dosyaları akışa kaydetmek için bir *MemoryStream* veya *FileStream* nesnesi oluşturun ve dosyayı bu akış nesnesine [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) nesnesinin [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) yöntemi ile kaydedin. [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) topluluğu kullanarak istediğiniz dosya biçimini belirtin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **Excel Dosyasını Html ve Mht Dosyalarına Nasıl Kaydedilir**
Aspose.Cells, bir Excel dosyasını, JSON, CSV veya Aspose.Cells tarafından .html ve .mht dosyaları olarak yüklenebilecek diğer dosyaları kolaylıkla kaydedebilir.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **Excel Dosyasını OpenOffice (ODS, SXC, FODS, OTS) Dosyalarına Nasıl Kaydedilir**
Dosyaları Açık Ofis formatında kaydedebiliriz: ODS, SXC, FODS, OTS vb.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **Excel Dosyasını JSON veya XML'e Nasıl Kaydedilir**

JSON (JavaScript Object Notation), veri paylaşımı için insan tarafından okunabilir metin kullanan açık standart bir dosya formatıdır. JSON dosyaları .json uzantısıyla saklanır. JSON, daha az biçimlendirme gerektirir ve XML için iyi bir alternatiftir. JSON, JavaScript'ten türetilmiş, ancak dilsiz bir veri formatıdır. JSON'un oluşturulması ve ayrıştırılması modern birçok programlama dilince desteklenmektedir. application/json, JSON için kullanılan medya türüdür.

Aspose.Cells, dosyaların JSON veya XML olarak kaydedilmesini destekler.

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


## **Gelişmiş Konular**
- [Çalışma kitabının sıkıştırma seviyesi ayarlanabilir.](/cells/tr/nodejs-cpp/adjust-workbook-compression-level/)
- [Sıkı Açık XML Elektronik Tablo Biçimine Çalışma Kitabını Kaydet](/cells/tr/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Yanıt Nesnesine Dosya Kaydetme](/cells/tr/nodejs-cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="nodejs-cpp" >}}
