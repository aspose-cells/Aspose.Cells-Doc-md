---
title: Ограничение количества генерируемых страниц - преобразование Excel в PDF
type: docs
weight: 180
url: /ru/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Иногда вам нужно напечатать диапазон страниц в выходной PDF-файл. Aspose.Cells имеет возможность установить ограничение на количество страниц, создаваемых при преобразовании электронной таблицы Excel в формат файла PDF.

{{% /alert %}}

## **Ограничение количества генерируемых страниц**

В следующем примере показано, как преобразовать диапазон страниц (3 и 4) в файле Excel Microsoft в формат PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

 Если электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.ВычислитьФормулу()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) непосредственно перед рендерингом в PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в выходном файле будут отображены правильные значения.

{{% /alert %}}
