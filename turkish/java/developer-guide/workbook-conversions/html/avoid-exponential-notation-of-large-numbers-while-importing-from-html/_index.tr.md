---
title: Html den içe aktarırken büyük sayıların üstel gösterimini önleme
type: docs
weight: 600
url: /tr/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

HTML'niz bazen 1234567890123456 gibi 15 basamaktan uzun sayılar içerebilir ve HTML'nizi excel dosyasına aktardığınızda bu sayılar 1.23457E+15 gibi üs tabanındaki gösterime dönüşebilir. Eğer istiyorsanız, sayınızın üs tabanında gösterilmesi yerine olduğu gibi alınmasını istiyorsanız, lütfen [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) özelliğini kullanın ve yüklerken bunu **true** olarak ayarlayın.

{{% /alert %}} 
## **HTML'den alınan büyük sayıların üs tabanındaki gösterimini önleme**
Aşağıdaki örnek kod, [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) özelliğinin kullanımını açıklar. Bu özellik sayıyı üs tabanındaki gösterime dönüştürmeden alır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
{{< app/cells/assistant language="java" >}}
