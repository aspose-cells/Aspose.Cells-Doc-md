---
title: Избегайте пустой страницы в выводе PDF, когда нечего печатать
type: docs
weight: 30
url: /ru/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Узнайте, как избежать пустой страницы в выводе PDF, когда нечего печатать с помощью Aspose.Cells for Python via .NET API.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **Возможные сценарии использования**

Когда файл Excel пуст и пользователь сохраняет его по адресу PDF, используя Aspose.Cells for Python via .NET, он отображает пустую страницу в выходных данных PDF. Иногда такое поведение по умолчанию нежелательно. Aspose.Cells for Python via .NET обеспечивает[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)имущество для решения этой проблемы. Если вы установите значение *false**, то[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)будет происходить всякий раз, когда в выводе PDF нечего печатать.

##  **Избегайте пустой страницы в выводе PDF, когда нечего печатать**

Следующий пример кода создает пустую книгу, а затем сохраняет ее под номером PDF после установки[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)свойство как *false**. Поскольку в выводе PDF нечего печатать,[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)происходит, как показано ниже.

##  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **Исключение**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
