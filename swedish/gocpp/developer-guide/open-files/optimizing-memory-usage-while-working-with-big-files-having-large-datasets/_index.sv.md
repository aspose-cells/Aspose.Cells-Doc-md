---
title: Optimera minnesanvändningen vid arbete med stora filer med stora datamängder med Golang via C++
linktitle: Optimera minnesanvändning
type: docs
weight: 180
url: /sv/go-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Lär dig hur du optimerar minnesanvändning vid arbete med stora Excel filer med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

När man bygger en arbetsbok med stora datamängder, eller läser en stor Microsoft Excel-fil, är den totala mängden RAM som processen kommer att ta alltid en oro. Det finns åtgärder som kan anpassas för att hantera utmaningen. Aspose.Cells tillhandahåller vissa relevanta alternativ och API-anrop för att minska, sänka och optimera minnesanvändningen. Det kan också hjälpa processen att fungera effektivare och köra snabbare.

Använd [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) för att optimera minnesanvändningen för celldata och minska den totala minneskostnaden. När man bygger en stor datamängd för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen ([**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/)).

{{% /alert %}}

## **Optimera minne**

### **Läsning av stora Excel-filer**

Det följande exemplet visar hur man läser en stor Microsoft Excel-fil i optimerat läge.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets.go" >}}
### **Skrivning av stora Excel-filer**

Det följande exemplet visar hur man skriver en stor datamängd till en arbetsbok i optimerat läge.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets-1.go" >}}
## **Försiktighet**

Standardalternativet, [**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/) tillämpas för alla versioner. För vissa situationer, som att bygga en arbetsbok med en stor datamängd för celler, kan [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) -alternativet optimera minnesanvändningen och minska minneskostnaden för applikationen. Dock kan detta alternativ försämra prestandan i vissa speciella fall som följer.

1. **Åtkomst av celler slumpmässigt och upprepade gånger**: Den mest effektiva sekvensen för att komma åt cellernas samling är cell för cell i en rad, och sedan rad för rad. Särskilt om du får åtkomst till rader/celler via uppräknaren som erhållits från [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) och [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), kommer prestandan att maximera med [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **Infoga & Ta bort celler & rader**: Observera att om det finns många infogning/ta bort-operationer för celler/rader, kommer prestandaförsämringen märkas för *MemoryPreference* läge jämfört med *Normal* läge.
1. **Infogning & Radering av celler & rader**: Observera att om det finns mycket infogning/radering av operationer för celler/rader, kommer prestandanedbrytningen att vara märkbar för *MemoryPreference*-läget jämfört med *Normal*-läget.
