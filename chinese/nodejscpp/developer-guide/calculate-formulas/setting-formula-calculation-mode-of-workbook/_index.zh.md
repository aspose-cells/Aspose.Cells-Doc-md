---  
title: 在使用 Node.js via C++ 时设置工作簿的公式计算模式  
linktitle: 设置工作簿的公式计算模式  
description: 本文介绍了如何通过 Aspose.Cells for Node.js via C++ 设置 Microsoft Excel 中文档的公式计算模式。通过加载现有的 Excel 文件或创建新文件，使用 Aspose.Cells 提供的方法设置公式计算模式并获取结果。最后，将修改后的 Excel 文件保存到磁盘。  
keywords: Aspose.Cells，Excel，工作簿，公式计算模式，设置，Node.js via C++  
type: docs  
weight: 110  
url: /zh/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
---  

{{% alert color="primary" %}}  
Microsoft Excel允许您设置公式计算模式，即公式计算的方式。有三种可能的值：  

- 自动 - 每当有变更时重新计算，并且每次打开工作簿时。  
- 自动除数据表外 - 每当有变更时重新计算，但是不包括数据表。  
- 手动 - 仅当用户通过按F9或CTRL+ALT+F9明确请求时，或者保存工作簿时重新计算。  
{{% /alert %}}  

在Microsoft Excel中设置公式计算模式：  

1. 选择**公式**然后**计算选项**。  
1. 选择其中一个选项。  

Aspose.Cells for Node.js via C++ 还允许你使用 [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--) 模式属性设置 **Formula Calculation Mode**。可以为其赋值为具有以下值之一的 [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype) 枚举：  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

