---
title: Sortera Kalkylbladsdata
type: docs
weight: 80
url: /sv/net/aspose-cells-gridweb/sort-worksheet-data/
keywords: GridWeb,sortera
description: Den här artikeln introducerar hur man sorterar data i GridWeb.
---

{{% alert color="primary" %}} 

Att sortera är en mycket värdefull funktion när det gäller datahantering. Osorterad data är smärtsamt för användare när de söker efter specifik information. Aspose.Cells.GridWeb stödjer kraftfulla sorteringsfunktioner. Det här ämnet diskuterar sortering av data med hjälp av Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Sortera Data**
Aspose.Cells.GridWeb tillåter utvecklare att sortera data horisontellt och vertikalt så att utvecklare kan sortera data uppifrån och ner eller från vänster till höger.
### **Från Uppifrån och Ner**
För att sortera data från upptill och ner orientering:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
1. Kom åt kalkylbladet som du vill sortera.
1. Sortera dataområdet i valfri ordning (stigande eller fallande). Se till att välja upptill och ner orientering.

Exemplet nedan sorterar data i fyra kolumner på ett kalkylblad i fallande ordning. Endast tjugo rader av de fyra kolumnerna är sorterade i upptill och ner orientering.

Innan du tillämpar koden innehåller kalkylbladet ostrukturerad data.

![todo:image_alt_text](sort-worksheet-data_1.png)

Efter att koden har körts är datan sorterad i stigande ordning.

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **Från Vänster till Höger**
För att sortera data från vänster till höger:

1. Lägg till Aspose.Cells.GridWeb-kontrollen i ditt webbformulär.
1. Kom åt kalkylbladet som du vill sortera.
1. Sortera dataområdet i valfri ordning (stigande eller fallande). Se till att välja vänster till höger orientering.

Exemplet nedan sorterar data i fyra rader i stigande ordning. Endast fyra rader av sju kolumner sorteras från vänster till höger.

Innan du tillämpar koden innehåller kalkylbladet ostrukturerad data.

![todo:image_alt_text](sort-worksheet-data_3.png)

Efter att koden har körts är datan sorterad i stigande ordning.

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: Ovanstående exempel visar sortering av data baserat på en kolumn (uppifrån och ner) eller rad (vänster till höger). Aspose.Cells.GridWeb kan också sortera data enligt mer än en kolumn eller rad. För att göra det, skicka en array av kolumn- eller radindex till Sort-metoden. Hybriddatatypsortering stöds också.

{{% /alert %}}
