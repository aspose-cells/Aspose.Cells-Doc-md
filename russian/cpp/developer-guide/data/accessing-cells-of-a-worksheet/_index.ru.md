---
title: Доступ к Cells рабочего листа
type: docs
weight: 10
url: /ru/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Мы знаем, что все рабочие листы могут содержать данные, которые в основном хранятся в ячейках (из которых состоит рабочий лист). Ячейка — это основная часть рабочего листа, которая используется для построения всего рабочего листа в виде последовательности строк и столбцов. Прежде чем мы попытаемся получить доступ к данным с рабочего листа, нам нужно получить доступ к его ячейкам. Итак, в этом разделе мы обсудим некоторые основные подходы к доступу к ячейкам рабочего листа во время выполнения с использованием Aspose.Cells.

{{% /alert %}} 
## **Доступ Cells**
 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет файл Excel.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) коллекция, которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)коллекция, представляющая все ячейки рабочего листа.

 Мы можем использовать[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)коллекция для доступа к ячейкам на листе. Aspose.Cells предоставляет три основных подхода к доступу к ячейкам на листе:

1. Использование имени ячейки.
1. Использование индекса строки и столбца ячейки.
1.  Использование индекса ячейки в[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)коллекция

{{% alert color="primary" %}} 

Мы упоминали, что 3-й подход — самый быстрый, а 1-й подход — самый медленный. Разница в производительности между подходами очень мала, поэтому не беспокойтесь о снижении производительности, какой бы подход вы ни использовали.

{{% /alert %}} 
### **Использование имени Cell**
 Разработчики могут получить доступ к любой конкретной ячейке, передав имя ее ячейки в[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)класс в качестве индекса.

 Если вы создаете пустой рабочий лист в начале, количество[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) сбор нулевой. Когда вы используете этот подход для доступа к ячейке, он проверяет, существует ли эта ячейка в коллекции или нет. Если да, он возвращает объект ячейки в коллекции, в противном случае он создает новый[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) объект, добавляет объект в[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection, а затем возвращает этот объект. Этот подход — самый простой способ доступа к ячейке, если вы знакомы с Microsoft Excel, но он самый медленный по сравнению с другими подходами.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName.cpp" >}}
### **Использование индекса строк и столбцов Cell**
 Разработчики могут получить доступ к любой конкретной ячейке, передав индексы ее строки и столбца в[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) коллекция[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)учебный класс. Этот подход работает так же, как и первый подход.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell.cpp" >}}
## **Доступ к максимальному диапазону отображения рабочего листа**
Aspose.Cells позволяет разработчикам получить доступ к максимальному диапазону отображения рабочего листа. Максимальный диапазон отображения — диапазон ячеек между первой и последней ячейкой с содержимым — полезен, когда вам нужно скопировать, выбрать или отобразить все содержимое рабочего листа на изображении.

 Вы можете получить доступ к максимальному диапазону отображения рабочего листа, используя[MaxDisplayIRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad351277ccaa0a4e1e8cd0693a1e2e988) метод[Cells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)коллекция.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet.cpp" >}}
