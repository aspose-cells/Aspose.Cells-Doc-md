---
title: Указание значащих цифр для сохранения в файле Excel
type: docs
weight: 30
url: /ru/net/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Возможные сценарии использования**

По умолчанию Aspose.Cells хранит 17 значащих цифр двойных значений внутри файла Excel, в отличие от MS-Excel, который хранит только 15 значащих цифр. Вы можете изменить поведение по умолчанию Aspose.Cells с 17 значащих цифр на 15 значащих цифр, используя[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)имущество.

## **Указание значащих цифр для сохранения в файле Excel**

 В следующем примере кода принудительно используется Aspose.Cells для использования 15 значащих цифр при сохранении двойных значений в файле Excel. Пожалуйста, проверьте[выходной файл excel](22774105.xlsx) . Измените его расширение на .zip и распакуйте его, и вы увидите, что внутри файла excel хранится только 15 значащих цифр. На следующем снимке экрана объясняется эффект[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)свойство в выходном файле Excel.

![дело:изображение_альтернативный_текст](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
