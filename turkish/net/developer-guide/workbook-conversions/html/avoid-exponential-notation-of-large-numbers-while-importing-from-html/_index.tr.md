---
title: Html den içe aktarırken büyük sayıların üstel gösterimini önleme
type: docs
weight: 10
url: /tr/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

Html'nizi Excel dosyasına aktardığınızda 1234567890123456 gibi 15 rakamdan uzun sayılar içerebilir ve HTML'nizi excel dosyasına aktardığınızda bu sayılar 1.23457E+15 gibi üstel gösterime dönüşebilir. Eğer isterseniz, sayınızın üstel gösterime dönüşmeden olduğu gibi alınmasını istiyorsanız, lütfen HTML'nizi yüklerken [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) özelliğini **true** olarak ayarlayın.

{{% /alert %}}

Aşağıdaki örnek kod, [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) özelliğinin kullanımını açıklar. API sayıyı üstel gösterime dönüştürmeden içe aktarır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
