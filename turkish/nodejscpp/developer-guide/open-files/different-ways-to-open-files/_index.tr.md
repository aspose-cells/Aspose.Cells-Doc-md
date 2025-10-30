---
title: Node.js ve C++ kullanarak Dosyaları Açmanın Farklı Yolları
linktitle: Dosyaları Açmanın Farklı Yolları
type: docs
weight: 10
url: /tr/nodejs-cpp/different-ways-to-open-files/
description: Bu makale, Aspose.Cells for Node.js via C++ API kullanarak Excel dosyasını nasıl açacağınızı açıklar.
keywords: Node.js ile Excel dosyasını açmak, Excel olmadan nasıl yapılır, Node.js kullanarak Excel dosyasını nasıl açarım?
---

{{% alert color="primary" %}}

Aspose.Cells ile, dosyaları açmak kolaydır; örneğin veri almak veya geliştirme sürecini hızlandırmak için tasarımcı şablonu kullanmak gibi.

{{% /alert %}}

## **Bir Excel Dosyasını Yol Üzerinden Nasıl Açılır**

Geliştiriciler, bir Microsoft Excel dosyasını, yerel bilgisayardaki dosya yolunu [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıf yapısında belirterek açabilir. Yolu, bir *dize* olarak geçirmeniz yeterlidir. Aspose.Cells otomatik olarak dosya formatını tespit eder.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **Bir Akış Üzerinden Excel Dosyasını Nasıl Açılır**

Bir Excel dosyasını akış olarak da açmak oldukça basittir. Bunu yapmak için, dosyayı içeren *Stream* nesnesini alan aşırı yüklenmiş yapıcıyı kullanın.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **Yalnızca Veri ile Bir Dosyayı Nasıl Açılır**

Sadece verileri içeren bir dosyayı açmak için, ilgili özellikleri ve seçenekleri ayarlamak üzere [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) ve [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) sınıflarını kullanın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **Yalnızca Görünür Sayfaları Yükleme**

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) yüklerken, bazen yalnızca çalışma kitabında görünür çalışanlardaki verilere ihtiyacınız olabilir. Aspose.Cells, bir çalışma kitabını yüklerken görünmez çalışanlardaki verileri atlamanıza izin verir. Bunu yapmak için, [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) sınıfından türeyen özelleştirilmiş bir fonksiyon oluşturun ve örneğini [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) özelliğine aktarın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

Yukarıdaki kod örneğinde referans verilen *CustomLoad* sınıfının uygulaması burada.

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

Aspose.Cells kullanarak yerel olmayan Excel dosyalarını veya diğer dosya formatlarını (örneğin PPT/PPTX, DOC/DOCX vb.) açmaya çalışırken bir istisna fırlatılacaktır.

{{% /alert %}} 

{{% alert color="primary" %}}

Büyük elektronik tablo yüklerken [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) yapıcı muhtemelen *OutOfMemoryError* hatası atabilir. Bu istisna, mevcut belleğin elektronik tabloyu tamamen belleğe yüklemek için yetersiz olduğunu gösterir; bu nedenle, Bellek Tercihleri etkinleştirilerek elektronik tablo yüklenmelidir.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
