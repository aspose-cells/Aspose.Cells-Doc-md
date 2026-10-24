---
title: Защита и снятие защиты
linktitle: Шифрование и защита
description: В этом разделе описано, как шифровать и расшифровывать файлы Excel, а также защищать данные Excel, включая шифрование файлов, защиту только для чтения, защиту структуры книги, защиту рабочих листов и цифровые подписи с использованием кода Python
keywords: Aspose.Cells, Python via .NET, шифрование, расшифровка, пароль, защита, снятие защиты, защита рабочей книги, защита рабочего листа, только для чтения, цифровая подпись, Python
type: docs
weight: 68
url: /ru/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Книги Excel часто содержат конфиденциальную финансовую, деловую или личную информацию, которую необходимо защитить от несанкционированного доступа. Aspose.Cells for Python via .NET предоставляет полный набор функций защиты, которые соответствуют возможностям Microsoft Excel, позволяя защищать данные на уровне файла, книги и рабочего листа.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET предлагает широкий спектр функций защиты, от уровня файла до уровня данных, аналогично MS Excel. Эти возможности включают шифрование файлов паролем, обеспечение доступа только для чтения с помощью пароля на изменение, защиту структуры книги, защиту рабочих листов и цифровую подпись книг.
{{% /alert %}}

## Шифрование и расшифровка файлов Excel
Пароль, установленный для файла Excel, не позволяет неавторизованным пользователям открывать или просматривать содержимое книги. Чтобы зашифровать книгу, присвойте строку пароля свойству `workbook.settings.password`, а затем сохраните книгу. Aspose.Cells записывает файл в зашифрованном виде. Чтобы открыть зашифрованную книгу для расшифровки, создайте объект `LoadOptions`, установите `load_options.password` равным тому же паролю, который использовался при шифровании, и передайте его в конструктор `Workbook`. Aspose.Cells прозрачно применяет указанный пароль, так что остальная часть вашего кода может работать с расшифрованным содержимым, как если бы файл был обычной книгой.

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

## Защита только для чтения (пароль на изменение)
Excel поддерживает два различных уровня парольной защиты. Первый — это пароль для открытия, который шифрует сам файл и рассматривается в предыдущем разделе. Второй — это пароль на изменение, который не блокирует открытие книги пользователями; вместо этого Excel рекомендует открывать файл в режиме только для чтения, если не указан пароль на изменение. Настройте это поведение в Aspose.Cells через `workbook.settings.write_protection`. Задайте в свойстве `password` пароль на изменение, а в свойстве `author` — идентификатор пользователя, применившего защиту. Используйте метод `write_protection.validate_password(string)` для проверки правильности предоставленного пароля на изменение, который возвращает `true` при совпадении и `false` в противном случае.

```python
import aspose.cells as ac
# Создаём новую рабочую книгу с нуля
workbook = ac.Workbook()
# Записываем пример значения в ячейку A1 первого рабочего листа
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# Настраиваем защиту от записи: задаём пароль на изменение и автора
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# Сохраняем рабочую книгу, чтобы защита от записи была сохранена
workbook.save("WriteProtectedWorkbook.xlsx")
# Проверяем пароль на изменение, используя правильный пароль
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Проверяем пароль на изменение, используя неверный пароль, чтобы продемонстрировать другую ветку
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## Защита и снятие защиты структуры книги
Защита структуры книги не позволяет другим пользователям просматривать скрытые рабочие листы, добавлять новые рабочие листы, перемещать рабочие листы, удалять рабочие листы, скрывать рабочие листы или переименовывать рабочие листы. Защищённое состояние применяется к структуре рабочих листов, а не к содержимому ячеек внутри какого-либо листа. Чтобы применить защиту структуры, вызовите `workbook.protect(ProtectionType.STRUCTURE, "password")`. Чтобы снять защиту, вызовите `workbook.unprotect("password")` и укажите правильный пароль. Здесь используется значение перечисления `ProtectionType.STRUCTURE`, которое отличается от других типов защиты, таких как `ProtectionType.WINDOWS`.

```python
import aspose.cells as ac
# Создать новую рабочую книгу
workbook = ac.Workbook()
# Добавить второй рабочий лист
workbook.worksheets.add()
# Записать образец значения в ячейку A1 первого рабочего листа
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# Защитить структуру рабочей книги
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# Сохранить рабочую книгу как structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Перезагрузить файл в новый экземпляр Workbook
loaded_workbook = ac.Workbook(file_path)
# Снять защиту структуры
loaded_workbook.unprotect("StructPwd")
# Вывести сообщение с подтверждением
print("Structure protection has been successfully removed from the workbook.")
```

## Защита и снятие защиты рабочих листов
Защита рабочего листа блокирует ячейки рабочего листа от случайных или преднамеренных изменений. Пользователи не могут редактировать заблокированные ячейки без указания пароля. Это типичная защита, используемая для защиты формул, заголовков или определённых областей ввода данных в общих электронных таблицах. Чтобы защитить рабочий лист, вызовите `worksheet.protect(ProtectionType.ALL, "password")`. Использование `ProtectionType.ALL` включает все доступные параметры защиты, такие как выбор заблокированных ячеек, форматирование ячеек, вставка строк и столбцов, а также удаление строк и столбцов. Чтобы снять защиту, вызовите `worksheet.unprotect("password")` с правильным паролем. Более детальный контроль доступен путём комбинирования других типов защиты, таких как `Contents`, `Objects` и `Scenarios`, с использованием побитового ИЛИ.

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

## Добавление и проверка цифровых подписей
Цифровая подпись гарантирует получателям, что содержимое книги является подлинным и не было изменено с момента подписания. Aspose.Cells обеспечивает поддержку цифровых подписей через пространство имён `aspose.cells.digital_signatures`. Типичный рабочий процесс загружает файл сертификата `.pfx` через `System.Security.Cryptography.X509Certificates.X509Certificate2`, оборачивает его в `aspose.cells.digital_signatures.DigitalSignature`, добавляет подпись в `DigitalSignatureCollection` и применяет коллекцию к книге через `workbook.add_digital_signature(DigitalSignatureCollection)`. Свойство `digital_signature.comments` может содержать контекст подписания, такой как время и цель подписания. Любое изменение, внесённое в книгу после подписания, делает подпись недействительной, поэтому этап проверки на стороне получателя может обнаружить вмешательство.

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

## Связанные статьи
- [Шифрование и расшифровка файлов Excel](/cells/ru/python-net/encrypt-and-decrypt-excel-files/)
- [Защита и снятие защиты структуры книги](/cells/ru/python-net/protect-and-unprotect-workbook-structure/)
- [Защита и снятие защиты рабочего листа](/cells/ru/python-net/protect-and-unprotect-worksheets/)
- [Защита паролем или снятие защиты общей книги](/cells/ru/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [Назначение и проверка цифровых подписей](/cells/ru/python-net/assign-and-validate-digital-signatures/)
- [Проверка пароля на изменение с помощью Aspose.Cells](/cells/ru/python-net/check-password-to-modify-using-aspose-cells/)
- [Определение формата зашифрованных файлов Office Open XML — OOXML](/cells/ru/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Шифрование файлов Excel](/cells/ru/python-net/encrypting-excel-files/)
- [Как определить формат файла и проверить, зашифрован ли файл](/cells/ru/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}