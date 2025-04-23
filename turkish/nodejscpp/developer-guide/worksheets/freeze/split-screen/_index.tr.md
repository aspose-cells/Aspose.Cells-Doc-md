---
title: Node.js ve C++ kullanarak Excel Çalışma Sayfasını Bölme Ekranı
linktitle: Bölünmüş Ekran
type: docs
weight: 190
url: /tr/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: Bu makalede, Node.js C++ Eklentisi kullanarak çalışma sayfasını iki veya dört parçaya bölerek belirli satır ve/veya sütunları ayrı panolarda görüntülemeyi programatik olarak nasıl yapacağınızı öğreneceksiniz.
keywords: Üst satırları dondurun, Üst satırı dondurun.
---

## **Giriş**

Bu makalede, çalışma sayfasını iki veya dört parçaya bölerek belirli satır ve/veya sütunları ayrı bölmelerde görüntülemenin C++ kullanılarak programatik olarak nasıl yapılacağı anlatılacaktır. Büyük veri setleriyle çalışırken, aynı çalışma sayfasındaki birkaç alanı aynı anda görmemiz gerekebilir, böylece farklı alt kümeleri karşılaştırabiliriz. Bölme ekran fonksiyonu ihtiyacınızı karşılayabilir.

## **Excel'de ekranı nasıl bölebilirsiniz**
Bir elektronik tabloyu ikiye veya dörde bölmek için aşağıdakileri yapın:

1. Bölme yapmak istediğiniz satır/sütun/hücreyi seçin.
2. Görünüm sekmesinde, Pencereler grubunda, Böl düğmesini tıklayın.

**![Bölünmüş Ekran](Bölünmüş-Ekran.png)**

## **Excel'de sütunlara dik olarak elektronik tabloyu bölmek**

Elektronik tablonun farklı alanlarını dikey olarak ayırmak için, bölmenin görünmesini istediğiniz sütunun sağındaki sütunu seçin ve Excel'de Böl düğmesini tıklayın.

Aspose.Cells for Node.js via C++ ile sütunlar üzerinde dikey çalışma sayfasını programatik olarak bölmek oldukça kolaydır, aktif hücre olarak en üst satırda bir hücre seçmeniz yeterlidir, ardından [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) yöntemiyle bölme.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **Satırlara yatay olarak elektronik tabloyu bölmek**
Excel'de pencerenizi yatay olarak ayırmak için, bölmeyi istediğiniz satırın altındaki satırı seçin.

Aspose.Cells for Node.js via C++ ile satırlar üzerinde yatay çalışma sayfasını programatik olarak bölmek oldukça kolaydır, aktif hücre olarak sol sütunda bir hücre seçmeniz yeterlidir, ardından [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) yöntemiyle bölme.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **Elektronik tabloyu dört bölüme ayırmak**
Aynı elektronik tablonun dört farklı bölümünü aynı anda görüntülemek için, Excel'de ekranınızı hem dikey hem yatay olarak bölebilirsiniz.

Aspose.Cells for Node.js via C++ ile sütunlar üzerinde dikey çalışma sayfasını programatik olarak bölmek oldukça kolaydır, ilk satır ve ilk sütun dışında bir hücreyi aktif hücre olarak seçmeniz yeterlidir, ardından [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--) yöntemiyle bölme.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **Bölünmüş bölgeyi kaldırmak için**
Elektronik tabloyu bölme ayarını kaldırmak için, sadece Böl düğmesini tekrar tıklayın.

Aspose.Cells for Node.js via C++, bölme ayarını kaldırmak için [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) metodunu sağlar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

