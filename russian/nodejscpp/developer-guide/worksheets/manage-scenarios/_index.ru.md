---
title: Создавайте, управляйте или удаляйте сценарии на листах с помощью Node.js через C++
linktitle: Управление сценариями
type: docs
weight: 190
url: /ru/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Научитесь создавать, управлять или удалять сценарии на листах Excel программно с помощью Node.js и API C++.
keywords: Создавать сценарий листа node.js через C++, удалять сценарий листа excel через node.js через C++, управлять сценарием листа node.js через C++
---

{{% alert color="primary" %}}

Иногда вам может понадобиться создавать, изменять или удалять сценарии в электронных таблицах. Сценарий - это именованная модель «что если?», которая включает в себя переменные ввода, связанные одной или несколькими формулами. Перед созданием сценария разработайте лист книги так, чтобы в нем была по крайней мере одна формула, зависимая от ячеек, в которые можно вводить различные значения. В следующем примере показано, как создавать и удалять сценарии из листа книги в книге с помощью API Aspose.Cells.

{{% /alert %}}

Aspose.Cells предоставляет некоторые полезные классы, например, классы [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection) и [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell). Он также предоставляет свойство [**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--). Приведенный ниже пример кода открывает файл Excel XLSX, содержащий несколько сценариев, удаляет существующий сценарий и добавляет новый сценарий на лист перед сохранением файла Excel. Пример использует очень простой файл шаблона, содержащий сценарий.

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
