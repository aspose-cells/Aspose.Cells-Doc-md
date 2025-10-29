---
title: Проверка пароля для изменений с Aspose.Cells с C++
linktitle: Проверка пароля для изменений
type: docs
weight: 2400
url: /ru/cpp/check-password-to-modify-using-aspose-cells/
description: Проверьте, совпадает ли введенный пароль с паролем для изменений с помощью Aspose.Cells с C++.
---

{{% alert color="primary" %}}

Иногда нужно программно проверить, совпадает ли заданный пароль с **Паролем для изменений**. Aspose.Cells предоставляет метод WorkbookSettings.WriteProtection.ValidatePassword(), который позволяет проверить правильность пароля для изменений.

{{% /alert %}}

## **Проверка пароля на доступ на изменение в Microsoft Excel**

Вы можете указать **Пароль на открытие** и **Пароль на доступ на изменение** при создании ваших книг в Microsoft Excel. Пожалуйста, посмотрите этот скриншот, который показывает интерфейс, предоставляемый Microsoft Excel для указания этих паролей.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Проверьте пароль для изменения с использованием Aspose.Cells**

Следующие образцы кода загружают файл [исходного Excel](5112232.xlsx). В нем есть пароль для открытия - 1234 и пароль для изменения - 5678. Код сначала проверяет, является ли 567 правильным паролем для изменения, и возвращает false, а затем проверяет, является ли 5678 паролем для изменения, и возвращает true.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleBook.xlsx";

    // Specify password to open inside the load options
    LoadOptions opts;
    opts.SetPassword(u"1234");

    // Open the source Excel file with load options
    Workbook workbook(inputFilePath, opts);

    // Check if "567" is the password to modify
    bool ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"567");
    std::wcout << L"Is 567 correct Password to modify: " << ret << std::endl;

    // Check if "5678" is the password to modify
    ret = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"5678");
    std::wcout << L"Is 5678 correct Password to modify: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Вывод в консоль**

Вот консольный вывод вышеуказанного образца кода после загрузки файла [исходного Excel](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
