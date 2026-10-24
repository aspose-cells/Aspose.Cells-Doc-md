---
title: 保护和取消保护
linktitle: 保护
description: 本节介绍如何加密和解密 Excel 文件以及保护 Excel 数据，涵盖文件加密、只读保护、工作簿结构保护、工作表保护以及使用 Python 代码进行数字签名
keywords: Aspose.Cells, Python via Java, 加密, 解密, 密码, 保护, 取消保护, 工作簿保护, 工作表保护, 只读, 数字签名, Python
type: docs
weight: 68
url: /zh/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 工作簿通常存储着敏感的财务、商业或个人数据，必须防止未经授权的访问。Aspose.Cells for Python via Java 提供了一套全面的保护功能，与 Microsoft Excel 的功能相匹配，允许您在文件级别、工作簿级别和工作表级别保护数据。

{{% alert color="primary" %}}
Aspose.Cells for Python via Java 提供了从文件级到数据级的广泛保护功能，与 MS Excel 类似。这些功能包括使用密码加密文件、通过修改密码强制启用只读访问、保护工作簿结构、保护工作表以及对工作簿进行数字签名。
{{% /alert %}}

## 加密和解密 Excel 文件
对 Excel 文件设置密码可以防止未经授权的用户打开或查看工作簿内容。要加密工作簿，请将密码字符串分配给 `workbook.getSettings().setPassword(...)`，然后保存工作簿。Aspose.Cells 以加密形式写入文件。要打开加密的工作簿进行解密，请实例化一个 `LoadOptions` 对象，通过 `load_options.setPassword(...)` 设置与加密时相同的密码，并将其传递给 `Workbook` 构造函数。Aspose.Cells 会透明地应用所提供的密码，使您其余的代码能够像访问常规工作簿一样与解密后的内容进行交互。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## 只读保护（修改密码）
Excel 支持两层不同的密码。第一层是打开密码，用于加密文件本身，已在上一节中介绍。第二层是修改密码，它不会阻止用户打开工作簿；而是 Excel 建议以只读模式打开文件，除非提供修改密码。通过 Aspose.Cells 中的 `workbook.getSettings().getWriteProtection()` 配置此行为。通过 `setPassword(...)` 设置修改密码，通过 `setAuthor(...)` 设置作者以标识谁应用了保护。使用 `writeProtection.validatePassword(String)` 方法检查所提供的修改密码是否正确，匹配时返回 `true`，否则返回 `false`。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# 从头创建一个新工作簿
workbook = Workbook()
# 在第一个工作表的 A1 单元格中写入示例值
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# 配置写保护：设置修改密码和作者
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# 保存工作簿以使写保护生效
workbook.save("WriteProtectedWorkbook.xlsx")
# 使用正确的修改密码进行验证
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# 使用错误的修改密码进行验证以演示其他分支情况
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## 保护与取消保护工作簿结构
保护工作簿结构可以防止其他用户查看隐藏的工作表、添加新的工作表、移动工作表、删除工作表、隐藏工作表或重命名工作表。受保护状态适用于工作表结构，而非任何工作表内的单元格内容。要应用结构保护，请调用 `workbook.protect(ProtectionType.STRUCTURE, "password")`。要移除保护，请调用 `workbook.unprotect("password")` 并提供正确的密码。此处使用的 `ProtectionType.STRUCTURE` 枚举值与其他保护类型（如 `ProtectionType.WINDOWS`）不同。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# 创建一个新工作簿
workbook = Workbook()
# 添加第二个工作表
workbook.getWorksheets().add()
# 在第一个工作表的 A1 单元格中写入示例值
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# 保护工作簿结构
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# 将工作簿保存为 structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# 将文件重新加载到新的 Workbook 实例中
loaded_workbook = Workbook(file_path)
# 移除结构保护
loaded_workbook.unprotect("StructPwd")
# 打印确认消息
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## 保护与取消保护工作表
工作表保护可以将工作表的单元格锁定，防止意外或故意的更改。用户在没有提供密码的情况下无法编辑锁定的单元格。这是用于在共享电子表格中保护公式、标题或指定数据输入区域的典型保护方式。要保护工作表，请调用 `worksheet.protect(ProtectionType.ALL, "password")`。使用 `ProtectionType.ALL` 可以启用所有可用的保护选项，如选择锁定的单元格、设置单元格格式、插入行和列以及删除行和列。要移除保护，请使用正确的密码调用 `worksheet.unprotect("password")`。通过使用按位或运算组合其他保护类型（如 `ProtectionType.CONTENTS`、`ProtectionType.OBJECTS` 和 `ProtectionType.SCENARIOS`），可以进行更细粒度的控制。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## 添加和验证数字签名
数字签名向接收者保证工作簿内容是真实的，并且自签名以来未被篡改。Aspose.Cells 通过 `Aspose.Cells.DigitalSignatures` 命名空间提供数字签名支持。典型的工作流程是通过 `java.security.KeyStore` 加载 `.pfx` 证书文件，将其包装在 `Aspose.Cells.DigitalSignatures.DigitalSignature` 中，将签名添加到 `DigitalSignatureCollection`，然后通过 `workbook.addDigitalSignature(digitalSignatureCollection)` 将该集合应用于工作簿。`digitalSignature.getComments()` 属性可以记录签名上下文，例如签名时间和签名目的。对已签名的工作簿所做的任何修改都会使签名失效，因此接收端的验证步骤可以检测篡改。

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# 使用 Java KeyStore 从 PFX 文件加载证书
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# 获取证书
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# 创建数字签名
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# 创建工作簿并添加签名
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## 相关文章
- [加密和解密 Excel 文件](/cells/zh/python-java/encrypt-and-decrypt-excel-files/)
- [保护和取消保护工作簿结构](/cells/zh/python-java/protect-and-unprotect-workbook-structure/)
- [保护和取消保护工作表](/cells/zh/python-java/protect-and-unprotect-worksheet/)
- [使用 Aspose.Cells 校验修改密码](/cells/zh/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}