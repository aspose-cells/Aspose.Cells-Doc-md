---
title: Node.js kullanarak Excel i CSV, TSV ve Txt ye dönüştürün
linktitle: CSV, TSV ve Txt olarak kaydet
type: docs
weight: 40
url: /tr/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarını CSV, TSV ve TXT formatlarına dönüştürmeyi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, Excel, ODS, JSON ve diğer format dosyalarını CSV, TSV ve TXT'ye dönüştürmeyi mümkün kılar.

{{% /alert %}}

## **Workbook'u Metin veya CSV Formatında Kaydet**

Bazen, bir çalışma kitabındaki birden çok sayfayı metin formatına dönüştürmek veya kaydetmek istersiniz. Metin formatları (örneğin TXT, TabDelim, CSV vb.) için, varsayılan olarak, hem Microsoft Excel hem de Aspose.Cells yalnızca aktif sayfanın içeriğini kaydeder.

Aşağıdaki kod örneği, tüm çalışma kitabını metin formatında kaydetmeyi açıklar. Kaynak çalışma kitabını yükleyin; bu, herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası olabilir (XLS, XLSX, XLSM, XLSB, ODS vb.) ve herhangi sayfa sayısına sahip olabilir.

Kod çalıştırıldığında, çalışma kitabındaki tüm sayfaların verilerini TXT formatına dönüştürür.

Aynı örneği CSV'ye kaydetmek için değiştirebilirsiniz. Varsayılan olarak, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) bir virgüldür, bu nedenle CSV biçimine kaydederken bir ayraç belirtmeyin.

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

## **Özel Ayraçla Metin Dosyaları Kaydetme**

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


## **Gelişmiş Konular**
- [CSV formatına yayınlarken Boş Satırlar için Ayraçları Sakla](/cells/tr/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [CSV formatına elektronik tabloları dışa aktarırken Öneki Boş Satırları ve Sütunları Kırp](/cells/tr/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
