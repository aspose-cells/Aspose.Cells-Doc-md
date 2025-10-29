---
title: Использование класса GlobalizationSettings для настройки пользовательских меток подитогов и других меток диаграмм с помощью Node.js через C++
linktitle: Использование класса GlobalizationSettings для пользовательских подписей и других меток в круговой диаграмме
type: docs
weight: 70
url: /ru/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Узнайте, как настроить метки подитогов и другие метки диаграмм с помощью класса GlobalizationSettings в Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

 APIs Aspose.Cells предоставили класс [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) для работы в сценариях, когда пользователь хочет использовать пользовательские метки для подитогов в таблице. Кроме того, класс [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) также может использоваться для изменения метки **Other** для диаграммы с круговой диаграммой при отображении листа или диаграммы.

## **Введение в класс GlobalizationSettings**

Класс [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) в настоящее время предлагает 3 метода, которые можно переопределить в пользовательском классе для получения нужных меток подитогов или для отображения пользовательского текста для метки **Other** круговой диаграммы.

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-): Получает полное имя функции.
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-): Получает полное имя итоговой функции.


### **Пользовательские метки для итогов**

Класс [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) можно использовать для настройки меток подитогов, переопределяя методы [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-) и [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-) как показано ниже.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}
```

Для внедрения пользовательских меток необходимо назначить свойство [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--) экземпляру класса **CustomSettings**, определенного выше, перед добавлением подитогов в лист.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads an existing spreadsheet containing some data
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
workbook.getSettings().setGlobalizationSettings(new CustomSettings());

// Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
const sheet = workbook.getWorksheets().get(0);

// Adds Subtotal of type Average to the worksheet
sheet.getCells().subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

// Calculates Formulas
workbook.calculateFormula();

// Auto fits all columns
sheet.autoFitColumns();

// Saves the workbook on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```

{{% alert color="primary" %}}

Класс [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) работает только для добавления новых подитогов. Если в таблице уже есть подитоги, их метки изменить нельзя.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
