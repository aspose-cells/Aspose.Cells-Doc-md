---
title: Передискретизация добавленных изображений - Преобразование Excel в PDF
type: docs
weight: 150
url: /ru/net/resampling-added-images-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

При работе с большими Microsoft файлами Excel с большим количеством изображений может потребоваться сжатие добавленных изображений, чтобы уменьшить размер выходного PDF-файла и повысить общую производительность преобразования. Aspose.Cells поддерживает повторную выборку добавленных изображений, чтобы уменьшить размер выходного PDF-файла и несколько повысить производительность.

{{% /alert %}}

См. следующий пример кода, описывающий выполнение задачи с использованием Aspose.Cells API. В примере файл Excel Microsoft преобразуется в файл PDF при сжатии изображений в файле.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

 Используя[**сетимажересампл**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)Параметр минимизирует размер выходного PDF-файла, но может немного повлиять на качество изображения.

{{% /alert %}} {{% alert color="primary" %}}

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.ВычислитьФормулу()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) непосредственно перед рендерингом электронной таблицы в формат PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в PDF-файле отобразятся правильные значения.

{{% /alert %}}
