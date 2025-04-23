---
title: Optimera minnesanvändningen vid arbete med stora filer med stora dataset
type: docs
weight: 110
url: /sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

När man bygger en arbetsbok med stora dataset eller läser in en stor Microsoft Excel-fil är den totala mängden RAM som processen tar alltid ett bekymmer. Det finns åtgärder som kan anpassas för att hantera utmaningen. Aspose.Cells tillhandahåller några relevanta alternativ och API-anrop för att minska, minska och optimera minnesanvändningen. Dessutom kan det hjälpa processen att arbeta mer effektivt och köra snabbare.

Använd [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE)-alternativet för att optimera minnet som används för celldata för att minska den totala minneskostnaden. Vid uppbyggnad av stora dataset för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Optimera minne**

### **Läsning av stora Excel-filer**

Det följande exemplet visar hur man läser en stor Microsoft Excel-fil i optimerat läge.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **Skrivning av stora Excel-filer**

Följande exempel visar hur man skriver en stor datamängd till ett kalkylblad i optimerat läge.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **Försiktighet**

Standardalternativet [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) tillämpas för alla versioner. För vissa situationer, som att bygga en arbetsbok med ett stort dataset för celler, kan alternativet [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE) optimera minnesanvändningen och minska minneskostnaden för programmet. Detta alternativ kan emellertid försämra prestandan i vissa specialfall såsom följer.

1. **Åtkomst av celler slumpmässigt och upprepade gånger**: Den mest effektiva sekvensen för att komma åt cellernas samling är cell för cell i en rad, och sedan rad för rad. Särskilt om du får åtkomst till rader/celler via uppräknaren som erhållits från [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) och [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row), kommer prestandan att maximera med [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE).
1. **Infoga & Ta bort celler & rader**: Observera att om det finns många infogningar/raderingar för celler/rader kommer prestandanedgraderingen att vara märkbar för [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE)-läget jämfört med [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)-läget.
1. **Arbete med olika celltyper**: Om de flesta cellerna innehåller strängvärden eller formler kommer minneskostnaden att vara densamma som [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)-läge, men om det finns många tomma celler eller cellvärden är numeriska, booleska och så vidare, kommer [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE)-alternativet att ge bättre prestanda.
{{< app/cells/assistant language="java" >}}
