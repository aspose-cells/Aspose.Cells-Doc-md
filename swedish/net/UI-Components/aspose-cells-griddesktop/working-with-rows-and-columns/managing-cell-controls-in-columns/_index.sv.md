---
title: Hantera Cell kontroller i kolumner
type: docs
weight: 100
url: /sv/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

Det här ämnet diskuterar några viktiga koncept för att hantera cellkontroller i kolumner med Aspose.Cells.GridDesktop API. Vi kommer att förklara hur utvecklare kan komma åt, ändra och ta bort cellkontroller från kolumnerna i deras kalkylblad. Låt oss ta en titt på det.

{{% /alert %}} 
## **Åtkomst till Cell kontroller**
 För att komma åt och ändra en befintlig cellkontroll i kolumnen kan utvecklare använda egenskapen CellControl för a**Aspose.Cells.GridDesktop.Data.GridColumn** . När en cellkontroll väl har nåtts kan utvecklare ändra dess egenskaper under körning. Till exempel, i exemplet nedan, har vi kommit åt en befintlig**Kryssruta** cellkontroll från en specifik**Aspose.Cells.GridDesktop.Data.GridColumn** och ändrade dess kontrollerade egenskap.

**VIKTIG:** CellControl-egenskapen tillhandahåller en cellkontroll i form av**CellControl**objekt. Så, om du behöver komma åt en specifik typ av cellkontroll, säg**Kryssruta** då måste du typcasta**CellControl** invända mot**Kryssruta** klass.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **Ta bort Cell kontroller**
 För att ta bort en befintlig cellkontroll kan utvecklare helt enkelt komma åt ett önskat kalkylblad och sedan**Ta bort** cellkontrollen från den specifika kolumnen genom att använda**Ta bortCellControl** metod av**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

 Varje kolumn i**Kolumner** samling av**Arbetsblad** representeras av en instans av**Aspose.Cells.GridDesktop.Data.GridColumn** klass.

{{% /alert %}}
