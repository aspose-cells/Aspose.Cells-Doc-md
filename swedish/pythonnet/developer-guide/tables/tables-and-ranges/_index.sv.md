---
title: Tabeller och Intervall
type: docs
weight: 50
url: /sv/python-net/tables-and-ranges/
---

## **Introduktion**

Ibland skapar du en tabell i Microsoft Excel och vill inte fortsätta arbeta med tabellfunktionaliteten den kommer med. Istället vill du ha något som ser ut som en tabell. För att behålla data i en tabell utan att förlora formateringen, konvertera tabellen till en vanlig datamängd.
Aspose.Cells för Python via .NET stöder denna funktion för Microsoft Excels tabeller och listobjekt.

## **Använda Microsoft Excel**

Använd **Konvertera till område**-funktionen för att snabbt konvertera en tabell till en mängd utan att förlora formateringen. I Microsoft Excel 2007/2010:

1. Klicka var som helst i tabellen för att se till att den aktiva cellen är i en tabellkolumn.
1. På fliken **Utformning**, i gruppen **Verktyg**, klicka på **Konvertera till område**.

## **Användning av Aspose.Cells för Python via .NET**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

Tabellfunktionerna är inte längre tillgängliga efter att tabellen har konverterats till en mängd. Till exempel inkluderar radrubrikerna inte längre sorterings- och filterpilar, och strukturerade referenser (referenser som använder tabellnamn) som användes i formler omvandlas till vanliga cellreferenser.

{{% /alert %}}

## **Konvertera tabell till område med alternativ.**

Aspose.Cells för Python via .NET erbjuder ytterligare alternativ vid konvertering av tabell till område via [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions)-klassen. Klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) tillhandahåller [**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/)-egenskapen som gör att du kan ange det sista indexet för tabellens rad. Formateringen av tabellen kommer att behållas upp till angivet radindex och resten av formateringen tas bort.

Den angivna provkoden nedan visar användningen av klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
