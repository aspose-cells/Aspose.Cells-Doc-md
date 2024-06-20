---
title: Доступ к ячейкам листа
type: docs
weight: 10
url: /ru/java/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Мы знаем, что все листы могут содержать данные, которые в основном хранятся в ячейках (из которых состоит лист). Ячейка является основной частью листа, используемой для построения всего листа в виде последовательности строк и столбцов. Прежде чем мы попытаемся получить доступ к данным из листа, нам нужно получить доступ к его ячейкам. Таким образом, в этой теме мы обсудим несколько основных подходов к доступу к ячейкам листа во время выполнения с использованием Aspose.Cells.

{{% /alert %}} 
## **Доступ к ячейкам**
Aspose.Cells предоставляет класс, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), представляющую все ячейки на листе.

Мы можем использовать коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), чтобы получить доступ к ячейкам в листе. Aspose.Cells предоставляет различные основные подходы для доступа к ячейкам:

1. [Использование имени ячейки](/cells/ru/java/accessing-cells-of-a-worksheet/).
1. [Использование индексов строки и столбца](/cells/ru/java/accessing-cells-of-a-worksheet/).
### **Использование имени ячейки**
Разработчики могут получить доступ к любой конкретной ячейке, передав её имя в коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Если вы создадите пустой лист в начале, то количество элементов в коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) будет равно нулю. При использовании этого подхода для доступа к ячейке, он проверит, существует ли эта ячейка в коллекции или нет. Если да, то он вернет объект ячейки в коллекции, в противном случае он создаст новый объект [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell), добавит его в коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) и затем вернет объект. Этот подход является самым простым способом доступа к ячейке, если вы знакомы с Microsoft Excel, но он медленнее, чем другие подходы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Использование индекса строки и столбца ячейки**
Разработчики могут получить доступ к любой конкретной ячейке, передав индексы её строки и столбца в коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) класса [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

Этот подход работает так же, как и первый подход.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Связанные статьи**
{{% alert color="primary" %}} 

- [Именованные диапазоны](/cells/ru/java/named-ranges/)

{{% /alert %}} 
## **Доступ к максимальному диапазону отображения рабочего листа**
Aspose.Cells позволяет разработчикам получить максимальный дисплейный диапазон листа. Максимальный дисплейный диапазон - диапазон ячеек между первой и последней ячейкой с содержимым - полезен, если вам нужно скопировать, выбрать или отобразить всё содержимое листа в изображении.

Вы можете получить доступ к максимальному диапазону отображения листа, используя [Worksheet.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

На следующей диаграмме показан максимальный диапазон отображения выбранного листа - A1:G15.

**Показ максимального диапазона отображения этого листа** 

![todo:image_alt_text](accessing-cells-of-a-worksheet_1.png)

Ниже приведен пример кода, иллюстрирующий, как получить доступ к свойству [MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange). Код генерирует следующий вывод.

{{< highlight java >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
