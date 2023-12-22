---
title: Доступ к Cells рабочего листа
type: docs
weight: 10
url: /ru/cpp/accessing-cells-of-a-worksheet/
---
{{% alert color="primary" %}} 

Мы знаем, что все рабочие листы могут содержать данные, которые в основном хранятся в ячейках (из которых состоит рабочий лист). Ячейка — это основная часть рабочего листа, которая используется для построения всего рабочего листа в виде последовательности строк и столбцов. Прежде чем мы попытаемся получить доступ к данным на листе, нам необходимо получить доступ к его ячейкам. Итак, в этой теме мы обсудим некоторые основные подходы к доступу к ячейкам рабочего листа во время выполнения с использованием Aspose.Cells.

{{% /alert %}} 
##  **Доступ к номеру Cells**
 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) который представляет файл Excel.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)коллекция, которая позволяет получить доступ к каждому листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) класс обеспечивает[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)коллекция, представляющая все ячейки на листе.

 Мы можем использовать[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)Collection для доступа к ячейкам на листе. Aspose.Cells предоставляет три основных подхода к доступу к ячейкам на листе:

1. Использование имени ячейки.
1. Использование индекса строки и столбца ячейки.
1.  Использование индекса ячейки в[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)коллекция

{{% alert color="primary" %}} 

Мы уже упоминали, что третий подход — самый быстрый, а первый — самый медленный. Разница в производительности между подходами очень мала, поэтому не беспокойтесь о снижении производительности, какой бы подход вы ни использовали.

{{% /alert %}} 
###  **Использование имени Cell**
 Разработчики могут получить доступ к любой конкретной ячейке, передав ее имя в[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)класс как индекс.

 Если вы вначале создаете пустой лист, количество[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)сбор равен нулю. Когда вы используете этот подход для доступа к ячейке, он проверяет, существует ли эта ячейка в коллекции или нет. Если да, он возвращает объект ячейки в коллекции, в противном случае он создает новый[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) объект, добавляет объект в[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)коллекцию, а затем возвращает этот объект. Этот подход — самый простой способ доступа к ячейке, если вы знакомы с Microsoft Excel, но он самый медленный по сравнению с другими подходами.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingCellName-new.cpp" >}}
###  **Использование индекса строки и столбца Cell**
 Разработчики могут получить доступ к любой конкретной ячейке, передав индексы ее строки и столбца в функцию.[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) коллекция[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)сорт. Этот подход работает так же, как и первый подход.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingCellsUsingRowAndColumnIndexOfTheCell-new.cpp" >}}
##  **Доступ к максимальному диапазону отображения рабочего листа**
Aspose.Cells позволяет разработчикам получить доступ к максимальному диапазону отображения рабочего листа. Максимальный диапазон отображения — диапазон ячеек между первой и последней ячейкой с содержимым — полезен, когда вам нужно скопировать, выбрать или отобразить все содержимое листа в изображении.

Вы можете получить доступ к максимальному диапазону отображения рабочего листа, используя[Макс.диапазон отображения](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) метод[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)коллекция.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AccessingCellsOfWorksheet-AccessingMaximumDisplayRangeOfWorksheet-new.cpp" >}}
