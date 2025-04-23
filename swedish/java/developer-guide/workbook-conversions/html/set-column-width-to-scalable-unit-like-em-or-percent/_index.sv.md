---
title: Ange kolumnbredden till skalbar enhet som em eller procent
type: docs
weight: 130
url: /sv/java/set-column-width-to-scalable-unit-like-em-or-percent/
---

Att generera en HTML-fil från ett kalkylblad är mycket vanligt. Kolumnernas storlek definieras i "pt" vilket fungerar i många fall. Det kan dock finnas fall där denna fasta storlek inte är nödvändig. Till exempel, om panelens bredd är 600px där den här HTML-sidan visas. I det fallet kan du få en horisontell rullningslist om den genererade tabellbredden är större. Det var nödvändigt att ändra denna fasta storlek till en skalbar enhet som em eller procent för att få en bättre presentation. Följande exempelkod kan användas där [**HtmlSaveOptions.WidthScalable**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#WidthScalable) är inställt till **true** för att skapa skalbar bredd.

Källfilen och utdatafiler kan laddas ned från följande länkar:

[sampleForScalableColumns.xlsx](74776596.xlsx)

[outsampleForScalableColumns.zip](74776597.zip)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-SetScalableColumnWidth.java" >}}
{{< app/cells/assistant language="java" >}}
