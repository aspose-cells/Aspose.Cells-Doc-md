---
title: Защита и снятие защиты
linktitle: Шифрование и защита
description: В этом разделе рассказывается, как шифровать и расшифровывать файлы Excel и защищать данные Excel, включая шифрование файлов, защиту только для чтения, защиту структуры рабочей книги, защиту рабочих листов и цифровые подписи с использованием кода JavaScript
keywords: Aspose.Cells, Node.js via Java, шифрование, расшифровка, пароль, защита, снятие защиты, защита рабочей книги, защита рабочего листа, только для чтения, цифровая подпись, JavaScript
type: docs
weight: 68
url: /ru/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Рабочие книги Excel часто содержат конфиденциальную финансовую, деловую или личную информацию, которую необходимо защитить от несанкционированного доступа. Aspose.Cells for Node.js via Java предоставляет комплексный набор функций защиты, который отражает возможности Microsoft Excel, позволяя защищать данные на уровне файла, на уровне рабочей книги и на уровне рабочего листа.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java предлагает широкий спектр функций защиты, от уровня файла до уровня данных, аналогично MS Excel. Эти возможности включают шифрование файлов с помощью пароля, принудительный доступ только для чтения через пароль на изменение, защиту структуры рабочей книги, защиту рабочих листов и цифровую подпись рабочих книг.
{{% /alert %}}

## Шифрование и расшифровка файлов Excel
Пароль, установленный для файла Excel, не позволяет неавторизованным пользователям открывать или просматривать содержимое рабочей книги. Чтобы зашифровать рабочую книгу, присвойте строку пароля методу `workbook.getSettings().setPassword(...)`, а затем сохраните рабочую книгу. Aspose.Cells записывает файл в зашифрованном виде. Чтобы открыть зашифрованную рабочую книгу для расшифровки, создайте экземпляр объекта `LoadOptions`, задайте `loadOptions.setPassword(...)` тот же пароль, который использовался при шифровании, и передайте его в конструктор `Workbook`. Aspose.Cells прозрачно применяет указанный пароль, чтобы остальная часть вашего кода могла взаимодействовать с расшифрованным содержимым, как если бы файл был обычной рабочей книгой.

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

## Защита только для чтения (пароль на изменение)
Excel поддерживает два различных уровня паролей. Первый — это пароль на открытие, который шифрует сам файл и рассматривается в предыдущем разделе. Второй — это пароль на изменение, который не блокирует открытие рабочей книги пользователями; вместо этого Excel рекомендует открывать файл в режиме только для чтения, если не указан пароль на изменение. Настройте это поведение в Aspose.Cells через `workbook.getSettings().getWriteProtection()`. Присвойте свойству `Password` значение пароля на изменение, а свойству `Author` — идентификатор пользователя, применившего защиту. Используйте метод `writeProtection.validatePassword(string)` для проверки правильности указанного пароля на изменение, который возвращает `true` при совпадении и `false` в противном случае.

```javascript
const AsposeCells = require("aspose.cells");
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
Защита структуры рабочей книги не позволяет другим пользователям просматривать скрытые рабочие листы, добавлять новые рабочие листы, перемещать рабочие листы, удалять рабочие листы, скрывать рабочие листы или переименовывать рабочие листы. Защищённое состояние применяется к структуре листов, а не к содержимому ячеек внутри какого-либо листа. Чтобы применить защиту структуры, вызовите `workbook.protect(ProtectionType.Structure, "password")`. Чтобы снять защиту, вызовите `workbook.unprotect("password")` и укажите правильный пароль. Здесь используется значение перечисления `ProtectionType.Structure`, которое отличается от других типов защиты, таких как `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Добавить второй рабочий лист
workbook.getWorksheets().add();
// Записать образец значения в ячейку A1 первого рабочего листа
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Защитить структуру рабочей книги
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// Сохранить рабочую книгу как structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Перезагрузить файл в новый экземпляр Workbook
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Снять защиту структуры
loadedWorkbook.unprotect("StructPwd");
// Вывести сообщение подтверждения
console.log("Structure protection has been successfully removed from the workbook.");
```

## Защита и снятие защиты рабочих листов
Защита рабочего листа блокирует ячейки рабочего листа от случайных или преднамеренных изменений. Пользователи не могут редактировать заблокированные ячейки без указания пароля. Это типичная защита, используемая для охраны формул, заголовков или определённых областей ввода данных в общих электронных таблицах. Чтобы защитить рабочий лист, вызовите `worksheet.protect(ProtectionType.All, "password")`. Использование `ProtectionType.All` включает все доступные параметры защиты, такие как выбор заблокированных ячеек, форматирование ячеек, вставка строк и столбцов, а также удаление строк и столбцов. Чтобы снять защиту, вызовите `worksheet.unprotect("password")` с правильным паролем. Более точный контроль доступен путём комбинирования других типов защиты, таких как `Contents`, `Objects` и `Scenarios`, с помощью побитового ИЛИ.

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

## Добавление и проверка цифровых подписей
Цифровая подпись гарантирует получателям, что содержимое рабочей книги подлинно и не было изменено с момента её подписания. Aspose.Cells поддерживает цифровые подписи через классы `AsposeCells.DigitalSignature` и `AsposeCells.DigitalSignatureCollection`. Типичный рабочий процесс: создать `AsposeCells.DigitalSignature` непосредственно из PFX-файла сертификата вместе с паролем и комментариями подписи, добавить подпись в `DigitalSignatureCollection` и применить коллекцию к рабочей книге через `workbook.addDigitalSignature(DigitalSignatureCollection)`. Свойство `DigitalSignature.Comments` может записывать контекст подписания, такой как время и цель подписания. Любое изменение, внесённое в рабочую книгу после подписания, делает подпись недействительной, поэтому этап проверки на принимающей стороне может обнаружить подделку.

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