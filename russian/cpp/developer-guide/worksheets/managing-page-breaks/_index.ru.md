---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

Согласно определению, разрыв страницы — это место в потоке текста, где заканчивается одна страница и начинается следующая. Microsoft Excel позволяет пользователям добавлять разрывы страниц в любую выбранную ячейку рабочего листа.

Расположение ячейки, в которой добавлен разрыв страницы, страница заканчивается, а все остальные данные после разрыва страницы печатаются на следующей странице во время печати. Проще говоря, разрывы страниц делят ваш рабочий лист на несколько страниц в соответствии с вашими требованиями. Вы также можете добавлять разрывы страниц на свои рабочие листы во время выполнения, используя Aspose.Cells. Aspose.Cells позволяет разработчикам добавлять два типа разрывов страниц:

- Горизонтальный разрыв страницы
- Вертикальный разрыв страницы

В оставшейся части обсуждения мы опишем, как вы можете добавить горизонтальные или вертикальные разрывы страниц в свои рабочие листы, используя Aspose.Cells.

{{% /alert %}} 
## **Разрывы страниц**
 Aspose.Cells предоставляет класс[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) который представляет файл Excel.[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) класс содержит[Рабочие листы](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) учебный класс.[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)Класс предоставляет широкий спектр методов, используемых для управления рабочим листом. Чтобы добавить разрывы страниц, используйте[ДобавитьPageBreaks](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5f8dd5624b81e0ee2e7455f2b83380f6) метод[рабочий лист](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)учебный класс.
### **Добавление разрывов страниц**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks.cpp" >}}
