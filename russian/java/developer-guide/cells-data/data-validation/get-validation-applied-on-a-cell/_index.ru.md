---
title: Применить проверку к номеру Cell
type: docs
weight: 80
url: /ru/java/get-validation-applied-on-a-cell/
description: В этой статье показано, как применить проверку на Cell с Java.
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 Вы можете использовать Aspose.Cells API, чтобы применить проверку к любой ячейке. Aspose.Cells обеспечивает[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() ) метод для этой цели. Если в ячейке нет проверки, возвращается значение null. Точно так же вы можете использовать[**Worksheet.getValidations().getValidationInCell (строка int, столбец int)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) для получения проверки, примененной к ячейке, путем предоставления ее индексов строки и столбца.

{{% /alert %}}

 На следующем снимке показан образец файла Excel Microsoft, используемый в примере кода ниже. Cell**С1** имеет**десятичная проверка** применяется и может принимать только значения**между 10 и 20**.

**Ячейка с проверкой**

![дело:изображение_альтернативный_текст](get-validation-applied-on-a-cell_1.png)

В приведенном ниже примере кода проверка применяется к C1 и считываются его различные свойства.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Вот вывод консоли из примера кода, выполненного с образцом файла, показанным на снимке выше.

{{< highlight "java" >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## Статьи по Теме

- [Проверка данных](/cells/ru/java/data-validation/)
