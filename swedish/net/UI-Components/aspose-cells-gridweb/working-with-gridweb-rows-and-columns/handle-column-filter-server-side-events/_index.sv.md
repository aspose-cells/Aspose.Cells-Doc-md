---
title: Hantera kolumnfilterserversidehändelser
type: docs
weight: 90
url: /sv/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

Datafiltrering är förmodligen den mest använda Excel-funktionen som låter dig filtrera data baserat på ett specifikt kriterium. Filtrerad data visar endast de rader som uppfyller villkoret genom att dölja de rader som inte uppfyller kriterierna.
Aspose.Cells.GridWeb-komponenten ger möjlighet att utföra datafiltrering med hjälp av dess gränssnitt. För att utöka dess kapacitet tillhandahåller Aspose.Cells.GridWeb-komponenten också två händelser som kan fungera som återuppringning till filtreringsmekanismen som görs genom GridWeb-gränssnittet.

{{% /alert %}} 
## **Hantera serversideshändelse vid tillämpning av kolumnfilter**
Det finns två huvudhändelser som beskrivs nedan.

1. OnBeforeColumnFilter: Utlöses innan filtret kommer att tillämpas på en kolumn.
1. OnAfterColumnFilter: Utlöses efter att filtret har applicerats på en kolumn.

Här är ASPX-skriptet för Aspose.Cells.GridWeb-komponenten för att lägga till och tilldela ovannämnda händelser.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Dessa händelser kan användas för att få användbar information om filtreringsprocessen såsom kolumnindex och värde på vilket filter måste tillämpas. Följande är utdraget som visar användningen av OnBeforeColumnFilter-händelsen för att hämta kolumnindexet och värdet som användaren har valt på GridWeb UI för filtrering.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


Å andra sidan, om kravet är att få antal filtrerade rader efter att filtret har tillämpats kan du använda händelsen OnAfterColumnFilter som visas nedan.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

 Kolla introduktionen till alla[Arbeta med GridWeb Events](/cells/sv/net/working-with-gridweb-events/) tillsammans med några detaljer om hur man hanterar dessa händelser.

{{% /alert %}}
