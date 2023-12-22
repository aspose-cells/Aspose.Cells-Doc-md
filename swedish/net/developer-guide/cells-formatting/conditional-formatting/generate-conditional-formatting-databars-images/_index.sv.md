---
title: Generera villkorlig formatering DataBars-bilder
description: Aspose.Cells är ett .NET-bibliotek för att arbeta med kalkylarksfiler. Den stöder generering av villkorligt formaterade datafält och bilder, vilket gör att användare kan anpassa visningen av kalkylarket baserat på värdet på cellerna. Den här artikeln kommer att introducera hur du använder Aspose.Cells-biblioteket för att generera villkorligt formaterade datafält och bilder.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /sv/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Ibland måste du skapa bilder av datafält för villkorlig formatering. Du kan använda Aspose.Cells[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) metod för att generera dessa bilder. Den här artikeln visar hur du genererar en DataBar-bild med Aspose.Cells.

{{% /alert %}}

 Följande exempelkod genererar DataBar-bilden av cell C1. Först får den åtkomst till formatvillkorsobjektet för cellen, och sedan från det objektet får den åtkomst till[**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) objekt och använder dess[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)metod för att generera bilden av cellen. Slutligen sparar den bilden på disken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
