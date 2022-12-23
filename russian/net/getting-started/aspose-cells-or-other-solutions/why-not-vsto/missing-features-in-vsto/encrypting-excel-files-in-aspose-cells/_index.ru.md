---
title: Шифрование файлов Excel в Aspose.Cells
type: docs
weight: 90
url: /ru/net/encrypting-excel-files-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel (97 – 2007) позволяет шифровать электронные таблицы и защищать их паролем. Он использует алгоритмы, предоставляемые поставщиком криптографических услуг, или CSP, набор криптографических алгоритмов с различными свойствами. CSP по умолчанию — «Совместимость с Office 97/2000» или «Слабое шифрование (XOR)». Важно выбрать правильную длину ключа шифрования. Некоторые CSP не поддерживают более 40 или 56 бит. Это считается слабым шифрованием. Для надежного шифрования требуется минимальная длина ключа 128 бит. Microsoft Windows содержит CSP, которые также предлагают надежные типы шифрования, например «Microsoft Strong Cryptographic Provider». Чтобы дать вам представление, 128-битное шифрование — это то, что банки используют для шифрования соединения со своими системами интернет-банкинга.

Aspose.Cells позволяет шифровать и защищать паролем Microsoft файлы Excel с желаемым типом шифрования.

{{% /alert %}} 
## **Использование Microsoft Excel**
Чтобы установить параметры шифрования файлов в Microsoft Excel (здесь Microsoft Excel 2003):

1.  От**Инструменты** меню, выберите**Параметры**.
 Появится диалоговое окно.
1.  Выберите**Безопасность** вкладка
1.  Введите пароль и нажмите**Передовой** 
   **Диалоговое окно параметров** 

![дело:изображение_альтернативный_текст](encrypting-excel-files-in-aspose-cells_1.png)




1.  Выберите тип шифрования и подтвердите пароль.

   **Диалоговое окно «Тип шифрования»** 

![дело:изображение_альтернативный_текст](encrypting-excel-files-in-aspose-cells_2.png)



## **Шифрование с Aspose.Cells**
В следующем примере показано, как зашифровать и защитить паролем файл Excel с помощью кода Aspose.Cells API.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a Workbook object.

//Open an excel file.

Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save("encryptedBook1.xls");



{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1))
