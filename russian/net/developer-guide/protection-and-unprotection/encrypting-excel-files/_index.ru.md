---
title: Шифрование файлов Excel
type: docs
weight: 90
url: /ru/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

Microsoft Excel (97–365) позволяет шифровать электронные таблицы и защищать их паролем. Он использует алгоритмы, предоставляемые поставщиком криптографических услуг, или CSP, набор криптографических алгоритмов с различными свойствами. CSP по умолчанию — «Совместимость с Office 97/2000» или «Слабое шифрование (XOR)». Важно выбрать правильную длину ключа шифрования. Некоторые CSP не поддерживают более 40 или 56 бит. Это считается слабым шифрованием. Для надежного шифрования требуется минимальная длина ключа 128 бит. Microsoft Windows содержит CSP, которые также предлагают надежные типы шифрования, например «Microsoft Strong Cryptographic Provider». Чтобы дать вам представление, 128-битное шифрование — это то, что банки используют для шифрования соединения со своими системами интернет-банкинга.

Aspose.Cells позволяет шифровать и защищать паролем Microsoft файлы Excel с желаемым типом шифрования.

{{% /alert %}}

## **Использование Microsoft Excel**

Чтобы установить параметры шифрования файлов в Microsoft Excel (здесь Microsoft Excel 2003):

1.  От**Инструменты** меню, выберите**Параметры**Появится диалоговое окно.
1.  Выберите**Безопасность** вкладка
1.  Введите пароль и нажмите**Передовой**
1. Выберите тип шифрования и подтвердите пароль.

## **Шифрование с Aspose.Cells**

В следующем примере показано, как зашифровать и защитить паролем файл Excel с помощью кода Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Указание пароля для изменения параметра**

 В следующем примере показано, как установить**Пароль для изменения** Microsoft Опция Excel для существующего файла с использованием Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **Проверьте пароль зашифрованного файла**

 Чтобы проверить пароль зашифрованного файла, Aspose.Cells for .NET предоставляет[**Подтвердите пароль**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) метод. Эти методы принимают два параметра: файловый поток и пароль, который необходимо проверить.
 Следующий фрагмент кода демонстрирует использование[**Подтвердите пароль**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) метод, чтобы проверить, является ли предоставленный пароль действительным или нет.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **Шифрование/дешифрование файла ODS с помощью Aspose.Cells**

Aspose.Cells позволяет зашифровать и расшифровать файл ODS. Расшифрованный файл ODS можно открыть как в Excel, так и в OpenOffice, однако зашифрованный файл ODS можно открыть только в OpenOffice после ввода пароля. Excel не может открыть зашифрованный файл ODS и может вывести предупреждающее сообщение. Параметры шифрования неприменимы к файлу ODS, в отличие от других типов файлов. Для шифрования файла ODS загрузите файл и установите[**WorkbookSettings.Пароль**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) значение фактического пароля перед его сохранением. Выходной зашифрованный файл ODS можно открыть только в OpenOffice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 Для расшифровки файла ODS загрузите файл, указав пароль в[**LoadOptions.Пароль**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . После загрузки файла установите[**WorkbookSettings.Пароль**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) строку в ноль.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
