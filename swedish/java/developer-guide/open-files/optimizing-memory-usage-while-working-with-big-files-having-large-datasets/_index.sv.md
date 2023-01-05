---
title: Optimera minnesanvändning när du arbetar med stora filer med stora datamängder
type: docs
weight: 110
url: /sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

När du bygger en arbetsbok med stora datamängder, eller läser en stor Microsoft Excel-fil, är den totala mängden RAM som processen kommer att ta alltid ett problem. Det finns åtgärder som kan anpassas för att klara utmaningen. Aspose.Cells ger några relevanta alternativ och API-anrop för att minska, minska och optimera minnesanvändningen. Det kan också hjälpa processen att arbeta mer effektivt och köra snabbare.

 Använda sig av[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) alternativ för att optimera minne som används för celldata för att minska den totala minneskostnaden. När du bygger stora datamängder för celler kan det spara en viss mängd minne jämfört med att använda standardinställningen[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Optimera minnet**

### **Läsa stora Excel-filer**

Följande exempel visar hur man läser en stor Microsoft Excel-fil i optimerat läge.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **Skriva stora Excel-filer**

Följande exempel visar hur man skriver en stor datamängd till ett kalkylblad i optimerat läge.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **Varning**

 Standardalternativet,[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)tillämpas för alla versioner. För vissa situationer, som att bygga en arbetsbok med en stor datamängd för celler,[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)alternativet kan optimera minnesanvändningen och minska minneskostnaden för programmet. Det här alternativet kan dock försämra prestandan i vissa speciella fall som följer.

1. **Åtkomst till Cells slumpmässigt och upprepade gånger** : Den mest effektiva sekvensen för att komma åt cellsamlingen är cell för cell i en rad och sedan rad för rad. Speciellt om du får åtkomst till rader/celler av Enumeratorn som hämtats från[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) och[**Rad**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) , skulle prestandan maximeras med[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Infoga & Ta bort Cells & Rader** : Observera att om det finns många insert/delete-operationer för Cells/Rows, kommer prestandaförsämringen att märkas för[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) läge jämfört med[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)läge.
1. **Fungerar på olika Cell typer** : Om de flesta av cellerna innehåller strängvärden eller formler blir minneskostnaden densamma som[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)läge men om det finns många tomma celler eller cellvärden är numeriska, bool och så vidare,[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)alternativet ger bättre prestanda.
