---
title: Inaktivera pivottabellribbon
type: docs
weight: 90
url: /sv/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Rapporter baserade på pivottabeller är användbara men benägna för fel om målgruppsanvändare inte har detaljerad kunskap om Excel för att konfigurera dessa rapporter. Under sådana omständigheter vill organisationer begränsa användare från att kunna ändra en rapport baserad på pivottabell. Vanliga pivottabellfunktioner som att lägga till ytterligare filter, slicers, fält eller ändra ordningen på vissa saker i rapporten rekommenderas inte för varje användare. Å andra sidan ska dessa användare också kunna uppdatera rapporten och använda befintliga filter eller slicers. Aspose.Cells har gett den här möjligheten till utvecklare att begränsa användare från att ändra dessa rapporter medan de skapar dessa rapporter. För detta ändamål tillhandahåller Excel en funktion för att inaktivera pivottabellribbon och samma sak tillhandahålls av Aspose.Cells dvs. utvecklaren kan inaktivera ribbon som innehåller kontroller för att modifiera dessa rapporter.

{{% /alert %}}

## **Inaktivera pivottabellribbon med hjälp av PivotTable.EnableWizard**

Följande kod visar den här funktionen genom att komma åt en pivottabell från ett blad och sedan ställa in [**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) till **false**. Provfilen för pivottabell kan laddas ned från denna [länk](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
