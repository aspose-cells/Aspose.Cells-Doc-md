---
title: Избегайте пустой страницы в выходном PDF-файле, когда нечего печатать
type: docs
weight: 30
url: /ru/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Возможные сценарии использования**

Когда файл Excel пуст и пользователь сохраняет его в формате PDF с помощью Aspose.Cells, он отображает пустую страницу в выходном PDF-файле. Иногда такое поведение по умолчанию нежелательно. Aspose.Cells обеспечивает[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) имущества для решения этой проблемы. Если вы установите его как**ЛОЖЬ**, тогда[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)будет происходить всякий раз, когда в выходном PDF-файле нечего печатать.

## **Избегайте пустой страницы в выходном PDF-файле, когда нечего печатать**

Следующий пример кода создает пустую книгу, а затем сохраняет ее как выходной PDF-файл после установки[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) собственность как**ЛОЖЬ**. Поскольку в выходном PDF-файле нечего печатать,[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)происходит, как показано ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Исключение**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
