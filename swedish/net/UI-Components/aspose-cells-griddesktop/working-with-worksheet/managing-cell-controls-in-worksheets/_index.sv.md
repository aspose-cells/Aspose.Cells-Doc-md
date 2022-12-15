---
title: Hantera Cell Kontroller i arbetsblad
type: docs
weight: 130
url: /sv/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

Det här ämnet diskuterar några viktiga koncept för att hantera cellkontroller med hjälp av API eller Aspose.Cells.GridDesktop. Vi kommer att förklara hur utvecklare kan komma åt, ändra och ta bort cellkontroller från sina kalkylblad. Låt oss ta en titt på det.

{{% /alert %}} 
## **Åtkomst till Cell kontroller**
 För att komma åt och ändra en befintlig cellkontroll i kalkylbladet kan utvecklare komma åt en specifik cellkontroll från**Kontroller** samling av**Arbetsblad** genom att ange cellen (med cellnamn eller dess plats i termer av rad- och kolumnnummer) där cellkontrollen visas. När en cellkontroll väl har nåtts kan utvecklare ändra dess egenskaper under körning. Till exempel, i exemplet nedan, har vi kommit åt en befintlig**Kryssruta** cellstyrning från**Arbetsblad** och ändrade dess kontrollerade egenskap.

**VIKTIG:** **Kontroller** samling innehåller alla typer av cellkontroller i form av**CellControl** objekt. Så, om du behöver komma åt en specifik typ av cellkontroll, säg**Kryssruta** då måste du typcasta**CellControl** invända mot**Kryssruta** klass.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **Ta bort Cell kontroller**
 För att ta bort en befintlig cellkontroll kan utvecklare helt enkelt komma åt ett önskat kalkylblad och sedan**Ta bort** cellkontrollen från**Kontroller** samling av**Arbetsblad** genom att ange cellen (med dess namn eller rad- och kolumnnummer) som innehåller cellkontroll.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
