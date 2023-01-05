---
title: Inaktivera pivottabellsband
type: docs
weight: 40
url: /sv/java/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

Pivottabellbaserade rapporter är användbara men risk för fel om målanvändare inte har detaljerad kunskap om Excel för att konfigurera dessa rapporter. Under dessa omständigheter kommer organisationer att vilja begränsa användare från att kunna ändra en pivottabellbaserad rapport. Vanliga pivottabellfunktioner som att lägga till ytterligare filter, skivare, fält eller ändra ordningen på vissa saker i rapporten rekommenderas oftast inte för alla användare. Å andra sidan ska dessa användare också kunna uppdatera rapporten och använda befintliga filter eller slicers. Aspose.Cells har tillhandahållit denna möjlighet till utvecklare för att hindra användare från att ändra dessa rapporter medan de skapar dessa rapporter. För detta ändamål tillhandahåller Excel en funktion för att inaktivera pivottabellen men detsamma tillhandahålls av Aspose.Cells, dvs utvecklaren kan inaktivera menyfliksområdet som innehåller kontroller för att ändra dessa rapporter.

{{% /alert %}}

## **Inaktivera Pivot Table Ribbon med PivotTable.setEnableWizard**

Följande kod demonstrerar denna funktion genom att komma åt en pivottabell från ett ark och sedan anropa[**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) för att ställa in denna flagga**falsk** . Exempel på pivottabellsfil kan laddas ner från denna[länk](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
