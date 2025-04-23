---
title: Excel kullanmadan Node.js ile C++ aracılığıyla Dondurulmuş Durumu nasıl kontrol edilir
linktitle: Dondurulmuş Durum
type: docs
weight: 190
url: /tr/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: Bu makalede, Node.js ve C++ kütüphanesi kullanarak bir Excel çalışma sayfasının dondurulmuş durumunu programatik olarak nasıl kontrol edeceğinizi öğreneceksiniz.

---

## **Giriş**

Bu makalede, bir Excel çalışma sayfasının programatik olarak nasıl dondurulmuş olduğunu kontrol etmeyi öğreneceğiz. MS Excel'de çalışma sayfasının dondurulup bölünüp bölünmediğini kolayca bulabiliriz. Ama Node.js ile dondurulmuş mu yoksa bölünmüş mü olduğunu bulmanın bir yolu var mı? Bunu basitçe Aspose.Cells for Node.js via C++ ile yapabiliriz.

## **Pencereler Dondurulmuş mu**
Aspose.Cells for Node.js via C++ ile pencerenin dondurulup durmadığını ve kaç satır ve sütunun kilitli olduğunu kontrol edebiliriz.

Lütfen [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--) özelliğini kullanarak pencere bölmelerinin durumunu kontrol edin ve [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--) yöntemiyle kilitli satır ve sütunları alın.
1. Dosyayı açmak için Workbook'u oluşturun.
2. Çalışma sayfasının dondurulup dondurulmadığını kontrol edin.
3. Kilitli satır ve sütunları alın.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
