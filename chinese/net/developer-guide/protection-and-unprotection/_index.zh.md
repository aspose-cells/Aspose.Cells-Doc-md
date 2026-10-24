---
title: 保护与撤销保护
linktitle: 保护与撤销保护
description: 本节介绍如何使用 C# 代码对 Excel 文件进行加密和解密以及保护 Excel 数据，涵盖文件加密、只读保护、工作簿结构保护、工作表保护以及数字签名
keywords: Aspose.Cells, .NET, 加密, 解密, 密码, 保护, 撤销保护, 工作簿保护, 工作表保护, 只读, 数字签名, C#
type: docs
weight: 68
url: /zh/net/protect-and-unprotect/
alias: [/net/security-features/]
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 工作簿通常存储敏感的财务、商业或个人信息，必须防止未经授权的访问。Aspose.Cells for .NET 提供了一套全面的保护功能，涵盖了 Microsoft Excel 的相应能力，允许您在文件级、工作簿级和工作表级保护数据安全。

{{% alert color="primary" %}}
Aspose.Cells for .NET 提供了从文件级到数据级的广泛保护功能，类似于 MS Excel。这些功能包括使用密码对文件进行加密、通过修改密码强制只读访问、保护工作簿结构、保护工作表以及为工作簿添加数字签名。
{{% /alert %}}

## 加密和解密 Excel 文件
在 Excel 文件上设置密码可以防止未经授权的用户打开或查看工作簿内容。要加密工作簿，需要将密码字符串分配给 `Workbook.Settings.Password`，然后保存工作簿。Aspose.Cells 将以加密形式写入文件。要打开加密的工作簿进行解密，请实例化一个 `LoadOptions` 对象，将 `LoadOptions.Password` 设置为加密时使用的相同密码，并将其传递给 `Workbook` 构造函数。Aspose.Cells 会透明地应用所提供的密码，以便代码其余部分可以像处理普通工作簿一样与解密后的内容进行交互。

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## 只读保护（修改密码）
Excel 支持两个不同的密码层。第一层是打开密码，用于加密文件本身，已在前一节中介绍。第二层是修改密码，它不会阻止用户打开工作簿；而是 Excel 建议以只读模式打开文件，除非提供修改密码。通过 `Workbook.Settings.WriteProtection` 在 Aspose.Cells 中配置此行为。将其 `Password` 属性设置为修改密码，将其 `Author` 属性设置为应用保护者的标识。使用 `WriteProtection.ValidatePassword(string)` 方法检查修改密码是否正确，匹配时返回 `true`，否则返回 `false`。

```csharp
using System;
using Aspose.Cells;
// 从头开始创建一个新的工作簿
Workbook workbook = new Workbook();
// 向第一个工作表的 A1 单元格写入一个示例值
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// 配置写保护：设置修改密码和作者
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// 保存工作簿以使写保护生效
workbook.Save("WriteProtectedWorkbook.xlsx");
// 使用正确的密码验证修改密码
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// 使用错误的密码验证修改密码以演示另一分支
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## 保护和撤销保护工作簿结构
保护工作簿结构可以防止其他用户查看隐藏工作表、添加新工作表、移动工作表、删除工作表、隐藏工作表或重命名工作表。受保护状态适用于工作表结构，而非任何工作表内的单元格内容。要应用结构保护，请调用 `workbook.Protect(ProtectionType.Structure, "password")`。要移除保护，请调用 `workbook.Unprotect("password")` 并提供正确的密码。此处使用了 `ProtectionType.Structure` 枚举值，它与 `ProtectionType.Windows` 等其他保护类型不同。

```csharp
using System;
using Aspose.Cells;
// 创建一个新的工作簿
Workbook workbook = new Workbook();
// 添加第二个工作表
workbook.Worksheets.Add();
// 向第一个工作表的A1单元格写入一个示例值
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// 保护工作簿结构
workbook.Protect(ProtectionType.Structure, "StructPwd");
// 将工作簿保存为 structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// 将文件重新加载到新的 Workbook 实例中
Workbook loadedWorkbook = new Workbook(filePath);
// 移除结构保护
loadedWorkbook.Unprotect("StructPwd");
// 打印确认消息
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## 保护和撤销保护工作表
工作表保护可锁定工作表中的单元格，以防止意外或故意的更改。用户在不提供密码的情况下无法编辑锁定的单元格。这是用于保护共享电子表格中公式、标题或指定数据输入区域的典型保护方式。要保护工作表，请调用 `worksheet.Protect(ProtectionType.All, "password")`。使用 `ProtectionType.All` 将启用所有可用的保护选项，例如选择锁定的单元格、格式化单元格、插入行和列以及删除行和列。要移除保护，请使用正确的密码调用 `worksheet.Unprotect("password")`。通过使用按位 OR 组合其他保护类型（如 `Contents`、`Objects` 和 `Scenarios`），可以实现更精细的控制。

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## 添加和验证数字签名
数字签名可确保接收方工作簿内容是真实的，并且在签名后未被篡改。Aspose.Cells 通过 `Aspose.Cells.DigitalSignatures` 命名空间提供数字签名支持。典型的工作流程是通过 `System.Security.Cryptography.X509Certificates.X509Certificate2` 加载 `.pfx` 证书文件，将其包装到 `Aspose.Cells.DigitalSignatures.DigitalSignature` 中，将签名添加到 `DigitalSignatureCollection`，然后通过 `Workbook.AddDigitalSignature(DigitalSignatureCollection)` 将该集合应用于工作簿。`DigitalSignature.Comments` 属性可以记录签名上下文，例如签名时间和目的。在签名后对工作簿所做的任何更改都会使签名失效，因此接收方的验证步骤可以检测篡改行为。

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## 相关文章
- [加密和解密 Excel 文件](/cells/zh/net/encrypt-and-decrypt-excel-files/)
- [保护和撤销保护工作簿结构](/cells/zh/net/protect-and-unprotect-workbook-structure/)
- [保护和撤销保护工作表](/cells/zh/net/protect-and-unprotect-worksheets/)
- [密码保护或撤销保护共享工作簿](/cells/zh/net/password-protect-or-unprotect-the-shared-workbook/)
- [分配和验证数字签名](/cells/zh/net/assign-and-validate-digital-signatures/)
- [使用 Aspose.Cells 检查修改密码](/cells/zh/net/check-password-to-modify-using-aspose-cells/)
- [检测加密的 Office Open XML - OOXML 文件的文件格式](/cells/zh/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [加密 Excel 文件](/cells/zh/net/encrypting-excel-files/)
- [如何检测文件格式并检查文件是否已加密](/cells/zh/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}