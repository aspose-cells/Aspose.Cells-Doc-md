---
title: Игнорировать ошибки при рендеринге Excel в PDF
type: docs
weight: 70
url: /ru/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **Возможные сценарии использования**

Иногда при преобразовании файла Excel в PDF возникают ошибки или исключения, и процесс преобразования завершается. Вы можете игнорировать все такие ошибки в процессе конвертации, используя[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)имущество. Таким образом, процесс преобразования завершится гладко, без каких-либо ошибок или исключений, но может произойти потеря данных. Поэтому используйте это свойство только в том случае, если потеря данных для вас не критична.

## **Игнорировать ошибки при рендеринге Excel в PDF**

Следующий код загружает[образец файла Excel](55541813.xlsx)но образец файла Excel ошибочен и выдает ошибку во время[преобразование в PDF](55541814.pdf)в 17.11, но так как мы используем[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)свойство, он не выдает ошибку. Однако одна закругленная красная стреловидная форма, как показано на этом снимке экрана, потеряна.

![дело:изображение_альтернативный_текст](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
