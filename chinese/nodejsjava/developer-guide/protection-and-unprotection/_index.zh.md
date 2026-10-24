---
title: 保护和取消保护
linktitle: 加密和保护
description: 本节介绍如何加密和解密 Excel 文件以及保护 Excel 数据，涵盖文件加密、只读保护、工作簿结构保护、工作表保护以及使用 JavaScript 代码进行数字签名
keywords: Aspose.Cells, Node.js via Java, 加密, 解密, 密码, 保护, 取消保护, 工作簿保护, 工作表保护, 只读, 数字签名, JavaScript
type: docs
weight: 68
url: /zh/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 工作簿通常存储敏感的财务、商业或个人数据，必须防止未经授权的访问。Aspose.Cells for Node.js via Java 提供了一整套与 Microsoft Excel 功能相对应的保护特性，允许您在文件级别、工作簿级别和工作表级别保护数据安全。

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java 提供从文件级到数据级的广泛保护功能，与 MS Excel 类似。这些功能包括使用密码加密文件、通过密码强制执行只读访问以进行修改、保护工作簿结构、保护工作表，以及对工作簿进行数字签名。
{{% /alert %}}

## 加密和解密 Excel 文件
在 Excel 文件上设置密码可以防止未经授权的用户打开或查看工作簿内容。要加密工作簿，请将密码字符串赋值给 `workbook.getSettings().setPassword(...)`，然后保存工作簿。Aspose.Cells 会以加密形式写入文件。要打开已加密的工作簿进行解密，请实例化一个 `LoadOptions` 对象，将 `loadOptions.setPassword(...)` 设置为加密时使用的相同密码，并将其传递给 `Workbook` 构造函数。Aspose.Cells 会透明地应用所提供的密码，使其余代码可以像访问普通工作簿一样与解密后的内容进行交互。

```javascript
const AsposeCells = require("aspose.cells");
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
Excel 支持两种不同的密码层。第一种是打开密码，它会对文件本身进行加密，已在上一节中介绍。第二种是修改密码，它不会阻止用户打开工作簿；而是 Excel 建议以只读模式打开文件，除非提供修改密码。可通过 Aspose.Cells 中的 `workbook.getSettings().getWriteProtection()` 配置此行为。将其 `Password` 属性设置为修改密码，并将其 `Author` 属性设置为应用该保护的用户标识。使用 `writeProtection.validatePassword(string)` 方法检查所提供的修改密码是否正确，匹配返回 `true`，否则返回 `false`。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// 向第一个工作表的 A1 单元格写入一个示例值
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

## 保护与取消保护工作簿结构
保护工作簿结构可以防止其他用户查看隐藏的工作表、添加新工作表、移动工作表、删除工作表、隐藏工作表或重命名工作表。受保护状态适用于工作表结构本身，而非任何工作表内的单元格内容。要应用结构保护，请调用 `workbook.protect(ProtectionType.Structure, "password")`。要取消保护，请调用 `workbook.unprotect("password")` 并提供正确的密码。此处使用的 `ProtectionType.Structure` 枚举值与其他保护类型（如 `ProtectionType.Windows`）有所区别。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// 添加第二个工作表
workbook.getWorksheets().add();
// 在第一个工作表的 A1 单元格中写入一个示例值
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// 保护工作簿结构
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// 将工作簿另存为 structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// 将文件重新加载到新的 Workbook 实例中
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// 移除结构保护
loadedWorkbook.unprotect("StructPwd");
// 打印确认消息
console.log("Structure protection has been successfully removed from the workbook.");
```

## 保护与取消保护工作表
工作表保护可以锁定工作表的单元格，防止意外或故意的更改。用户在未提供密码的情况下无法编辑锁定的单元格。这是用于在共享电子表格中保护公式、标题或指定数据输入区域的典型保护方式。要保护工作表，请调用 `worksheet.protect(ProtectionType.All, "password")`。使用 `ProtectionType.All` 将启用所有可用的保护选项，例如选择锁定的单元格、设置单元格格式、插入行和列以及删除行和列。要取消保护，请使用正确的密码调用 `worksheet.unprotect("password")`。通过使用按位或组合其他保护类型（如 `Contents`、`Objects` 和 `Scenarios`），可以提供更精细的控制。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## 添加和验证数字签名
数字签名可向接收方保证工作簿内容是真实的，并且自签名以来未被篡改。Aspose.Cells 通过 `AsposeCells.DigitalSignature` 和 `AsposeCells.DigitalSignatureCollection` 等类提供数字签名支持。典型流程是直接从 `.pfx` 证书文件及其密码和签名备注创建 `AsposeCells.DigitalSignature`，将签名添加到 `DigitalSignatureCollection`，再通过 `workbook.addDigitalSignature(DigitalSignatureCollection)` 应用到工作簿。`DigitalSignature.Comments` 属性可以记录签名上下文，例如签名时间和用途。对签名后的工作簿所做的任何修改都会使签名失效，因此接收方的验证步骤可以检测篡改行为。

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}