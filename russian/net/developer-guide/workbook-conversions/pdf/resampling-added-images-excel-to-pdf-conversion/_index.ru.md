---
title: Добавление перерасчета изображений  конвертация Excel в PDF
type: docs
weight: 150
url: /ru/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

При работе с большими файлами Microsoft Excel с большим количеством изображений вам может потребоваться сжимать добавленные изображения, чтобы уменьшить размер выходного PDF файла и улучшить общую производительность конвертации. Aspose.Cells поддерживает перерасчет добавленных изображений для уменьшения размера выходного PDF файла и улучшения производительности в некоторой степени.

{{% /alert %}}

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, описывающим, как выполнить задачу с использованием API Aspose.Cells. В примере происходит преобразование файла Microsoft Excel в файл PDF с одновременным сжатием изображений в файле.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

Использование опции [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) помогает минимизировать размер выходного PDF, но это может немного повлиять на качество изображения.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
