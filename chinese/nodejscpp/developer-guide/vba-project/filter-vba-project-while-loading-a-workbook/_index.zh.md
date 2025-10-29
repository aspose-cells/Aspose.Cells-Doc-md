---
title: 在加载工作簿时使用Node.js通过C++过滤VBA项目
linktitle: 在加载Excel工作簿时过滤VBA项目
type: docs
weight: 140
url: /zh/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: 学习如何在加载Excel工作簿时使用Aspose.Cells for Node.js via C++过滤VBA项目。
---

## **在Node.js通过C++加载Excel工作簿时过滤VBA项目**

某些.xlsm/.xslb文件具有极大量的宏（或非常长的宏）。Aspose.Cells for Node.js via C++在打开此类工作簿时会无条件加载这些（元）数据。在你只需要提取工作表名称而不需加载任务的情况下，可能需要控制此项，避免加载无用内容。这通过引入新选项[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions)实现。

## **示例代码**

以下示例代码加载工作簿，仅过滤 VBA。可以从以下链接下载用于测试此功能的示例文件：

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
