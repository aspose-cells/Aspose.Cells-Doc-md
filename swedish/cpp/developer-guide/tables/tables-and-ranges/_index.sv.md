---
title: Tabeller och Intervall
type: docs
weight: 30
url: /sv/cpp/tables-and-ranges/
---

## **Introduktion**
Ibland skapar du en tabell i Microsoft Excel och vill inte fortsätta arbeta med tabellfunktionaliteten som medföljer den. Istället vill du ha något som ser ut som en tabell. För att behålla data i en tabell utan att förlora formatering, konvertera tabellen till ett vanligt datarange. Aspose.Cells stöder denna funktion i Microsoft Excels tabeller och listobjekt.
## **Använda Microsoft Excel**
Använd **Konvertera till område**-funktionen för att snabbt konvertera en tabell till en mängd utan att förlora formateringen. I Microsoft Excel 2007/2010:

1. Klicka var som helst i tabellen för att se till att den aktiva cellen är i en tabellkolumn.
1. På fliken **Utformning**, i gruppen **Verktyg**, klicka på **Konvertera till område**.

{{% alert color="primary" %}} 

Tabellfunktionerna är inte längre tillgängliga efter att tabellen har konverterats till en mängd. Till exempel inkluderar radrubrikerna inte längre sorterings- och filterpilar, och strukturerade referenser (referenser som använder tabellnamn) som användes i formler omvandlas till vanliga cellreferenser.

{{% /alert %}} 
## **Använda Aspose.Cells**
Följande kodsnutt visar samma funktionalitet med hjälp av Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
