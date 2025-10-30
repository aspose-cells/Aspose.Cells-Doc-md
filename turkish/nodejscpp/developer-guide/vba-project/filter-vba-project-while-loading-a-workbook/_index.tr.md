---
title: Bir çalışma kitabını yüklerken VBA Projesini filtreleme (Node.js ve C++ ile)
linktitle: Çalışma kitabı yüklenirken VBA Projesini filtrele
type: docs
weight: 140
url: /tr/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: Aspose.Cells for Node.js via C++ kullanarak Excel çalışma kitaplarını yüklerken VBA projelerini nasıl filtreleyeceğinizi öğrenin.
---

## **Node.js ve C++ kullanarak bir Excel çalışma kitabını yüklerken VBA Projesini filtrele**

Bazı .xlsm/.xslb dosyalarında aşırı büyük miktarda makro (veya çok uzun makrolar) bulunur. Aspose.Cells for Node.js via C++, bu tür çalışma kitaplarını açarken bu (meta) verileri fark etmeden yükleyecektir. Bunun yerine, yalnızca sayfa adlarını çıkarmak istiyorsanız, bu gereksiz içeriği atlamak için [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) kullanabilirsiniz. Bu filtre, yeni bir seçenek olan [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) eklenerek sağlanmıştır.

## **Örnek Kod**

Aşağıdaki örnek kod, yalnızca VBA'nın filtrelenerek bir çalışma kitabı yükler. Bu özelliği test etmek için kullanılabilecek bir örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
