---
title: Шифрование и дешифрование файлов ODS
type: docs
weight: 10
url: /ru/java/encrypt-and-decrypt-ods-files/
description: защищает паролем и шифрует файлы ODS с помощью Aspose.Cells for Java, который является чистой библиотекой Java.
---

{{% alert color="primary" %}}
OpenOffice.org - это полнофункциональный офисный пакет, который поддерживает защиту паролем и шифрование файлов. Однако зашифрованный файл ODS может быть открыт только в OpenOffice после ввода пароля. Excel не может открыть зашифрованный файл ODS и может выдать предупреждающее сообщение. Опции шифрования не применимы к файлам ODS, в отличие от других типов файлов. 
Aspose.Cells позволяет шифровать и дешифровать файлы ODS. Расшифрованный файл ODS можно открыть как в Excel, так и в OpenOffice, 
{{% /alert %}}

## **Шифровать с помощью OpenOffice Calc**
1. Выберите **Сохранить как** и нажмите флажок **Сохранить с паролем**.
1. Нажмите кнопку **Сохранить**.
1. Введите желаемый пароль в поля **Введите пароль для открытия** и **Подтвердите пароль** в окне установки пароля, которое откроется. 
1. Нажмите кнопку **OK**, чтобы сохранить файл.

## **Шифрование/дешифрование файла ODS:**

Для шифрования файла ODS загрузите файл и передайте фактический пароль в [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) перед его сохранением. Зашифрованный файл ODS можно открыть только в OpenOffice. Для дешифрования файла ODS загрузите файл, указав пароль в [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password). После загрузки файла вызовите функцию [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect-java.lang.String-) с фактическим паролем в качестве аргумента и, наконец, передайте null в [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Образец кода:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
{{< app/cells/assistant language="java" >}}
