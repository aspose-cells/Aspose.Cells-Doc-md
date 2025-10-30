---
title: Optimera minnesanvändningen vid arbete med stora filer med stora dataset
type: docs
weight: 180
url: /sv/python-net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

När du bygger ett arbetsblad med stora datamängder eller läser en stor Excel-fil är den totala mängden RAM-minne som processen kräver alltid en oro. Det finns åtgärder som kan anpassas för att hantera utmaningen. Aspose.Cells för Python via .NET ger några relevanta alternativ och API-anrop för att sänka, minska och optimera minnesanvändningen. Det kan också hjälpa processen att arbeta effektivare och snabbare.

Använd [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) för att optimera minnesanvändningen för celldata och minska den totala minneskostnaden. När man bygger en stor datamängd för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen ([**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Optimera minne**

### **Läsning av stora Excel-filer**

Det följande exemplet visar hur man läser en stor Microsoft Excel-fil i optimerat läge.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.py" >}}

### **Skrivning av stora Excel-filer**

Det följande exemplet visar hur man skriver en stor datamängd till en arbetsbok i optimerat läge.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-WritingLargeExcelFiles-1.py" >}}

## **Försiktighet**

Standardalternativet, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) tillämpas för alla versioner. För vissa situationer, som att bygga en arbetsbok med en stor datamängd för celler, kan [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) -alternativet optimera minnesanvändningen och minska minneskostnaden för applikationen. Dock kan detta alternativ försämra prestandan i vissa speciella fall som följer.

1. **Åtkomst av celler slumpmässigt och upprepade gånger**: Den mest effektiva sekvensen för att komma åt cellernas samling är cell för cell i en rad, och sedan rad för rad. Särskilt om du får åtkomst till rader/celler via uppräknaren som erhållits från [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/rowcollection) och [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row), kommer prestandan att maximera med [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting).
1. **Infoga & Ta bort celler & rader**: Observera att om det finns många infogning/ta bort-operationer för celler/rader, kommer prestandaförsämringen märkas för *MemoryPreference* läge jämfört med *Normal* läge.
1. **Infogning & Radering av celler & rader**: Observera att om det finns mycket infogning/radering av operationer för celler/rader, kommer prestandanedbrytningen att vara märkbar för *MemoryPreference*-läget jämfört med *Normal*-läget.

{{< app/cells/assistant language="python-net" >}}
