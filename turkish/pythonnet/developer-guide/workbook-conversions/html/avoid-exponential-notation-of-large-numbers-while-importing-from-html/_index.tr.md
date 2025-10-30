---
title: Html den içe aktarırken büyük sayıların üstel gösterimini önleme
type: docs
weight: 10
url: /tr/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Bu konu, Aspose.Cells için Python via NET kullanarak HTML den içe aktarırken büyük sayıların üstel işaretleme yapısını engelleme yöntemini gösterir.
keywords: HTML den içe aktarırken büyük sayıların üstel işaretleme yapısını engelleme, html içe aktarırken hassasiyeti koruma.
---

{{% alert color="primary" %}}

Html'nizi Excel dosyasına aktardığınızda 1234567890123456 gibi 15 rakamdan uzun sayılar içerebilir ve HTML'nizi excel dosyasına aktardığınızda bu sayılar 1.23457E+15 gibi üstel gösterime dönüşebilir. Eğer isterseniz, sayınızın üstel gösterime dönüşmeden olduğu gibi alınmasını istiyorsanız, lütfen HTML'nizi yüklerken [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) özelliğini **true** olarak ayarlayın.

{{% /alert %}}

Aşağıdaki örnek kod, [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) özelliğinin kullanımını açıklar. API sayıyı üstel gösterime dönüştürmeden içe aktarır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
