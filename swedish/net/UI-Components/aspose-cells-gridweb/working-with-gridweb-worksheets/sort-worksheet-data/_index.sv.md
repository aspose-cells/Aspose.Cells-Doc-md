---
title: Sortera kalkylbladsdata
type: docs
weight: 80
url: /sv/net/sort-worksheet-data/
---
{{% alert color="primary" %}} 

Sortering är en mycket värdefull funktion när det kommer till databehandling. Osorterade data är jobbigt för användare när de söker efter specifik information. Aspose.Cells.GridWeb stöder kraftfulla sorteringsfunktioner. Det här ämnet diskuterar sortering av data med hjälp av Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Sortering av data**
Aspose.Cells.GridWeb låter utvecklare sortera data horisontellt och vertikalt så att utvecklare kan sortera data från topp till botten eller vänster till höger.
### **Från topp till tå**
Så här sorterar du data från topp till botten:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Öppna kalkylbladet som du vill sortera.
1. Sortera dataintervallet i valfri ordning (stigande eller fallande). Var noga med att välja topp till botten orientering.

Exemplet nedan sorterar data i fyra kolumner i ett kalkylblad i fallande ordning. Endast tjugo rader av de fyra kolumnerna är sorterade i topp till botten orientering.

Innan du använder koden innehåller kalkylbladet oordnade data.

![todo:image_alt_text](sort-worksheet-data_1.png)

Efter exekvering av koden sorteras data i stigande ordning.

![todo:image_alt_text](sort-worksheet-data_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortTopToBottom.cs" >}}
### **Från vänster till höger**
Så här sorterar du data från vänster till höger:

1. Lägg till Aspose.Cells.GridWeb-kontrollen till ditt webbformulär.
1. Öppna kalkylbladet som du vill sortera.
1. Sortera dataintervallet i valfri ordning (stigande eller fallande). Var noga med att välja vänster till höger.

Exemplet nedan sorterar data i fyra rader i stigande ordning. Endast fyra rader med sju kolumner sorteras från vänster till höger.

Innan du använder koden innehåller kalkylbladet oordnade data.

![todo:image_alt_text](sort-worksheet-data_3.png)

Efter exekvering av koden sorteras data i stigande ordning.

![todo:image_alt_text](sort-worksheet-data_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-SortData.aspx-SortLeftToRight.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: Exemplen ovan visar sorteringsdata på basis av en kolumn (uppifrån och ned) eller rad (vänster till höger). Aspose.Cells.GridWeb kan också sortera data efter mer än en kolumn eller rad. För att göra det, skicka en matris med kolumn- eller radindex till sorteringsmetoden. Hybrid sortering av datatyper stöds också.

{{% /alert %}}
