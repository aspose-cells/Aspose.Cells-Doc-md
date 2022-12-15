---
title: Доступ к Cells рабочего листа
type: docs
weight: 10
url: /ru/java/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Мы знаем, что все рабочие листы могут содержать данные, которые в основном хранятся в ячейках (из которых состоит рабочий лист). Ячейка — это основная часть рабочего листа, которая используется для построения всего рабочего листа в виде последовательности строк и столбцов. Прежде чем мы попытаемся получить доступ к данным с рабочего листа, нам нужно получить доступ к его ячейкам. Итак, в этом разделе мы обсудим некоторые основные подходы к доступу к ячейкам рабочего листа во время выполнения с использованием Aspose.Cells.

{{% /alert %}} 
## **Доступ Cells**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет собой файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция, представляющая все ячейки рабочего листа.

 Мы можем использовать[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция для доступа к ячейкам на листе. Aspose.Cells предоставляет различные базовые подходы для доступа к ячейкам:

1. [Использование имени ячейки](/cells/ru/java/accessing-cells-of-a-worksheet/).
1. [Использование индекса строки и столбца](/cells/ru/java/accessing-cells-of-a-worksheet/).
### **Использование имени Cell**
 Разработчики могут получить доступ к любой конкретной ячейке, передав имя ее ячейки в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)учебный класс.

 Если вы создаете пустой рабочий лист в начале, количество[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)сбор нулевой. Когда вы используете этот подход для доступа к ячейке, он проверяет, существует ли эта ячейка в коллекции или нет. Если да, он возвращает объект ячейки в коллекции, в противном случае он создает новый[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) объект, добавляет объект в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection, а затем возвращает объект. Этот подход является самым простым способом доступа к ячейке, если вы знакомы с Microsoft Excel, но он медленнее, чем другие подходы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingCellName-UsingCellName.java" >}}



### **Использование индекса строк и столбцов Cell**
 Разработчики могут получить доступ к любой конкретной ячейке, передав индексы ее строки и столбца в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)учебный класс.

Этот подход работает так же, как и первый подход.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UsingRowAndColumnIndexOfCell-UsingRowAndColumnIndexOfCell.java" >}}
### **Статьи по Теме**
{{% alert color="primary" %}} 

- [Именованные диапазоны](/cells/ru/java/named-ranges/)

{{% /alert %}} 
## **Доступ к максимальному диапазону отображения рабочего листа**
Aspose.Cells позволяет разработчикам получить доступ к максимальному диапазону отображения рабочего листа. Максимальный диапазон отображения — диапазон ячеек между первой и последней ячейкой с содержимым — полезен, когда вам нужно скопировать, выбрать или отобразить все содержимое рабочего листа на изображении.

 Вы можете получить доступ к максимальному диапазону отображения рабочего листа, используя[Рабочий лист.getCells().getMaxDisplayRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange).

На следующем рисунке максимальный диапазон отображения выбранного рабочего листа составляет A1: G15.

**Отображение максимального диапазона отображения этого рабочего листа** 

![дело:изображение_альтернативный_текст](accessing-cells-of-a-worksheet_1.png)

 В следующем примере кода показано, как получить доступ к[MaxDisplayRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MaxDisplayRange)имущество. Код генерирует следующий вывод.

{{< highlight "java" >}}

 Maximum Display Range: =Sheet1!$A$1:$G$15

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessingMaximumDisplayRangeofWorksheet-AccessingMaximumDisplayRangeofWorksheet.java" >}}
