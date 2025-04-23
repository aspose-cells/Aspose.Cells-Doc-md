---
title: Şerit XML sini Node.js ile C++ kullanarak özelleştirme
linktitle: Excel Menüsünü Özelleştirme
type: docs
weight: 1500
url: /tr/nodejs-cpp/customizing-the-ribbon-xml/
description: Excel de Şerit XML sini nasıl özelleştireceğinizi öğrenin Aspose.Cells for Node.js via C++ kullanarak. 
---

{{% alert color="primary" %}} 

Microsoft Office, ofis 2007'den bu yana uygulama penceresinin üstünde bir Ribbon ile menüleri ve araç çubuklarını değiştirdi. Ribbon özelleştirilebilir. 
Aspose.Cells for Node.js via C++ şöyle yapmanıza olanak sağlar

- Parse etmeden Ribbon XML'yi saklamanıza olanak tanır.
- Açılış işareti ve açılış etiketi işareti XML sınıfı kullanarak işaretleme.
- Veri ilişkilendirmesi yöntemi kullanarak XML dosyalarını aktifleştirebilme.

Eğer açılış XML’ni değiştirmek istiyorsanız, XML veri işaretleme aracıları ya da başka bir açılış XML aracı kullanarak, onu işaretleşmelisiniz.

{{% /alert %}} 

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");
// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

const ribbonXml = `<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui"></customUI>`;
workbook.setRibbonXml(ribbonXml);
```
