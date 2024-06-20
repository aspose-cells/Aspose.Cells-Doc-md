---
title: Вставка гиперссылок в Excel или OpenOffice
linktitle: Управление гиперссылками
type: docs
weight: 160
url: /ru/java/insert-hyperlinks-to-excel/
---

## **Добавление гиперссылок для связи данных**
{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя сущностями. Каждый знаком с использованием гиперссылок, особенно на веб-сайтах.

Используя Aspose.Cells, разработчики могут создавать различные виды гиперссылок в файлах Microsoft Excel. В этой теме обсуждается, какие типы гиперссылок поддерживает Aspose.Cells и как они могут быть использованы в наших файлах Excel.

{{% /alert %}} 
## **Добавление гиперссылок**
С помощью Aspose.Cells можно добавлять три типа гиперссылок в ячейку:

- [Добавление ссылки на URL](/cells/ru/java/working-with-hyperlinks-to-link-data/).
- [Добавление ссылки на другую ячейку в том же файле](/cells/ru/java/working-with-hyperlinks-to-link-data/).
- [Добавление ссылки на внешний файл](/cells/ru/java/working-with-hyperlinks-to-link-data/).

Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel с помощью API или [дизайнерских электронных таблиц](/cells/ru/java/what-is-a-designer-spreadsheet/) (электронные таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие электронные таблицы).

Aspose.Cells создает класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет различные методы для добавления различных гиперссылок в файлы Excel.
## **Добавление ссылки на URL**
Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) содержит коллекцию [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). Каждый элемент коллекции [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) представляет [Hyperlink](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink). Чтобы добавить гиперссылки на URL, вызовите метод [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) коллекции [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Hyperlinks). Метод [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL-адрес, адрес URL.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURL-AddingLinkToURL.java" >}}


В приведенном выше примере гиперссылка добавляется на URL в пустую ячейку **A1**. В таких случаях, если ячейка пуста, то адрес URL также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пуста и в нее добавлена гиперссылка, значение ячейки выглядит как обычный текст. Чтобы сделать его похожим на гиперссылку, примените соответствующие параметры форматирования на эту ячейку.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToURLNotEmpty-AddingLinkToURLNotEmpty.java" >}}



## **Добавление ссылки на ячейку в том же файле**
Возможно добавить гиперссылки на ячейки в том же файле Excel, вызвав метод [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) коллекции [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection). Метод [Add ](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) работает как для внутренних, так и для внешних гиперссылок. Одна из версий перегруженного метода принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToAnotherCell-AddingLinkToAnotherCell.java" >}}



## **Добавление ссылки на внешний файл**
Возможно добавить гиперссылки на внешние файлы Excel, вызвав метод [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) коллекции [Hyperlinks](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection) . Метод [Add](https://reference.aspose.com/cells/java/com.aspose.cells/HyperlinkCollection#add\(int,%20int,%20int,%20int,%20java.lang.String\)) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingLinkToExternalFile-AddingLinkToExternalFile.java" >}}

## **Продвинутые темы**
- [Добавление гиперссылок на изображения](/cells/ru/java/add-image-hyperlinks/)
- [Определение типа гиперссылки](/cells/ru/java/detect-hyperlink-type/)
- [Редактирование гиперссылок в рабочем листе](/cells/ru/java/editing-hyperlinks-of-worksheet/)
- [Получение гиперссылок в диапазоне](/cells/ru/java/get-hyperlinks-in-range/)


