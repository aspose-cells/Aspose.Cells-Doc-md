---
title: Hantera kolumnfilter server händelser
type: docs
weight: 90
url: /sv/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: I den här artikeln introduceras hur man hanterar händelsen för kolumnfilter i GridWeb.
---

{{% alert color="primary" %}} 

Datafiltrering är förmodligen den mest använda Excel-funktionen som gör att du kan filtrera data baserat på ett specifikt kriterium. Filtrerad data visar endast de rader som uppfyller villkoret genom att dölja de rader som inte uppfyller kriterierna.
Aspose.Cells.GridWeb-komponenten möjliggör datafiltrering genom sitt gränssnitt. För att utöka dess funktioner tillhandahåller även Aspose.Cells.GridWeb-komponenten två händelser som kan fungera som återutrop till filtreringsmekanismen som utförs genom GridWeb UI.

{{% /alert %}} 
## **Hantering av serverhändelse vid tillämpning av kolumnfilter**
Det finns två huvudsakliga händelser som beskrivs nedan.

1. OnBeforeColumnFilter: Utlöses innan filtret ska tillämpas på en kolumn.
1. OnAfterColumnFilter: Utlöses efter att filtret har tillämpats på en kolumn.

Här är ASPX-skriptet för komponenten Aspose.Cells.GridWeb för att lägga till och tilldela de tidigare nämnda händelserna.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



Dessa händelser kan användas för att få användbar information om filtreringsprocessen, som kolumnindex och värde på vilket filter ska tillämpas. Följande är en snutt som visar användningen av händelsen OnBeforeColumnFilter för att hämta kolumnindex och värde som användaren har valt på GridWeb UI för filtrering.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


Å andra sidan, om kravet är att få antalet filtrerade rader efter att filtret har tillämpats kan du använda händelsen OnAfterColumnFilter som visas nedan.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

Checka introduktionen till [Arbeta med GridWeb-händelser](/cells/sv/net/aspose-cells-gridweb/working-with-gridweb-events/) tillsammans med några detaljer om hur man hanterar dessa händelser.

{{% /alert %}}
