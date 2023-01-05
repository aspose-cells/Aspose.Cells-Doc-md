---
title: Вставьте гиперссылки в Excel или OpenOffice
linktitle: Управление гиперссылками
type: docs
weight: 45
url: /ru/net/insert-hyperlinks-to-excel/
description: Как вставить гиперссылки в файл Excel с библиотекой Aspose.Cells без MS Excel.
---
{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя объектами. Все знакомы с использованием гиперссылок, особенно на веб-сайтах.
Используя Aspose.Cells, разработчики могут создавать различные типы гиперссылок в Microsoft файлах Excel. В этом разделе обсуждается, какие типы гиперссылок поддерживаются Aspose.Cells и как их можно использовать в наших файлах Excel.

{{% /alert %}} 
## **Добавление гиперссылок**
Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel либо с помощью API, либо с помощью электронных таблиц дизайнера (электронные таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие электронные таблицы).

 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Класс предоставляет различные методы для добавления различных гиперссылок в файлы Excel.
## **Добавление ссылки к URL-адресу**
[Рабочий лист](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс содержит[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) коллекция. Каждый элемент в[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) коллекция представляет собой[Гиперссылка](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) . Добавьте гиперссылки к URL-адресам, вызвав[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) коллекция[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) метод.[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)метод принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок
- URL-адрес, URL-адрес.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToURL-1.cs" >}}

{{% alert color="primary" %}} 

 В приведенном выше примере гиперссылка добавляется к URL-адресу в пустой ячейке.**А1**. В таких случаях, если ячейка пуста, URL-адрес также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пуста и добавлена гиперссылка, значение ячейки выглядит как обычный текст. Чтобы она выглядела как гиперссылка, примените к этой ячейке соответствующие параметры форматирования.

{{% /alert %}} 
## **Добавление ссылки на Cell в тот же файл**
 Можно добавить гиперссылки на ячейки в том же файле Excel, вызвав[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) коллекция[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) метод.[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)Метод работает как для внутренних, так и для внешних гиперссылок. Одна версия перегруженного метода принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToAnotherCell-1.cs" >}}
## **Добавление ссылки на внешний файл**
 Можно добавить гиперссылки на внешние файлы Excel, вызвав[Гиперссылки](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection) коллекция[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index) метод.[Добавлять](https://reference.aspose.com/cells/net/aspose.cells/hyperlinkcollection/methods/add/index)метод принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Hyperlinks-AddingLinkToExternalFile-1.cs" >}}

## **Предварительные темы**
- [Добавить гиперссылки на изображения](/cells/ru/net/add-image-hyperlinks/)
- [Определить тип гиперссылки](/cells/ru/net/detect-hyperlink-type/)
- [Редактирование гиперссылок рабочего листа](/cells/ru/net/editing-hyperlinks-of-worksheet/)
- [Получить гиперссылки в диапазоне](/cells/ru/net/get-hyperlinks-in-range/)

