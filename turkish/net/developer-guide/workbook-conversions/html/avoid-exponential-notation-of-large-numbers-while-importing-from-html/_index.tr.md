---
title: HTML'den içe aktarırken büyük sayıların üstel gösteriminden kaçının
type: docs
weight: 10
url: /tr/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

 Bazen Html'niz 1234567890123456 gibi 15 basamaktan uzun sayılar içerir ve HTML'inizi excel dosyasına aktardığınızda bu sayılar 1.23457E+15 gibi üstel gösterime dönüşür. İsterseniz numaranız olduğu gibi içe aktarılmalı ve üstel gösterime dönüştürülmemelidir, o zaman lütfen kullanın.[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) özellik ve ayarlayın**doğru** HTML'inizi yüklerken.

{{% /alert %}}

 Aşağıdaki örnek kod, kullanımını açıklar[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)Emlak. API, sayıyı üstel gösterime dönüştürmeden olduğu gibi içe aktaracaktır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
