---
title: Вставка гиперссылок в Excel или OpenOffice с помощью Golang через C++
linktitle: Управление гиперссылками
type: docs
weight: 45
url: /ru/go-cpp/insert-hyperlinks-to-excel/
description: Как вставить гиперссылки в файл Excel с помощью библиотеки Aspose.Cells без MS Excel на C++.
keywords: Вставить гиперссылки в Excel, Добавить или вставить гиперссылки, Добавить или вставить ссылку на URL, Добавить или вставить ссылку в ячейку, Добавить ссылку на внешний файл
---

{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя сущностями. Каждый знаком с использованием гиперссылок, особенно на веб-сайтах.
Используя Aspose.Cells, разработчики могут создавать различные виды гиперссылок в файлах Microsoft Excel. В этой теме обсуждается, какие типы гиперссылок поддерживает Aspose.Cells и как они могут быть использованы в наших файлах Excel.

{{% /alert %}} 

## **Добавление гиперссылок**
 Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel либо с помощью API, либо через дизайнерские таблицы (таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие таблицы).

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) содержит [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), который позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Этот класс предоставляет различные методы для добавления различных гиперссылок в файлы Excel.

## **Добавление ссылки на URL**
Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) содержит коллекцию [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/). Каждый элемент в коллекции [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) представляет [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Добавляйте гиперссылки на URL, вызывая метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) коллекции [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL-адрес, адрес URL.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks.go" >}}
{{% alert color="primary" %}} 

В приведенном выше примере гиперссылка добавляется в URL в пустую ячейку **A1**. В таких случаях, если ячейка пустая, то адрес URL также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пустая и в нее добавляется гиперссылка, значение ячейки выглядит как обычный текст. Чтобы сделать его похожим на гиперссылку, примените соответствующие настройки форматирования к этой ячейке.

{{% /alert %}} 

## **Добавление ссылки на ячейку в том же файле**
Можно добавить гиперссылки в ячейки того же файла Excel, вызывая метод [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) коллекции [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/). Метод [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) работает как для внутренних, так и для внешних гиперссылок. Одна из версий переопределенного метода принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-1.go" >}}
## **Добавление ссылки на внешний файл**
Можно добавлять гиперссылки во внешние файлы Excel, вызывая метод [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) коллекции [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/). Метод [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Hyperlinks-2.go" >}}
## **Продвинутые темы**
- [Добавление гиперссылок на изображения](/cells/ru/cpp/add-image-hyperlinks/)
- [Определение типа гиперссылки](/cells/ru/cpp/detect-hyperlink-type/)
- [Редактирование гиперссылок в рабочем листе](/cells/ru/cpp/editing-hyperlinks-of-worksheet/)
- [Получение гиперссылок в диапазоне](/cells/ru/cpp/get-hyperlinks-in-range/)
