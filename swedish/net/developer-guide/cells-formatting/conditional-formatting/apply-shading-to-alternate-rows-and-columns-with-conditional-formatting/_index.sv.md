---
title: Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering
description: Hur man använder Aspose.Cells biblioteket i C# för att tillämpa villkorlig formateringsskuggor för alternerande rader och kolumner. Genom att justera dessa kriterier har du mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells, Betingad formatering, C#, Växelrader, Växelkolumner, Skuggor
type: docs
weight: 30
url: /sv/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API:er ger möjligheten att lägga till och manipulera betingad formateringsregler för [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-objektet. Dessa regler kan anpassas på flera sätt för att få önskad formatering baserat på villkor eller regler. Denna artikel kommer att visa användningen av Aspose.Cells for .NET API:er för att applicera nyanser på växelrader och kolumner med hjälp av betingad formatering och Excels inbyggda funktioner.

{{% /alert %}}

Denna artikel använder Excels inbyggda funktioner såsom RAD, KOLUMN och MOD. Här är några detaljer om dessa funktioner för en bättre förståelse av kodsnutten som följer.

- **RAD()**-funktionen returnerar radnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där RAD-funktionen har skrivits in.
- **KOLUMN()**-funktionen returnerar kolumnnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där KOLUMN-funktionen har skrivits in.
- **MOD()**-funktionen returnerar resten efter att ett nummer har delats av en divisor, där det första parametern till funktionen är det numeriska värdet vars rest du vill hitta och det andra parametern är det tal som används för att dela in i nummerparametern. Om divisorn är 0 kommer den att returnera felen #DIV/0!.

Låt oss börja skriva lite kod för att uppnå detta mål med hjälp av Aspose.Cells for .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

Följande ögonblicksbild visar det resulterande kalkylarket som är laddat i Excel-applikationen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

För att applicera nyanser på alternativa kolumner, behöver du bara ändra formeln **=MOD(RAD(),2)=0** till **=MOD(KOLUMN(),2)=0**, det vill säga; istället för att få radindexet, modifiera formeln för att hämta kolumnindexet. 
Det resulterande kalkylarket kommer i detta fall att se ut som följer.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="csharp" >}}
