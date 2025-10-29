---  
title: 用 Node.js 通过 C++ 实现其他语言的 Subtotal 或 Grand Total 标签  
linktitle: 实现其他语言的子合计或总计标签  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/implement-subtotal-or-grand-total-labels-in-other-languages/  
---  

## **可能的使用场景**  

 有时，你希望用非英文语言如中文、日语、阿拉伯语、印地语等显示 subtotal 和 grand total 标签。Aspose.Cells for Node.js via C++ 允许你通过 [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) 类和 [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/) 属性实现。请参阅关于如何使用 [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) 类的相关文章。  

- [使用GlobalizationSettings类自定义小计标签和饼图的其他标签](/cells/zh/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)  

## **用其他语言实现子合计或总计标签**  

 以下示例代码加载【示例 Excel 文件】(5115151.xlsx)，并用中文实现了 subtotal 和 grand total 的名称。请检查由此代码生成的【输出 Excel 文件】(5115152.xlsx)，以供参考。我们首先创建 [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) 类的实例，然后在代码中使用它。  

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

 现在在代码中使用上述创建的类如下：  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
