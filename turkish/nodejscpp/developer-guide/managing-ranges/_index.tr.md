---
title: Node.js ve C++ kullanarak Aralıkları Yönetme
linktitle: Aralıklar
type: docs
weight: 105
url: /tr/nodejs-cpp/managing-ranges/
description: Excel de aralıkları yönetmeyi Aspose.Cells for Node.js via C++ kullanarak öğrenin. Aralıklar oluşturun, değerler, stiller ayarlayın ve çeşitli işlemler yapın.
---

## **Giriş**

Excel'de, bir fare kutusu seçimi ile çoklu hücreleri seçebilirsiniz; seçili hücreler kümesi "Aralık" olarak adlandırılır.

Örneğin, Excel'de "A1" hücresinde sol fare düğmesine tıklayabilir ve ardından "C4" hücresine sürükleyebilirsiniz. Seçtiğiniz dikdörtgen alan da kolayca bir nesne olarak oluşturulabilir ve Aspose.Cells for Node.js via C++ kullanılarak yapılabilir.

İşte bir aralık oluşturmak, değer koymak, stil ayarlamak ve daha fazla işlem yapmak için yol.

## **Aspose.Cells for Node.js via C++ Kullanarak Aralıkları Yönetme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışsayfa [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu sağlar.

### **Aralık Oluştur**

A1:C4 üzerine uzanan bir dikdörtgen alan oluşturmak istediğinizde aşağıdaki kodu kullanabilirsiniz:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **Aralık Hücrelerine Değer Atama**

Örneğin, A1:C4'e uzanan bir hücre aralığınız var. Matris, 4 * 3 = 12 hücre oluşturur. Aralık hücreleri sıralı bir şekilde düzenlenir: Aralık[0,0], Aralık[0,1], Aralık[0,2], Aralık[1,0], Aralık[1,1], Aralık[1,2], Aralık[2,0], Aralık[2,1], Aralık[2,2], Aralık[3,0], Aralık[3,1], Aralık[3,2].

Aşağıdaki örnek, Aralık hücrelerine bazı değerleri girme işlemini göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **Aralık Hücrelerinin Stilini Belirleme**

Aşağıdaki örnek, Aralık hücrelerinin stilini nasıl ayarlayacağınızı gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **Aralık 'ın Mevcut Bölgesini Al**

CurrentRegion, mevcut bir bölgeyi temsil eden bir Aralık nesnesi döndüren bir özelliktir. 

Mevcut bölge, herhangi bir kombinasyonla sınırlandırılmış bir aralıktır. Salt okunur.

Excel'de, CurrentRegion alanını şu şekilde alabilirsiniz:
1. Fareyi mouse kutusu ile alanı (range1) seçin.
2. "Ev - Düzenleme - Bul ve Seç - Özel Git - Mevki Bölgesi"ne tıklayın veya "Ctrl+Shift+*" kullanın, Excel'in otomatik olarak size bir alan (range2) seçmenize yardımcı olmasını sağlayacaksınız. Sizin yaptığınız gibi, range2 range1'in Mevki Bölgesidir.

Lütfen aşağıdaki test dosyasını indirin, Excel’de açın, fare kutusu ile "A1:D7" alanını seçin, ardından "Ctrl+Shift+*" tuşlarına basın, "A1:C3" alanının seçildiğini göreceksiniz.

[current_region.xlsx](current_region.xlsx)

Şimdi aşağıdaki örneği çalıştırarak Aspose.Cells'te nasıl çalıştığını görebilirsiniz:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **Gelişmiş Konular**
- [Excel dosyasının Otomatik Doldurması](/cells/tr/nodejs-cpp/autofill-ranges/)
- [Excel'in Aralıklarını Kopyala](/cells/tr/nodejs-cpp/copy-ranges-of-Excel/)
- [Yalnızca Aralık Verisini Kopyala](/cells/tr/nodejs-cpp/copy-range-data-only/)
- [Yalnızca Aralık Verisiyle Kopyala](/cells/tr/nodejs-cpp/copy-range-data-with-style/)
- [Yalnızca Aralık Stiliyle Kopyala](/cells/tr/nodejs-cpp/copy-range-style-only/)
- [Birleşik Aralık Oluştur](/cells/tr/nodejs-cpp/create-union-range/)
- [Aralığı Kes ve Yapıştır](/cells/tr/nodejs-cpp/cut-and-paste-cells/)
- [Aralıkları Sil](/cells/tr/nodejs-cpp/delete-ranges-from-Excel/)
- [Aralığın Adresini, Hücre Sayısını ve Konumunu, Tüm Sütunu ve Tüm Satırı Al](/cells/tr/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Aralık Ekle](/cells/tr/nodejs-cpp/insert-ranges-to-Excel/)
- [Hücreleri Birleştir veya Birleşikliği Kaldır](/cells/tr/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [Çalışma Sayfasında Hücre Aralığını Taşıma](/cells/tr/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [Çalışma Kitabı ve Çalışma Sayfası Kapsamlı Adlandırılan Aralıkları Oluştur](/cells/tr/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Aralıktaki Veriyi Arama ve Değiştirme](/cells/tr/nodejs-cpp/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="nodejs-cpp" >}}
