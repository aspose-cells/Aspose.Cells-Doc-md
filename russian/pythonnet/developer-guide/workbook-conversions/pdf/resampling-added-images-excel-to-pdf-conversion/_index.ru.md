---
title: Повторная выборка добавленных изображений — преобразование Excel в PDF
type: docs
weight: 150
url: /ru/python-net/resample-added-images-excel-to-pdf-conversion/
description: Узнайте, как изменить размер добавленных изображений при преобразовании Excel в PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

При работе с большими файлами Excel Microsoft с большим количеством изображений может потребоваться сжать добавленные изображения, чтобы уменьшить размер выходного файла PDF и повысить общую производительность преобразования. Aspose.Cells for Python via .NET поддерживает повторную выборку добавленных изображений, чтобы уменьшить размер выходного файла PDF и несколько улучшить производительность.

{{% /alert %}}

См. следующий пример кода, который описывает, как выполнить задачу с помощью Aspose.Cells for Python via .NET API. В этом примере файл Excel Microsoft преобразуется в файл PDF при сжатии изображений в файле.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

 Используя[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)Опция минимизирует размер вывода PDF, но это может немного повлиять на качество изображения.

{{% /alert %}} {{% alert color="primary" %}}

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) непосредственно перед преобразованием таблицы в формат PDF. Это обеспечит перерасчет зависимых от формулы значений и отображение правильных значений в PDF.

{{% /alert %}}
