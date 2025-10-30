---
title: HTML den büyük sayıların üssel gösterimini önleme Golang ve C++ ile
linktitle: Html den içe aktarırken büyük sayıların üstel gösterimini önleme
type: docs
weight: 10
url: /tr/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Aspose.Cells for C++ kullanarak, HTML ye aktarırken büyük sayıların üssel gösterimini önlemeyi öğrenin.
---

{{% alert color="primary" %}}

Bazen HTML'nizde 1234567890123456 gibi 15'ten uzun sayılar bulunur ve bu sayılar Excel'e ithal edildiğinde 1.23457E+15 gibi üssel gösterime dönüşür. Sayınızın olduğu gibi kalmasını ve üssel gösterimle dönüştürülmemesini istiyorsanız, lütfen [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) özelliğini kullanın ve HTML yüklerken **true** olarak ayarlayın.

{{% /alert %}}

Aşağıdaki örnek kod, [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) özelliğinin kullanımını anlatır. API, sayıyı olduğu gibi ithal eder ve üssel gösterime dönüştürmez.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
