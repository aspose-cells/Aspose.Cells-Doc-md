---
title: Node.js kullanarak C++ ile İsimlendirilmiş Aralıkları Silin
linktitle: Adlandırılmış Aralıkları Sil
type: docs
weight: 90
url: /tr/nodejs-cpp/Delete-named-ranges/
description: Aspose.Cells for Node.js via C++ kullanarak Excel veya OpenOffice dosyalarından tanımlanmış isimleri veya isimlendirilmiş aralıkları kaldırmayı öğrenebilirsiniz.
---

## **Giriş**
Eğer Excel dosyalarında çok fazla tanımlanmış isim veya adlandırılmış aralık varsa, tekrar atıfta bulunulmadığından bazılarını temizlememiz gerekebilir.

## **MS Excel'de Adlandırılmış Aralığı Kaldır**

Excel'den adlandırılmış bir aralığı kaldırmak için şu adımları izleyebilirsiniz:
1. Microsoft Excel'i açın ve adlandırılmış aralığı içeren çalışma kitabını açın.
2. Excel kurdelesindeki "Formüller" sekmesine gidin.
3. "Tanımlı İsimler" grubundaki "Ad Yöneticisi" düğmesini tıklayın. Bu, Ad Yöneticisi iletişim kutusunu açacaktır.
4. Ad Yöneticisi iletişim kutusunda, kaldırmak istediğiniz adlandırılmış aralığı seçin.
5. "Sil" düğmesine tıklayın. İstenildiğinde silme işlemini onaylayın.
6. Ad Yöneticisi iletişim kutusunu kapatmak için "Kapat" düğmesine tıklayın.
7. Değişiklikleri korumak için çalışma kitabını kaydedin.

## **Aspose.Cells for Node.js via C++ kullanarak İsmiyle Aralık Silme**
Aspose.Cells for Node.js via C++ ile liste içerisinde [metin](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) veya [indeks](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) kullanarak isimlendirilmiş aralıkları veya tanımlı isimleri kaldırabilirsiniz.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

Not: Eğer tanımlanmış isim formüller tarafından referans gösteriliyorsa, kaldırılamaz. Sadece tanımlanmış ismin formülü kaldırabiliriz.

## **Bazı Adlandırılmış Aralıkları Kaldırma**
Bir tanımlı ismi kaldırdığımızda, dosyadaki tüm formüller tarafından kullanılıp kullanılmadığını kontrol etmeliyiz.
İsimlendirilmiş aralıkların kaldırma performansını artırmak için bazılarını birlikte kaldırabiliriz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Yinelenen Tanımlı İsimleri Kaldırma**
Bazı Excel dosyaları, aynı isimli tanımlanmış isimler nedeniyle bozulur. Bu yüzden bu yinelenen isimleri kaldırıp dosyayı onarabiliriz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



{{< app/cells/assistant language="nodejs-cpp" >}}
