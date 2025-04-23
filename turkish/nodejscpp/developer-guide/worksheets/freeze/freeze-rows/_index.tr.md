---
title: Node.js ve C++ kullanarak Excel Çalışma Sayfasının Üst Satır(ları)nı Dondurun
linktitle: Satırları Sabitle
type: docs
weight: 190
url: /tr/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: Bu makalede, Node.js kütüphanesi ve C++ API kullanarak Excel Çalışma Sayfalarının üst satırlarını nasıl programatik olarak donduracağınızı öğreneceksiniz.
keywords: Üst Satırları Dondurun, Node.js ve C++ ile Üst Satırı Dondurun.
---

## **Giriş**

Bu makalede, üst satır(lar)ı nasıl donduracağımızı öğreneceğiz. Ortak başlık altında büyük miktarda veri olduğunda, aşağı kaydırırken başlıkları göremeyebilirsiniz. Üst satır(ları) dondurup kilitleyerek, kalan veriyi kaydırırken bile o kısmı görebilirsiniz. Üst satırlarda başlıkları kolayca görebilirsiniz.

## **Excel'de Satırları Dondur**

![Excel'de üst satır(ları) dondur](Freeze-Rows.png)

1. Üst satır(lar)ı dondurmak istiyorsanız, önce dondurulması gereken satırın altındaki satırı seçin.
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden Üst Satırı Dondur'a tıklayın.
4. Aşağı kaydırırsanız, ilk satır her zaman üst görünümde kalır.

**![Dondurulmuş satır](Frozen-Row.png)**

Görüleceği üzere, 1. satır dondurulmuştur; ilk satır aşağı kaydırırken her zaman görüntüde üstte kalır.

Satırları Dondurun, büyük verinizi satır etiketiyle ilgilenmeden görüntülemenizi sağlar.

## **Aspose.Cells for Node.js via C++ ile Satırları Dondurun**
Aspose.Cells for Node.js via C++ kullanarak satırları dondurmak çok basittir. 
Lütfen seçilen satırda satır(lar)ı dondurmak için [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) metodunu kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.freezePanes() yöntemiyle ilk satırı dondurun.
3. Dosyayı kaydedin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

Ekli [örnek kaynak Excel dosyası](../Freeze.xlsx).
