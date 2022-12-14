---
title: Använda funktioner på klientsidan för att välja intervall eller hämta det valda intervallet i GridWeb
type: docs
weight: 60
url: /sv/net/using-client-side-functions-to-select-range-or-get-the-selected-range-in-gridweb/
---
{{% alert color="primary" %}} 

Du kan använda följande funktioner på klientsidan för att välja ett intervall eller för att hämta det valda intervallet i en GridWeb med JavaScript.

- getSelectRange()
- setSelectRange()
- clearSelections()

getSelectRange() returnerar det senast valda intervallet. setSelectRange() väljer det givna intervallet. clearSelections() rensar alla markeringar exklusive aktuell aktiv cell.

{{% /alert %}} 
## **Använda klientsidans funktioner för att välja ett intervall eller för att få det valda intervallet i en GridWeb med JavaScript**
Följande kod förklarar användningen av dessa funktioner.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingClientSideRangeFunctions-UsingRangeFunctions.aspx" >}}
