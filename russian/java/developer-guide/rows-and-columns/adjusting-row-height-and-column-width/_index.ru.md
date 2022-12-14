---
title: Настройка высоты строки и ширины столбца
type: docs
weight: 10
url: /ru/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

При работе с электронными таблицами и добавлении данных в строки или столбцы может потребоваться изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что для отображения данных необходимо изменить текущую высоту или ширину. Обычно пользователи настраивают высоту строк и ширину столбцов в среде WYSIWYG с помощью Microsoft Excel. Но с Aspose.Cells разработчики могут выполнять эти операции во время выполнения. Индексы строк и столбцов будут начинаться с 0.

{{% /alert %}} 
## **Работа со строками**
### **Регулировка высоты строки**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция, представляющая все ячейки рабочего листа.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже более подробно.
### **Настройка высоты строки**
 Можно установить высоту одной строки, вызвав функцию[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\) ) метод.[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы меняете.
- **Высота строки**, высота строки, применяемая к строке.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Установка высоты всех строк**
 Чтобы установить одинаковую высоту строки для всех строк на листе, используйте[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)метод.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Работа со столбцами**
### **Установка ширины столбца**
 Задайте ширину столбца, вызвав метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\) ) метод.[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) принимает следующие параметры:

- **Индекс столбца**, индекс столбца, ширину которого вы меняете.
- **Ширина колонки**, желаемая ширина столбца.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Настройка ширины всех столбцов**
 Чтобы установить одинаковую ширину столбца для всех столбцов на листе, используйте[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)метод.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
