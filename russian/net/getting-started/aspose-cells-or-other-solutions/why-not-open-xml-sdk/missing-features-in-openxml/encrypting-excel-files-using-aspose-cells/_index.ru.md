---
title: Шифрование файлов Excel с использованием Aspose.Cells
type: docs
weight: 30
url: /ru/net/encrypting-excel-files-using-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel (97 - 2007) позволяет шифровать и защищать паролем ваши электронные таблицы. Для этого используются алгоритмы, предоставленные криптографическим поставщиком услуг, или CSP, набор криптографических алгоритмов с разными свойствами. Умолчательным CSP является 'Совместимый с Office 97/2000' или 'Слабое шифрование (XOR)'. Важно выбрать правильную длину ключа шифрования. Некоторые CSP не поддерживают более 40 или 56 бит. Это считается слабым шифрованием. Для сильного шифрования требуется минимальная длина ключа 128 бит. В Microsoft Windows имеются CSP, которые также предлагают сильные типы шифрования, например, 'Microsoft Strong Cryptographic Provider'. Для примера, 128-битное шифрование - это то, что используют банки для шифрования связи с их системами Интернет-банкинга.

Aspose.Cells позволяет шифровать и защищать паролем файлы Microsoft Excel с выбранным вами типом шифрования.

{{% /alert %}} 
## **Использование Microsoft Excel**
Для установки параметров шифрования файла в Microsoft Excel (например, Microsoft Excel 2003):

1. В меню **Сервис** выберите **Параметры**.
   Появляется диалоговое окно.
1. Выберите вкладку **Безопасность**.
1. Введите пароль и нажмите **Дополнительно**. 
   **Диалоговое окно параметров** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_1.png)




1. Выберите тип шифрования и подтвердите пароль. 

   **Диалоговое окно типа шифрования** 

![todo:image_alt_text](encrypting-excel-files-using-aspose-cells_2.png)



## **Шифрование с помощью Aspose.Cells**
В следующем примере показано, как зашифровать и защитить паролем файл Excel с использованием API Aspose.Cells.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string srcFileName = FilePath + "Encrypting Excel Files.xlsx";

string destFileName = FilePath + "Result Encrypting Excel Files.xlsx";

//Open an excel file.

Workbook workbook = new Workbook(srcFileName);

//Specify XOR encryption type.

workbook.SetEncryptionOptions(EncryptionType.XOR, 40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).

workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.

workbook.Settings.Password = "1234";

//Save the excel file.

workbook.Save(destFileName);

{{< /highlight >}}
## **Скачать работающий код**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Encrypting%20Excel%20Files)

{{< app/cells/assistant language="csharp" >}}
