---
title: Node.js ile C++ kullanarak Worksheet e Metin Kutusu ekleme/yerleştirme
linktitle: Çalışma Sayfasına Metin Kutusu Ekle
type: docs
weight: 10
url: /tr/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Aspose.Cells for Node.js via C++ kullanarak Worksheet e Metin Kutusu ekleme/yerleştirme
keywords: Excel Aspose Node.js ile C++ kullanarak Metin Kutusu ekle/yerleştir
---

## Excel'de Çalışma Sayfasına Metin Kutusu Ekle

Excel programında (sürüm 07 ve üzeri), metin kutusu ekebileceğiniz iki yer vardır. Biri 'insert-shapes' içinde, diğeri ise 'Insert' seçeneğinin sağ üst menüsündedir.

### yöntem biri:

![1](1.png)

### yöntem iki:

![2](2.png)

## Nasıl oluşturulur

Metin Kutusu, yatay veya dikey metinle oluşturulabilir.

- Karşılık gelen seçeneği seçin (yatay veya dikey)
- Sayfada sol tuşa basın.
- Sol tuşa basılı tutun ve sayfada bir mesafe sürükleyin.
- Sol tuşu bırakın.

Şimdi bir metin kutusuna sahipsiniz.

## Aspose.Cells for Node.js via C++ ile Worksheet'e Metin Kutusu Ekleme

İş sayfasına toplu olarak TextBox eklemeniz gerektiğinde, manuel ekleme yöntemi açıkça bir felakettir. Eğer bu sizi rahatsız ediyorsa, bu belgenin size yardımcı olacağını düşünüyorum. [Aspose.Cells](https://products.aspose.com/cells/) size kodunuzda toplu eklemeleri kolayca yapmanızı sağlayan bir API sunar.

Aşağıdaki örnek kod bir metin kutusu oluşturur.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Benzer bir dosya alacaksınız [sonuç dosyası](result.xlsx). Dosyada aşağıdakileri göreceksiniz:

![](52449.png)

