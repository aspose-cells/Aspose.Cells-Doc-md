---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Согласно определению, разрыв страницы — это место в потоке текста, где заканчивается одна страница и начинается следующая. Microsoft Excel позволяет пользователям добавлять разрывы страниц в любую выбранную ячейку листа.

Местоположение ячейки, в которой добавляется разрыв страницы, страница заканчивается, а все остальные данные после разрыва страницы печатаются на следующей странице во время печати. Проще говоря, разрывы страниц делят ваш лист на несколько страниц в соответствии с вашими требованиями. Вы также можете добавлять разрывы страниц в свои рабочие листы во время выполнения, используя Aspose.Cells. Aspose.Cells позволяет разработчикам добавлять два типа разрывов страниц:

- Горизонтальный разрыв страницы
- Вертикальный разрыв страницы

В оставшейся части обсуждения мы опишем, как можно добавить горизонтальные или вертикальные разрывы страниц в ваши рабочие листы, используя Aspose.Cells.

{{% /alert %}} 
##  **Разрывы страниц**
 Aspose.Cells предоставляет класс[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) который представляет файл Excel.[Рабочая тетрадь](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)коллекция, которая обеспечивает доступ к каждому листу в файле Excel.

Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) сорт.[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)Класс предоставляет широкий спектр методов, используемых для управления листом. Чтобы добавить разрывы страниц, используйте[Добавить PageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) метод[Рабочий лист](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)сорт.
###  **Добавление разрывов страниц**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
