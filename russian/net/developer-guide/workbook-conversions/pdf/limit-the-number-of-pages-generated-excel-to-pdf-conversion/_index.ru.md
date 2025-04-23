---
title: Ограничение количества сгенерированных страниц при преобразовании Excel в PDF
type: docs
weight: 180
url: /ru/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Иногда вам может понадобиться напечатать диапазон страниц в выходной файл PDF. Aspose.Cells позволяет установить ограничение на количество генерируемых страниц при конвертации электронной таблицы Excel в формат PDF.

{{% /alert %}}

## **Ограничение количества сгенерированных страниц**

В следующем примере показано, как отображать диапазон страниц (3 и 4) в файле Microsoft Excel в формате PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

Если электронная таблица содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) прямо перед ее рендерингом в PDF. Это гарантирует, что зависимые от формулы значения будут пересчитаны, и правильные значения будут отображены в выходном файле.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
