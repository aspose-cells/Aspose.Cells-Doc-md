---
title: Защита и снятие защиты
linktitle: Шифрование и защита
type: docs
weight: 68
url: /ru/net/protect-and-unprotect/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/net/security-features/]
description: В этом разделе описано, как шифровать и расшифровывать файлы Excel, а также защищать данные Excel, включая шифрование файлов, защиту только для чтения, защиту структуры рабочей книги, защиту рабочих листов и цифровые подписи с использованием кода C#
keywords: Aspose.Cells, .NET, шифрование, расшифровка, пароль, защита, снятие защиты, защита рабочей книги, защита рабочего листа, только для чтения, цифровая подпись, C#
---

Рабочие книги Excel часто содержат конфиденциальную финансовую, коммерческую или личную информацию, которую необходимо защитить от несанкционированного доступа. Aspose.Cells for .NET предоставляет полный набор функций защиты, аналогичный возможностям Microsoft Excel, позволяющий защищать данные на уровне файла, на уровне рабочей книги и на уровне рабочего листа.

{{% alert color="primary" %}}
Aspose.Cells for .NET предлагает широкий спектр функций защиты — от уровня файла до уровня данных, аналогично MS Excel. Эти возможности включают шифрование файлов паролем, ограничение доступа только для чтения с помощью пароля на изменение, защиту структуры рабочей книги, защиту рабочих листов и цифровую подпись рабочих книг.
{{% /alert %}}

## Шифрование и расшифровка файлов Excel
Пароль, установленный для файла Excel, запрещает неавторизованным пользователям открывать или просматривать содержимое рабочей книги. Чтобы зашифровать рабочую книгу, присвойте строку пароля свойству `Workbook.Settings.Password`, а затем сохраните рабочую книгу. Aspose.Cells сохраняет файл в зашифрованном виде. Чтобы открыть зашифрованную рабочую книгу для расшифровки, создайте экземпляр объекта `LoadOptions`, установите `LoadOptions.Password` равным тому же паролю, который использовался при шифровании, и передайте его в конструктор `Workbook`. Aspose.Cells прозрачно применяет переданный пароль, поэтому остальная часть вашего кода может взаимодействовать с расшифрованным содержимым так, как если бы файл был обычной рабочей книгой.

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

## Защита только для чтения (пароль на изменение)
Excel поддерживает два разных уровня паролей. Первый — пароль на открытие, который шифрует сам файл и рассматривается в предыдущем разделе. Второй — пароль на изменение, который не запрещает пользователям открывать рабочую книгу; вместо этого Excel рекомендует открывать файл в режиме только для чтения, если не указан пароль на изменение. Настройте это поведение в Aspose.Cells с помощью свойства `Workbook.Settings.WriteProtection`. Задайте его свойству `Password` пароль на изменение, а свойству `Author` — идентификатор пользователя, применившего защиту. Используйте метод `WriteProtection.ValidatePassword(string)` для проверки правильности переданного пароля на изменение: метод возвращает `true` при совпадении и `false` в противном случае.

```csharp
using System;
using Aspose.Cells;
// Создать новую книгу с нуля
Workbook workbook = new Workbook();
// Записать пример значения в ячейку A1 первого листа
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// Настроить защиту от записи: установить пароль на изменение и автора
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// Сохранить книгу, чтобы сохранить настройки защиты от записи
workbook.Save("WriteProtectedWorkbook.xlsx");
// Проверить правильность пароля на изменение, используя правильный пароль
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Проверить правильность пароля на изменение, используя неверный пароль, чтобы показать другую ветвь
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Защита и снятие защиты структуры рабочей книги
Защита структуры рабочей книги запрещает другим пользователям просматривать скрытые рабочие листы, добавлять новые рабочие листы, перемещать рабочие листы, удалять рабочие листы, скрывать рабочие листы или переименовывать рабочие листы. Защищённое состояние применяется к структуре листов, а не к содержимому ячеек внутри какого-либо листа. Чтобы применить защиту структуры, вызовите `workbook.Protect(ProtectionType.Structure, "password")`. Чтобы снять защиту, вызовите `workbook.Unprotect("password")` и передайте правильный пароль. Здесь используется значение перечисления `ProtectionType.Structure`, которое отличается от других типов защиты, таких как `ProtectionType.Windows`.

```csharp
using System;
using Aspose.Cells;
// Создать новую рабочую книгу
Workbook workbook = new Workbook();
// Добавить второй рабочий лист
workbook.Worksheets.Add();
// Записать образец значения в ячейку A1 первого рабочего листа
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// Защитить структуру рабочей книги
workbook.Protect(ProtectionType.Structure, "StructPwd");
// Сохранить рабочую книгу как structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// Перезагрузить файл в новый экземпляр Workbook
Workbook loadedWorkbook = new Workbook(filePath);
// Снять защиту структуры
loadedWorkbook.Unprotect("StructPwd");
// Вывести сообщение подтверждения
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## Защита и снятие защиты рабочих листов
Защита рабочего листа блокирует ячейки рабочего листа от случайных или преднамеренных изменений. Пользователи не могут редактировать заблокированные ячейки без ввода пароля. Это типичная защита, используемая для охраны формул, заголовков или определённых областей ввода данных в общих электронных таблицах. Чтобы защитить рабочий лист, вызовите `worksheet.Protect(ProtectionType.All, "password")`. Использование `ProtectionType.All` включает все доступные параметры защиты, такие как выделение заблокированных ячеек, форматирование ячеек, вставка строк и столбцов, а также удаление строк и столбцов. Чтобы снять защиту, вызовите `worksheet.Unprotect("password")` с правильным паролем. Доступен более тонкий контроль путём комбинирования других типов защиты, таких как `Contents`, `Objects` и `Scenarios`, с помощью побитового ИЛИ.

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

## Добавление и проверка цифровых подписей
Цифровая подпись гарантирует получателям, что содержимое рабочей книги является подлинным и не было изменено с момента подписания. Aspose.Cells обеспечивает поддержку цифровых подписей через пространство имён `Aspose.Cells.DigitalSignatures`. Типичный рабочий процесс включает загрузку файла сертификата `.pfx` через `System.Security.Cryptography.X509Certificates.X509Certificate2`, его обёртывание в `Aspose.Cells.DigitalSignatures.DigitalSignature`, добавление подписи в коллекцию `DigitalSignatureCollection` и применение коллекции к рабочей книге через `Workbook.AddDigitalSignature(DigitalSignatureCollection)`. Свойство `DigitalSignature.Comments` может фиксировать контекст подписания, например время и цель подписания. Любое изменение, внесённое в рабочую книгу после подписания, делает подпись недействительной, поэтому этап проверки на стороне получателя позволяет обнаружить подделку.

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

## Связанные статьи
- [Шифрование и расшифровка файлов Excel](/cells/ru/net/encrypt-and-decrypt-excel-files/)
- [Защита и снятие защиты структуры рабочей книги](/cells/ru/net/protect-and-unprotect-workbook-structure/)
- [Защита и снятие защиты рабочего листа](/cells/ru/net/protect-and-unprotect-worksheets/)
- [Защита паролем или снятие защиты общей рабочей книги](/cells/ru/net/password-protect-or-unprotect-the-shared-workbook/)
- [Назначение и проверка цифровых подписей](/cells/ru/net/assign-and-validate-digital-signatures/)
- [Проверка пароля на изменение с помощью Aspose.Cells](/cells/ru/net/check-password-to-modify-using-aspose-cells/)
- [Определение формата зашифрованных файлов Office Open XML — OOXML](/cells/ru/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Шифрование файлов Excel](/cells/ru/net/encrypting-excel-files/)
- [Как определить формат файла и проверить, зашифрован ли файл](/cells/ru/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}