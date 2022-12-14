---
title: Ställ in kolumnbredden på skalbar enhet som em eller procent
type: docs
weight: 130
url: /sv/net/set-column-width-to-scalable-unit-like-em-or-percent/
---
Att generera en HTML-fil från ett kalkylblad är mycket vanligt. Storleken på kolumnerna definieras i "pt" vilket fungerar i många fall. Det kan dock finnas ett fall där denna fasta storlek kanske inte krävs. Till exempel, om en containerpanels bredd är 600px där denna HTML-sida visas. I det här fallet kan du få en horisontell rullningslist om den genererade tabellbredden är större. Det krävdes att denna fasta storlek skulle ändras till en skalbar enhet som em eller procent för att få en bättre presentation. Följande exempelkod kan användas var[**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/widthscalable) är satt till**Sann** för att skapa skalbar bredd.

Exempel på källfiler och utdatafiler kan laddas ner från följande länkar:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetScalableColumnWidth-1.cs" >}}
