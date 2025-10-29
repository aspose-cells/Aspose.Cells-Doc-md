---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

Согласно определению, перерыв страницы - это место в текучем тексте, где заканчивается одна страница, и начинается другая. Microsoft Excel позволяет пользователям добавлять перерывы страницы в любую выбранную ячейку листа.

Местоположение ячейки, куда добавлен разрыв страницы, страница завершается, и вся остальная информация после разрыва страницы печатается на следующей странице во время печати. Простыми словами, разрывы страниц разделяют рабочий лист на несколько страниц в соответствии с вашими спецификациями. Вы также можете добавлять разрывы страниц в свои рабочие листы во время выполнения с помощью Aspose.Cells. Aspose.Cells позволяет разработчикам добавлять два вида разрывов страниц:

- Горизонтальный перерыв страницы
- Вертикальный перерыв страницы

В остальной части обсуждения мы опишем, как вы можете добавить горизонтальные или вертикальные перерывы страниц в свои листы с использованием Aspose.Cells.

{{% /alert %}} 
## **Разрывы страниц**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook), представляющий файл Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection), позволяющую получать доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет широкий спектр методов, используемых для управления рабочим листом. Чтобы добавить разрывы страниц, используйте метод [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) класса [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).
### **Добавление разрывов страниц**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
