---
title: Optimera minnesanvändningen vid arbete med stora filer med stora dataset
type: docs
weight: 110
url: /sv/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

När man bygger en arbetsbok med stora dataset eller läser in en stor Microsoft Excel-fil är den totala mängden RAM som processen tar alltid ett bekymmer. Det finns åtgärder som kan anpassas för att hantera utmaningen. Aspose.Cells tillhandahåller några relevanta alternativ och API-anrop för att minska, minska och optimera minnesanvändningen. Dessutom kan det hjälpa processen att arbeta mer effektivt och köra snabbare.

Använd [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-alternativet för att optimera minnet som används för celldata för att minska den totala minneskostnaden. Vid uppbyggnad av stora dataset för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).

{{% /alert %}}

## **Optimera minne**

Följande exempel visar hur man optimerar minnesanvändningen vid arbete med stora data i Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "OptimizingMemory.js" >}}

## **Försiktighet**

Standardalternativet [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) tillämpas för alla versioner. För vissa situationer, som att bygga en arbetsbok med ett stort dataset för celler, kan alternativet [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) optimera minnesanvändningen och minska minneskostnaden för programmet. Detta alternativ kan emellertid försämra prestandan i vissa specialfall såsom följer.

1. **Åtkomst av celler slumpmässigt och upprepade gånger**: Den mest effektiva sekvensen för att komma åt cellernas samling är cell för cell i en rad, och sedan rad för rad. Särskilt om du får åtkomst till rader/celler via uppräknaren som erhållits från [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) och [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), kommer prestandan att maximera med [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).
1. **Infoga & Ta bort celler & rader**: Observera att om det finns många infogningar/raderingar för celler/rader kommer prestandanedgraderingen att vara märkbar för [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-läget jämfört med [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-läget.
1. **Arbete med olika celltyper**: Om de flesta cellerna innehåller strängvärden eller formler kommer minneskostnaden att vara densamma som [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-läge, men om det finns många tomma celler eller cellvärden är numeriska, booleska och så vidare, kommer [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)-alternativet att ge bättre prestanda.

{{< app/cells/assistant language="nodejs-cpp" >}}
