---
title: 用Node.js via C++保护和取消保护
linktitle: 加密和保护
description: 本节介绍如何加密和解密 Excel 文件以及如何保护 Excel 数据，涵盖文件加密、只读保护、工作簿结构保护、工作表保护以及使用 JavaScript 代码进行数字签名
keywords: Aspose.Cells, Node.js, C++, 加密, 解密, 密码, 保护, 取消保护, 工作簿保护, 工作表保护, 只读, 数字签名, JavaScript
type: docs
weight: 68
url: /zh/nodejs-cpp/protect-and-unprotect/
alias: [/nodejs-cpp/security-features/]
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 工作簿通常存储必须防止未经授权访问的敏感财务、商业或个人数据。Aspose.Cells for Node.js via C++ 提供了一套全面的保护功能，涵盖了 Microsoft Excel 的相应能力，使您可以在文件级别、工作簿级别和工作表级别保护数据。

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ 提供了从文件级到数据级的广泛保护功能，类似于 MS Excel。这些功能包括使用密码加密文件、通过修改密码强制只读访问、保护工作簿结构、保护工作表以及对工作簿进行数字签名。
{{% /alert %}}

## 加密和解密 Excel 文件
为 Excel 文件设置密码可防止未经授权的用户打开或查看工作簿内容。要加密工作簿，请将密码字符串分配给 `workbook.getSettings().setPassword()`，然后保存工作簿。Aspose.Cells 会以加密形式写入文件。要打开加密的工作簿进行解密，请实例化一个 `LoadOptions` 对象，将 `loadOptions.setPassword()` 设置为加密时使用的相同密码，然后将其传递给 `Workbook` 构造函数。Aspose.Cells 会透明地应用所提供的密码，以便代码的其余部分可以像访问普通工作簿一样与解密后的内容进行交互。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## 只读保护（修改密码）
Excel 支持两种不同的密码层。第一种是打开密码，用于加密文件本身，在上一节中已介绍过。第二种是修改密码，它不会阻止用户打开工作簿；而是 Excel 建议在未提供修改密码的情况下以只读模式打开文件。通过 Aspose.Cells 中的 `workbook.getSettings().getWriteProtection()` 配置此行为。将其 `password` 属性设置为修改密码，将其 `author` 属性设置为标识应用保护的人员。使用 `writeProtection.validatePassword(string)` 方法检查所提供的修改密码是否正确，匹配时返回 `true`，否则返回 `false`。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// 向第一个工作表的 A1 单元格写入示例值
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// 配置写保护：设置修改密码和作者
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// 保存工作簿以使写保护生效
workbook.save("WriteProtectedWorkbook.xlsx");
// 使用正确的密码验证修改密码
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// 使用错误的密码验证修改密码以演示另一种情况
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## 保护和取消保护工作簿结构
保护工作簿结构可防止其他用户查看隐藏的工作表、添加新工作表、移动工作表、删除工作表、隐藏工作表或重命名工作表。受保护状态适用于工作表结构，而不是任何工作表内的单元格内容。要应用结构保护，请调用 `workbook.protect(ProtectionType.Structure, "password")`。要取消保护，请调用 `workbook.unprotect("password")` 并提供正确的密码。此处使用的 `ProtectionType.Structure` 枚举值与其他保护类型（例如 `ProtectionType.Windows`）不同。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// 添加第二个工作表
workbook.getWorksheets().add();
// 向第一个工作表的 A1 单元格写入示例值
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// 保护工作簿结构
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// 将工作簿另存为 structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// 将文件重新加载到新的 Workbook 实例中
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// 移除结构保护
loadedWorkbook.unprotect("StructPwd");
// 打印确认信息
console.log("Structure protection has been successfully removed from the workbook.");
```

## 保护和取消保护工作表
工作表保护可锁定工作表的单元格，防止意外或故意的更改。用户在不提供密码的情况下无法编辑已锁定的单元格。这是用于保护共享电子表格中的公式、标题或指定数据输入区域的典型保护方式。要保护工作表，请调用 `worksheet.protect(ProtectionType.All, "password")`。使用 `ProtectionType.All` 将启用所有可用的保护选项，例如选择锁定的单元格、格式化单元格、插入行和列以及删除行和列。要取消保护，请使用正确的密码调用 `worksheet.unprotect("password")`。可以通过按位 OR 组合其他保护类型（例如 `Contents`、`Objects` 和 `Scenarios`）来实现更精细的控制。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.All, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## 添加和验证数字签名
数字签名向收件人保证工作簿内容是真实的，并且在签名后未被篡改。Aspose.Cells 通过 `Aspose.Cells.DigitalSignatures` 命名空间提供数字签名支持。典型的工作流程是使用 Node.js 的加密工具加载 `.pfx` 证书文件，将其包装在 `Aspose.Cells.DigitalSignatures.DigitalSignature` 中，将签名添加到 `DigitalSignatureCollection`，然后通过 `workbook.addDigitalSignature(digitalSignatureCollection)` 将该集合应用到工作簿。`digitalSignature.comments` 属性可以记录签名上下文，例如签名时间和用途。签名后对工作簿所做的任何修改都会使签名失效，因此接收方可以通过验证步骤检测篡改行为。

```javascript
const AsposeCells = require("aspose.cells.node");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

## 相关文章
- [加密和解密 Excel 文件](/cells/zh/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [保护和取消保护工作簿结构](/cells/zh/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [保护和取消保护工作表](/cells/zh/nodejs-cpp/protect-and-unprotect-worksheets/)
- [密码保护或取消保护共享工作簿](/cells/zh/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [分配和验证数字签名](/cells/zh/nodejs-cpp/assign-and-validate-digital-signatures/)
- [使用 Aspose.Cells 检查修改密码](/cells/zh/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [检测加密的 Office Open XML - OOXML 文件的文件格式](/cells/zh/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [加密 Excel 文件](/cells/zh/nodejs-cpp/encrypting-excel-files/)
- [如何检测文件格式以及检查文件是否已加密](/cells/zh/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}