---
title: Generera bilder för betingad formatering DataBars
description: Aspose.Cells är ett .NET bibliotek för att arbeta med kalkylbladsfiler. Det stöder generering av betingat formaterade dataremsor och bilder, vilket gör det möjligt för användare att anpassa visningen av kalkylarket baserat på cellernas värden. Denna artikel kommer att introducera hur man använder Aspose.Cells biblioteket för att generera betingat formaterade dataremsor och bilder.
keywords: Aspose.Cells, Betingad formatering, Databalkar, Bilder, Kalkylblad
type: docs
weight: 40
url: /sv/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Ibland behöver du generera bilder på DataBars för betingad formatering. Du kan använda Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)-metod för att generera dessa bilder. Denna artikel visar hur man genererar en DataBar-bild med hjälp av Aspose.Cells.

{{% /alert %}}

Följande kodexempel genererar DataBar-bilden för cell C1. Först får den åtkomst till formatvillkorsobjektet för cellen, och sedan från det objektet hämtar den [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar)-objektet och använder dess [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)-metod för att generera bilden av cellen. Till sist sparar den bilden på disken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
