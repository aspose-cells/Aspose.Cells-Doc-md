---
title: Inaktivera pivottabellribbon
type: docs
weight: 90
url: /sv/nodejs-cpp/disable-pivot-table-ribbons/
description: Hur man inaktiverar PivotTabellBand med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells för Node.js Excel, Node.js Excel bibliotek, Inaktivera PivotTabellband med Aspose.Cells for Node.js via C++ Excel bibliotek.
---

{{% alert color="primary" %}}

Rapporter baserade på pivottabeller är användbara men kan vara felaktiga om målarna inte har detaljerad kunskap om Excel för att konfigurera dessa rapporter. I dessa situationer vill organisationer begränsa användarnas möjlighet att ändra en pivottabellbaserad rapport. Vanliga funktioner i pivottabellen som att lägga till ytterligare filter, skivor, fält eller ändra ordningen på vissa saker i rapporten rekommenderas inte för alla användare. Å andra sidan ska dessa användare kunna uppdatera rapporten och använda befintliga filter eller skivor. Aspose.Cells for Node.js via C++ har gett utvecklare denna möjlighet att begränsa användare från att ändra dessa rapporter när de skapar dem. För detta ändamål erbjuder Excel en funktion för att inaktivera pivottabellbandet, och samma funktion tillhandahålls av Aspose.Cells for Node.js via C++, dvs. utvecklaren kan inaktivera bandet som innehåller kontroller för att modifiera dessa rapporter.

{{% /alert %}}

## **Hur man inaktiverar pivottabellbandet med Aspose.Cells for Node.js via C++**

Följande kod visar den här funktionen genom att komma åt en pivottabell från ett blad och sedan ställa in [**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-) till **false**. Provfilen för pivottabell kan laddas ned från denna [länk](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
