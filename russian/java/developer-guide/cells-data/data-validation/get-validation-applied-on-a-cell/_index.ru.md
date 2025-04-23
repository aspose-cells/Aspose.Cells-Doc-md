---
title: Получить примененную валидацию для ячейки
type: docs
weight: 80
url: /ru/java/get-validation-applied-on-a-cell/
description: В этой статье показано, как применять проверку в ячейке с помощью Java
keywords: применить проверку ячейки в Excel с помощью Java, применить проверку к ячейке в Excel с помощью Java, применить проверку в Excel с помощью Java, проверка ячейки в Excel с помощью Java, Java применить проверку ячейки в Excel, Java применить проверку к ячейке в Excel, Java проверка ячейки в Excel, Java проверка ячейки
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells API, чтобы получить проверку, примененную к любой ячейке. Aspose.Cells предоставляет метод [**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--) для этой цели. Если на ячейке нет проверки, он возвращает null. Точно так же, вы можете использовать метод [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell-int-int-), чтобы получить проверку, примененную к ячейке, указав ее индексы строки и столбца.

{{% /alert %}}

На следующем снимке экрана показан образец файла Microsoft Excel, используемый в следующем образце кода. Ячейка **C1** имеет примененную **десятичную проверку** и может принимать только значения **от 10 до 20**.

**Ячейка с проверкой**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

В следующем образце кода получается примененная проверка к ячейке C1 и считываются ее различные свойства.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Вот вывод на консоль из примера кода, выполненного с образцом файла, показанным на снимке экрана выше.

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## Связанные статьи

- [Валидация данных](/cells/ru/java/data-validation/)
{{< app/cells/assistant language="java" >}}
