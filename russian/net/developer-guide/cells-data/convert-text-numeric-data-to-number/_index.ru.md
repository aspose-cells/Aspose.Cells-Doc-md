---
title: Преобразование текстовых числовых данных в число
type: docs
weight: 900
url: /ru/net/convert-text-numeric-data-to-number/
description: Узнайте, как преобразовывать числа, сохраненные в виде текста в Excel, в числа с помощью функции Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
{{% alert color="primary" %}}

 Иногда требуется преобразовать числовые данные, введенные в виде текста, в числа. Вы можете вводить числа как текст в Microsoft Excel, поставив апостроф перед числом, например**'12345**. Затем Excel обрабатывает число как строку. Aspose.Cells позволяет преобразовывать строки в числа.

{{% /alert %}}

Aspose.Cells обеспечивает[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)метод, который можно использовать для преобразования всех строковых или текстовых числовых данных в числа.

 На следующем снимке экрана показаны номера строк в ячейках.**А1:А17**. Номера строк выравниваются по левому краю.

|**Входной файл: числа, введенные в виде текстовых строк**|
|:- |
|![дело:изображение_альтернативный_текст](convert-text-numeric-data-to-number_1.png)|

Эти строковые номера были преобразованы в числа с использованием[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)на следующем снимке экрана. Как видите, теперь они выровнены по правому краю.

|**Выходной файл: строки были преобразованы в числа**|
|:- |
|![дело:изображение_альтернативный_текст](convert-text-numeric-data-to-number_2.png)|

## C# код для преобразования строковых числовых данных в фактические числа

В следующем примере кода показано, как преобразовать все строковые числовые данные в фактические числа на всех листах.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
