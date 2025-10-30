---
title: Inaktivera banderoller för pivottabell med Golang via C++
linktitle: Inaktivera pivottabellribbon
type: docs
weight: 90
url: /sv/go-cpp/disable-pivot-table-ribbons/
description: Lär dig hur man avaktiverar pivot tabellflikar i Excel filer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Pivot-tabellbaserade rapporter är användbara men sårbara för fel om målbrukare inte har tillräcklig kunskap om Excel för att konfigurera dessa rapporter. I dessa fall vill organisationer begränsa användare från att kunna ändra en pivot-tabellbaserad rapport. Vanliga funktioner som att lägga till ytterligare filter, slicers, fält eller ändra ordningen i rapporten rekommenderas ofta inte för alla användare. Å andra sidan ska dessa användare också kunna uppdatera rapporten och använda befintliga filter eller slicers. Aspose.Cells har gett utvecklare möjligheten att begränsa användare från att ändra dessa rapporter under skapandet. För detta ändamål erbjuder Excel en funktion att inaktivera pivot-tabellfliken, och detta stöds även av Aspose.Cells. Utvecklare kan inaktivera fliken som innehåller kontroller för att ändra dessa rapporter.

{{% /alert %}}

## **Inaktivera pivottabellribbon med hjälp av PivotTable.EnableWizard**

Följande kod demonstrerar denna funktion genom att komma åt en pivot-tabell från ett blad och sedan ställa in [**GetEnableWizard()**](https://reference.aspose.com/cells/go-cpp/pivottable/getenablewizard/) till **falskt**. En exempel-pivot-tabell kan laddas ner från denna [länk](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisablePivotTableRibbons.go" >}}
