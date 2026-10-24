---
title: Шифрование, дешифрование, защита и снятие защиты для файлов Excel
linktitle: Шифрование и защита
description: В этом разделе описано, как шифровать и расшифровывать файлы Excel, а также защищать данные Excel с использованием кода Java, включая шифрование файлов, защиту от записи, защиту структуры рабочей книги, защиту рабочих листов и цифровые подписи
keywords: Aspose.Cells, Java, шифрование, расшифровка, пароль, защита, снятие защиты, защита рабочей книги, защита рабочего листа, только для чтения, цифровая подпись
type: docs
weight: 68
url: /ru/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Книги Excel часто содержат конфиденциальную финансовую, коммерческую или личную информацию, которую необходимо защитить от несанкционированного доступа. Aspose.Cells for Java предоставляет полный набор функций защиты, которые соответствуют возможностям Microsoft Excel и позволяют защищать данные на уровне файла, рабочей книги и рабочего листа.

{{% alert color="primary" %}}
Aspose.Cells for Java предлагает широкий спектр функций защиты — от уровня файла до уровня данных, аналогично MS Excel. Эти возможности включают шифрование файлов с помощью пароля, принудительное ограничение доступа на запись с помощью пароля, защиту структуры рабочей книги, защиту рабочих листов и применение цифровых подписей к рабочим книгам.
{{% /alert %}}

## Шифрование и расшифровка файлов Excel
Пароль, установленный для файла Excel, не позволяет неавторизованным пользователям открывать или просматривать содержимое рабочей книги. Чтобы зашифровать рабочую книгу, присвойте строку пароля свойству `Workbook.Settings.Password` (доступ через `workbook.getSettings().setPassword(...)`) и затем сохраните рабочую книгу. Aspose.Cells записывает файл в зашифрованном виде. Чтобы открыть зашифрованную рабочую книгу для расшифровки, создайте экземпляр объекта `LoadOptions`, задайте свойству `LoadOptions.Password` (через `loadOptions.setPassword(...)`) тот же пароль, который использовался при шифровании, и передайте его в конструктор `Workbook`. Aspose.Cells применяет переданный пароль прозрачно, поэтому остальная часть вашего кода может работать с расшифрованным содержимым так, как если бы файл был обычной рабочей книгой.

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

## Защита только для чтения (пароль на изменение)
Excel поддерживает два различных уровня парольной защиты. Первый — это пароль на открытие, который шифрует сам файл и рассмотрен в предыдущем разделе. Второй — это пароль на изменение, который не блокирует открытие рабочей книги пользователями; вместо этого Excel рекомендует открыть файл в режиме только для чтения, если не указан пароль на изменение. Настройте это поведение в Aspose.Cells с помощью `Workbook.Settings.WriteProtection` (доступ через `workbook.getSettings().getWriteProtection()`). Задайте его свойству `Password` (через `writeProtection.setPassword(...)`) пароль на изменение, а его свойству `Author` (через `writeProtection.setAuthor(...)`) — имя автора защиты. Используйте метод `WriteProtection.validatePassword(String)` для проверки правильности переданного пароля на изменение: он возвращает `true` при совпадении и `false` в противном случае.

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

## Защита и снятие защиты структуры рабочей книги
Защита структуры рабочей книги не позволяет другим пользователям просматривать скрытые рабочие листы, добавлять новые рабочие листы, перемещать, удалять, скрывать или переименовывать рабочие листы. Защищённое состояние применяется к структуре листов, а не к содержимому ячеек внутри листов. Чтобы применить защиту структуры, вызовите `workbook.protect(ProtectionType.STRUCTURE, "password")`. Чтобы снять защиту, вызовите `workbook.unprotect("password")` и передайте правильный пароль. Здесь используется значение перечисления `ProtectionType.STRUCTURE`, которое отличается от других типов защиты, таких как `ProtectionType.WINDOWS`.

```java
import com.aspose.cells.*;
// Создать новую рабочую книгу
Workbook workbook = new Workbook();
// Добавить второй рабочий лист
workbook.getWorksheets().add();
// Записать образец значения в ячейку A1 первого рабочего листа
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Защитить структуру рабочей книги
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// Сохранить рабочую книгу как structure_protected.xlsx
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Перезагрузить файл в новый экземпляр Workbook
Workbook loadedWorkbook = new Workbook(filePath);
// Снять защиту структуры
loadedWorkbook.unprotect("StructPwd");
// Вывести сообщение подтверждения
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## Защита и снятие защиты рабочих листов
Защита рабочего листа блокирует ячейки рабочего листа от случайных или намеренных изменений. Пользователи не могут редактировать заблокированные ячейки без указания пароля. Это типичная защита, используемая для охраны формул, заголовков или выделенных областей ввода данных в общих электронных таблицах. Чтобы защитить рабочий лист, вызовите `worksheet.protect(ProtectionType.ALL, "password")`. Использование `ProtectionType.ALL` включает все доступные параметры защиты, такие как выбор заблокированных ячеек, форматирование ячеек, вставка строк и столбцов, а также удаление строк и столбцов. Чтобы снять защиту, вызовите `worksheet.unprotect("password")` с правильным паролем. Более тонкая настройка доступна путём комбинирования других типов защиты, таких как `CONTENTS`, `OBJECTS` и `SCENARIOS`, с помощью побитового ИЛИ.

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

## Добавление и проверка цифровых подписей
Цифровая подпись гарантирует получателям, что содержимое рабочей книги является подлинным и не было изменено с момента подписания. Aspose.Cells обеспечивает поддержку цифровых подписей через пакет `com.aspose.cells.DigitalSignatures`. Типичный рабочий процесс загружает файл сертификата `.pfx` через API-интерфейсы безопасности Java (такие как `java.security.KeyStore` и `java.security.cert.X509Certificate`), оборачивает его в `com.aspose.cells.DigitalSignatures.DigitalSignature`, добавляет подпись в коллекцию `DigitalSignatureCollection` и применяет коллекцию к рабочей книге через `workbook.addDigitalSignature(DigitalSignatureCollection)`. Свойство `DigitalSignature.getComments()` может записать контекст подписания, например, время и цель подписания. Любое изменение, внесённое в рабочую книгу после подписания, делает подпись недействительной, поэтому этап проверки на стороне получателя позволяет выявить вмешательство.

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

## Связанные статьи
- [Шифрование и расшифровка файлов Excel](/cells/ru/java/encrypt-and-decrypt-excel-files/)
- [Защита и снятие защиты структуры рабочей книги](/cells/ru/java/protect-and-unprotect-workbook-structure/)
- [Защита и снятие защиты рабочего листа](/cells/ru/java/protect-and-unprotect-worksheet/)
- [Защита паролем или снятие защиты общей рабочей книги](/cells/ru/java/password-protect-or-unprotect-the-shared-workbook/)
- [Назначение и проверка цифровых подписей](/cells/ru/java/assign-and-validate-digital-signatures/)
- [Определение формата зашифрованных файлов Office Open XML — OOXML](/cells/ru/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Как определить формат файла и проверить, зашифрован ли файл](/cells/ru/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}