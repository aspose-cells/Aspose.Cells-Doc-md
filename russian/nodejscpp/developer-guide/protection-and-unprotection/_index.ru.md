---
title: Защита и снятие защиты с помощью Node.js через C++
linktitle: Шифрование и защита
description: В этом разделе представлены способы шифрования и расшифровки файлов Excel и защиты данных Excel, включая шифрование файлов, защиту только для чтения, защиту структуры рабочей книги, защиту рабочих листов и цифровые подписи с использованием кода JavaScript
keywords: Aspose.Cells, Node.js, C++, шифрование, расшифровка, пароль, защита, снятие защиты, защита рабочей книги, защита рабочего листа, только для чтения, цифровая подпись, JavaScript
type: docs
weight: 68
url: /ru/nodejs-cpp/protect-and-unprotect/
alias: [/nodejs-cpp/security-features/]
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Рабочие книги Excel часто содержат конфиденциальную финансовую, деловую или личную информацию, которую необходимо защищать от несанкционированного доступа. Aspose.Cells for Node.js via C++ предоставляет комплексный набор средств защиты, соответствующих возможностям Microsoft Excel, и позволяет защищать данные на уровне файла, рабочей книги и рабочего листа.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ предлагает широкий набор средств защиты, охватывающий уровень от файлов до данных и сходный с возможностями MS Excel. Эти возможности включают шифрование файлов паролем, принудительный доступ только для чтения с помощью пароля на изменение, защиту структуры рабочей книги, защиту рабочих листов и подписание рабочих книг с помощью цифровых подписей.
{{% /alert %}}

## Шифрование и расшифровка файлов Excel
Пароль, установленный для файла Excel, не позволяет неавторизованным пользователям открыть рабочую книгу или просмотреть ее содержимое. Чтобы зашифровать рабочую книгу, задайте пароль с помощью метода `workbook.getSettings().setPassword()`, а затем сохраните рабочую книгу. Aspose.Cells записывает файл в зашифрованном виде. Чтобы открыть зашифрованную рабочую книгу и расшифровать ее, создайте экземпляр объекта `LoadOptions`, задайте с помощью `loadOptions.setPassword()` тот же пароль, который использовался при шифровании, и передайте объект `LoadOptions` в конструктор `Workbook`. Aspose.Cells прозрачно применяет переданный пароль, поэтому остальная часть кода может взаимодействовать с расшифрованным содержимым так же, как если бы файл был обычной рабочей книгой.

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

## Защита только для чтения (пароль на изменение)
Excel поддерживает два разных уровня парольной защиты. Первый — пароль для открытия, который шифрует сам файл и описан в предыдущем разделе. Второй — пароль на изменение, который не запрещает пользователям открывать рабочую книгу, но при его отсутствии Excel рекомендует открывать файл в режиме только для чтения. Настройте это поведение в Aspose.Cells с помощью `workbook.getSettings().getWriteProtection()`. Установите для свойства `password` пароль на изменение, а в свойстве `author` укажите пользователя, применившего защиту. Используйте метод `writeProtection.validatePassword(string)` для проверки правильности указанного пароля на изменение: он возвращает `true` при совпадении и `false` в противном случае.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Записать образец значения в ячейку A1 первого листа
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Настроить защиту от записи: установить пароль на изменение и автора
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Сохранить книгу, чтобы защита от записи была сохранена
workbook.save("WriteProtectedWorkbook.xlsx");
// Проверить пароль на изменение, используя правильный пароль
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Проверить пароль на изменение, используя неправильный пароль, чтобы продемонстрировать другую ветвь
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Защита и снятие защиты структуры рабочей книги
Защита структуры рабочей книги не позволяет другим пользователям просматривать скрытые рабочие листы, добавлять новые рабочие листы, перемещать, удалять, скрывать или переименовывать рабочие листы. Эта защита относится к структуре листов, а не к содержимому ячеек в них. Чтобы применить защиту структуры, вызовите `workbook.protect(ProtectionType.Structure, "password")`. Чтобы снять защиту, вызовите `workbook.unprotect("password")` с указанием правильного пароля. Здесь используется значение перечисления `ProtectionType.Structure`, отличающееся от других типов защиты, таких как `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Добавить второй рабочий лист
workbook.getWorksheets().add();
// Записать образец значения в ячейку A1 первого рабочего листа
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Защитить структуру рабочей книги
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// Сохранить рабочую книгу как structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Перезагрузить файл в новый экземпляр Workbook
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Удалить защиту структуры
loadedWorkbook.unprotect("StructPwd");
// Вывести сообщение подтверждения
console.log("Structure protection has been successfully removed from the workbook.");
```

## Защита и снятие защиты рабочих листов
Защита рабочего листа блокирует случайные или намеренные изменения ячеек. Пользователи не могут редактировать защищённые ячейки без ввода пароля. Это типичный способ защиты формул, заголовков или выделенных областей ввода данных в совместно используемых электронных таблицах. Чтобы защитить рабочий лист, вызовите `worksheet.protect(ProtectionType.All, "password")`. Использование `ProtectionType.All` включает все доступные параметры защиты, например возможность выбора защищённых ячеек, форматирования ячеек, вставки и удаления строк и столбцов. Чтобы снять защиту, вызовите `worksheet.unprotect("password")`, передав правильный пароль. Более гибкое управление доступно при комбинировании других типов защиты, таких как `Contents`, `Objects` и `Scenarios`, с помощью побитового оператора ИЛИ.

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

## Добавление и проверка цифровых подписей
Цифровая подпись гарантирует получателям, что содержимое рабочей книги является подлинным и не было изменено после подписания. Aspose.Cells обеспечивает поддержку цифровых подписей с помощью пространства имён `Aspose.Cells.DigitalSignatures`. Типичный рабочий процесс предусматривает загрузку файла сертификата `.pfx` с помощью средств Node.js crypto, создание экземпляра `Aspose.Cells.DigitalSignatures.DigitalSignature`, добавление подписи в коллекцию `DigitalSignatureCollection` и применение коллекции к рабочей книге с помощью `workbook.addDigitalSignature(digitalSignatureCollection)`. Свойство `digitalSignature.comments` позволяет зафиксировать контекст подписания, например время и цель подписания. Любое изменение, внесённое в рабочую книгу после подписания, делает подпись недействительной, поэтому проверка на стороне получателя позволяет выявить факт подмены.

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

## Связанные статьи
- [Шифрование и расшифровка файлов Excel](/cells/ru/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [Защита и снятие защиты структуры рабочей книги](/cells/ru/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [Защита и снятие защиты рабочего листа](/cells/ru/nodejs-cpp/protect-and-unprotect-worksheets/)
- [Защита паролем или снятие защиты общей рабочей книги](/cells/ru/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Добавление и проверка цифровых подписей](/cells/ru/nodejs-cpp/assign-and-validate-digital-signatures/)
- [Проверка пароля на изменение с помощью Aspose.Cells](/cells/ru/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [Определение формата зашифрованных файлов Office Open XML — OOXML](/cells/ru/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Шифрование файлов Excel](/cells/ru/nodejs-cpp/encrypting-excel-files/)
- [Как определить формат файла и проверить, зашифрован ли файл](/cells/ru/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}