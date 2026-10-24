---
title: 保护和取消保护
linktitle: 加密和保护
description: 本节介绍如何使用 Python 代码加密和解密 Excel 文件以及保护 Excel 数据，涵盖文件加密、只读保护、工作簿结构保护、工作表保护以及数字签名
keywords: Aspose.Cells, Python via .NET, 加密, 解密, 密码, 保护, 取消保护, 工作簿保护, 工作表保护, 只读, 数字签名, Python
type: docs
weight: 68
url: /zh/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 工作簿经常存储必须防止未经授权访问的敏感财务、商业或个人信息。Aspose.Cells for Python via .NET 提供了一整套与 Microsoft Excel 功能相对应的保护功能，允许您在文件级别、工作簿级别和工作表级别保护数据。

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET 提供了范围广泛的保护功能，从文件级到数据级，类似于 MS Excel。这些功能包括使用密码加密文件、通过修改密码强制执行只读访问、保护工作簿结构、保护工作表以及对工作簿进行数字签名。
{{% /alert %}}

## 加密和解密 Excel 文件
在 Excel 文件上设置的密码可以防止未经授权的用户打开或查看工作簿内容。要加密工作簿，请将密码字符串赋值给 `workbook.settings.password`，然后保存工作簿。Aspose.Cells 以加密形式写入文件。要打开加密的工作簿进行解密，请实例化一个 `LoadOptions` 对象，将 `load_options.password` 设置为加密时使用的相同密码，并将其传递给 `Workbook` 构造函数。Aspose.Cells 会透明地应用所提供的密码，使代码的其他部分能够像处理普通工作簿一样与解密后的内容进行交互。

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## 只读保护（修改密码）
Excel 支持两个不同的密码层。第一层是打开密码，它会对文件本身进行加密，已在前一节中介绍。第二层是修改密码，它不会阻止用户打开工作簿；相反，除非提供修改密码，否则 Excel 建议以只读模式打开文件。通过 Aspose.Cells 中的 `workbook.settings.write_protection` 配置此行为。将其 `password` 属性设置为修改密码，并将其 `author` 属性设置为应用该保护的用户。使用 `write_protection.validate_password(string)` 方法检查所提供的修改密码是否正确，匹配时返回 `true`，否则返回 `false`。

```python
import aspose.cells as ac
# 创建一个全新的工作簿
workbook = ac.Workbook()
# 向第一个工作表的 A1 单元格写入示例值
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# 配置写保护：设置修改密码和作者
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# 保存工作簿以使写保护生效
workbook.save("WriteProtectedWorkbook.xlsx")
# 使用正确的密码验证修改密码
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# 使用错误的密码验证修改密码以演示另一种情况
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## 保护和取消保护工作簿结构
保护工作簿结构可防止其他用户查看隐藏的工作表、添加新工作表、移动工作表、删除工作表、隐藏工作表或重命名工作表。受保护状态适用于工作表结构，而不是任何工作表内的单元格内容。要应用结构保护，请调用 `workbook.protect(ProtectionType.STRUCTURE, "password")`。要移除保护，请调用 `workbook.unprotect("password")` 并提供正确的密码。此处使用的是 `ProtectionType.STRUCTURE` 枚举值，与 `ProtectionType.WINDOWS` 等其他保护类型不同。

```python
import aspose.cells as ac
# 创建一个新工作簿
workbook = ac.Workbook()
# 添加第二个工作表
workbook.worksheets.add()
# 向第一个工作表的 A1 单元格写入示例值
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# 保护工作簿结构
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# 将工作簿保存为 structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# 将文件重新加载到新的 Workbook 实例中
loaded_workbook = ac.Workbook(file_path)
# 移除结构保护
loaded_workbook.unprotect("StructPwd")
# 打印确认消息
print("Structure protection has been successfully removed from the workbook.")
```

## 保护和取消保护工作表
工作表保护可锁定工作表的单元格，防止意外或故意的更改。用户在没有提供密码的情况下无法编辑已锁定的单元格。这是在共享电子表格中用于保护公式、标题或指定数据输入区域的典型保护方式。要保护工作表，请调用 `worksheet.protect(ProtectionType.ALL, "password")`。使用 `ProtectionType.ALL` 可启用所有可用的保护选项，例如选择锁定的单元格、设置单元格格式、插入行和列以及删除行和列。要移除保护，请使用正确的密码调用 `worksheet.unprotect("password")`。还可以使用按位 OR 组合其他保护类型（如 `Contents`、`Objects` 和 `Scenarios`）以实现更精细的控制。

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## 添加和验证数字签名
数字签名可向接收方保证工作簿内容的真实性，并且自签名以来未被修改。Aspose.Cells 通过 `aspose.cells.digital_signatures` 命名空间提供数字签名支持。典型的工作流程是通过 `System.Security.Cryptography.X509Certificates.X509Certificate2` 加载 `.pfx` 证书文件，将其包装到 `aspose.cells.digital_signatures.DigitalSignature` 中，将签名添加到 `DigitalSignatureCollection`，然后通过 `workbook.add_digital_signature(DigitalSignatureCollection)` 将该集合应用于工作簿。`digital_signature.comments` 属性可以记录签名上下文，例如签名时间和用途。在签名后对工作簿所做的任何修改都会使签名失效，因此接收端的验证步骤可以发现篡改行为。

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## 相关文章
- [加密和解密 Excel 文件](/cells/zh/python-net/encrypt-and-decrypt-excel-files/)
- [保护和取消保护工作簿结构](/cells/zh/python-net/protect-and-unprotect-workbook-structure/)
- [保护和取消保护工作表](/cells/zh/python-net/protect-and-unprotect-worksheets/)
- [使用密码保护或取消保护共享工作簿](/cells/zh/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [分配和验证数字签名](/cells/zh/python-net/assign-and-validate-digital-signatures/)
- [使用 Aspose.Cells 检查修改密码](/cells/zh/python-net/check-password-to-modify-using-aspose-cells/)
- [检测加密的 Office Open XML - OOXML 文件的文件格式](/cells/zh/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [加密 Excel 文件](/cells/zh/python-net/encrypting-excel-files/)
- [如何检测文件格式并检查文件是否已加密](/cells/zh/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}