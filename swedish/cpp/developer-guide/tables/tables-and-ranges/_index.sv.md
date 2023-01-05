---
title: Tabeller och intervall
type: docs
weight: 30
url: /sv/cpp/tables-and-ranges/
---
## **Introduktion**
Ibland skapar du en tabell i Microsoft Excel och vill inte fortsätta arbeta med tabellfunktionaliteten som den kommer med. Istället vill du ha något som ser ut som ett bord. Om du vill behålla data i en tabell utan att förlora formatering konverterar du tabellen till ett vanligt dataintervall. Aspose.Cells stöder den här funktionen i Microsoft Excel för tabeller och listobjekt.
## **Använder Microsoft Excel**
 Använd**Konvertera till Range** funktion för att snabbt konvertera en tabell till ett intervall utan att förlora formatering. I Microsoft Excel 2007/2010:

1. Klicka var som helst i tabellen för att se till att den aktiva cellen finns i en tabellkolumn.
1.  På**Design** fliken, i**Verktyg** grupp, klicka**Konvertera till Range**.

{{% alert color="primary" %}} 

Tabellfunktionerna är inte längre tillgängliga efter att tabellen har konverterats till ett intervall. Till exempel innehåller radrubriker inte längre sortering- och filterpilarna, och strukturerade referenser (referenser som använder tabellnamn) som användes i formler förvandlas till vanliga cellreferenser.

{{% /alert %}} 
## **Använder Aspose.Cells**
Följande kodavsnitt visar samma funktionalitet med Aspose.Cells.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange.cpp" >}}
