---
title: Inaktivera pivottabellsband
type: docs
weight: 90
url: /sv/net/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

Pivottabellbaserade rapporter är användbara men risk för fel om målanvändare inte har detaljerad kunskap om Excel för att konfigurera dessa rapporter. Under dessa omständigheter kommer organisationer att vilja begränsa användare från att kunna ändra en pivottabellbaserad rapport. Vanliga pivottabellfunktioner som att lägga till ytterligare filter, skivare, fält eller ändra ordningen på vissa saker i rapporten rekommenderas oftast inte för alla användare. Å andra sidan ska dessa användare också kunna uppdatera rapporten och använda befintliga filter eller slicers. Aspose.Cells har tillhandahållit denna möjlighet till utvecklare för att hindra användare från att ändra dessa rapporter medan de skapar dessa rapporter. För detta ändamål tillhandahåller Excel en funktion för att inaktivera pivottabellen men detsamma tillhandahålls av Aspose.Cells, dvs utvecklaren kan inaktivera menyfliksområdet som innehåller kontroller för att ändra dessa rapporter.

{{% /alert %}}

## **Inaktivera Pivot Table Ribbon med PivotTable.EnableWizard**

Följande kod demonstrerar denna funktion genom att komma åt en pivottabell från ett ark och sedan ställa in[**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) till**falsk** . Exempel på pivottabellsfil kan laddas ner från denna[länk](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
