---
title: Вставка гиперссылок в Excel или OpenOffice
linktitle: Управление гиперссылками
type: docs
weight: 45
url: /ru/nodejs-cpp/insert-hyperlinks-to-excel/
description: Как вставлять гиперссылки в файл Excel с помощью библиотеки Aspose.Cells без MS Excel, используя Node.js через C++.
keywords: Вставка гиперссылок в Excel Node.js через C++, добавление или вставка гиперссылок Node.js через C++, добавление или вставка ссылки на URL Node.js через C++, добавление или вставка ссылки в ячейку Node.js через C++, добавление ссылки на внешний файл Node.js через C++
---

{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя сущностями. Каждый знаком с использованием гиперссылок, особенно на веб-сайтах.
Используя Aspose.Cells, разработчики могут создавать различные виды гиперссылок в файлах Microsoft Excel. В этой теме обсуждается, какие типы гиперссылок поддерживает Aspose.Cells и как они могут быть использованы в наших файлах Excel.

{{% /alert %}} 

## **Добавление гиперссылок**
 Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel либо с помощью API, либо через дизайнерские таблицы (таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие таблицы).

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection), который обеспечивает доступ ко всем листам в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет различные методы для добавления гиперссылок в файлы Excel.
## **Добавление ссылки на URL**
Класс [Worksheet](https://reference.aspose.com/cells/nodejs-cpp/worksheet) содержит коллекцию [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--). Каждый элемент в коллекции [getHyperlinks()](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--) представляет [Hyperlink](https://reference.aspose.com/cells/nodejs-cpp/hyperlink). Добавляйте гиперссылки на URL, вызывая метод [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-). Метод [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL-адрес, адрес URL.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToURL.js" >}}


{{% alert color="primary" %}} 

В приведенном выше примере гиперссылка добавляется в URL в пустую ячейку **A1**. В таких случаях, если ячейка пустая, то адрес URL также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пустая и в нее добавляется гиперссылка, значение ячейки выглядит как обычный текст. Чтобы сделать его похожим на гиперссылку, примените соответствующие настройки форматирования к этой ячейке.

{{% /alert %}} 
## **Добавление ссылки на ячейку в том же файле**
Можно добавлять гиперссылки в ячейки в одном и том же файле Excel, вызывая метод [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) коллекции [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). Этот метод работает как для внутренних, так и для внешних гиперссылок. Один из вариантов перегруженного метода принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToCell.js" >}}


## **Добавление ссылки на внешний файл**
Можно добавлять гиперссылки на внешние файлы Excel, вызывая метод [add](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection/#add-string-number-number-string-) коллекции [Hyperlinks](https://reference.aspose.com/cells/nodejs-cpp/hyperlinkcollection). Этот метод принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-AddLinkToExternalFile.js" >}}



## **Продвинутые темы**
- [Добавление гиперссылок на изображения](/cells/ru/nodejs-cpp/add-image-hyperlinks/)
- [Определение типа гиперссылки](/cells/ru/nodejs-cpp/detect-hyperlink-type/)
- [Редактирование гиперссылок в рабочем листе](/cells/ru/nodejs-cpp/editing-hyperlinks-of-worksheet/)
- [Получение гиперссылок в диапазоне](/cells/ru/nodejs-cpp/get-hyperlinks-in-range/)

{{< app/cells/assistant language="nodejs-cpp" >}}
