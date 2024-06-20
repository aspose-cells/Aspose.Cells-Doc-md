---
title: Ограничение количества сгенерированных страниц при преобразовании Excel в PDF
type: docs
weight: 60
url: /ru/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Иногда вам может понадобиться напечатать диапазон страниц в выходной PDF-файл. У Aspose.Cells есть возможность установить ограничение на количество сгенерированных страниц при конвертации электронной таблицы Excel в PDF.

{{% /alert %}}

## **Ограничение количества сгенерированных страниц**

В следующем примере показано, как отображать диапазон страниц (3 и 4) в файле Microsoft Excel в формате PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

Если таблица содержит формулы, лучше всего вызвать [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) прямо перед отображением ее в формате PDF. Таким образом гарантируется пересчет значений, зависящих от формулы, и правильные значения будут отображены в выходном файле.

{{% /alert %}}
