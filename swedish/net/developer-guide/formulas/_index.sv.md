---
title: Hantera formler för Excel filer
linktitle: Formler
type: docs
weight: 122
url: /sv/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells kan enkelt få, sätta och beräkna formler för excel filer.
description: Lär dig hur man hanterar formler för Excel filer genom de Aspose.Cells for NET API erna.
keywords: Hur man beräknar formler i C#, formler och funktioner med C#, C# Hantera Inbyggda Funktioner, Hur man Använder Tilläggsfunktioner med C#, Hur man Använder Matrisformel via C#, Hur man Använder R1C1 formel i C#.
---

## **Introduktion**

En av Microsoft Excels kraftfulla funktioner är dess möjlighet att bearbeta data med hjälp av formler och funktioner. Microsoft Excel ger ett set av inbyggda funktioner och formler som hjälper användare att snabbt utföra komplexa beräkningar. Aspose.Cells tillhandahåller också ett stort antal inbyggda funktioner och formler som hjälper utvecklare att enkelt beräkna värden. Aspose.Cells stöder också tilläggsfunktioner. Dessutom stöder Aspose.Cells array- och R1C1-formler.

## **Hur man Använder formler och funktioner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samling. Varje objekt i Cells-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-klassen.

Det är möjligt att använda formler på celler med egenskaper och metoder som erbjuds av [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-klassen, som diskuteras mer detaljerat nedan.

- Använda inbyggda funktioner.
- Använda tilläggsfunktioner.
- Arbeta med matrisformler.
- Skapa en R1C1-formel.

## **Hur man Använder Inbyggda Funktioner**

Inbyggda funktioner eller formler tillhandahålls som färdiga funktioner för att minska utvecklares ansträngningar och tid. Se [en lista över inbyggda funktioner](/cells/sv/net/supported-formula-functions/) som stöds av Aspose.Cells. Funktionerna listas i alfabetisk ordning. Fler funktioner kommer att stödjas i framtiden.

Aspose.Cells stöder de flesta formler eller funktioner som erbjuds av Microsoft Excel. Utvecklare kan använda dessa formler genom API:n eller [designer kalkylarket](/cells/sv/net/what-is-a-designer-spreadsheet/). Aspose.Cells stöder en stor uppsättning matematiska, sträng-, booleska, datums-/tid-, statistiska, databas-, sök- och referens formler.

Använd [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-klassens [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)-egenskap för att lägga till en formula i en cell. **Komplexa formler**, till exempel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, stöds också i Aspose.Cells. När du tillämpar en formel på en cell, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

I exemplet nedan tillämpas en komplex formula på den första cellen i kalkylbladets [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-samling. Formeln använder en inbyggd **OM**-funktion som tillhandahålls av Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Hur man Använder Tilläggsfunktioner**

Vi kan ha några användardefinierade formler som vi vill inkludera som en excel-tillägg. När du ställer in cell.Formula-funktionen fungerar inbyggda funktioner bra, men det finns ett behov av att ställa in de anpassade funktionerna eller formlerna med tilläggsfunktionerna.

Aspose.Cells tillhandahåller funktioner för att registrera tilläggsfunktioner med hjälp av [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Efteråt, när vi ställer in cell.Formula = anyFunctionFromAddIn, innehåller den resulterande Excel-filen det beräknade värdet från tilläggsfunktionen.

Följande XLAM-fil ska laddas ned för att registrera tilläggsfunktionen enligt nedanstående provkod. På samma sätt kan den resulterande filen "test_udf.xlsx" laddas ned för att kontrollera resultatet.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Hur man Använder Matrisformel**

Matrisformler är formler som tar matriser, istället för enskilda nummer, som argument till de funktioner som utgör formeln. När en matrisformel visas, omges den av måsvingar ({ }).

Vissa Microsoft Excel-funktioner returnerar matriser med värden. För att beräkna flera resultat med en arrayformel, ange matrisen i en cellintervall med samma antal rader och kolumner som matrisargumenten.

Det är möjligt att tillämpa en matrisformel på en cell genom att anropa [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-klassens [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)-metod. [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)-metoden tar följande parametrar:

- **Arrayformel**, arrayformeln.
- **Antal rader**, antalet rader för att fylla resultatet av arrayformeln.
- **Antal kolumner**, antalet kolumner för att fylla resultatet av matrisformeln.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Hur man Använder R1C1-formel**

Lägg till en formel med referensstil **R1C1** i en cell med klassens [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula)-egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Fortsatta ämnen**
- [Föregångare och efterföljande](/cells/sv/net/precedents-and-dependents/)
- [Ange externa länkar i formler](/cells/sv/net/set-external-links-in-formulas/)
- [Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader](/cells/sv/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Ange formel för namngivet område](/cells/sv/net/setting-formula-for-named-range/)
- [Inställning av formler - Meddelande för användare som inte talar engelska](/cells/sv/net/setting-formulas-notice-for-non-english-users/)
- [Inställning av delad formel](/cells/sv/net/setting-shared-formula/)
- [Ange maximala rader för delad formel](/cells/sv/net/specify-maximum-rows-of-shared-formula/)
- [Stödda Excel-funktioner](/cells/sv/net/supported-formula-functions/)

{{< app/cells/assistant language="csharp" >}}
