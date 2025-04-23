---
title: Power Query Formel Öğesi ile Node.js kullanarak Güncelleyin
linktitle: Güç Sorgusu Formül Öğesini Güncelle
type: docs
weight: 120
url: /tr/nodejs-cpp/update-power-query-formula-item/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyasındaki Power Query Formel öğesinin veri kaynağını nasıl güncelleyeceğinizi öğrenin.
---

## **Kullanım Senaryosu**

Veri kaynağı dosyaları taşındığında ve Excel dosyası dosyayı bulamadığında, Aspose.Cells API, [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) sınıfını kullanarak kaynak dosyanın konumunu güncelleyerek Power Query Formel Öğesini güncelleme seçeneği sunar.

## **Power Query Formel Öğesi Güncelleme**

Aspose.Cells API, Power Query Formel Öğelerini güncelleme yeteneği sağlar. Aşağıdaki kod parçacığı, [**PowerQueryFormulaItem.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#getValue--) özelliğini kullanarak Excel dosyasındaki veri kaynağı dosya konumunu güncellemeyi gösterir. Kaynak ve çıktı dosyaları referansınız için eklenmiştir.

- [Kaynak Dosya 1](106364953.xlsx)
- [Kaynak Dosya 2](106364954.xlsx)
- [Çıktı Dosyası](106364955.xlsx)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Working directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SamplePowerQueryFormula.xlsx"));
const mashupData = workbook.getDataMashup();

const powerQueryFormulas = mashupData.getPowerQueryFormulas();
const count = powerQueryFormulas.getCount();
for (let i = 0; i < count; i++) 
{
const formula = powerQueryFormulas.get(i);
const items = formula.getPowerQueryFormulaItems();
const itemsCount = items.getCount();
for (let j = 0; j < itemsCount; j++) 
{
const item = items.get(j);
if (item.getName() === "Source") 
{
item.setValue(`Excel.Workbook(File.Contents("${path.join(sourceDir, "SamplePowerQueryFormulaSource.xlsx")}", null, true)`);
}
}
}

// Save the output workbook.
workbook.save(outputDir + "SamplePowerQueryFormula_out.xlsx");
```
