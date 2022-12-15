---
title: Печать рабочих тетрадей
type: docs
weight: 20
url: /ru/java/printing-workbooks/
description: Как печатать листы и книги с помощью Java. В этой статье представлен код Java для печати листов и книг с помощью Aspose.Cells for Java API.
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

Этот документ предназначен для того, чтобы дать разработчикам представление (в компактной форме) о том, как печатать электронные таблицы.

{{% /alert %}}

## Сценарий использования

После того, как вы закончите создание электронной таблицы, вы, вероятно, захотите распечатать бумажную копию листа для своих нужд. Когда вы печатаете, MS Excel предполагает, что вы хотите напечатать всю область рабочего листа, если вы не укажете свой выбор. На следующем снимке экрана показано диалоговое окно для печати книги с помощью Excel.

![дело:изображение_альтернативный_текст](printing-workbooks_1.png)

**Фигура:** Диалоговое окно печати

## Печать рабочих книг с использованием Aspose.Cells

 Aspose.Cells for Java обеспечивает[**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) ) метод[**Листрендеринг**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) учебный класс. С помощью[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)), вы можете указать имя принтера, а также имя задания на печать.

## Образец кода

### Распечатать выбранный рабочий лист

 Следующий фрагмент кода демонстрирует использование[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) для печати выбранного рабочего листа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Распечатать всю книгу

 Вы также можете использовать[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) ) для печати всей книги. Следующий фрагмент кода демонстрирует использование[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) для печати всей книги.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Статьи по Теме

- [Укажите имя задания или документа при печати с помощью Aspose.Cells.](/cells/ru/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
