---
title: Управление разрывами страниц
type: docs
weight: 30
url: /ru/java/managing-page-breaks/
---
{{% alert color="primary" %}}

Разрыв страницы — это место в тексте, где заканчивается одна страница и начинается следующая. Microsoft Excel может добавлять разрывы страниц в любую выбранную ячейку на листе.
Страница заканчивается в ячейке, где добавлен разрыв страницы, и все данные после разрыва страницы печатаются на следующей странице. Проще говоря, страница разбивает рабочие листы на несколько страниц. Также можно добавить разрывы страниц на рабочие листы во время выполнения, используя Aspose.Cells. Aspose.Cells поддерживает два типа разрывов страниц:

- горизонтальный
- вертикальный.

В этой статье описывается, как добавить горизонтальные или вертикальные разрывы страниц на листы с помощью Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells и разрывы страниц**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)класс, который предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы добавить разрывы страниц, используйте[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[**ГоризонтальныйPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) и[**Вертикальные разрывы страниц**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)характеристики.

[**ГоризонтальныйPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) и[**Вертикальные разрывы страниц**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)свойства на самом деле являются коллекциями, которые могут содержать несколько разрывов страниц. Каждая коллекция содержит несколько методов управления горизонтальными и вертикальными разрывами страниц. Как используются эти методы, обсуждается ниже.

## **Добавление разрывов страниц**

 Чтобы добавить разрыв страницы на листе, вставьте вертикальные и горизонтальные разрывы страниц в указанной ячейке, вызвав метод[**ГоризонтальныйPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) и[**Вертикальные разрывы страниц**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) коллекции**Добавлять** методы. Каждый**Добавлять**Метод принимает имя ячейки, в которую должен быть добавлен разрыв страницы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

В режимах предварительного просмотра разрывов страниц или предварительного просмотра печати вы можете увидеть, как работают эти разрывы страниц.

{{% /alert %}}

## **Удаление всех разрывов страниц**

 Чтобы удалить все разрывы страниц на листе, вызовите метод[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) и[**ВертикальнаяPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) коллекции**Прозрачный**методы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **Удаление определенного разрыва страницы**

 Чтобы удалить определенный разрыв страницы на листе, вызовите метод[**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) и[**ВертикальнаяPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) коллекции**удалить в** методы. Каждый**удалить в**Метод возьмет индекс разрыва страницы, который нужно удалить.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**Важно знать** : Когда вы устанавливаете соответствие свойствам страницы (т.[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) и[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) в настройках параметров страницы затрагиваются параметры разрыва страницы, поэтому при печати листа параметры разрыва страницы не учитываются, хотя они все еще существуют в файле.

{{% /alert %}}
