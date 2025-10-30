---
title: Ange kolumnbredden till skalbar enhet som em eller procent
type: docs
weight: 130
url: /sv/python-net/set-column-width-to-scalable-unit-like-em-or-percent/
---

Att generera en HTML-fil från ett kalkylblad är mycket vanligt. Storleken på kolumnerna definieras i "pt" vilket fungerar i många fall. Det kan dock vara så att denna fasta storlek inte är nödvändig. Till exempel om en behållarepanel har en bredd på 600px där den här HTML-sidan visas. I detta fall kan du få en horisontell rullgardin om den genererade tabellbredden är större. Det var nödvändigt att denna fasta storlek ska ändras till en skalbar enhet som em eller procent för att få en bättre presentation. Följande provkod kan användas där [**HtmlSaveOptions.width_scalable**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/width_scalable) är inställd på **true** för att skapa skalbar bredd.

Källfilen och utdatafiler kan laddas ned från följande länkar:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetScalableColumnWidth-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
