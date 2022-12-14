---
title: Передискретизировать изображения для преобразования Excel в PDF
type: docs
weight: 250
url: /ru/java/resample-images-for-excel-to-pdf-conversion/
description: В этой статье показано уменьшение размеров изображений при преобразовании файлов Excel в PDF.
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

При работе с большими Microsoft файлами Excel с большим количеством изображений может потребоваться сжатие добавленных изображений, чтобы уменьшить размер выходного PDF-файла и повысить общую производительность преобразования. Aspose.Cells поддерживает повторную выборку добавленных изображений для уменьшения размера выходного PDF-файла и повышения производительности.

{{% /alert %}}

## **Передискретизировать изображения для преобразования Excel в PDF**

См. следующий пример кода, описывающий выполнение задачи с использованием Aspose.Cells API. В примере файл Excel Microsoft преобразуется в файл PDF при сжатии изображений в файле.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

 С использованием[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) минимизирует размер выходного PDF-файла, но может немного повлиять на качество изображения.

{{% /alert %}} {{% alert color="primary" %}}

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()непосредственно перед преобразованием электронной таблицы в формат PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в PDF-файле отобразятся правильные значения.

{{% /alert %}}
