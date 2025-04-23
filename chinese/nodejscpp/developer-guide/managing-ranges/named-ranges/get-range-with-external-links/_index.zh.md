---
title: 通过 C++ 使用 Node.js 获取带有外部链接的范围
linktitle: 获取带有外部链接的范围
type: docs
weight: 120
url: /zh/nodejs-cpp/get-range-with-external-links/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 获取带有外部链接的范围。高效地从不同的 Excel 文件中检索数据。
---

## **获取带有外部链接的范围**

许多时候，Excel 文件通过外部链接访问其他文件中的数据。Aspose.Cells for Node.js via C++ 提供了使用 [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) 方法检索这些外部链接的选项。[**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) 方法返回一个类型为 [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) 的数组。[**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) 类提供一个 [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) 属性，返回外部文件的名称。[**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) 类公开以下成员。

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): 区域的结束列
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): 区域的结束行
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): 获取外部文件名（如果这是外部引用）
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): 表示这是否是一个区域
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): 表示这是不是外部链接
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): 表示这引用在哪个工作表中
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): 区域的起始列
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): 区域的起始行

下面的示例代码演示了如何使用 [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) 方法获取带外部链接的范围。

## **示例代码**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
