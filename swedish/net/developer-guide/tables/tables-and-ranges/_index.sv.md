---
title: Tabeller och Intervall
type: docs
weight: 50
url: /sv/net/tables-and-ranges/
---

## **Introduktion**

Ibland skapar du en tabell i Microsoft Excel och vill inte fortsätta arbeta med tabellfunktionaliteten den kommer med. Istället vill du ha något som ser ut som en tabell. För att behålla data i en tabell utan att förlora formateringen, konvertera tabellen till en vanlig datamängd.
Aspose.Cells stöder denna funktion i Microsoft Excel för tabeller och listobjekt.

## **Använda Microsoft Excel**

Använd **Konvertera till område**-funktionen för att snabbt konvertera en tabell till en mängd utan att förlora formateringen. I Microsoft Excel 2007/2010:

1. Klicka var som helst i tabellen för att se till att den aktiva cellen är i en tabellkolumn.
1. På fliken **Utformning**, i gruppen **Verktyg**, klicka på **Konvertera till område**.

## **Använda Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

Tabellfunktionerna är inte längre tillgängliga efter att tabellen har konverterats till en mängd. Till exempel inkluderar radrubrikerna inte längre sorterings- och filterpilar, och strukturerade referenser (referenser som använder tabellnamn) som användes i formler omvandlas till vanliga cellreferenser.

{{% /alert %}}

## **Konvertera tabell till område med alternativ.**

Aspose.Cells tillhandahåller ytterligare alternativ när du konverterar tabell till intervall genom klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions). Klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) tillhandahåller egenskapen [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow) som gör att du kan ange den sista indexet för tabellraden. Tabellformateringen behålls upp till det angivna radindexet och resten av formateringen tas bort.

Den angivna provkoden nedan visar användningen av klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
