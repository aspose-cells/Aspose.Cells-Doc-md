---
title: Скрытие и отображение строк и столбцов
type: docs
weight: 50
url: /ru/java/hiding-and-showing-rows-and-columns/
---
## **Вступление**
Иногда пользователям также может потребоваться скрыть определенные строки или столбцы рабочего листа, а затем отобразить их позже. Microsoft Excel предоставляет эту функцию, а также Aspose.Cells.
## **Управление видимостью строк и столбцов**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция, представляющая все ячейки рабочего листа.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже.
### **Скрытие строк или столбцов**
 Разработчики могут скрыть строку или столбец, вызвав метод[HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ) и[СкрытьКолонку](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) ) методы[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)сборник соответственно. Оба метода принимают индекс строки/столбца в качестве параметра, чтобы скрыть конкретную строку или столбец.

{{% alert color="primary" %}} 

Примечание. Также можно скрыть строку или столбец, если мы установим высоту строки или ширину столбца равными 0 соответственно.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Отображение строк и столбцов**
 Разработчики могут отобразить любую скрытую строку или столбец, вызвав метод[UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ) и[Показать столбец](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) ) методы[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)сборник соответственно. Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенная строке или столбцу после его отображения.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

При отображении скрытого столбца/строки, если вам нужно восстановить ранее заданную ширину или высоту или исходную ширину или высоту, отобразите столбец или строку с отрицательной шириной или высотой. Например, worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
