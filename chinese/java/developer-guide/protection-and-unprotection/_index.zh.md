---
title: 加密、解密、保护和取消保护 Excel 文件
linktitle: 加密和保护
description: 本节介绍如何使用 Java 代码加密和解密 Excel 文件并保护 Excel 数据，涵盖文件加密、只读保护、工作簿结构保护、工作表保护以及数字签名
keywords: Aspose.Cells, Java, 加密, 解密, 密码, 保护, 取消保护, 工作簿保护, 工作表保护, 只读, 数字签名
type: docs
weight: 68
url: /zh/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 工作簿通常存储敏感的财务、业务或个人信息，这些信息必须防止未经授权的访问。Aspose.Cells for Java 提供了一套全面的保护功能，与 Microsoft Excel 的功能相对应，允许您在文件级别、工作簿级别和工作表级别保护数据。

{{% alert color="primary" %}}
Aspose.Cells for Java 提供从文件级别到数据级别的广泛保护功能，类似于 MS Excel。这些功能包括使用密码加密文件、通过修改密码强制实施只读访问、保护工作簿结构、保护工作表以及对工作簿进行数字签名。
{{% /alert %}}

## 加密和解密 Excel 文件
在 Excel 文件上设置密码可防止未经授权的用户打开或查看工作簿内容。要加密工作簿，请为 `Workbook.Settings.Password`（通过 `workbook.getSettings().setPassword(...)` 访问）分配一个密码字符串，然后保存工作簿。Aspose.Cells 以加密形式写入文件。要打开加密的工作簿进行解密，请实例化一个 `LoadOptions` 对象，将 `LoadOptions.Password`（通过 `loadOptions.setPassword(...)`）设置为加密时使用的相同密码，并将其传递给 `Workbook` 构造函数。Aspose.Cells 会透明地应用所提供的密码，以便您代码的其余部分可以像操作普通工作簿一样与解密后的内容进行交互。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## 只读保护（修改密码）
Excel 支持两种不同的密码层。第一种是打开密码，用于加密文件本身，已在上一节中介绍。第二种是修改密码，它不会阻止用户打开工作簿；相反，除非提供修改密码，否则 Excel 建议以只读模式打开文件。通过 `Workbook.Settings.WriteProtection`（通过 `workbook.getSettings().getWriteProtection()` 访问）在 Aspose.Cells 中配置此行为。将其 `Password` 属性（通过 `writeProtection.setPassword(...)`）设置为修改密码，并将其 `Author` 属性（通过 `writeProtection.setAuthor(...)`）设置为标识应用保护的人员。使用 `WriteProtection.validatePassword(String)` 方法检查所提供的修改密码是否正确，匹配时返回 `true`，否则返回 `false`。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## 保护和取消保护工作簿结构
保护工作簿结构可防止其他用户查看隐藏的工作表、添加新工作表、移动工作表、删除工作表、隐藏工作表或重命名工作表。受保护状态应用于工作表结构，而非任何工作表内的单元格内容。要应用结构保护，请调用 `workbook.protect(ProtectionType.STRUCTURE, "password")`。要移除保护，请调用 `workbook.unprotect("password")` 并提供正确的密码。此处使用 `ProtectionType.STRUCTURE` 枚举值，并且它与其他保护类型（如 `ProtectionType.WINDOWS`）不同。

```java
import com.aspose.cells.*;
// 创建一个新的工作簿
Workbook workbook = new Workbook();
// 添加第二个工作表
workbook.getWorksheets().add();
// 将示例值写入第一个工作表的 A1 单元格
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// 保护工作簿结构
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// 将工作簿保存为 structure_protected.xlsx
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// 将文件重新加载到新的 Workbook 实例中
Workbook loadedWorkbook = new Workbook(filePath);
// 移除结构保护
loadedWorkbook.unprotect("StructPwd");
// 打印确认消息
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## 保护和取消保护工作表
工作表保护可锁定工作表的单元格，防止意外或蓄意的更改。如果不提供密码，用户无法编辑锁定的单元格。这是在共享电子表格中保护公式、标题或指定数据输入区域的典型保护方式。要保护工作表，请调用 `worksheet.protect(ProtectionType.ALL, "password")`。使用 `ProtectionType.ALL` 可启用所有可用的保护选项，例如选择锁定的单元格、格式化单元格、插入行和列以及删除行和列。要移除保护，请使用正确的密码调用 `worksheet.unprotect("password")`。通过使用按位或组合其他保护类型（如 `CONTENTS`、`OBJECTS` 和 `SCENARIOS`），可以实现更细粒度的控制。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## 添加和验证数字签名
数字签名可确保接收方工作簿内容是真实的，并且在签名后未被篡改。Aspose.Cells 通过 `com.aspose.cells.DigitalSignatures` 包提供数字签名支持。典型的工作流程是通过 Java 安全 API（例如 `java.security.KeyStore` 和 `java.security.cert.X509Certificate`）加载 `.pfx` 证书文件，将其包装在 `com.aspose.cells.DigitalSignatures.DigitalSignature` 中，将签名添加到 `DigitalSignatureCollection` 中，然后通过 `workbook.addDigitalSignature(DigitalSignatureCollection)` 将该集合应用到工作簿。`DigitalSignature.getComments()` 属性可以记录签名上下文，例如签名时间和用途。在签名后对工作簿进行的任何修改都会使签名失效，因此接收端的验证步骤可以检测篡改。

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## 相关文章
- [加密和解密 Excel 文件](/cells/zh/java/encrypt-and-decrypt-excel-files/)
- [保护和取消保护工作簿结构](/cells/zh/java/protect-and-unprotect-workbook-structure/)
- [保护和取消保护工作表](/cells/zh/java/protect-and-unprotect-worksheet/)
- [密码保护或取消保护共享工作簿](/cells/zh/java/password-protect-or-unprotect-the-shared-workbook/)
- [分配和验证数字签名](/cells/zh/java/assign-and-validate-digital-signatures/)
- [检测加密的 Office Open XML - OOXML 文件的文件格式](/cells/zh/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [如何检测文件格式并检查文件是否已加密](/cells/zh/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}