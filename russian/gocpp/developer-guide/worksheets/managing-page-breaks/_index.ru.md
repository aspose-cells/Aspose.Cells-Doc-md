---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/go-cpp/managing-page-breaks/
---

{{% alert color="primary" %}}

Согласно определению, перерыв страницы - это место в текучем тексте, где заканчивается одна страница, и начинается другая. Microsoft Excel позволяет пользователям добавлять перерывы страницы в любую выбранную ячейку листа.

Местоположение ячейки, куда добавлен разрыв страницы, страница завершается, и вся остальная информация после разрыва страницы печатается на следующей странице во время печати. Простыми словами, разрывы страниц разделяют рабочий лист на несколько страниц в соответствии с вашими спецификациями. Вы также можете добавлять разрывы страниц в свои рабочие листы во время выполнения с помощью Aspose.Cells. Aspose.Cells позволяет разработчикам добавлять два вида разрывов страниц:

- Горизонтальный перерыв страницы
- Вертикальный перерыв страницы

В остальной части обсуждения мы опишем, как вы можете добавить горизонтальные или вертикальные перерывы страниц в свои листы с использованием Aspose.Cells.

{{% /alert %}}

## **Разрывы страниц**

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook), который представляет файл Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection), которая позволяет получать доступ к каждому листу в файле.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) предоставляет широкий набор методов для управления листом. Чтобы добавить разрывы страниц, используйте метод [AddPageBreaks](https://reference.aspose.com/cells/go-cpp/worksheet/addpagebreaks) класса [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/).

### **Добавление разрывов страниц**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingPageBreaks.go" >}}
