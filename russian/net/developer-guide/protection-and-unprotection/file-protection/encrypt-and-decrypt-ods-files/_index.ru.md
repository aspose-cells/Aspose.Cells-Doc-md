---
title: Шифрование и дешифрование файлов ODS
type: docs
weight: 10
url: /ru/net/encrypt-and-decrypt-ods-files/
description: защита паролем и шифрование файлов ODS с использованием Aspose.Cells для .Net, который является чистой библиотекой .Net.
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

## **Шифрование файла ODS с помощью Aspose.Cells для .Net**
Для шифрования файла ODS загрузите файл и установите значение [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) в фактический пароль перед его сохранением. Зашифрованный файл ODS можно открыть только в OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Дешифрование файла ODS с помощью Aspose.Cells для .Net**

Для расшифровки файла ODS загрузите файл, предоставив пароль в [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). После загрузки файла установите строку [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) в null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
