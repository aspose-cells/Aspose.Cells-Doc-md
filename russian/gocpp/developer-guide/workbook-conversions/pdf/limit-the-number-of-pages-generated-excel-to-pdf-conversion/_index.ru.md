---
title: Ограничение количества создаваемых страниц — Преобразование Excel в PDF с помощью Golang через C++
linktitle: Ограничить количество создаваемых страниц
type: docs
weight: 180
url: /ru/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Узнайте, как ограничить число страниц при преобразовании Excel в PDF с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

Иногда вам может понадобиться напечатать диапазон страниц в выходной файл PDF. Aspose.Cells позволяет установить ограничение на количество генерируемых страниц при конвертации электронной таблицы Excel в формат PDF.

{{% /alert %}}

## **Ограничение количества сгенерированных страниц**

В следующем примере показано, как отображать диапазон страниц (3 и 4) в файле Microsoft Excel в формате PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Если электронная таблица содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) прямо перед ее рендерингом в PDF. Это гарантирует, что зависимые от формулы значения будут пересчитаны, и правильные значения будут отображены в выходном файле.

{{% /alert %}}
