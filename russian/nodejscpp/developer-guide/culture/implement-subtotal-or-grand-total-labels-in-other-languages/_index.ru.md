---  
title: Реализуйте метки Подитог или Итог в других языках с помощью Node.js через C++  
linktitle: Реализуйте метки Подитог или Итог в других языках  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **Возможные сценарии использования**  

 Иногда вы хотите отображать метки подитогов и итогов на неанглийских языках, таких как китайский, японский, арабский, хинди и т. д. Aspose.Cells for Node.js via C++ позволяет сделать это с помощью класса [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) и свойства [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/). См. статью, как использовать класс [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).  

- [Использование класса GlobalizationSettings для пользовательских меток итогов и других меток круговой диаграммы](/cells/ru/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## ** Реализуйте метки Подитог или Итог в других языках**  

 Следующий пример кода загружает [пример файла Excel](5115151.xlsx) и реализует названия подитогов и итогов на китайском языке. Проверьте созданный по этому коду [выходной файл Excel](5115152.xlsx). Сначала создайте класс [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings), а затем используйте его в нашем коде.  

```javascript
const AsposeCells = require("aspose.cells.node");

class GlobalizationSettingsImp extends AsposeCells.GlobalizationSettings {
// This function will return the sub total name
getTotalName(functionType) {
return "Chinese Total - 可能的用法";
}

// This function will return the grand total name
getGrandTotalName(functionType) {
return "Chinese Grand Total - 可能的用法";
}
}
```  

 Теперь используйте созданный выше класс в коде следующим образом:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Set the globalization setting to change subtotal and grand total names
const globalizationSettings = new AsposeCells.GlobalizationSettings();
workbook.getSettings().setGlobalizationSettings(globalizationSettings);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Apply subtotal on A1:B10
const cellArea = AsposeCells.CellArea.createCellArea("A1", "B10");
worksheet.getCells().subtotal(cellArea, 0, AsposeCells.ConsolidationFunction.Sum, [2, 3, 4]);

// Set the width of the first column
worksheet.getCells().setColumnWidth(0, 40);

// Save the output excel file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

