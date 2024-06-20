---
title: Избегайте экспоненциальной нотации больших чисел при импорте из HTML
type: docs
weight: 600
url: /ru/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

Иногда ваш HTML содержит числа, такие как 1234567890123456, которые длиннее 15 цифр, и при импорте вашего HTML в файл Excel эти числа преобразуются в экспоненциальную нотацию, например 1.23457E+15. Если вы хотите, чтобы ваше число импортировалось в исходном виде, а не преобразовывалось в экспоненциальную нотацию, то используйте свойство [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) и установите его в значение **true** при загрузке вашего HTML.

{{% /alert %}} 
## **Избегайте экспоненциальной нотации больших чисел при импорте из HTML**
Приведенный ниже образец кода поясняет использование свойства [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision). Он будет импортировать число в исходном виде, без преобразования его в экспоненциальную нотацию.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
