---
title: Игнорировать ошибки при рендеринге Excel в PDF
type: docs
weight: 80
url: /ru/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **Возможные сценарии использования**

 Иногда при преобразовании файла Excel в PDF возникают ошибки или исключения, и процесс преобразования завершается. Вы можете игнорировать все такие ошибки в процессе преобразования, используя[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)имущество. Таким образом, процесс преобразования завершится гладко, без каких-либо ошибок или исключений, но может произойти потеря данных. Поэтому используйте это свойство только в том случае, если потеря данных для вас не критична.

## **Игнорировать ошибки при рендеринге Excel в PDF**

 Следующий код загружает[образец файла Excel](55541778.xlsx) но образец файла Excel ошибочен и выдает ошибку во время[преобразование в PDF](55541779.pdf) в 17.11, но так как мы используем[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)свойство, он не выдает ошибку. Однако один*округлая красная стрелка, как форма*как показано на этом снимке экрана, теряется.

![дело:изображение_альтернативный_текст](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
