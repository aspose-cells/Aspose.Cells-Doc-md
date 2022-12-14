---
title: Вставьте гиперссылки в Excel или OpenOffice
linktitle: Управление гиперссылками
type: docs
weight: 160
url: /ru/java/insert-hyperlinks-to-excel/
---
## **Добавление гиперссылок к данным связи**
{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя объектами. Все знакомы с использованием гиперссылок, особенно на веб-сайтах.

Используя Aspose.Cells, разработчики могут создавать различные типы гиперссылок в Microsoft файлах Excel. В этом разделе обсуждается, какие типы гиперссылок поддерживаются Aspose.Cells и как их можно использовать в наших файлах Excel.

{{% /alert %}} 
## **Добавление гиперссылок**
С помощью Aspose.Cells в ячейку можно добавить три типа гиперссылок:

- [Добавление ссылки к URL](/cells/ru/java/working-with-hyperlinks-to-link-data/).
- [Добавление ссылки на другую ячейку в том же файле](/cells/ru/java/working-with-hyperlinks-to-link-data/).
- [Добавление ссылки на внешний файл](/cells/ru/java/working-with-hyperlinks-to-link-data/).

 Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel либо с помощью API, либо[дизайнерские таблицы](/cells/ru/java/what-is-a-designer-spreadsheet/)(электронные таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие электронные таблицы).

Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет собой файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Класс предоставляет различные методы для добавления различных гиперссылок в файлы Excel.
## **Добавление ссылки к URL-адресу**
[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) класс содержит[Гиперссылки](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) коллекция. Каждый элемент в[Гиперссылки](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) коллекция представляет собой[Гиперссылка](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) . Добавьте гиперссылки к URL-адресам, вызвав[Гиперссылки](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks) коллекция[Добавлять](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) ) метод.[Добавлять](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов этого диапазона гиперссылок
- URL-адрес, URL-адрес.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


 В приведенном выше примере гиперссылка добавляется к URL-адресу в пустой ячейке.**А1**В таких случаях, если ячейка пуста, URL-адрес также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пуста и добавлена гиперссылка, значение ячейки выглядит как обычный текст. Чтобы она выглядела как гиперссылка, примените к этой ячейке соответствующие параметры форматирования.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Добавление ссылки на Cell в тот же файл**
 Можно добавить гиперссылки на ячейки в том же файле Excel, вызвав[Гиперссылки](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) коллекция[Добавлять](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) ) метод.[Добавлять](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) метод работает как для внутренних, так и для внешних гиперссылок. Одна версия перегруженного метода принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Добавление ссылки на внешний файл**
 Можно добавить гиперссылки на внешние файлы Excel, вызвав[Гиперссылки](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) коллекция[Добавлять](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\) ) метод.[Добавлять](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) принимает следующие параметры:

- Cell имя, имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Предварительные темы**
- [Добавить гиперссылки на изображения](/cells/ru/java/add-image-hyperlinks/)
- [Определить тип гиперссылки](/cells/ru/java/detect-hyperlink-type/)
- [Редактирование гиперссылок рабочего листа](/cells/ru/java/editing-hyperlinks-of-worksheet/)
- [Получить гиперссылки в диапазоне](/cells/ru/java/get-hyperlinks-in-range/)


