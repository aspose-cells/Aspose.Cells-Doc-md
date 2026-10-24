---
title: Защита и снятие защиты с помощью C++
linktitle: Шифрование и защита
description: Этот раздел описывает, как шифровать и расшифровывать файлы Excel, а также защищать данные Excel, охватывая шифрование файлов, защиту только для чтения, защиту структуры книги, защиту рабочего листа и цифровые подписи с использованием кода C++
keywords: Aspose.Cells, Aspose.Cells for C++, шифрование, расшифровка, пароль, защита, снятие защиты, защита рабочей книги, защита рабочего листа, только для чтения, цифровая подпись, C++
type: docs
weight: 68
url: /ru/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Книги Excel часто хранят конфиденциальную финансовую, деловую или личную информацию, которую необходимо защитить от несанкционированного доступа. Aspose.Cells for C++ предоставляет полный набор функций защиты, которые отражают возможности Microsoft Excel, позволяя защитить ваши данные на уровне файла, на уровне книги и на уровне рабочего листа.

{{% alert color="primary" %}}
Aspose.Cells for C++ предлагает широкий спектр функций защиты, от уровня файла до уровня данных, аналогично MS Excel. Эти возможности включают шифрование файлов с помощью пароля, принудительное применение доступа только для чтения через пароль на изменение, защиту структуры книги, защиту рабочих листов и цифровую подпись книг.
{{% /alert %}}

## Шифрование и расшифровка файлов Excel
Пароль, установленный для файла Excel, запрещает неавторизованным пользователям открывать или просматривать содержимое рабочей книги. Чтобы зашифровать рабочую книгу, присвойте строку пароля свойству `workbook.GetSettings().SetPassword()` и затем сохраните рабочую книгу. Aspose.Cells записывает файл в зашифрованном виде. Чтобы открыть зашифрованную рабочую книгу для расшифровки, создайте экземпляр объекта `LoadOptions`, установите `LoadOptions.SetPassword()` в тот же пароль, который использовался при шифровании, и передайте его в конструктор `Workbook`. Aspose.Cells применяет предоставленный пароль прозрачно, так что остальная часть вашего кода может взаимодействовать с расшифрованным содержимым так, как если бы файл был обычной рабочей книгой.

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

## Защита только для чтения (пароль на изменение)
Excel поддерживает два различных уровня паролей. Первый — это пароль для открытия, который шифрует сам файл и рассматривается в предыдущем разделе. Второй — это пароль на изменение, который не блокирует пользователям открытие книги; вместо этого Excel рекомендует открывать файл в режиме только для чтения, если не указан пароль на изменение. Настройте это поведение в Aspose.Cells через `workbook.GetSettings().GetWriteProtection()`. Установите свойство `Password` равным паролю на изменение, а свойство `Author` — чтобы указать, кто применил защиту. Используйте метод `WriteProtection.ValidatePassword()` для проверки правильности предоставленного пароля на изменение, который возвращает `true` при совпадении и `false` в противном случае.

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

## Защита и снятие защиты структуры книги
Защита структуры книги запрещает другим пользователям просматривать скрытые рабочие листы, добавлять новые рабочие листы, перемещать рабочие листы, удалять рабочие листы, скрывать рабочие листы или переименовывать рабочие листы. Состояние защиты применяется к структуре листа, а не к содержимому ячеек внутри какого-либо листа. Чтобы применить защиту структуры, вызовите `workbook.Protect(ProtectionType::Structure, "password")`. Чтобы снять защиту, вызовите `workbook.Unprotect("password")` и укажите правильный пароль. Значение перечисления `ProtectionType::Structure` используется здесь и отличается от других типов защиты, таких как `ProtectionType::Windows`.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Создать новую рабочую книгу
    Workbook workbook;
    // Добавить второй рабочий лист
    workbook.GetWorksheets().Add();
    // Записать образец значения в ячейку A1 первого рабочего листа
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // Защитить структуру рабочей книги
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // Сохранить рабочую книгу как structure_protected.xlsx
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // Перезагрузить файл в новый экземпляр Workbook
    Workbook loadedWorkbook(filePath);
    // Снять защиту структуры
    loadedWorkbook.Unprotect(u"StructPwd");
    // Вывести подтверждающее сообщение
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Защита и снятие защиты рабочих листов
Защита рабочего листа блокирует ячейки рабочего листа от случайных или намеренных изменений. Пользователи не могут редактировать заблокированные ячейки без указания пароля. Это типичная защита, используемая для защиты формул, заголовков или определённых областей ввода данных в общих таблицах. Чтобы защитить рабочий лист, вызовите `worksheet.Protect(ProtectionType::All, "password")`. Использование `ProtectionType::All` включает все доступные параметры защиты, такие как выбор заблокированных ячеек, форматирование ячеек, вставка строк и столбцов, а также удаление строк и столбцов. Чтобы снять защиту, вызовите `worksheet.Unprotect("password")` с правильным паролем. Более точное управление доступно путём комбинирования других типов защиты, таких как `Contents`, `Objects` и `Scenarios`, с использованием побитового ИЛИ.

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

## Добавление и проверка цифровых подписей
Цифровая подпись подтверждает получателям, что содержимое книги подлинно и не было изменено с момента подписания. Aspose.Cells обеспечивает поддержку цифровых подписей через пространство имён `Aspose::Cells::DigitalSignatures`. Типичный рабочий процесс загружает файл сертификата `.pfx`, оборачивает его в `Aspose::Cells::DigitalSignatures::DigitalSignature`, добавляет подпись в коллекцию `DigitalSignatureCollection` и применяет коллекцию к рабочей книге через `workbook.AddDigitalSignature(DigitalSignatureCollection)`. Свойство `DigitalSignature.GetComments()` может записать контекст подписания, такой как время и цель подписания. Любое изменение, внесённое в книгу после подписания, делает подпись недействительной, поэтому шаг проверки на принимающей стороне может обнаружить подделку.

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

## Связанные статьи
- [Шифрование и расшифровка файлов Excel](/cells/ru/cpp/encrypt-and-decrypt-excel-files/)
- [Защита и снятие защиты структуры книги](/cells/ru/cpp/protect-and-unprotect-workbook-structure/)
- [Защита и снятие защиты рабочего листа](/cells/ru/cpp/protect-and-unprotect-worksheets/)
- [Защита паролем или снятие защиты общей книги](/cells/ru/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Проверка пароля на изменение с помощью Aspose.Cells](/cells/ru/cpp/check-password-to-modify-using-aspose-cells/)
- [Определение формата зашифрованных файлов Office Open XML — OOXML](/cells/ru/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Шифрование файлов Excel](/cells/ru/cpp/encrypting-excel-files/)
- [Как определить формат файла и проверить, зашифрован ли файл](/cells/ru/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}