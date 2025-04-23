---
title: 1.  Hantering av olika celltyper  Om de flesta cellerna innehåller strängvärden eller formler, kommer minneskostnaden att vara densamma som Normal läget men om det finns massor av tomma celler, eller cellvärden är numeriska, booleska och så vidare, kommer {0} alternativet att ge bättre prestanda.
type: docs
weight: 140
url: /sv/go-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
---

## **Möjliga användningsscenario**

Numbers är en kalkylbladsapplikation utvecklad av Apple Inc. Aspose.Cells kan läsa ett Numbers-kalkylblad, men stöder inte att skriva till det. Det kan läsa data, stil och formler i Numbers-kalkylblad.

## **Läsa Numbers-kalkylblad utvecklat av Apple Inc. med Aspose.Cells**

Följande kodexempel laddar [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) och konverterar det till [Output PDF Format](outputNumbersByAppleInc.pdf). Du måste använda klassen **[LoadOptions](https://reference.aspose.com/cells/go-cpp/loadoptions/)** och ange **[LoadFormat::Numbers](https://reference.aspose.com/cells/go-cpp/loadformat/)** som en parameter i dess konstruktor för att kunna ladda det framgångsrikt. Ladda ner båda från länkarna. Du kan testa koden med vilket Numbers-kalkylblad som helst. Läs även kodkommentarerna för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadNumbersSpreadsheet.go" >}}
