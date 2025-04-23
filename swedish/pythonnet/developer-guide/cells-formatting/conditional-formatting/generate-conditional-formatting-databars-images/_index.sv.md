---
title: Generera bilder för betingad formatering DataBars
description: Aspose.Cells för Python via .NET är ett Python bibliotek för att arbeta med kalkylbladsfiler. Det stöder generering av villkorsformatade datastaplar och bilder, vilket ger användare möjlighet att anpassa visningen av kalkylbladet baserat på cellvärdena. Denna artikel introducerar hur man använder Aspose.Cells för Python via biblioteket för att generera villkorsformatade datastaplar och bilder.
keywords: Aspose.Cells för Python via .NET, Villkorsformatering, Datastaplar, Bilder, Kalkylblad
type: docs
weight: 40
url: /sv/python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Ibland behöver du generera bilder av villkorsformaterade datastaplar. Du kan använda Aspose.Cells [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) metod för att generera dessa bilder. Denna artikel visar hur man genererar en datastapelbild med Aspose.Cells för Python via .NET.

{{% /alert %}}

Följande kodexempel genererar DataBar-bilden för cell C1. Först får den åtkomst till formatvillkorsobjektet för cellen, och sedan från det objektet hämtar den [**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar)-objektet och använder dess [**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image)-metod för att generera bilden av cellen. Till sist sparar den bilden på disken.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}
