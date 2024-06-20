---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/java/managing-page-breaks/
---

{{% alert color="primary" %}}

Разрыв страницы — это место в тексте, где заканчивается одна страница, и начинается следующая. В Microsoft Excel можно добавить разрывы страниц в любую выбранную ячейку на листе.
Страница заканчивается на ячейке, в которой добавлен разрыв страницы, и все данные после разрыва печатаются на следующей странице. Проще говоря, разрывы страниц разделяют листы на несколько страниц. Также возможно добавление разрывов страниц на листы во время выполнения с помощью Aspose.Cells. Aspose.Cells поддерживает два вида разрывов страниц:

- горизонтальный
- вертикальный.

В данной статье описывается, как добавлять горизонтальные или вертикальные разрывы страниц в листы с помощью Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells и разрывы страниц**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), позволяющий получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet), который предоставляет широкий набор свойств и методов для управления листами. Чтобы добавить разрывы страниц, используйте свойства [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) и [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Свойства {0} и {1] фактически являются коллекциями, которые могут содержать несколько разрывов страниц. Каждая коллекция содержит несколько методов для управления горизонтальными и вертикальными разрывами страниц. Как использовать эти методы, рассматривается ниже.

## **Добавление разрывов страниц**

Чтобы добавить разрыв страницы на листе, вставьте вертикальный и горизонтальный разрывы в указанную ячейку, вызвав методы **Add** коллекций [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) и [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). Каждый метод **Add** принимает имя ячейки, в которой нужно добавить разрыв страницы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

В режиме предварительного просмотра разрывов страниц или предварительного просмотра печати можно увидеть, как работают эти разрывы страниц.

{{% /alert %}}

## **Очистка всех разрывов страниц**

Для очистки всех разрывов страниц на листе вызовите методы **Clear** коллекций [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) и [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Удаление определенного разрыва страницы**

Для удаления определенного разрыва страницы на листе вызовите методы **removeAt** коллекций [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) и [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). Каждый метод **removeAt** примет индекс разрыва страницы, который нужно удалить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Важно знать**: При установке параметров подгонки к странице (то есть [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) и [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) в настройках формата страницы, настройки разрывов страниц на них влияют, поэтому, если вы печатаете лист, настройки разрывов страниц не учитываются, хотя они все еще существуют в файле.

{{% /alert %}}
