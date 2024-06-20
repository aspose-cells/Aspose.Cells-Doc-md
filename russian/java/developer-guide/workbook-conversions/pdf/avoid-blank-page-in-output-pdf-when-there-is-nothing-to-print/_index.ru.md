---
title: Избегание пустой страницы в выходном PDF, когда нет ничего для печати
type: docs
weight: 30
url: /ru/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Возможные сценарии использования**

Когда файл Excel пустой, а пользователь сохраняет его в PDF, используя Aspose.Cells, в выходном PDF создается пустая страница. Иногда это поведение по умолчанию нежелательно. Aspose.Cells предоставляет свойство [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) для решения этой проблемы. Если вы установите его как **false**, то [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) возникнет в случае отсутствия чего-либо для печати в выходном PDF.

## **Избегание пустой страницы в выходном PDF, когда нет ничего для печати**

Следующий образец кода создает пустую книгу и затем сохраняет ее как выходной PDF после установки свойства [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) как **false**. Поскольку в выходном PDF нет ничего для печати, происходит [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException), как показано ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Исключение**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
