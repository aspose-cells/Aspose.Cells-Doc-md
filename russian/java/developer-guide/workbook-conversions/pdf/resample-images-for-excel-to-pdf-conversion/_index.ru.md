---
title: Изменение размеров изображений для преобразования Excel в PDF
type: docs
weight: 250
url: /ru/java/resample-images-for-excel-to-pdf-conversion/
description: В этой статье демонстрируется уменьшение размеров изображений при преобразовании файлов Excel в PDF
keywords: excel в pdf, изменение размеров изображений во время преобразования excel в pdf, сжатие изображений во время преобразования excel в pdf, уменьшение размеров изображений во время преобразования excel в pdf, преобразование excel в pdf с меньшим размером, преобразование excel в pdf с изменением размеров изображений, преобразование excel в pdf с сжатием изображений, изменение размеров изображений во время преобразования excel в pdf на Java
---

{{% alert color="primary" %}}

При работе с большими файлами Microsoft Excel с большим количеством изображений может потребоваться сжатие изображений для уменьшения размера выходного файла PDF и улучшения общей производительности преобразования. Aspose.Cells поддерживает пересемплирование добавленных изображений для уменьшения размера выходного файла PDF и улучшения производительности.

{{% /alert %}}

## **Изменение размеров изображений для преобразования Excel в PDF**

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, описывающим, как выполнить задачу с использованием API Aspose.Cells. В примере происходит преобразование файла Microsoft Excel в файл PDF с одновременным сжатием изображений в файле.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

Использование опции [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) позволяет минимизировать размер выходного PDF, но это может немного повлиять на качество изображения.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
