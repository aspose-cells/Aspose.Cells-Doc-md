---
title: Избегание пустой страницы в выходном PDF, когда нет ничего для печати
type: docs
weight: 30
url: /ru/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Возможные сценарии использования**

Когда файл Excel пустой, а пользователь сохраняет его в PDF, используя Aspose.Cells, в выходном PDF создается пустая страница. Иногда это поведение по умолчанию нежелательно. Aspose.Cells предоставляет свойство [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) для решения этой проблемы. Если вы установите его как **false**, то [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) возникнет в случае отсутствия чего-либо для печати в выходном PDF.

## **Избегание пустой страницы в выходном PDF, когда нет ничего для печати**

Приведенный ниже образец кода создает пустую книгу и затем сохраняет ее в формате PDF после установки свойства [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) в **false**. Поскольку в выходном PDF нет ничего для печати, [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) присутствует вот так.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Исключение**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
