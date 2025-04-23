---  
title: 使用 Node.js通过 C++ 中的正则表达式替换工作簿中的文本  
linktitle: 使用正则表达式在工作簿中替换文本  
type: docs  
weight: 90  
url: /zh/nodejs-cpp/replace-text-in-a-workbook-using-regular-expression/  
description: 在 Node.js 通过 C++ 中使用正则表达式替换工作簿中的文本。  
---  

Aspose.Cells 提供通过正则表达式替换工作簿中内容的功能。为此，API 提供 [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) 属性在 [**ReplaceOptions**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions) 类中。将 [**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--) 设置为 **true** 表示搜索的关键词将作为正则表达式处理。

以下代码片段演示了如何使用[**ReplaceOptions.getRegexKey()**](https://reference.aspose.com/cells/nodejs-cpp/replaceoptions/#getRegexKey--)属性，配合[示例Excel文件](101089318.xlsx)。生成的[输出文件](101089319.xlsx)已附带供参考。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "SampleRegexReplace.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const replace = new AsposeCells.ReplaceOptions();
replace.setCaseSensitive(false);
replace.setMatchEntireCellContents(false);
// Set to true to indicate that the searched key is regex
replace.setRegexKey(true);

workbook.replace("\\bKIM\\b", "^^^TIM^^^", replace);
workbook.save(path.join(outputDir, "RegexReplace_out.xlsx"));
```  

