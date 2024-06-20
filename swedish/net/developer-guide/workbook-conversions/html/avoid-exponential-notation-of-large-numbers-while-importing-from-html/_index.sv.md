---
title: Undvik exponentiell notation för stora tal vid import från HTML
type: docs
weight: 10
url: /sv/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

Ibland innehåller din Html siffror som 1234567890123456 som är längre än 15 siffror och när du importerar din HTML till en excelfil, omvandlas dessa siffror till exponentiell notation som 1.23457E+15. Om du vill att ditt nummer ska importeras som det är och inte omvandlas till exponentiell notation, använd då egenskapen [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) och sätt den till **true** vid inläsning av din HTML.

{{% /alert %}}

Följande exempelkod förklarar användningen av egenskapen [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision). API:et kommer att importera numret som det är utan att omvandla det till exponentiell notation.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
