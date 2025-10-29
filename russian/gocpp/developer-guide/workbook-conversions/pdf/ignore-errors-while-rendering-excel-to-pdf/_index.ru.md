---
title: Игнорировать ошибки при преобразовании Excel в PDF с помощью Golang через C++
linktitle: Игнорировать ошибки при преобразовании Excel в PDF
type: docs
weight: 80
url: /ru/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Узнайте, как игнорировать ошибки во время конвертации Excel в PDF с использованием Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда при преобразовании Excel-файла в PDF возникают ошибки или исключения, и преобразование прерывается. Можно игнорировать все такие ошибки в процессе преобразования, используя свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/). Таким образом, процесс преобразования завершится гладко, без ошибок или исключений, но возможна потеря данных. Используйте это свойство только если потеря данных для вас не критична.

## **Игнорировать ошибки при преобразовании Excel в PDF**

Следующий код загружает [пример Excel файла](55541778.xlsx), который содержит ошибку и вызывает ошибку при [преобразовании в PDF](55541779.pdf) в версии 17.11. Однако, поскольку мы используем свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/), ошибка не возникает. Однако одна *округлая стрелка красного цвета*, показанная на скриншоте, утеряна.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
