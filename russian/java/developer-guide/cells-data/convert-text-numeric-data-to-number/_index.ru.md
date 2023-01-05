---
title: Преобразование текстовых числовых данных в число
type: docs
weight: 150
url: /ru/java/convert-text-numeric-data-to-number/
description: Узнайте, как преобразовывать числа, хранящиеся в виде текста, в числа, используя код Aspose.Cells for Java API.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
{{% alert color="primary" %}}

 Иногда требуется преобразовать числовые данные, введенные в виде текста, в числа. Вы можете вводить числа как текст в Microsoft Excel, поставив апостроф перед числом, например**'12345**. Затем Excel обрабатывает число как строку. Aspose.Cells позволяет преобразовывать строки в числа.

{{% /alert %}}

Aspose.Cells for Java API обеспечивает[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()), который можно использовать для преобразования всех строковых или текстовых числовых данных в числа.

 На следующем снимке экрана показаны номера строк в ячейках.**А1:А17**. Номера строк выравниваются по левому краю.

**Входной файл: числа, введенные в виде текстовых строк** 

![дело:изображение_альтернативный_текст](convert-text-numeric-data-to-number_1.png)

Эти строковые номера были преобразованы в числа с использованием[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) на следующем снимке экрана. Как видите, теперь они выровнены по правому краю.

**Выходной файл: строки были преобразованы в числа** 

![дело:изображение_альтернативный_текст](convert-text-numeric-data-to-number_2.png)

В следующем примере кода показано, как преобразовать все строковые числовые данные в фактические числа на всех листах.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
