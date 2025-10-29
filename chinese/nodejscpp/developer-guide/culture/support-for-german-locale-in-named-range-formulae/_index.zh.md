---  
title: 通过C++在Node.js中支持德国本地化的命名范围公式  
linktitle: 支持在命名范围公式中使用德国区域设置  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/support-for-german-locale-in-named-range-formulae/  
description: 学习如何使用Aspose.Cells for Node.js via C++支持命名范围公式中的德国本地化。  
---  

英文公式被写入命名区域。此Excel文件可以在系统配置为德国本地化的环境中打开，但英文公式应被翻译为德语。以下示例演示了此功能；但需要在德语环境下安装Excel，并且系统区域设置也应为德语。  

可从以下链接下载用于测试此功能的示例文件：  

[sampleNamedRangeTest.xlsm](73990165.xlsm)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const fs = require("fs");

const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNamedRangeTest.xlsm");
const outputFilePath = path.join(dataDir, "sampleOutputNamedRangeTest.xlsm");

const wb = new AsposeCells.Workbook();
wb.save(sourceFilePath);

const name = "HasFormula";
const value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))";

const wbSource = new AsposeCells.Workbook(sourceFilePath);
const wsCol = wbSource.getWorksheets();

const nameIndex = wsCol.getNames().add(name);
const namedRange = wsCol.getNames().get(nameIndex);
namedRange.setRefersTo(value);

wbSource.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
