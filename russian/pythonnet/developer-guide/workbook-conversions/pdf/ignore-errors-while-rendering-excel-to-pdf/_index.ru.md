---
title: Игнорировать ошибки при рендеринге Excel по номеру PDF
type: docs
weight: 80
url: /ru/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Узнайте, как игнорировать ошибки при рендеринге Excel в PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **Возможные сценарии использования**

 Иногда при преобразовании файла Excel в PDF возникают ошибки или исключения, и процесс преобразования завершается. Вы можете игнорировать все такие ошибки в процессе преобразования, используя команду[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)свойство. Таким образом, процесс преобразования завершится гладко, без каких-либо ошибок или исключений, но может произойти потеря данных. Поэтому используйте это свойство только в том случае, если потеря данных для вас не критична.

##  **Игнорировать ошибки при рендеринге Excel по номеру PDF**

 Следующий код загружает[образец файла Excel](55541778.xlsx) но образец файла Excel ошибочен и выдает ошибку во время[преобразование в PDF](55541779.pdf) в 17.11, но поскольку мы используем[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)свойство, оно не выдает ошибку. Однако один*округлая красная стрелка, похожая на форму*как показано на этом скриншоте, потеряно.

![задача: image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
