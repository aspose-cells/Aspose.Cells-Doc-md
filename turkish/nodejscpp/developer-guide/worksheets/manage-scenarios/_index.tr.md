---
title: Node.js ve C++ kullanarak çalışma sayfalarından Senaryolar Oluşturma, Manipüle Etme veya Kaldırma
linktitle: Senaryoları Yönetme
type: docs
weight: 190
url: /tr/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Node.js ve C++ API kullanarak Excel Çalışma Sayfalarından senaryolar oluşturmayı, manipüle etmeyi veya kaldırmayı öğrenin.
keywords: senaryo oluşturma node.js ve C++ ile çalışma sayfası, çalışma sayfasından senaryoyu kaldırma node.js ve C++ ile, senaryo manipülasyonu node.js ve C++ ile
---

{{% alert color="primary" %}}

Bazen Elektronik Tablolarda senaryolar oluşturmanızı, manipüle etmenizi veya silmenizi gerekebilir. Senaryo, bir veya daha fazla formülle bağlı değişken giriş hücrelerini içeren adlandırılmış 'ne olurdu?' modelidir. Bir senaryo oluşturmadan önce, farklı değerlerin eklenebileceği en az bir formül içeren çalışma sayfasını tasarlayın. Aşağıdaki örnek, Aspose.Cells API'leri aracılığıyla bir iş kitabındaki bir çalışma sayfasından senaryolar oluşturmayı ve kaldırmayı gösterir.

{{% /alert %}}

Aspose.Cells, örneğin [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection), ve [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell) sınıfları gibi bazı kullanışlı sınıflar sağlar. Ayrıca [**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--) özelliğini sağlar. Aşağıdaki örnek, birkaç senaryo içeren XLSX Excel dosyasını açar ve mevcut bir senaryoyu kaldırır. Ayrıca, Excel dosyasını kaydetmeden önce çalışma sayfasına yeni bir senaryo ekler. Örnek, senaryo içeren çok basit bir şablon dosyası kullanır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

if (worksheet.getScenarios().getCount() > 0) {
// Remove the existing first scenario from the sheet
worksheet.getScenarios().removeAt(0);

// Create a scenario
const i = worksheet.getScenarios().add("MyScenario");
// Get the scenario
const scenario = worksheet.getScenarios().get(i);
// Add comment to it
scenario.setComment("Test scenario is created.");
// Get the input cells for the scenario
const sic = scenario.getInputCells();
// Add the scenario on B4 (as changing cell) with default value
sic.add(3, 1, "1100000");

const outputFilePath = path.join(dataDir, "outBk_scenarios1.out.xlsx");

// Save the Excel file.
workbook.save(outputFilePath);
console.log("\nProcess completed successfully.\nFile saved at " + outputFilePath);
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
