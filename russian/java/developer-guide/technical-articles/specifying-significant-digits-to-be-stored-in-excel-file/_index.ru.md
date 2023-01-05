---
title: Указание значащих цифр для сохранения в файле Excel
type: docs
weight: 20
url: /ru/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Возможные сценарии использования**

По умолчанию Aspose.Cells хранит 17 значащих цифр двойных значений в электронных таблицах, в отличие от приложения Excel, которое хранит только 15 значащих цифр. Вы можете изменить поведение по умолчанию Aspose.Cells для этого случая, то есть; вы можете изменить количество значащих цифр с 17 до 15 при использовании[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)имущество.

## **Указание значащих цифр для сохранения в файле Excel**

 В следующем примере кода принудительно используется Aspose.Cells для использования 15 значащих цифр при сохранении двойных значений в файле Excel. Пожалуйста, проверьте[выходной файл excel](23166982.xlsx) . Измените его расширение на .zip и распакуйте его, и вы увидите, что внутри файла excel хранится только 15 значащих цифр. На следующем снимке экрана объясняется эффект[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)свойство в выходном файле Excel.

![дело:изображение_альтернативный_текст](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
