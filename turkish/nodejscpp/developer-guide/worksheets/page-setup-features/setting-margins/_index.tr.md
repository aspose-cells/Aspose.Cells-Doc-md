---
title: Node.js ile C++ üzerinden Kenar Boşluğu Ayarlama
linktitle: Kenar Boşlukları Ayarlama
type: docs
weight: 20
url: /tr/nodejs-cpp/setting-margins/
description: Bu makalede, örnek kod kullanarak Excel çalışma sayfasının kenar boşluklarını nasıl ayarlayacağınızı öğreneceksiniz. Ayrıca, Node.js API kullanarak sayfa ortası, başlık ve altbilgi kenar boşluklarını programlı olarak ayarlamayı da öğrenin.
keywords: Excel çalışma sayfası kenar boşluklarını C++ aracılığıyla Node.js kullanarak ortalayın, çalışma sayfası başlık ve altbilgi kenar boşluklarını Node.js ile C++ kullanarak ayarlayın
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel'in sayfa düzeni seçeneklerini tamamen destekler. Geliştiriciler, baskı işlemini kontrol etmek için çalışma sayfaları için sayfa düzeni ayarlarını yapılandırabilirler. Bu konu, Aspose.Cells'ı kullanarak sayfa kenar boşluklarını yapılandırmanın nasıl yapıldığını tartışmaktadır.

{{% /alert %}}

## **Kenar Boşlukları Ayarlama**

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, bir çalışma sayfası için sayfa düzeni seçeneklerini ayarlamak amacıyla kullanılan [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) özelliği sağlar. [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) niteliği, geliştiricilerin yazdırılan çalışma sayfası için farklı sayfa düzeni seçenekleri belirlemesine olanak tanıyan [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) sınıfının bir nesnesidir. [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) sınıfı, sayfa düzeni ayarlarını yapmak için kullanılan çeşitli özellikler ve metodlar sağlar.

### **Sayfa Kenar Boşlukları**

Sayfa kenar boşluklarını (sol, sağ, üst, alt) [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) sınıf üyelerini kullanarak belirleyin. İşte sayfa kenar boşluklarını belirtmek için kullanılan birkaç metod:

- [**PageSetup.getLeftMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getLeftMargin--)
- [**PageSetup.getRightMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getRightMargin--)
- [**PageSetup.getTopMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getTopMargin--)
- [**PageSetup.getBottomMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBottomMargin--)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Set bottom, left, right and top page margins
pageSetup.setBottomMargin(2);
pageSetup.setLeftMargin(1);
pageSetup.setRightMargin(1);
pageSetup.setTopMargin(3);

// Save the Workbook.
workbook.save(path.join(dataDir, "SetMargins_out.xls"));
```

### **Sayfa Üzerinde Ortala**

Bir şeyi yatay ve dikey olarak sayfada ortalayabilirsiniz. Bunun için [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) sınıfının, [**PageSetup.getCenterHorizontally()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterHorizontally--) ve [**PageSetup.getCenterVertically()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCenterVertically--) üyeleri bazı kullanışlıdır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Center on page Horizontally and Vertically
pageSetup.setCenterHorizontally(true);
pageSetup.setCenterVertically(true);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```

### **Üst Bilgi ve Alt Bilgi Kenar Boşlukları**

Başlık ve altbilgi kenar boşluklarını [**Worksheet.getPageSetup()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPageSetup--) sınıf üyeleri olan [**PageSetup.getHeaderMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeaderMargin--) ve [**PageSetup.getFooterMargin()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooterMargin--) kullanarak ayarla.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook object
const workbook = new AsposeCells.Workbook();

// Get the worksheets in the workbook
const worksheets = workbook.getWorksheets();

// Get the first (default) worksheet
const worksheet = worksheets.get(0);

// Get the pagesetup object
const pageSetup = worksheet.getPageSetup();

// Specify Header / Footer margins
pageSetup.setHeaderMargin(2);
pageSetup.setFooterMargin(2);

// Save the Workbook.
workbook.save(path.join(dataDir, "CenterOnPage_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
