---
title: Избегайте экспоненциального представления больших чисел при импорте из HTML.
type: docs
weight: 10
url: /ru/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

 Иногда ваш HTML-код содержит числа, такие как 1234567890123456, которые длиннее 15 цифр, и когда вы импортируете свой файл HTML в файл excel, эти числа преобразуются в экспоненциальное представление, например 1.23457E+15. Если вы хотите, чтобы ваше число было импортировано как есть, а не преобразовано в экспоненциальную запись, используйте[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) свойство и установить его**истинный** при загрузке вашего HTML.

{{% /alert %}}

 В следующем примере кода объясняется использование[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)имущество. API импортирует число как есть, не преобразовывая его в экспоненциальное представление.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
