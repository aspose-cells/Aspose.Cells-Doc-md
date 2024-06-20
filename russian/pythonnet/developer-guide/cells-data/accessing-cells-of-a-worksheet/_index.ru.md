---
title: Доступ к ячейкам листа
type: docs
weight: 10
url: /ru/python-net/accessing-cells-of-a-worksheet/
description: Эта статья показывает, как получить максимальный диапазон отображения листа и получать доступ к ячейкам с использованием API Aspose.Cells для Python via .NET.
keywords: Библиотека Excel для Python, Получить объект Ячейки, Доступ к Ячейкам, Как получить объект Ячейки по индексу строки и столбца ячейки, Как получить объект Ячейки по индексу ячейки в коллекции ячеек, Как получить объект Ячейки по индексу строки и столбца ячейки, Получить максимальный диапазон отображения листа. 
---

{{% alert color="primary" %}}

Мы знаем, что все листы могут содержать данные, которые в основном хранятся в ячейках (из которых состоит лист). Ячейка - это основная часть листа, которая используется для построения всего листа в виде последовательности строк и столбцов. Прежде чем мы попробуем получить доступ к данным на листе, нам нужно получить доступ к его ячейкам. Поэтому в этой теме мы обсудим некоторые основные методы доступа к ячейкам листа во время выполнения с использованием Aspose.Cells для Python via .NET.

{{% /alert %}}

## **Как получить доступ к ячейкам**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), который позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), представляющую все ячейки на листе.

Мы можем использовать коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), чтобы получить доступ к ячейкам на листе. Aspose.Cells для Python via .NET предоставляет три основных подхода к доступу к ячейкам на листе:

1. Использование имени ячейки.
2. Использование индекса строки и столбца ячейки.
1. Использование индекса ячейки в коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)

**ВАЖНО:** Мы отметили, что третий подход является самым быстрым, а первый - самым медленным. Разница в производительности между подходами очень мала, поэтому не стоит беспокоиться о снижении производительности, какой бы подход вы ни использовали.

### **Как получить объект Ячейки по имени ячейки**

Разработчики могут получить доступ к любой конкретной ячейке, передав ее имя ячейки в коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) в качестве индекса.

Если вы создаете пустой лист на старте, количество коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) равно нулю. Когда вы используете этот подход для доступа к ячейке, он будет проверять, существует ли эта ячейка в коллекции или нет. Если да, то возвращает объект ячейки в коллекции, в противном случае создает новый объект [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell), добавляет объект в коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) и затем возвращает объект. Этот подход является самым простым способом доступа к ячейке, если вы знакомы с Microsoft Excel, но он самый медленный по сравнению с другими подходами.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellName-1.py" >}}

### **Как получить объект Ячейки по индексу строки и столбца ячейки**

Разработчики могут получить доступ к любой конкретной ячейке, передав индексы ее строки и столбца в коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Этот подход работает так же, как и первый подход.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingRowAndColumnIndexOfCell-1.py" >}}

### **Как получить объект Ячейки по индексу ячейки в коллекции ячеек**

К ячейке также можно получить доступ, передав числовой индекс ячейки в коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

Если вы используете этот подход для доступа к ячейкам, может быть сгенерировано исключение, если числовой индекс ячейки находится вне диапазона. Этот подход является самым быстрым для доступа к ячейкам, но важно знать, что если вы используете этот подход для доступа к объекту ячейки, числовой индекс может измениться после добавления новых ячеек в коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Объекты ячеек в коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) внутренне сортируются по индексам строки и столбца.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-UsingCellIndexInCellsCollection-1.py" >}}

## **Как получить максимальный диапазон отображения листа**

Aspose.Cells для Python via .NET позволяет разработчикам получить доступ к максимальному диапазону отображения листа. Максимальный диапазон отображения - диапазон ячеек между первой и последней ячейкой с содержимым - полезен, когда вам нужно скопировать, выбрать или отобразить все содержимое листа в изображении.

Вы можете получить доступ к максимальному диапазону отображения листа с помощью [**Worksheet.cells.max_display_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/). В следующем примере кода показано, как получить доступ к свойству [**MaxDisplayRange**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/max_display_range/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AccessingCells-AccessingMaximumDisplayRangeofWorksheet-1.py" >}}
