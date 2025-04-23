---
title: Hur man använder färgpaletten
type: docs
weight: 80
url: /sv/python-net/excel-color-palette/
description: Python kod för att lägga till anpassade färger till paletten och använda Excel färgpalett med Aspose.Cells för Python via .NET API
keywords: Python lägger till anpassade färger till paletten, Python programmatisk Excel färgpalett, hur man använder färgpaletten i arbetsboken programmässigt, Python hur man använder färgpaletten i Excel
---

## **Färger och Palett**

En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.

Med Aspose.Cells för Python via .NET är det inte bara möjligt att använda paletteens befintliga färger utan även anpassade färger. Innan du använder en anpassad färg, lägg till den i paletten först.

Detta ämne diskuterar hur man lägger till anpassade färger i paletten.

## **Lägg till anpassade färger i paletten**

Aspose.Cells för Python via .NET stöder Microsoft Excels 56 färgpalett. För att använda en anpassad färg som inte är definierad i paletten, lägg till färgen till paletten.

Aspose.Cells för Python via .NET tillhandahåller en klass, {0}, som representerar en Microsoft Excel-fil. Klassen {1} innehåller en {2} samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av klassen {3}. Klassen {4} tillhandahåller en {5} samling. Varje objekt i {6} samlingen representerar ett objekt av klassen {7}.

- Anpassad färg, den anpassade färgen som ska läggas till.
- Index, index för färgen i paletten som den anpassade färgen kommer att ersätta. Ska vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg (Orchid) i paletten innan den tillämpas på en font.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och alla element i filen formaterade med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen i XLS (Excel 97 - 2003) filformat endast då det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010 eller 2013) filformat.

{{% /alert %}}

