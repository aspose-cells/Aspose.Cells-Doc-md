---  
title: 使用Node.js通过C++实现错误检查选项  
linktitle: 使用错误检查选项  
type: docs  
weight: 140  
url: /zh/nodejs-cpp/use-error-checking-options/  
description: 学习如何使用Excel工作表中的错误检查选项，使用Aspose.Cells for Node.js via C++进行编程  
keywords: 使用Node.js通过C++在Excel中将存储人数作为文本，错误检查Excel选项Node.js通过C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel允许用户定义错误检查选项和规则。当创建公式时，用户通常会看到错误检查，单元格右上角的小三角形突出显示当单元格存在问题时。Excel提供帮助用户纠正常见问题的信息。  
{{% /alert %}}  

## **错误类型**  

 表示公式无法返回结果的错误（如将数字除以零）需要立即处理，会在单元格中显示错误值。点击绿色三角会显示感叹号，点击会打开选项列表。  

 可以使用选项解决错误或忽略。忽略错误意味着该错误在后续错误检查中不会再次显示。  

 Aspose.Cells提供错误检查选项功能。[**ErrorCheckOption**](https://reference.aspose.com/cells/nodejs-cpp/errorcheckoption)类管理不同类型的错误检查，例如，将文本存储的数字、公式计算错误和验证错误。使用[**ErrorCheckType**](https://reference.aspose.com/cells/nodejs-cpp/errorchecktype)枚举设置所需的错误检查。  

## **作为文本存储的数字**  

有时，数字可能被格式化并作为文本存储在单元格中。这可能会导致计算出现问题或产生令人困惑的排序顺序。格式为文本的数字在单元格中是左对齐而不是右对齐的。如果应执行单元格上的公式未返回值，则检查公式引用的单元格中的对齐方式 - 可能是其中一些或全部的单元格被格式为文本。  

可以使用错误检查选项快速将作为文本存储的数字转换为实际数字。在Microsoft Excel 2003中：  

1. 在“工具”菜单上，单击“选项”。  
1. 选择“错误检查”选项卡。  
   **将作为文本存储的数字** 选项默认为选中状态。  
1. 取消其选中状态。  

以下示例代码显示如何使用Aspose.Cells APIs在模板XLS文件中禁用工作表中的文本存储的数字错误检查选项。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a workbook and opening a template spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Instantiate the error checking options
const opts = sheet.getErrorCheckOptions();

const index = opts.add();
const opt = opts.get(index);
// Disable the numbers stored as text option
opt.setErrorCheck(AsposeCells.ErrorCheckType.NumberStoredAsText, false);
// Set the range
opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

const outputFilePath = path.join(dataDir, "out_test.out.xlsx");
// Save the Excel file
workbook.save(outputFilePath);
```  
