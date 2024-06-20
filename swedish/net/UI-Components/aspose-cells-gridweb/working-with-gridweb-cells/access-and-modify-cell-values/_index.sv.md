---
title: Åtkomst och Modifiera cellvärde
type: docs
weight: 20
url: /sv/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb, cellvärde, modifiera, värde
description: Denna artikel introducerar hur man får och modifierar cellvärde i GridWeb.
---

{{% alert color="primary" %}} 

[Tillgång till Arbetsbladsceller](/cells/sv/net/aspose-cells-gridweb/access-worksheet-cells/) diskuterar tillgång till celler. Detta ämne utvidgar den diskussionen för att visa hur man får tillgång till och modifierar cellvärden med hjälp av Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Komma åt och ändra ett cells värde**
### **Strängvärden**
Innan man får tillgång till och modifierar värdet på en cell måste man veta hur man får tillgång till celler. För detaljer om de olika tillvägagångssätten för att få tillgång till celler, hänvisa till [Tillgång till Arbetsbladsceller](/cells/sv/net/aspose-cells-gridweb/access-worksheet-cells/).

Varje cell har en egenskap som heter StringValue. När en cell är åtkomst, kan utvecklare använda egenskapen StringValue för att få tillgång till cellernas strängvärde. För att modifiera cellvärden tillhandahålls en särskild metod PutValue, som kan användas för att uppdatera cellens strängvärde.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Alla typer av värden**
PutValue-metoden för ett cellsobjekt har 8 överbelastningar tillgängliga som kan användas för att modifiera vilken typ av värde som helst (Boolean, int, double, DateTime och sträng) i en cell.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Det finns också en överbelastad version av PutValue-metoden som kan ta vilken typ av värde som helst i strängformat och automatiskt konvertera det till en korrekt datatyp. För att detta ska ske, skicka det booleska värdet true till en annan parameter av PutValue-metoden som visas nedan i exemplet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
