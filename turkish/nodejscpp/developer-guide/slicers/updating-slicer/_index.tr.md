---
title: Node.js ve C++ kullanarak Dilimleyiciyi Güncelleme
linktitle: Süzgeci Güncelleme
type: docs
weight: 50
url: /tr/nodejs-cpp/updating-slicer/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak bağlantılı pivot tabloları dilimleyici güncelleyerek nasıl güncelleneceğini gösterir.
keywords: Aspose.Cells Node.js ve C++, Dilimleyiciyi Güncelle, Node.js de dilimleyiciyi nasıl değiştirilir, Node.js de dilimleyiciyi nasıl ayarlarız, Node.js ile dilimleyici öğelerini seç veya seçiminden kaldır.
---

## **Olası Kullanım Senaryoları**

 Bir dilimleyiciyi Microsoft Excel'de güncellemek istiyorsanız, öğelerini seçin veya seçimden kaldırın ve ardından dilimleyici tablosunu veya pivot tablosunu buna göre güncelleyecektir. Lütfen [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--) kullanarak Aspose.Cells ile dilimleyici öğelerini seç veya kaldır ve sonra [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--) metodunu çağırarak dilimleyici tablosunu veya pivot tablosunu güncelleyin.

## **Süzgeci Nasıl Güncellenir**

Aşağıdaki örnek kod, mevcut bir süzgeç içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Süzgecin 2. ve 3. öğelerini seçmez ve süzgeci yeniler. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Ekran görüntüsünde, örnek kodun örnek Excel dosyasındaki etkisini görebilirsiniz. Ekran görüntüsünde, seçili öğelerle süzgeci yenilemenin aynı zamanda özet tabloyu da yenilediğini görebilirsiniz.

![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
