---
title: Доступ к ячейкам листа
type: docs
weight: 10
url: /ru/cpp/accessing-cells-of-a-worksheet/
---

{{% alert color="primary" %}} 

Мы знаем, что все листы могут содержать данные, которые в основном хранятся в ячейках (из которых состоит лист). Ячейка является основной частью листа, используемой для построения всего листа в виде последовательности строк и столбцов. Прежде чем мы попытаемся получить доступ к данным из листа, нам нужно получить доступ к его ячейкам. Таким образом, в этой теме мы обсудим несколько основных подходов к доступу к ячейкам листа во время выполнения с использованием Aspose.Cells.

{{% /alert %}} 
## **Доступ к ячейкам**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет собой файл Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), представляющую все ячейки на листе.

Мы можем использовать коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) для доступа к ячейкам на листе. Aspose.Cells предоставляет три основных подхода к доступу к ячейкам на листе:

1. Использование имени ячейки.
2. Использование индекса строки и столбца ячейки.
3. Использование индекса ячейки в коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

{{% alert color="primary" %}} 

Мы отметили, что 3-й подход является самым быстрым, а 1-й подход является самым медленным. Разница в производительности между подходами очень невелика, поэтому не беспокойтесь о снижении производительности, какой бы подход вы ни использовали.

{{% /alert %}} 
### **Использование имени ячейки**
Разработчики могут получить доступ к любой конкретной ячейке, передав ее имя ячейки в коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) в качестве индекса.

Если вы создаете пустую рабочую книгу в начале, количество элементов в коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) будет равно нулю. Когда вы используете этот подход для доступа к ячейке, он проверит, существует ли эта ячейка в коллекции или нет. Если да, он вернет объект ячейки в коллекции, в противном случае создаст новый объект [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), добавит объект в коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) и затем вернет этот объект.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
### **Использование индекса строки и столбца ячейки**
Разработчики могут получить доступ к любой конкретной ячейке, передав индексы ее строки и столбца в коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Этот подход работает так же, как и первый.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
## **Доступ к максимальному диапазону отображения рабочего листа**
Aspose.Cells позволяет разработчикам получить доступ к максимальному диапазону отображения рабочего листа. Максимальный диапазон отображения - это диапазон ячеек между первой и последней ячейкой с содержимым - полезен, когда вам нужно скопировать, выбрать или отобразить все содержимое рабочего листа в изображении.

Вы можете получить доступ к максимальному диапазону отображения рабочего листа, используя метод [MaxDisplayRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
