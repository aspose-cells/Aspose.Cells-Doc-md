---
title: Шифровать и расшифровывать файлы ODS
type: docs
weight: 10
url: /ru/net/encrypt-and-decrypt-ods-files/
description: защищать паролем и шифровать файлы ODS, используя Aspose.Cells для .Net, которая является чистой сетевой библиотекой.
---
{{% alert color="primary" %}}
OpenOffice.org — полнофункциональный офисный пакет, поддерживающий защиту паролем и шифрование файлов. Однако зашифрованный файл ODS может быть открыт только OpenOffice после ввода пароля. Excel не может открыть зашифрованный файл ODS и может выдать предупреждающее сообщение. Параметры шифрования неприменимы к файлу ODS, в отличие от других типов файлов.
 Aspose.Cells позволяет зашифровать и расшифровать файл ODS. Расшифрованный файл ODS можно открыть как в Excel, так и в OpenOffice,
{{% /alert %}}

## **Шифрование с помощью OpenOffice Calc**
1.  Выбирать**Сохранить как** и щелкните**Сохранить с паролем** коробка.
1.  Нажмите на**Сохранять** кнопка.
1.  Введите желаемый пароль в оба**Введите пароль для открытия** а также**Подтвердить Пароль** поля в открывшемся окне Установить пароль.
1.  Нажмите на**ХОРОШО** кнопку для сохранения файла.

## **Зашифровать файл ODS с помощью Aspose.Cells для .Net**
 Для шифрования файла ODS загрузите файл и установите[**WorkbookSettings.Пароль**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) значение фактического пароля перед его сохранением. Выходной зашифрованный файл ODS можно открыть только в OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Расшифровать файл ODS с помощью Aspose.Cells для .Net**

 Для расшифровки файла ODS загрузите файл, указав пароль в[**LoadOptions.Пароль**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . После загрузки файла установите[**WorkbookSettings.Пароль**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) строку в ноль.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
