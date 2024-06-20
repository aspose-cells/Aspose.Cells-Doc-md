---
title: Изменение размера добавленных изображений  преобразование Excel в PDF
type: docs
weight: 150
url: /ru/python-net/resample-added-images-excel-to-pdf-conversion/
description: Узнайте, как изменить размер добавленных изображений при преобразовании Excel в PDF с помощью Aspose.Cells для Python via .NET API.
keywords: Изменить размер добавленных изображений с помощью Python при преобразовании Excel в PDF
---

{{% alert color="primary" %}}

При работе с большими файлами Microsoft Excel, содержащими множество изображений, может потребоваться сжатие изображений для уменьшения размера выходного файла PDF и улучшения общей производительности конвертации. Aspose.Cells для Python via .NET поддерживает изменение размера добавленных изображений для уменьшения размера выходного файла PDF и некоторого улучшения производительности.

{{% /alert %}}

 Пожалуйста, ознакомьтесь с приведенным ниже примером кода, который описывает, как выполнить задачу с использованием Aspose.Cells для Python via .NET API. В примере производится преобразование файла Microsoft Excel в файл PDF при сжатии изображений в файле.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

Использование опции [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) помогает минимизировать размер выходного PDF, но это может немного повлиять на качество изображения.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
