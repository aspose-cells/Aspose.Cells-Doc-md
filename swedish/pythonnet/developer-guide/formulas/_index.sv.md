---
title: Hantera formler för Excel filer
linktitle: Formler
type: docs
weight: 122
url: /sv/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells för Python via .NET kan enkelt hämta, sätta och beräkna formler i Excel filer.
description: Lär dig Hur man hanterar formler i Excel filer via Aspose.Cells för Python via .NET för .NET API er.
keywords: Hur man beräknar formler i Python, Formler och funktioner med Python, Python Hantera inbyggda funktioner, Hur man använder tilläggsfunktions med Python, Hur man använder Array formler via Python, Hur man använder R1C1 formler i Python.
---

## **Introduktion**

En av de mest övertygande funktionerna i Microsoft Excel är dess förmåga att bearbeta data med formler och funktioner. Microsoft Excel tillhandahåller ett antal inbyggda funktioner och formler som hjälper användare att snabbt utföra komplexa beräkningar. Aspose.Cells för Python via .NET erbjuder också ett stort antal inbyggda funktioner och formler som hjälper utvecklare att enkelt beräkna värden. Aspose.Cells för Python via .NET stödjer även tilläggsfunktions. Dessutom stöder Aspose.Cells för Python via .NET array och R1C1-formler.

## **Hur man Använder formler och funktioner**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-samling som ger tillgång till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samling. Varje objekt i Cells-samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Det är möjligt att använda formler på celler med egenskaper och metoder som erbjuds av [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-klassen, som diskuteras mer detaljerat nedan.

- Använda inbyggda funktioner.
- Använda tilläggsfunktioner.
- Arbeta med matrisformler.
- Skapa en R1C1-formel.

## **Hur man Använder Inbyggda Funktioner**

Inbyggda funktioner eller formler tillhandahålls som färdiga funktioner för att minska utvecklarnas insats och tid. Se [en lista över inbyggda funktioner](/cells/sv/python-net/supported-formula-functions/) som stöds av Aspose.Cells för Python via .NET. Funktionerna listas i alfabetisk ordning. Fler funktioner kommer att stödjas i framtiden.

Aspose.Cells för Python via .NET stöder de flesta av formlerna eller funktionerna som erbjuds av Microsoft Excel. Utvecklare kan använda dessa formler via API:et eller [designer kalkylblad](/cells/sv/net/what-is-a-designer-spreadsheet/). Aspose.Cells för Python via .NET stöder ett stort antal matematiska, sträng-, booleska, datum/tid-, statistik-, databas-, uppslags- och referensformler.

Använd [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-klassens [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula)-egenskap för att lägga till en formula i en cell. **Komplexa formler**, till exempel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, stöds också i Aspose.Cells för Python via .NET. När du tillämpar en formel på en cell, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att separera funktionsparametrar.

I nedanstående exempel tillämpas en komplex formel på den första cellen i ett kalkylblads [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-samling. Formeln använder en inbyggd **IF**-funktion som tillhandahålls av Aspose.Cells för Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **Hur man Använder Tilläggsfunktioner**

Vi kan ha några användardefinierade formler som vi vill inkludera som en excel-tillägg. När du ställer in cell.Formula-funktionen fungerar inbyggda funktioner bra, men det finns ett behov av att ställa in de anpassade funktionerna eller formlerna med tilläggsfunktionerna.

Aspose.Cells för Python via .NET tillhandahåller funktioner för att registrera tilläggsfunktionsanvändning med [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function). Därefter, när vi sätter cell.Formula = någonFunktionFrånTillägget, innehåller den utdata excelfilen det beräknade värdet från Tilläggsfunktionen.

Följande XLAM-fil ska laddas ned för att registrera tilläggsfunktionen enligt nedanstående provkod. På samma sätt kan den resulterande filen "test_udf.xlsx" laddas ned för att kontrollera resultatet.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **Hur man Använder Matrisformel**

Matrisformler är formler som tar matriser, istället för enskilda nummer, som argument till de funktioner som utgör formeln. När en matrisformel visas, omges den av måsvingar ({ }).

Vissa Microsoft Excel-funktioner returnerar matriser med värden. För att beräkna flera resultat med en arrayformel, ange matrisen i en cellintervall med samma antal rader och kolumner som matrisargumenten.

Det är möjligt att tillämpa en matrisformel på en cell genom att anropa [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-klassens [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula)-metod. [**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula)-metoden tar följande parametrar:

- **Arrayformel**, arrayformeln.
- **Antal rader**, antalet rader för att fylla resultatet av arrayformeln.
- **Antal kolumner**, antalet kolumner för att fylla resultatet av matrisformeln.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **Hur man Använder R1C1-formel**

Lägg till en formel med referensstil **R1C1** i en cell med klassens [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) [**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula)-egenskap.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **Fortsatta ämnen**
- [Föregångare och efterföljande](/cells/sv/python-net/precedents-and-dependents/)
- [Ange externa länkar i formler](/cells/sv/python-net/set-external-links-in-formulas/)
- [Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader](/cells/sv/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Ange formel för namngivet område](/cells/sv/python-net/setting-formula-for-named-range/)
- [Inställning av formler - Meddelande för användare som inte talar engelska](/cells/sv/python-net/setting-formulas-notice-for-non-english-users/)
- [Inställning av delad formel](/cells/sv/python-net/setting-shared-formula/)
- [Ange maximala rader för delad formel](/cells/sv/python-net/specify-maximum-rows-of-shared-formula/)
- [Stödda Excel-funktioner](/cells/sv/python-net/supported-formula-functions/)


{{< app/cells/assistant language="python-net" >}}
