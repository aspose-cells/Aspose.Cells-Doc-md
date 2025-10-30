---
title: Undvik exponentiell notation för stora tal vid import från HTML
type: docs
weight: 10
url: /sv/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Detta ämne visar hur du undviker exponentiell notation för stora tal vid import från HTML med hjälp av Aspose.Cells för Python via NET.
keywords: Undvik exponentiell notation för stora tal vid import från HTML, behåll precisionen vid import av html.
---

{{% alert color="primary" %}}

Ibland innehåller din Html siffror som 1234567890123456 som är längre än 15 siffror och när du importerar din HTML till en excelfil, omvandlas dessa siffror till exponentiell notation som 1.23457E+15. Om du vill att ditt nummer ska importeras som det är och inte omvandlas till exponentiell notation, använd då egenskapen [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) och sätt den till **true** vid inläsning av din HTML.

{{% /alert %}}

Följande exempelkod förklarar användningen av egenskapen [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/). API:et kommer att importera numret som det är utan att omvandla det till exponentiell notation.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
