---
title: Вставка гиперссылок в Excel или OpenOffice
linktitle: Управление гиперссылками
type: docs
weight: 45
url: /ru/net/insert-hyperlinks-to-excel/
description: Как вставить гиперссылки в файл Excel с помощью библиотеки Aspose.Cells без MS Excel.
keywords: Вставить гиперссылки в Excel, Добавить или вставить гиперссылки, Добавить или вставить ссылку на URL, Добавить или вставить ссылку в ячейку, Добавить ссылку на внешний файл
---

{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя сущностями. Каждый знаком с использованием гиперссылок, особенно на веб-сайтах.
Используя Aspose.Cells, разработчики могут создавать различные виды гиперссылок в файлах Microsoft Excel. В этой теме обсуждается, какие типы гиперссылок поддерживает Aspose.Cells и как они могут быть использованы в наших файлах Excel.

{{% /alert %}} 
## **Добавление гиперссылок**
Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel, либо с помощью API, либо в дизайнерских электронных таблицах (таблицах, в которых гиперссылки создаются вручную, и Aspose.Cells используется для их импорта в другие электронные таблицы).

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), который позволяет получить доступ к каждому листу Excel-файла. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет различные методы для добавления гиперссылок в файлы Excel.
## **Добавление ссылки на URL**
Класс [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet) содержит коллекцию [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks). Каждый элемент в коллекции [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) представляет [Hyperlink](https://reference.aspose.com/cells/net/aspose.cells/hyperlink). Добавляйте гиперссылки на URL, вызывая метод [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) коллекции [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). Метод [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок
- URL-адрес, адрес URL.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

В приведенном выше примере гиперссылка добавляется в URL в пустую ячейку **A1**. В таких случаях, если ячейка пустая, то адрес URL также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пустая и в нее добавляется гиперссылка, значение ячейки выглядит как обычный текст. Чтобы сделать его похожим на гиперссылку, примените соответствующие настройки форматирования к этой ячейке.

{{% /alert %}} 
## **Добавление ссылки на ячейку в том же файле**
Возможно добавить гиперссылки к ячейкам в том же файле Excel, вызывая метод [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) коллекции [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection). Метод [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) работает как для внутренних, так и для внешних гиперссылок. Одна из перегруженных версий метода принимает следующие параметры:

- Имя ячейки, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Добавление ссылки на внешний файл**
Вы можете добавлять гиперссылки на внешние файлы Excel, вызывая метод [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) коллекции [Hyperlinks](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) . Метод [Add](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Продвинутые темы**
- [Добавление гиперссылок на изображения](/cells/ru/net/add-image-hyperlinks/)
- [Определение типа гиперссылки](/cells/ru/net/detect-hyperlink-type/)
- [Редактирование гиперссылок в рабочем листе](/cells/ru/net/editing-hyperlinks-of-worksheet/)
- [Получение гиперссылок в диапазоне](/cells/ru/net/get-hyperlinks-in-range/)

{{< app/cells/assistant language="csharp" >}}
