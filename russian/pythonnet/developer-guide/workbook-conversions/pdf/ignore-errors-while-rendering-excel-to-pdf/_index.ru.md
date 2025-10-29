---
title: Игнорировать ошибки при преобразовании Excel в PDF
type: docs
weight: 80
url: /ru/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Узнайте, как игнорировать ошибки при выводе Excel в PDF с использованием Aspose.Cells для Python via .NET API.
keywords: Python Игнорировать ошибки при выводе Excel в PDF, Игнорировать ошибки при сохранении Excel в PDF с помощью Python, Python Игнорировать ошибки при преобразовании Excel в PDF
---

## **Возможные сценарии использования**

Иногда при конвертации вашего файла Excel в PDF возникают ошибки или исключения, и процесс конвертации прерывается. Вы можете игнорировать все такие ошибки во время процесса конвертации, используя свойство [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/). Таким образом, процесс конвертации завершится гладко, без возникновения ошибок или исключений, но возможна потеря данных. Поэтому пожалуйста, используйте это свойство только в том случае, если потеря данных для вас не критична.

## **Игнорировать ошибки при преобразовании Excel в PDF**

Следующий код загружает [образец файла Excel](55541778.xlsx), но образец файла Excel содержит ошибку и вызывает ошибку при [конвертации в PDF](55541779.pdf) в версии 17.11, но поскольку мы используем свойство [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/), ошибка не возникает. Однако одна *загнутая красная стрелка* в форме, показанная на этом скриншоте, теряется.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
{{< app/cells/assistant language="python-net" >}}
