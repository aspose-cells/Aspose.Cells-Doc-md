---
title: Node.js ile C++ kullanarak Çalışma Kitabını yüklerken Tanımlı İsimleri Filtrele
linktitle: Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele
type: docs
weight: 50
url: /tr/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabındaki tanımlı isimleri filtrelemenize veya kaldırmanıza olanak tanır. Lütfen [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) kullanarak tanımlı isimleri yükleyin ve [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) kullanarak yükleme sırasında bunları kaldırın. Lütfen, tanımlı isimleri kaldırırsanız, çalışma kitabındaki formüllerin bozulabileceğini unutmayın.

## **Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele**

Aşağıdaki örnek kod, içinde tanımlı isimler bulunan ve hücre **C1**'de formül olan [örnek Excel dosyasını](61767860.xlsx) yükler; yani, *=SUM(MyName1, MyName2)*. Çalışma kitabını yüklerken [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) kullanarak tanımlı isimleri kaldırdığımız için, [çıktı Excel dosyasındaki](61767861.xlsx) C1 hücresindeki formül bozulur ve yerine *#NAME?* görünür. Lütfen aşağıdaki ekran görüntüsüne bakın, bu kodun örnek Excel dosyası üzerindeki etkisini gösterir.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
