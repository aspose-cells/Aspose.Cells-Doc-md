---
title: Sayfa Kırılması Yönetimi Node.js ve C++ ile
linktitle: Sayfa Kesmelerinin Yönetimi
type: docs
weight: 30
url: /tr/nodejs-cpp/managing-page-breaks/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Excel çalışma sayfalarında belirli sayfa kırılmalarını ekleme, temizleme veya silme işlemlerine örnek kod sağlar ve açıklar.
keywords: sayfa kırılması Node.js ve C++ ile, excel sayfa kırılması Node.js ve C++ ile, sayfa kırmasını temizle Node.js ve C++ ile, belirli sayfa kırmasını sil Node.js ve C++ ile
---

{{% alert color="primary" %}}

Tanıma göre, bir sayfa kesmesi, metin akışının bir sayfanın bittiği ve diğerinin başladığı yeridir. Microsoft Excel kullanıcılarına herhangi bir seçili hücreye sayfa kesmeleri eklemelerine izin verir.

Sayfa kırığı eklenen hücrenin konumunda, sayfa biter ve sayfa kırığından sonraki veri bir sonraki sayfaya basılırken. Basitçe söylemek gerekirse, sayfa kırıkları çalışma sayfanızı istediğiniz özelliklere göre birden çok sayfaya böler. Ayrıca, Aspose.Cells kullanarak çalışma sayfalarınızda çalışma zamanında sayfa kırıkları ekleyebilirsiniz. Aspose.Cells, geliştiricilere iki tür sayfa kırığı ekleme olanağı sağlar:

- Yatay sayfa kesmesi
- Dikey sayfa kesmesi

Tartışmanın geri kalanında, Aspose.Cells kullanarak çalışma sayfalarınıza yatay veya dikey sayfa kesme nasıl ekleyebileceğinizi açıklayacağız.

{{% /alert %}}

## **Sayfa Sonları**

Aspose.Cells, Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfasını yönetmek için kullanılan geniş bir özellik ve yöntem yelpazesi sağlar.

Sayfa kırıklarını eklemek için, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) ve [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) özelliklerini kullanın.

[**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) ve [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) özellikleri, birkaç sayfa kırığı içerebilen koleksiyonlardır. Her koleksiyon, yatay ve dikey sayfa kırıklarını yönetmek için birçok yöntem içerir.

### **Sayfa Kesmeleri Eklemek**

Bir çalışma sayfasına sayfa kırması eklemek için, belirtilen hücreye dikey ve yatay sayfa kırmaları eklemek amacıyla [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-) ve [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-) metodlarını çağırın. Her **add** yöntemi, kırmanın ekleneceği hücrenin adını alır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

Sayfa kesmeleri önizleme veya yazdırma önizleme modlarında, bu sayfa kesmelerinin nasıl çalıştığını görebilirsiniz.

{{% /alert %}}

### **Belirli Sayfa Kesmesini Kaldırma**

Belirli bir sayfa kırmasını kaldırmak için, [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-) ve [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-) metodlarını çağırın. Her **removeAt** yöntemi, kaldırılacak olan sayfa kırmasının indeksini alır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **Bilinmesi Gerekenler**

Sayfa ayarları yapılandırılırken, **fitToPages** özellikleri ([**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) ve [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)) ayarlandığında, sayfa kırma ayarları etkilenir, bu nedenle, çalışma sayfasını yazdırırken, ayarlar yine de yapılandırılmış olmasına rağmen dikkate alınmaz.
