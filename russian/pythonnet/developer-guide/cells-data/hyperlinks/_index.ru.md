---
title: Вставка гиперссылок в Excel или OpenOffice
linktitle: Управление гиперссылками
type: docs
weight: 45
url: /ru/python-net/insert-hyperlinks-to-excel/
description: Как вставить гиперссылки в файл Excel с помощью библиотеки Aspose.Cells для Python via .NET без MS Excel.
keywords: Python Excel Library, Python Insert Hyperlinks into Excel, Python Add or Insert Hyperlinks, Python Add or Insert a link to a URL, Python Add or Insert a Link to a Cell, Python Add a Link to an External File
---

{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя сущностями. Каждый знаком с использованием гиперссылок, особенно на веб-сайтах.
Используя Aspose.Cells для Python via .NET, разработчики могут создавать различные виды гиперссылок в файлах Microsoft Excel. В этой теме обсуждается, какие типы гиперссылок поддерживаются Aspose.Cells для Python via .NET и как они могут быть использованы в наших файлах Excel.

{{% /alert %}} 
## **Как добавить гиперссылки**
Aspose.Cells для Python via .NET позволяет разработчикам добавлять гиперссылки в файлы Excel либо с помощью API, либо с помощью электронных таблиц дизайнера (электронные таблицы, в которых гиперссылки создаются вручную, и используется Aspose.Cells для Python via .NET для их импорта в другие электронные таблицы).

Aspose.Cells для Python via .NET предоставляет класс [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), позволяющую получить доступ к каждой электронной таблице в файле Excel. Электронная таблица представлена классом [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет различные методы для добавления различных гиперссылок в файлы Excel.

## **Как добавить ссылку на URL**
Класс [Worksheet](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) содержит коллекцию [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). Каждый элемент коллекции [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/) представляет [Hyperlink](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink). Добавляйте гиперссылки на URL, вызывая метод [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) коллекции [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). Метод [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок
- URL-адрес, адрес URL.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToURL-1.py" >}}

{{% alert color="primary" %}} 

В приведенном выше примере гиперссылка добавляется в URL в пустую ячейку **A1**. В таких случаях, если ячейка пустая, то адрес URL также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пустая и в нее добавляется гиперссылка, значение ячейки выглядит как обычный текст. Чтобы сделать его похожим на гиперссылку, примените соответствующие настройки форматирования к этой ячейке.

{{% /alert %}} 

## **Как добавить ссылку на ячейку в том же файле**
Возможно добавление гиперссылок в ячейки в том же файле Excel, вызывая метод [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) коллекции [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). Метод [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) работает как для внутренних, так и для внешних гиперссылок. Одна из перегруженных версий метода принимает следующие параметры:

- Имя ячейки, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToAnotherCell-1.py" >}}

## **Как добавить ссылку на внешний файл**
Возможно добавление гиперссылок на внешние файлы Excel, вызывая метод [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) коллекции [hyperlinks](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/hyperlinks/). Метод [add](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlinkcollection/add/#int-int-int-int-str) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Hyperlinks-AddingLinkToExternalFile-1.py" >}}

## **Продвинутые темы**
- [Добавление гиперссылок на изображения](/cells/ru/python-net/add-image-hyperlinks/)
- [Определение типа гиперссылки](/cells/ru/python-net/detect-hyperlink-type/)
- [Редактирование гиперссылок в рабочем листе](/cells/ru/python-net/editing-hyperlinks-of-worksheet/)
- [Получение гиперссылок в диапазоне](/cells/ru/python-net/get-hyperlinks-in-range/)

