---
title: Tillämpa skuggning på alternerande rader och kolumner med villkorlig formatering
description: Hur man använder Aspose.Cells biblioteket i Python för att tillämpa villkorsskuggning för skiftande rader och kolumner i villkorsformatering. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och framstår.
keywords: Aspose.Cells, Villkorsformatering, Python Skiftande rader, Skiftande kolumner, Skuggor
type: docs
weight: 30
url: /sv/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET API:er ger möjligheten att lägga till och manipulera villkorsformateringsregler för [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) objektet. Dessa regler kan anpassas på flera sätt för att få önskad formatering baserat på villkor eller regler. Denna artikel visar hur man använder Aspose.Cells för Python via .NET API:er för att applicera skuggning på skiftande rader och kolumner med hjälp av villkorsformateringsregler och Excels inbyggda funktioner.

{{% /alert %}}

Denna artikel använder Excels inbyggda funktioner såsom RAD, KOLUMN och MOD. Här är några detaljer om dessa funktioner för en bättre förståelse av kodsnutten som följer.

- **RAD()**-funktionen returnerar radnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där RAD-funktionen har skrivits in.
- **KOLUMN()**-funktionen returnerar kolumnnumret för en cellreferens. Om referensparametern utelämnas, antar den att referensen är celladressen där KOLUMN-funktionen har skrivits in.
- **MOD()**-funktionen returnerar resten efter att ett nummer har delats av en divisor, där det första parametern till funktionen är det numeriska värdet vars rest du vill hitta och det andra parametern är det tal som används för att dela in i nummerparametern. Om divisorn är 0 kommer den att returnera felen #DIV/0!.

Låt oss börja skriva kod för att uppnå detta mål med hjälp av Aspose.Cells för Python via .NET API.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyShadingToAlternateRowsColumns-1.py" >}}

Följande ögonblicksbild visar det resulterande kalkylarket som är laddat i Excel-applikationen.

|![todo:image_alt_text](1.png)|
| :- |

För att applicera nyanser på alternativa kolumner, behöver du bara ändra formeln **=MOD(RAD(),2)=0** till **=MOD(KOLUMN(),2)=0**, det vill säga; istället för att få radindexet, modifiera formeln för att hämta kolumnindexet. 
Det resulterande kalkylarket kommer i detta fall att se ut som följer.

|![todo:image_alt_text](2.png)|
| :- |

