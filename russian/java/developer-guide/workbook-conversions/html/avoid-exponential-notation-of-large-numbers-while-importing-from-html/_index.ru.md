---
title: Избегайте экспоненциального представления больших чисел при импорте из HTML
type: docs
weight: 600
url: /ru/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

Иногда ваш HTML содержит числа, такие как 1234567890123456, которые длиннее 15 цифр, и когда вы импортируете свой HTML в файл Excel, эти числа преобразуются в экспоненциальное представление, например 1.23457E+15. Если вы хотите, чтобы ваше число было импортировано как есть, а не преобразовано в экспоненциальную запись, используйте[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) свойство и установить его**истинный** при загрузке вашего HTML.

{{% /alert %}} 
## **Избегайте экспоненциального представления больших чисел при импорте из HTML**
 В следующем примере кода объясняется использование[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)имущество. Он импортирует число как есть, не преобразовывая его в экспоненциальное представление.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
