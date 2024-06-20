---
title: Избегание пустой страницы в выходном PDF, когда нет ничего для печати
type: docs
weight: 30
url: /ru/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Узнайте, как избежать пустой страницы в выходном PDF, когда нет ничего для печати, с помощью Aspose.Cells для Python via .NET API.
keywords: Python избегает пустой страницы в выходном PDF, когда нет ничего для печати
---

## **Возможные сценарии использования**

Когда файл Excel пуст, и пользователь сохраняет его в формате PDF с использованием Aspose.Cells для Python via .NET, в выходном PDF появляется пустая страница. Иногда это поведение по умолчанию нежелательно. Aspose.Cells для Python via .NET предоставляет свойство [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) для решения этой проблемы. Если установить его как **false**, то произойдет [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/), когда в выходном PDF нет ничего для печати.

## **Избегание пустой страницы в выходном PDF, когда нет ничего для печати**

Приведенный ниже образец кода создает пустую книгу и затем сохраняет ее в формате PDF после установки свойства [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) в **false**. Поскольку в выходном PDF нет ничего для печати, [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) присутствует вот так.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **Исключение**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
