---
title: Игнорировать ошибки при преобразовании Excel в PDF
type: docs
weight: 70
url: /ru/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **Возможные сценарии использования**

Иногда при преобразовании вашего файла Excel в PDF возникают ошибки или исключения, и процесс преобразования прерывается. Вы можете игнорировать все такие ошибки во время процесса преобразования, используя свойство [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError). Таким образом, процесс преобразования завершится гладко, без генерации ошибок или исключений, но может произойти потеря данных. Поэтому используйте это свойство только в том случае, если потеря данных для вас не критична.

## **Игнорировать ошибки при преобразовании Excel в PDF**

Следующий код загружает [образец Excel-файла](55541813.xlsx), но образец Excel-файл содержит ошибки и вызывает ошибку во время [преобразования в PDF](55541814.pdf) в версии 17.11, но поскольку мы используем свойство [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError), ошибка не возникает. Однако имеется потеря одной как показано на этом снимке экрана.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
{{< app/cells/assistant language="java" >}}
