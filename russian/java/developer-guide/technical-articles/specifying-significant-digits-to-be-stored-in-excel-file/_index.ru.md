---
title: Указание количества значащих цифр, которые будут сохранены в файл Excel
type: docs
weight: 20
url: /ru/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Возможные сценарии использования**

По умолчанию Aspose.Cells сохраняет 17 значащих цифр вещественных значений в таблицах, в отличие от приложения Excel, которое сохраняет только 15 значащих цифр. Вы можете изменить стандартное поведение Aspose.Cells в данном случае, то есть; можно изменить количество значащих цифр с 17 до 15 при использовании свойства [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits).

## **Указание количества значащих цифр, которые будут сохранены в файл Excel**

Приведенный ниже образец кода заставляет Aspose.Cells использовать 15 значащих цифр при сохранении вещественных значений в файл Excel. Пожалуйста, проверьте [файл Excel](23166982.xlsx) вывода. Измените его расширение на .zip, распакуйте его, и вы увидите, что в файле Excel сохранены только 15 значащих цифр. На следующем снимке экрана объясняется влияние свойства [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) на выходной файл Excel.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
{{< app/cells/assistant language="java" >}}
