---
title: Undvik exponentiell notation av stora nummer vid import från HTML med Golang via C++
linktitle: Undvik exponentiell notation för stora tal vid import från HTML
type: docs
weight: 10
url: /sv/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Lär dig hur man undviker exponentiell notation av stora nummer vid import från HTML med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland innehåller din HTML nummer som 1234567890123456 som är längre än 15 siffror, och när du importerar din HTML till en Excel-fil konverteras dessa nummer till exponentiell notation som 1.23457E+15. Om du vill att ditt nummer ska importeras som det är och inte omvandlas till exponentiell notation, använd då [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/)-egenskapen och ställ in den till **true** när du laddar din HTML.

{{% /alert %}}

Följande kodexempel förklarar användningen av [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/)-egenskapen. API:et kommer att importera numret som det är utan att omvandla det till exponentiell notation.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
