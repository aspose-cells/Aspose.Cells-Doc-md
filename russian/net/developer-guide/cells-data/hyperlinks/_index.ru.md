---
title: Вставка гиперссылок в Excel или OpenOffice
linktitle: Управление гиперссылками
type: docs
weight: 45
url: /ru/net/insert-hyperlinks-to-excel/
description: Как вставить гиперссылки в файл Excel с библиотекой Aspose.Cells без MS Excel.
keywords: Insert Hyperlinks into Excel, Add or Insert Hyperlinks, Add or Insert link to a URL, Add or Insert a Link to a Cell, Add a Link to an External File
---
{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя объектами. Все знакомы с использованием гиперссылок, особенно на веб-сайтах.
Используя Aspose.Cells, разработчики могут создавать различные виды гиперссылок в файлах Excel Microsoft. В этой теме обсуждаются, какие типы гиперссылок поддерживаются Aspose.Cells и как их можно использовать в наших файлах Excel.

{{% /alert %}} 
##  **Добавление гиперссылок**
Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel с помощью электронных таблиц API или дизайнера (таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для импорта их в другие электронные таблицы).

 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[Рабочий ЛистКоллекция](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)это обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[Рабочий лист](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Класс предоставляет различные методы для добавления различных гиперссылок в файлы Excel.
##  **Добавление ссылки в URL**
[Рабочий лист](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс содержит[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) коллекция. Каждый предмет в[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) коллекция представляет собой[Гиперссылка](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Добавьте гиперссылки к URL-адресам, вызвав[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) коллекция[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) метод.[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)метод принимает следующие параметры:

- Cell name — имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк — количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, URL-адрес.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

В приведенном выше примере гиперссылка добавляется к URL-адресу в пустой ячейке *A1**. В таких случаях, если ячейка пуста, URL-адрес также добавляется к этой пустой ячейке в качестве ее значения. Если ячейка не пуста и добавлена гиперссылка, значение ячейки выглядит как обычный текст. Чтобы она выглядела как гиперссылка, примените к этой ячейке соответствующие параметры форматирования.

{{% /alert %}} 
##  **Добавление ссылки на Cell в тот же файл**
 К ячейкам одного и того же файла Excel можно добавлять гиперссылки, вызвав метод[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) коллекция[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) метод.[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)метод работает как для внутренних, так и для внешних гиперссылок. Одна версия перегруженного метода принимает следующие параметры:

- Cell name — имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк — количество строк в этом диапазоне гиперссылок.
- Количество столбцов — количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
##  **Добавление ссылки на внешний файл**
 Можно добавить гиперссылки во внешние файлы Excel, вызвав команду[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) коллекция[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) метод.[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)метод принимает следующие параметры:

- Cell name — имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк — количество строк в этом диапазоне гиперссылок.
- Количество столбцов — количество столбцов в этом диапазоне гиперссылок.
- URL-адрес, адрес цели, внешний файл Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

##  **Предварительные темы**
- [Добавить гиперссылки на изображения](/cells/ru/net/add-image-hyperlinks/)
- [Определить тип гиперссылки](/cells/ru/net/detect-hyperlink-type/)
- [Редактирование гиперссылок рабочего листа](/cells/ru/net/editing-hyperlinks-of-worksheet/)
- [Получить гиперссылки в диапазоне](/cells/ru/net/get-hyperlinks-in-range/)

