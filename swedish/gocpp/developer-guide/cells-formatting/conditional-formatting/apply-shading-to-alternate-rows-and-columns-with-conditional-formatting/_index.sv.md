---
title: Tillämpa skuggning på varannan rad och kolumn med villkorlig formatering med Golang via C++
linktitle: Tillämpa skuggning på varannan rad och kolumn
description: Hur man använder Aspose.Cells biblioteket i C++ för att tillämpa villkorsskuggningar för varannan rad och kolumn. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och visas.
keywords: Aspose.Cells, Villkorsformatering, C++, Varannan rad, Varannan kolumn, Skuggor
type: docs
weight: 30
url: /sv/go-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API:er möjliggör att lägga till och manipulera villkorsformateringsregler för [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/)-objektet. Dessa regler kan anpassas på flera sätt för att få önskad formatering baserat på villkor eller regler. Denna artikel visar hur man använder API:erna Aspose.Cells for C++ för att tillämpa skuggning på varannan rad och kolumn med hjälp av villkorsformatering och Excels inbyggda funktioner.

{{% /alert %}}

Denna artikel använder Excels inbyggda funktioner såsom RAD, KOLUMN och MOD. Här är några detaljer om dessa funktioner för en bättre förståelse av kodsnutten som följer.

- **RAD()**-funktionen returnerar radnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där RAD-funktionen har skrivits in.
- **KOLUMN()**-funktionen returnerar kolumnnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där KOLUMN-funktionen har skrivits in.
- **MOD()**-funktionen returnerar resten efter att ett nummer har delats av en divisor, där det första parametern till funktionen är det numeriska värdet vars rest du vill hitta och det andra parametern är det tal som används för att dela in i nummerparametern. Om divisorn är 0 kommer den att returnera felen #DIV/0!.

Låt oss börja skriva kod för att uppnå detta mål med hjälp av API:erna Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyShadingToAlternateRowsAndColumnsWithConditionalFormatting.go" >}}
Följande ögonblicksbild visar det resulterande kalkylarket som är laddat i Excel-applikationen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

För att applicera nyanser på alternativa kolumner, behöver du bara ändra formeln **=MOD(RAD(),2)=0** till **=MOD(KOLUMN(),2)=0**, det vill säga; istället för att få radindexet, modifiera formeln för att hämta kolumnindexet. 
Det resulterande kalkylarket kommer i detta fall att se ut som följer.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
