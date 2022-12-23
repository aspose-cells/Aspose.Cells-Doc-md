---
title: Optimera minnesanvändning när du arbetar med stora filer med stora datamängder
type: docs
weight: 180
url: /sv/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

När du bygger en arbetsbok med stora datamängder, eller läser en stor Microsoft Excel-fil, är den totala mängden RAM som processen kommer att ta alltid ett problem. Det finns åtgärder som kan anpassas för att klara utmaningen. Aspose.Cells ger några relevanta alternativ och API-anrop för att minska, minska och optimera minnesanvändningen. Det kan också hjälpa processen att fungera mer effektivt och köras snabbare.

 Använd[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)alternativ för att optimera minnesanvändningen för celldata och minska den totala minneskostnaden. När du bygger en stor datamängd för celler kan den spara en viss mängd minne jämfört med att använda standardinställningen ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Optimera minnet**

### **Läsa stora Excel-filer**

Följande exempel visar hur man läser en stor Microsoft Excel-fil i optimerat läge.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Skriva stora Excel-filer**

Följande exempel visar hur man skriver en stor datamängd till ett kalkylblad i ett optimerat läge.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Varning**

 Standardalternativet,[**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)tillämpas för alla versioner. För vissa situationer, som att bygga en arbetsbok med en stor datamängd för celler,[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)alternativet kan optimera minnesanvändningen och minska minneskostnaden för programmet. Det här alternativet kan dock försämra prestandan i vissa speciella fall som följer.

1. **Åtkomst till Cells slumpmässigt och upprepade gånger** : Den mest effektiva sekvensen för att komma åt cellsamlingen är cell för cell i en rad och sedan rad för rad. Speciellt om du får åtkomst till rader/celler av Enumeratorn som hämtats från[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) och[**Rad**](https://reference.aspose.com/cells/net/aspose.cells/row) , skulle prestandan maximeras med[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Infoga & Ta bort Cells & Rader** : Observera att om det finns många insert/delete-operationer för Cells/Rows, kommer prestandaförsämringen att märkas för*Minnespreferens* läge jämfört med*Vanligt*läge.
1. **Fungerar på olika Cell typer** : Om de flesta av cellerna innehåller strängvärden eller formler blir minneskostnaden densamma som*Vanligt* läge men om det finns många tomma celler eller cellvärden är numeriska, bool och så vidare,[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)alternativet ger bättre prestanda.
