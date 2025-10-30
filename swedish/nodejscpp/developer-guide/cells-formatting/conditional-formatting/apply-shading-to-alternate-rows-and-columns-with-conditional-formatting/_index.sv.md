---
title: Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering
linktitle: Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering
description: Hur man använder Aspose.Cells biblioteket i Node.js via C++ för att tillämpa villkorsskuggning för alternerande rader och kolumner. Genom att justera dessa kriterier får du mer kontroll över hur celler ser ut och framträder.
keywords: Aspose.Cells, Villkorsstyrd formatering, Node.js via C++, Alternativa rader, Alternativa kolumner, Skuggor
type: docs
weight: 30
url: /sv/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API:er ger möjligheten att lägga till och manipulera villkorsstyrda formateringsregler för [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-objektet. Dessa regler kan skräddarsys på många sätt för att få önskad formatering baserat på villkor eller regler. Denna artikel visar hur man använder API:erna Aspose.Cells for Node.js via C++ för att applicera skuggning på alternativa rader och kolumner med hjälp av villkorsstyrda formateringsregler och Excels inbyggda funktioner.

{{% /alert %}}

Denna artikel använder Excels inbyggda funktioner såsom RAD, KOLUMN och MOD. Här är några detaljer om dessa funktioner för en bättre förståelse av kodsnutten som följer.

- **RAD()** funktionen returnerar radnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där RAD()-funktionen har använts.
- **KOLON()** funktionen returnerar kolumnnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där KOLON()-funktionen har använts.
- **MOD()**-funktionen returnerar resten efter att ett nummer har delats av en divisor, där det första parametern till funktionen är det numeriska värdet vars rest du vill hitta och det andra parametern är det tal som används för att dela in i nummerparametern. Om divisorn är 0 kommer den att returnera felen #DIV/0!.

Låt oss börja skriva lite kod för att uppnå detta mål med hjälp av API:et Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyShadingToAlternateRowsAndColumns.js" >}}


Följande ögonblicksbild visar det resulterande kalkylarket som är laddat i Excel-applikationen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

För att applicera nyanser på alternativa kolumner, behöver du bara ändra formeln **=MOD(RAD(),2)=0** till **=MOD(KOLUMN(),2)=0**, det vill säga; istället för att få radindexet, modifiera formeln för att hämta kolumnindexet.  
Det resulterande kalkylarket kommer i detta fall att se ut som följer.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="nodejs-cpp" >}}
