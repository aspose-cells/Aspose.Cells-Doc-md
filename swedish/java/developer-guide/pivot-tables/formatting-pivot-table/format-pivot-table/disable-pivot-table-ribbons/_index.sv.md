---
title: Inaktivera pivottabellribbon
type: docs
weight: 40
url: /sv/java/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Rapporter baserade på pivottabeller är användbara men benägna för fel om målgruppsanvändare inte har detaljerad kunskap om Excel för att konfigurera dessa rapporter. Under sådana omständigheter vill organisationer begränsa användare från att kunna ändra en rapport baserad på pivottabell. Vanliga pivottabellfunktioner som att lägga till ytterligare filter, slicers, fält eller ändra ordningen på vissa saker i rapporten rekommenderas inte för varje användare. Å andra sidan ska dessa användare också kunna uppdatera rapporten och använda befintliga filter eller slicers. Aspose.Cells har gett den här möjligheten till utvecklare att begränsa användare från att ändra dessa rapporter medan de skapar dessa rapporter. För detta ändamål tillhandahåller Excel en funktion för att inaktivera pivottabellribbon och samma sak tillhandahålls av Aspose.Cells dvs. utvecklaren kan inaktivera ribbon som innehåller kontroller för att modifiera dessa rapporter.

{{% /alert %}}

## **Inaktivera Pivot Table Ribbon med hjälp av PivotTable.setEnableWizard**

Följande kod demonstrerar denna funktion genom att komma åt en pivot-tabell från ett blad och sedan anropa [**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) för att sätta denna flagga till **false**. Exempelpivot-tabellsfil kan hämtas från denna [länk](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
{{< app/cells/assistant language="java" >}}
