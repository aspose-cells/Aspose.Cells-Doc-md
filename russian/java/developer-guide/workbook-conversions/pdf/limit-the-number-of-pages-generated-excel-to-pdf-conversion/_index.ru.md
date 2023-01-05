---
title: Ограничение количества генерируемых страниц - преобразование Excel в PDF
type: docs
weight: 60
url: /ru/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Иногда вы хотите напечатать диапазон страниц в выходной файл PDF. Aspose.Cells имеет возможность установить ограничение на количество страниц, создаваемых при преобразовании электронной таблицы Excel в PDF.

{{% /alert %}}

## **Ограничение количества генерируемых страниц**

В следующем примере показано, как преобразовать диапазон страниц (3 и 4) в файле Excel Microsoft в PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

 Если электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) непосредственно перед рендерингом в формат PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в выходном файле будут отображены правильные значения.

{{% /alert %}}
