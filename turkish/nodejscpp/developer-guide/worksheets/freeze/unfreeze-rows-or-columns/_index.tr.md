---
title: Node.js ve C++ kullanarak Satır veya Sütunları Çözmek
linktitle: Pencereleri dondur
type: docs
weight: 190
url: /tr/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: Bu makalede, Node.js API ve C++ kullanarak Excel Çalışma Sayfalarının satır, sütun veya panolarını programatik olarak nasıl çözülür öğreneceksiniz.
keywords: Pane çözme, satır çözme, sütun çözme, pencereleri çözme Node.js ve C++ aracılığıyla.
---

## **Giriş**

Bu makalede, satırları, sütunları ve panoları nasıl çözeriz öğreneceğiz. Eğer Excel dosyasındaki çalışma sayfaları dondurulmuşsa, bazen çalışma sayfasını veya dondurulmuş satır, sütun veya panoları çözmek isteriz.


## **Excel'de**

1. Görünüm sekmesine tıklayın > Bölmeleri Dondur > Bölmeleri Çöz

**![Excel'de bölmeleri çöz](Unfreeze-Panes.png)**




## **Aspose.Cells for Node.js via C++ ile Satır, Sütun veya Panoları Çözme**
Pane çözme işlemini Aspose.Cells for Node.js via C++ ile kolayca yapabilirsiniz. Lütfen [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--) metodunu kullanarak panoları çözün.

1. Donmuş dosyayı açmak için Workbook oluşturun.
2. Worksheet.unfreezePanes() yöntemiyle panoları çöz.
3. Dosyayı kaydedin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Ekli [örnek kaynak Excel dosyası](Frozen.xlsx).
