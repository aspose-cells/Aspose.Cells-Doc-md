---  
title: Sheet Sekme Çubuğu nu Node.js ve C++ kullanarak nasıl kontrol edebilirsiniz  
linktitle: Sayfa Sekmesi Çubuğunu Nasıl Kontrol Edilir  
type: docs  
weight: 600  
url: /tr/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Aspose.Cells for Node.js via C++ kullanarak sayfa sekmesi çubuğunu nasıl kontrol edileceğini öğrenin.  
keywords: Node.js ve C++ kullanarak Sayfa Sekmesi Çubuğunu Kontrol Etme, Sayfa Sekmesi Çubuğu Operasyonu, Sayfa Sekmesi Çubuğunu Kuru, C++ ve Node.js ile Sayfa Sekmesi Çubuğu Kontrolü.  
---  

## **Olası Kullanım Senaryoları**  
Excel sayfa çubuğunun gösterimini ayarlamak istediğinizde, sayfa sekmesi çubuğunu nasıl kontrol edeceğinizi bilmeniz gerekir, örneğin gizleme veya gösterme, genişliği değiştirme, ilk görünür sekmeyi belirleme vb. Aspose.Cells for Node.js via C++ bu özellikleri destekler. Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olacak aşağıdaki özellikleri ve yöntemleri sağlar.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **Aspose.Cells for Node.js via C++ kullanarak Sayfa Sekmesi Çubuğunu Kontrol Etme**  
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Sayfa sekmesini görüntüleyin ve sekme çubuğunun genişliğini ayarlayın.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

Sonuç dosyası önizlemesi:  
<br>  
<image src="result.png" width="70%" />  


{{< app/cells/assistant language="nodejs-cpp" >}}
