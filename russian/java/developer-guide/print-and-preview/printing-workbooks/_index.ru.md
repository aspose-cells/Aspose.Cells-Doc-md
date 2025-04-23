---
title: Печать книг
type: docs
weight: 20
url: /ru/java/printing-workbooks/
description: Как распечатать рабочие листы и книгу с помощью Java. Эта статья предоставляет код на Java для печати рабочих листов и книги с помощью Aspose.Cells for Java API.
keywords: печать рабочих книг, печать листов книги, печать листов рабочих книг, печать рабочей книги, печать рабочей книги на Java, печать листов книги на Java, печать книги Excel на Java, печать листа Excel на Java, печать книги, печать листа
---

{{% alert color="primary" %}}

Этот документ предназначен для обеспечения разработчиков пониманием (компактным образом) того, как печатать электронные таблицы.

{{% /alert %}}

## Сценарий использования

После того, как вы закончите создание таблицы, вам, вероятно, захочется распечатать бумажную копию листа по вашей потребности. При печати MS Excel предполагает, что вы хотите распечатать всю область листа, если не указано другое. На следующем снимке экрана показан диалоговый блок для печати книги с Excel.

![todo:image_alt_text](printing-workbooks_1.png)

**Рисунок:** Диалоговое окно печати

## Печать рабочих книг с использованием Aspose.Cells

Aspose.Cells for Java предоставляет метод [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) класса [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). Используя метод [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-), вы можете указать имя принтера, а также имя задания на печать.

## Образец кода

### Печать выбранного листа

Нижеприведенный фрагмент кода демонстрирует использование метода [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) для печати выбранного листа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Печать всей книги

Вы также можете использовать метод [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) для печати всей книги. Нижеприведенный фрагмент кода демонстрирует использование метода [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) для печати всей книги.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Связанные статьи

- [Укажите название задания или документа при печати с помощью Aspose.Cells](/cells/ru/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="java" >}}
