---
title: Избегайте пустой страницы в выходном PDF-файле, когда нечего печатать
type: docs
weight: 30
url: /ru/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Возможные сценарии использования**

Когда файл Excel пуст и пользователь сохраняет его в формате PDF с помощью Aspose.Cells, он отображает пустую страницу в выходном PDF-файле. Иногда такое поведение по умолчанию нежелательно. Aspose.Cells обеспечивает[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) имущества для решения этой проблемы. Если вы установите его как**ЛОЖЬ**, тогда[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)будет происходить всякий раз, когда в выходном PDF-файле нечего печатать.

## **Избегайте пустой страницы в выходном PDF-файле, когда нечего печатать**

Следующий пример кода создает пустую книгу, а затем сохраняет ее в формате PDF после установки[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) собственность как**ЛОЖЬ**. Поскольку в выходном PDF-файле нечего печатать,[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)происходит, как показано ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Исключение**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
