---
title: 用C++保护和取消保护
linktitle: 加密和保护
description: 本节介绍如何加密和解密 Excel 文件以及保护 Excel 数据，涵盖文件加密、只读保护、工作簿结构保护、工作表保护以及使用 C++ 代码进行数字签名
keywords: Aspose.Cells, Aspose.Cells for C++, 加密, 解密, 密码, 保护, 取消保护, 工作簿保护, 工作表保护, 只读, 数字签名, C++
type: docs
weight: 68
url: /zh/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel 工作簿经常存储敏感的财务、业务或个人信息，必须防止未经授权的访问。Aspose.Cells for C++ 提供了一套全面的保护功能，与 Microsoft Excel 的功能相对应，允许您在文件级别、工作簿级别和工作表级别保护数据。

{{% alert color="primary" %}}
Aspose.Cells for C++ 提供从文件级别到数据级别的广泛保护功能，类似于 MS Excel。这些功能包括使用密码加密文件、通过修改密码强制只读访问、保护工作簿结构、保护工作表以及为工作簿添加数字签名。
{{% /alert %}}

## 加密和解密 Excel 文件
在 Excel 文件上设置密码可以防止未经授权的用户打开或查看工作簿内容。要加密工作簿，请将密码字符串赋值给 `workbook.GetSettings().SetPassword()`，然后保存工作簿。Aspose.Cells 会以加密形式写入文件。要打开已加密的工作簿进行解密，请实例化一个 `LoadOptions` 对象，将 `LoadOptions.SetPassword()` 设置为加密时使用的相同密码，并将其传递给 `Workbook` 构造函数。Aspose.Cells 以透明方式应用所提供的密码，使代码的其余部分可以像普通工作簿一样与解密后的内容交互。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 只读保护（修改密码）
Excel 支持两种不同的密码层。第一种是打开密码，它对文件本身进行加密，已在上一节中介绍。第二种是修改密码，它不会阻止用户打开工作簿；相反，除非提供修改密码，否则 Excel 建议以只读模式打开文件。在 Aspose.Cells 中，可通过 `workbook.GetSettings().GetWriteProtection()` 配置此行为。将其 `Password` 属性设置为修改密码，将其 `Author` 属性设置为应用保护者的标识。使用 `WriteProtection.ValidatePassword()` 方法检查所提供的修改密码是否正确，匹配时返回 `true`，否则返回 `false`。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 保护和取消保护工作簿结构
保护工作簿结构可以防止其他用户查看隐藏的工作表、添加新工作表、移动工作表、删除工作表、隐藏工作表或重命名工作表。受保护状态应用于工作表结构，而不是任何工作表内的单元格内容。要应用结构保护，请调用 `workbook.Protect(ProtectionType::Structure, "password")`。要移除保护，请调用 `workbook.Unprotect("password")` 并提供正确的密码。此处使用 `ProtectionType::Structure` 枚举值，该值不同于其他保护类型（例如 `ProtectionType::Windows`）。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 创建一个新工作簿
    Workbook workbook;
    // 添加第二个工作表
    workbook.GetWorksheets().Add();
    // 向第一个工作表的 A1 单元格写入一个示例值
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // 保护工作簿结构
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // 将工作簿另存为 structure_protected.xlsx
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // 将文件重新加载到新的 Workbook 实例中
    Workbook loadedWorkbook(filePath);
    // 移除结构保护
    loadedWorkbook.Unprotect(u"StructPwd");
    // 打印确认消息
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 保护和取消保护工作表
工作表保护可以锁定工作表的单元格，防止意外或故意的更改。用户在没有提供密码的情况下无法编辑被锁定的单元格。这是在共享电子表格中保护公式、标题或指定数据输入区域的典型保护方式。要保护工作表，请调用 `worksheet.Protect(ProtectionType::All, "password")`。使用 `ProtectionType::All` 可启用所有可用的保护选项，例如选择锁定的单元格、格式化单元格、插入行和列以及删除行和列。要移除保护，请使用正确的密码调用 `worksheet.Unprotect("password")`。还可以通过按位 OR 组合其他保护类型（如 `Contents`、`Objects` 和 `Scenarios`）实现更细粒度的控制。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 添加和验证数字签名
数字签名向收件人保证工作簿内容是真实的，并且在签名后未被篡改。Aspose.Cells 通过 `Aspose::Cells::DigitalSignatures` 命名空间提供数字签名支持。典型的工作流程是加载 `.pfx` 证书文件，将其包装到 `Aspose::Cells::DigitalSignatures::DigitalSignature` 中，将签名添加到 `DigitalSignatureCollection`，然后通过 `workbook.AddDigitalSignature(DigitalSignatureCollection)` 将该集合应用到工作簿。`DigitalSignature.GetComments()` 属性可以记录签名上下文，例如签名时间和用途。签名后对工作簿所做的任何修改都会使签名失效，因此接收方可以通过验证步骤检测篡改。

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 相关文章
- [加密和解密 Excel 文件](/cells/zh/cpp/encrypt-and-decrypt-excel-files/)
- [保护和取消保护工作簿结构](/cells/zh/cpp/protect-and-unprotect-workbook-structure/)
- [保护和取消保护工作表](/cells/zh/cpp/protect-and-unprotect-worksheets/)
- [密码保护或取消保护共享工作簿](/cells/zh/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [使用 Aspose.Cells 检查修改密码](/cells/zh/cpp/check-password-to-modify-using-aspose-cells/)
- [检测加密 Office Open XML - OOXML 文件的文件格式](/cells/zh/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [加密 Excel 文件](/cells/zh/cpp/encrypting-excel-files/)
- [如何检测文件格式并检查文件是否已加密](/cells/zh/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}