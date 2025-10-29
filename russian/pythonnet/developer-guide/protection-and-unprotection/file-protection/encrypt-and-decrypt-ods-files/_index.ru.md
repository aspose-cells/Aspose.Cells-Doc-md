---
title: Шифрование и дешифрование файлов ODS
type: docs
weight: 10
url: /ru/python-net/encrypt-and-decrypt-ods-files/
description: захищать паролем и шифровать файлы ODS с помощью Aspose.Cells для Python via .NET, который является чистой библиотекой для .NET.
---

{{% alert color="primary" %}}
OpenOffice.org - это полнофункциональный офисный пакет, который поддерживает защиту паролем и шифрование файлов. Однако зашифрованный файл ODS может быть открыт только в OpenOffice после ввода пароля. Excel не может открыть зашифрованный файл ODS и может выдать предупреждающее сообщение. Опции шифрования не применимы к файлам ODS, в отличие от других типов файлов. 
Aspose.Cells для Python via .NET позволяет шифровать и расшифровывать файлы ODS. Расшифрованный файл ODS можно открывать как в Excel, так и в OpenOffice. 
{{% /alert %}}

## **Шифровать с помощью OpenOffice Calc**
1. Выберите **Сохранить как** и нажмите флажок **Сохранить с паролем**.
1. Нажмите кнопку **Сохранить**.
1. Введите желаемый пароль в поля **Введите пароль для открытия** и **Подтвердите пароль** в окне установки пароля, которое откроется. 
1. Нажмите кнопку **OK**, чтобы сохранить файл.

## **Зашифровать файл ODS с помощью Aspose.Cells для Python via .NET**
Для шифрования файла ODS загрузите файл и установите значение [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) в фактический пароль перед его сохранением. Зашифрованный файл ODS можно открыть только в OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Дешифровать файл ODS с помощью Aspose.Cells для Python via .NET**

Для расшифровки файла ODS загрузите файл, предоставив пароль в [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). После загрузки файла установите строку [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) в null.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
