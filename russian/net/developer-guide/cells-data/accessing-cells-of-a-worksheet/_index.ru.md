---
title: Доступ к Cells рабочего листа
type: docs
weight: 10
url: /ru/net/accessing-cells-of-a-worksheet/
description: В этой статье показано, как получить максимальный диапазон отображения рабочего листа и получить доступ к ячейкам с помощью Aspose.Cells for .NET API.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet. 
---
{{% alert color="primary" %}}

Мы знаем, что все рабочие листы могут содержать данные, которые в основном хранятся в ячейках (из которых состоит рабочий лист). Ячейка — это основная часть рабочего листа, которая используется для построения всего рабочего листа в виде последовательности строк и столбцов. Прежде чем мы попытаемся получить доступ к данным на листе, нам необходимо получить доступ к его ячейкам. Итак, в этой теме мы обсудим некоторые основные подходы к доступу к ячейкам рабочего листа во время выполнения с использованием Aspose.Cells.

{{% /alert %}}

##  **Как получить доступ к номеру Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочий ЛистКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)это обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция, представляющая все ячейки на листе.

 Мы можем использовать[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Collection для доступа к ячейкам на листе. Aspose.Cells предоставляет три основных подхода к доступу к ячейкам на листе:

1. Использование имени ячейки.
1. Использование индекса строки и столбца ячейки.
1.  Использование индекса ячейки в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция

**ВАЖНЫЙ:**Мы уже упоминали, что третий подход — самый быстрый, а первый — самый медленный. Разница в производительности между подходами очень мала, поэтому не беспокойтесь о снижении производительности, какой бы подход вы ни использовали.

###  **Как получить объект Cell по имени Cell**

 Разработчики могут получить доступ к любой конкретной ячейке, передав ее имя в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)класс как индекс.

 Если вы вначале создаете пустой лист, количество[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)сбор равен нулю. Когда вы используете этот подход для доступа к ячейке, он проверяет, существует ли эта ячейка в коллекции или нет. Если да, он возвращает объект ячейки в коллекции, в противном случае он создает новый[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) объект, добавляет объект в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекцию, а затем возвращает объект. Этот подход — самый простой способ доступа к ячейке, если вы знакомы с Microsoft Excel, но он самый медленный по сравнению с другими подходами.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellName-1.cs" >}}

###  **Как получить объект Cell по индексу строки и столбца Cell**

 Разработчики могут получить доступ к любой конкретной ячейке, передав индексы ее строки и столбца в функцию.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)сорт.

Этот подход работает так же, как и первый подход.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingRowAndColumnIndexOfCell-1.cs" >}}

###  **Как получить объект Cell по индексу Cell в коллекции Cells**

 Доступ к ячейке также можно получить, передав числовой индекс ячейки в функцию[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекция.

Если вы используете этот подход для доступа к ячейкам, исключение может быть выдано, если числовой индекс ячейки выходит за пределы допустимого диапазона. Этот подход является самым быстрым для доступа к ячейкам, но важно знать, что если вы используете этот подход для доступа к объекту ячейки, числовой индекс может измениться после добавления новых ячеек в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция. Объекты ячейки в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)коллекции внутренне сортируются по индексам строк и столбцов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-UsingCellIndexInCellsCollection-1.cs" >}}

##  **Как получить максимальный диапазон отображения рабочего листа**

Aspose.Cells позволяет разработчикам получить доступ к максимальному диапазону отображения рабочего листа. Максимальный диапазон отображения — диапазон ячеек между первой и последней ячейкой с содержимым — полезен, когда вам нужно скопировать, выбрать или отобразить все содержимое листа в изображении.

Вы можете получить доступ к максимальному диапазону отображения рабочего листа, используя[**Рабочий лист.Cells.MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) . В следующем примере кода показано, как получить доступ к[**Макс.диапазон отображения**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.cs" >}}
