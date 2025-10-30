---
title: Node.js kullanarak C++ ile Sparkline ekleme
linktitle: Kıvılcımlar
type: docs
weight: 160
url: /tr/nodejs-cpp/creating-sparklines/
description: Aspose.Cells for Node.js via C++ kullanarak Excel için sparkline oluşturun.
---

## **Bir kıvılcım ekleyin**
{{% alert color="primary" %}} 

Sparkline, bir çalışma sayfası hücresinde küçük bir grafiktir ve verilerin görsel temsilini sağlar. Trendleri göstermek için sparklines kullanın, örneğin mevsimsel artışlar veya azalmalar, ekonomik döngüler veya maksimum ve minimum değerleri vurgulamak için. En etkili sonuç için sparklini veriye yakın konumlandırın. Üç tür Sparkline vardır: Çizgi, Sütun ve Yığılmış.

{{% /alert %}} 

Aşağıdaki örnek kodlar ile Aspose.Cells for Node.js via C++ kullanarak basitçe bir sparkline oluşturabilirsiniz:



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);

sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);

// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);

const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);

const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);

// Customize Sparklines

// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight 
group.setLineWeight(1.0);

// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```

## **Gelişmiş Konular**
- [Kıvılcımları ve Ayarları 3B Biçimi kullanarak Kullanma](/cells/tr/nodejs-cpp/using-sparklines-and-settings-3d-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
