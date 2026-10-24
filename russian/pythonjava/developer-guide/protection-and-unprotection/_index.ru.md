---
title: Защита и снятие защиты
linktitle: Защита
description: В этом разделе описано, как зашифровать и расшифровать файлы Excel, а также защитить данные Excel, включая шифрование файлов, защиту только для чтения, защиту структуры рабочей книги, защиту рабочих листов и цифровые подписи с использованием кода Python
keywords: Aspose.Cells, Python via Java, шифрование, расшифровка, пароль, защита, снятие защиты, защита рабочей книги, защита рабочего листа, только для чтения, цифровая подпись, Python
type: docs
weight: 68
url: /ru/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Рабочие книги Excel часто содержат конфиденциальную финансовую, коммерческую или личную информацию, которую необходимо защитить от несанкционированного доступа. Aspose.Cells for Python via Java предоставляет комплексный набор функций защиты, отражающий возможности Microsoft Excel, который позволяет защищать данные на уровне файла, рабочей книги и рабочего листа.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java предлагает широкий спектр функций защиты — от уровня файла до уровня данных, аналогично MS Excel. Эти возможности включают шифрование файлов с помощью пароля, принудительное открытие только для чтения с использованием пароля на изменение, защиту структуры рабочей книги, защиту рабочих листов и добавление цифровых подписей к рабочим книгам.
{{% /alert %}}

## Шифрование и расшифровка файлов Excel
Пароль, установленный для файла Excel, запрещает неавторизованным пользователям открывать или просматривать содержимое рабочей книги. Чтобы зашифровать рабочую книгу, задайте строку пароля через `workbook.getSettings().setPassword(...)` и сохраните рабочую книгу. Aspose.Cells запишет файл в зашифрованном виде. Чтобы открыть зашифрованную рабочую книгу для расшифровки, создайте экземпляр объекта `LoadOptions`, задайте пароль через `load_options.setPassword(...)`, используя тот же пароль, что применялся при шифровании, и передайте его в конструктор `Workbook`. Aspose.Cells прозрачно применяет переданный пароль, поэтому остальной код может работать с расшифрованным содержимым так, как если бы файл был обычной рабочей книгой.

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

## Защита только для чтения (пароль на изменение)
Excel поддерживает два различных уровня парольной защиты. Первый — это пароль на открытие, который шифрует сам файл и рассмотрен в предыдущем разделе. Второй — это пароль на изменение, который не блокирует открытие рабочей книги пользователями; вместо этого Excel рекомендует открывать файл в режиме только для чтения, если не указан пароль на изменение. Настройте это поведение в Aspose.Cells через `workbook.getSettings().getWriteProtection()`. Задайте пароль с помощью `setPassword(...)` как пароль на изменение, а автора — с помощью `setAuthor(...)`, чтобы указать, кто применил защиту. Используйте метод `writeProtection.validatePassword(String)` для проверки правильности переданного пароля на изменение, который возвращает `true` при совпадении и `false` в противном случае.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Создать новую рабочую книгу с нуля
workbook = Workbook()
# Записать образец значения в ячейку A1 первого листа
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# Настроить защиту от записи: задать пароль на изменение и автора
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# Сохранить рабочую книгу, чтобы защита от записи была сохранена
workbook.save("WriteProtectedWorkbook.xlsx")
# Проверить пароль на изменение, используя правильный пароль
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Проверить пароль на изменение, используя неправильный пароль, чтобы продемонстрировать другую ветку
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## Защита и снятие защиты структуры рабочей книги
Защита структуры рабочей книги не позволяет другим пользователям просматривать скрытые рабочие листы, добавлять новые рабочие листы, перемещать рабочие листы, удалять рабочие листы, скрывать рабочие листы или переименовывать рабочие листы. Защищённое состояние применяется к структуре листов, а не к содержимому ячеек внутри какого-либо листа. Чтобы применить защиту структуры, вызовите `workbook.protect(ProtectionType.STRUCTURE, "password")`. Чтобы снять защиту, вызовите `workbook.unprotect("password")` и укажите правильный пароль. Здесь используется значение перечисления `ProtectionType.STRUCTURE`, которое отличается от других типов защиты, таких как `ProtectionType.WINDOWS`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# Создать новую рабочую книгу
workbook = Workbook()
# Добавить второй рабочий лист
workbook.getWorksheets().add()
# Записать образец значения в ячейку A1 первого рабочего листа
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# Защитить структуру рабочей книги
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# Сохранить рабочую книгу как structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Перезагрузить файл в новый экземпляр Workbook
loaded_workbook = Workbook(file_path)
# Снять защиту структуры
loaded_workbook.unprotect("StructPwd")
# Вывести сообщение подтверждения
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## Защита и снятие защиты рабочих листов
Защита рабочего листа блокирует ячейки рабочего листа от случайных или намеренных изменений. Пользователи не могут редактировать заблокированные ячейки без указания пароля. Это типичный вид защиты, используемый для охраны формул, заголовков или определённых областей ввода данных в общих электронных таблицах. Чтобы защитить рабочий лист, вызовите `worksheet.protect(ProtectionType.ALL, "password")`. Использование `ProtectionType.ALL` включает все доступные параметры защиты, такие как выбор заблокированных ячеек, форматирование ячеек, вставка строк и столбцов, а также удаление строк и столбцов. Чтобы снять защиту, вызовите `worksheet.unprotect("password")` с правильным паролем. Более точное управление доступно путём комбинирования других типов защиты, таких как `ProtectionType.CONTENTS`, `ProtectionType.OBJECTS` и `ProtectionType.SCENARIOS`, с помощью побитового ИЛИ.

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

## Добавление и проверка цифровых подписей
Цифровая подпись гарантирует получателям, что содержимое рабочей книги является подлинным и не было изменено с момента подписания. Aspose.Cells обеспечивает поддержку цифровых подписей через пространство имён `Aspose.Cells.DigitalSignatures`. Типичный рабочий процесс загружает файл сертификата `.pfx` через `java.security.KeyStore`, оборачивает его в `Aspose.Cells.DigitalSignatures.DigitalSignature`, добавляет подпись в коллекцию `DigitalSignatureCollection` и применяет коллекцию к рабочей книге через `workbook.addDigitalSignature(digitalSignatureCollection)`. Свойство `digitalSignature.getComments()` может фиксировать контекст подписания, например время и назначение подписания. Любое изменение, внесённое в рабочую книгу после подписания, делает подпись недействительной, поэтому этап проверки на стороне получателя позволяет обнаружить подделку.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Загрузка сертификата из PFX-файла с помощью Java KeyStore
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# Получение сертификата
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# Создание цифровой подписи
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# Создание рабочей книги и добавление подписи
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## Связанные статьи
- [Шифрование и расшифровка файлов Excel](/cells/ru/python-java/encrypt-and-decrypt-excel-files/)
- [Защита и снятие защиты структуры рабочей книги](/cells/ru/python-java/protect-and-unprotect-workbook-structure/)
- [Защита и снятие защиты рабочего листа](/cells/ru/python-java/protect-and-unprotect-worksheet/)
- [Проверка пароля на изменение с помощью Aspose.Cells](/cells/ru/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}