---
title: Зашифровать и расшифровать ODS файлов
type: docs
weight: 10
url: /ru/java/encrypt-and-decrypt-ods-files/
description: защищать паролем и шифровать ODS файлы, используя Aspose.Cells for Java, которая является чистой Java библиотекой.
---
{{% alert color="primary" %}}
OpenOffice.org — полнофункциональный офисный пакет, поддерживающий защиту паролем и шифрование файлов. Однако зашифрованный файл ODS может быть открыт только OpenOffice после ввода пароля. Excel не может открыть зашифрованный файл ODS и может вывести предупреждающее сообщение. Параметры шифрования неприменимы к файлу ODS, в отличие от других типов файлов.
 Aspose.Cells позволяет зашифровать и расшифровать файл ODS. Расшифрованный файл ODS можно открыть как в Excel, так и в OpenOffice,
{{% /alert %}}

## **Шифрование с помощью OpenOffice Calc**
1.  Выбирать**Сохранить как** и щелкните**Сохранить с паролем** коробка.
1.  Нажмите на**Сохранять** кнопка.
1.  Введите желаемый пароль в оба**Введите пароль для открытия** и**Подтвердите пароль** поля в открывшемся окне Установить пароль.
1.  Нажмите на**ХОРОШО** кнопку для сохранения файла.

## **Шифрование/дешифрование ODS Файл:**

 Для шифрования файла ODS загрузите файл и передайте фактический пароль[**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password)перед сохранением. Выходной зашифрованный файл ODS можно открыть только в OpenOffice. Для расшифровки файла ODS загрузите файл, указав пароль в[**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) . После загрузки файла вызовите функцию[**Рабочая книга.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) с фактическим паролем в качестве аргумента и, наконец, передать null в[**Рабочая книга.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Образец кода:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
