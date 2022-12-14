---
title: Få åtkomst till och ändra Cell värden
type: docs
weight: 20
url: /sv/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[Åtkomst till arbetsblad Cells](/cells/sv/net/access-worksheet-cells/) diskuterade tillgång till celler. Det här ämnet utökar diskussionen till att visa hur man kommer åt och ändrar cellvärden med Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Få åtkomst till och ändra en Cells värde**
### **Strängvärden**
 Innan du kommer åt och ändrar värdet på en cell måste du veta hur du kommer åt celler. För detaljer om de olika metoderna för att komma åt celler, se[Åtkomst till arbetsblad Cells](/cells/sv/net/access-worksheet-cells/).

Varje cell har en egenskap som heter StringValue. När en cell väl har nåtts kan utvecklare använda egenskapen StringValue för att komma åt cellens strängvärde. För att ändra cellvärden tillhandahålls en speciell metod PutValue, som kan användas för att uppdatera cellens strängvärde.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Alla typer av värden**
PutValue-metoden för en cells objekt har 8 tillgängliga överbelastningar som kan användas för att modifiera vilken typ av värde som helst (Boolean, int, double, DateTime och string) i en cell.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Det finns också en överbelastad version av PutValue-metoden som kan ta vilken typ av värde som helst i strängformat och konvertera det till en korrekt datatyp automatiskt. För att få det att hända, skicka det booleska värdet true till en annan parameter i PutValue-metoden som visas nedan i exemplet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
