---
title: HTML'den içe aktarırken büyük sayıların üstel gösteriminden kaçının
type: docs
weight: 600
url: /tr/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

Bazen HTML'niz 1234567890123456 gibi 15 basamaktan uzun sayılar içerir ve HTML'nizi excel dosyasına aktardığınızda bu sayılar 1.23457E+15 gibi üstel gösterime dönüşür. İsterseniz numaranız olduğu gibi içe aktarılmalı ve üstel gösterime dönüştürülmemelidir, o zaman lütfen kullanın.[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) özellik ve ayarlayın**doğru** HTML'nizi yüklerken.

{{% /alert %}} 
## **HTML'den içe aktarırken büyük sayıların üstel gösteriminden kaçının**
 Aşağıdaki örnek kod, kullanımını açıklar[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)Emlak. Sayıyı üstel gösterime dönüştürmeden olduğu gibi içe aktaracaktır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
