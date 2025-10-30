---
title: Node.js via C++ ile Çalışma Sayfası Görünümleri
linktitle: Sayfa Görünümleri
type: docs
weight: 40
url: /tr/nodejs-cpp/worksheet-views/
description: Bu makale, Node.js ve Node.js API sini kullanarak bir Excel çalışma kitabının ve çalışma sayfalarının sayfa kırpma önizlemesi ile nasıl etkileşime geçileceğini anlatacaktır. Bölünmüş paneller, dondurulmuş paneller ve yakınlaştırma faktörü ile de çalışılacaktır.
---

## **Sayfa Kesme Önizleme**

Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa kesme önizlemesi.

Normal görünüm, çalışma sayfasının varsayılan görünümüdür. Sayfa kırma önizlemesi, bir çalışma sayfasını yazdırılacağı şekilde gösteren düzenleme görünümüdür. Sayfa kırma önizlemesi, her sayfada neyin olacağını gösterir ve yazdırma alanını ve sayfa kırgalarını ayarlamanızı sağlar. Aspose.Cells for Node.js via C++ kullanılarak, geliştiriciler normal görünüm veya sayfa kırma önizleme modlarını etkinleştirebilir.

### **Görünüm Modlarını Kontrol Etme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı sunar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Normal veya sayfa görünümü önizlemesi modlarını etkinleştirmek için [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) özelliğini kullanın. [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--), yalnızca bir **true** ya da **false** değerini depolayabilen bir Boolean özelliğidir.

#### **Normal Görünümü Etkinleştirme**

Normal görünüm için çalışma sayfasını, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) özelliğini **false** olarak ayarlayarak belirleyin.

#### **Sayfa Kesme Önizlemesini Etkinleştirme**

Herhangi bir çalışma sayfasını sayfa görünümü önizlemesi için [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) özelliğini **true** olarak ayarlayarak belirleyin. Bunu yapmak, çalışma sayfasını normal görünümden sayfa görünümü önizlemesine geçirir.

Aşağıda, bir Excel dosyasının ilk çalışma sayfası için sayfa görünümü önizleme modunu etkinleştirmek için [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) özelliğini nasıl kullanacağını gösteren tam bir örnek verilmiştir.

book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının bir örneği oluşturularak açılır. İlk çalışma sayfası için görünüm, [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) özelliğinin **true** olarak ayarlanmasıyla sayfa görünümü önizlemesi olarak değiştirilir. Değiştirilmiş dosya, çıktı.xls olarak kaydedilir.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Yakınlaştırma Faktörü**

### **Microsoft Excel Kullanımı**

Microsoft Excel, kullanıcılara bir çalışma tablosunun yakınlaştırma veya ölçekleme faktörünü ayarlamalarına izin veren bir özellik sağlar. Bu özellik, kullanıcıların çalışma tablosu içeriğini daha küçük veya daha büyük görüntülemelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilirler.

### **Aspose.Cells ve Yakınlaştırma Faktörü**

Aspose.Cells, geliştiricilere çalışma sayfası yakınlaştırma faktörünü ayarlama olanağı tanır.
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir.

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) özelliğini kullanın. Yakınlaştırma faktörü, [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) özelliğine sayısal (tamsayı) bir değer atayarak ayarlanır.

Aşağıda, Excel dosyasının ilk çalışma sayfasının yakınlaştırma faktörünü ayarlamak için [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) özelliğini kullanmayı gösteren tam bir örnek verilmiştir.

Book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının bir örneğini oluşturarak açılır. İlk çalışma sayfasının yakınlaştırma faktörü 75 olarak ayarlanır ve değiştirilmiş dosya output.xls olarak kaydedilir.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Pencereyi Dondurma**

### **Microsoft Excel Kullanımı**

Pencerelerin dondurulmasını sağlayan bir özellik, Microsoft Excel tarafından sağlanır. Pencereyi dondurma, bir çalışma tablosunda kaydırma yaparken görünmesini istediğiniz verileri seçmenize olanak tanır.

### **Aspose.Cells & Pencereleri Dondurma**

Aspose.Cells, çalışma sayfalarına çalışma zamanında sabit panolar uygulamak için geliştiricilere olanak tanır.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Dondurulmuş panelleri yapılandırmak için, Worksheet sınıfının [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) yöntemini çağırın. [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) yöntemi aşağıdaki parametreleri alır:

- **Satır**, dondurulmanın başlayacağı hücrenin satır indeksi.
- **Sütun**, dondurulmanın başlayacağı hücrenin sütun indeksi.
- **Dondurulan satırlar**, üst bölmedeki görünür satır sayısı.
- **Donuk sütunlar**, sol panelde görünür sütunların sayısı.

Book1.xls dosyası, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının yapılandırıcısını çağırarak açılır ve ilk çalışma sayfasında birkaç satır ve sütun sabitlenir. Değiştirilmiş dosya output.xls olarak kaydedilir.

Aşağıdaki tam örnek, bir Excel dosyasının ilk çalışma sayfasının (0 dizininden başlayarak 4. satır ve 3. sütunu temsil eden C4'ten başlayarak) satır ve sütunları sabitlemek için [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) yönteminin nasıl kullanılacağını gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **Bölmeler**

Aynı çalışma tablosunda farklı görünümler elde etmek için ekranı bölmek istemeniz durumunda bölmeler. Microsoft Excel, çalışma sayfanızın kopyasını birden fazla görüntülemenize ve her bir pencerede bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölmeler.

Pencereler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik diğerinde aynı anda görünür. Aspose.Cells, kullanıcılar için bölme bölmeleri özelliği sağlar.

### **Bölmelerin Uygulanması ve Kaldırılması**

#### **Bölmeleri Böleme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıfı içeren bir özelliktir. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bölünmüş görünümleri uygulamak için, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) özelliğini kullanın. Bölünmüş panoları kaldırmak için, [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) yöntemini kullanın.

Örnekte, basit bir şablon dosyası kullanılır, ardından ilk çalışma sayfasındaki bir hücreye bölme bölmeleri özelliği uygulanır. Güncellenmiş dosya kaydedilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

Yukarıdaki kodu çalıştırdıktan sonra, oluşturulan dosyanın bölünmüş bir görünüme sahip olacağı.

#### **Pencereleri Kaldırma**

Bölme panolarını [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) yöntemiyle kaldırın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Gelişmiş Konular**
- [Çalışma Sayfasında Sıfır Değerlerinin Görüntüsünü Gizleme](/cells/tr/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Çalışma Sayfası Sekme Rengini Ayarlama](/cells/tr/nodejs-cpp/set-worksheet-tab-color/)
- [Kılavuz Çizgilerini ve Satır Sütun Başlıklarını Gösterme ve Gizleme](/cells/tr/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Satır Sütun ve Kaydırma Çubuklarını Gösterme ve Gizleme](/cells/tr/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Çalışma Sayfalarını ve Sekmeleri Gösterme ve Gizleme](/cells/tr/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [Çalışma Sayfasında Değerlerin Yerine Formülleri Gösterme](/cells/tr/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Hata Kontrol Seçeneklerini Kullan](/cells/tr/nodejs-cpp/use-error-checking-options/)

{{< app/cells/assistant language="nodejs-cpp" >}}
