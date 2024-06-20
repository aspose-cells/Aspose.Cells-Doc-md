---
title: Избегайте экспоненциальной нотации больших чисел при импорте из HTML
type: docs
weight: 10
url: /ru/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

Иногда в вашем HTML содержатся числа, например, 1234567890123456, которые длиннее 15 цифр, и при импорте вашего HTML в файл Excel эти числа преобразуются в экспоненциальную запись, например, 1.23457Е+15. Если вы хотите, чтобы ваше число импортировалось как есть и не преобразовывалось в экспоненциальную запись, то пожалуйста, используйте свойство [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) и установите его в **true** при загрузке вашего HTML.

{{% /alert %}}

В следующем образце кода объясняется использование свойства [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision). API импортирует число как есть, не преобразуя его в экспоненциальную нотацию.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
