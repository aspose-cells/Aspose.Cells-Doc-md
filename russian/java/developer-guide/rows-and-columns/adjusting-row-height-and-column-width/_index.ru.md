---
title: Настройка высоты строки и ширины столбца
type: docs
weight: 10
url: /ru/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

При работе со электронными таблицами и добавлении данных в строки или столбцы может потребоваться изменить высоту строк или ширину столбцов. Иногда применение форматирования к строкам или столбцам означает, что текущая высота или ширина должны измениться для отображения данных. Обычно пользователи настраивают высоту строк и ширину столбцов в среде WYSIWYG с помощью Microsoft Excel. Но с помощью Aspose.Cells разработчики могут выполнять эти операции во время выполнения. Индексы строк и столбцов начинаются с 0.

{{% /alert %}} 
## **Работа со строками**
### **Изменение высоты строки**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), позволяющий получать доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), представляющую все ячейки на листе.

Коллекция [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них подробно обсуждаются ниже.
### **Установка высоты строки**
Возможно установить высоту одной строки, вызвав метод [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Метод [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы изменяете.
- **Высота строки**, высота строки, применяемая к строке.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Установка высоты всех строк**
Чтобы установить одинаковую высоту строк для всех строк на листе, используйте метод [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight) коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Работа с колонками**
### **Установка ширины колонки**
Установите ширину столбца, вызвав метод [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Метод [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) принимает следующие параметры:

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.
- **Ширина колонки**, желаемая ширина колонки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Установка ширины всех столбцов**
Чтобы установить одинаковую ширину столбцов для всех столбцов на листе, используйте метод [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth) коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
