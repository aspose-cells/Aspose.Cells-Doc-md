---
title: Скрытие и отображение строк и столбцов
type: docs
weight: 50
url: /ru/java/hiding-and-showing-rows-and-columns/
---

## **Введение**
Иногда пользователям также может потребоваться скрыть определенные строки или столбцы в листе и затем в последствии их отобразить. Функция для этого предоставляется Microsoft Excel, а также Aspose.Cells.
## **Управление видимостью строк и столбцов**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), который позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), представляющую все ячейки в листе. Коллекция [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) предоставляет несколько методов для управления строками или столбцами в листе. Некоторые из них обсуждаются ниже.
### **Скрытие строк или столбцов**
Разработчики могут скрывать строку или столбец, вызвав методы [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow-int-) и [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn-int-) коллекции [Cells]. Оба метода принимают индекс строки или столбца в качестве параметра для скрытия конкретной строки или столбца.

{{% alert color="primary" %}} 

Примечание: Также возможно скрыть строку или столбец, установив высоту строки или ширину столбца в 0 соответственно.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Показ строк и столбцов**
Разработчики могут сделать скрытую строку или столбец видимыми снова, вызвав методы [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow-int-double-) и [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn-int-double-) коллекции [Cells]. Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенная строке или столбцу после отображения.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

При отображении скрытого столбца/строки, если вам нужно восстановить его предварительно назначенную ширину или высоту, или его исходную ширину или высоту, пожалуйста, отобразите столбец или строку с отрицательной шириной или высотой. Например, worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
