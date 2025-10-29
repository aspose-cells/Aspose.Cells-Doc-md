---
title: Указание значимых цифр для хранения в файле Excel с помощью Golang через C++
linktitle: Указание значительных цифр
type: docs
weight: 30
url: /ru/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Узнайте, как указать значащие цифры для хранения в файлах Excel с помощью Aspose.Cells и Golang через C++.
---

## **Возможные сценарии использования**

По умолчанию Aspose.Cells сохраняет 17 значимых цифр для чисел с плавающей точкой внутри файла Excel, в отличие от MS-Excel, который сохраняет только 15 значимых цифр. Вы можете изменить стандартное поведение Aspose.Cells с 17 на 15 значимых цифр, используя свойство [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/).

## **Указание значащих разрядов для хранения в файле Excel**

Следующий пример кода принуждает Aspose.Cells использовать 15 значимых цифр при сохранении чисел с плавающей точкой внутри файла Excel. Проверьте [выходной файл Excel](22774105.xlsx). Поменяйте его расширение на .zip, распакуйте, и вы увидите, что внутри файла сохранено только 15 значимых цифр. Следующий скриншот показывает эффект свойства [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) на выходном файле Excel.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
