---
title: Ange hur man korsar sträng i utdata HTML med HtmlCrossType med Golang via C++
linktitle: Ange kolumnbredden till skalbar enhet som em eller procent
type: docs
weight: 130
url: /sv/go-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Lär dig hur du ställer in kolumnbredd till skalbara enheter som em eller procent med Aspose.Cells for C++.
---

Att generera en HTML-fil från ett kalkylblad är mycket vanligt. Storleken på kolumnerna definieras i "pt" vilket fungerar i många fall. Det kan dock vara så att denna fasta storlek inte är nödvändig. Till exempel om en behållarepanel har en bredd på 600px där den här HTML-sidan visas. I detta fall kan du få en horisontell rullgardin om den genererade tabellbredden är större. Det var nödvändigt att denna fasta storlek ska ändras till en skalbar enhet som em eller procent för att få en bättre presentation. Följande provkod kan användas där [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getwidthscalable/) är inställd på **true** för att skapa skalbar bredd.

Källfilen och utdatafiler kan laddas ned från följande länkar:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetColumnWidthToScalableUnitLikeEmOrPercent.go" >}}
