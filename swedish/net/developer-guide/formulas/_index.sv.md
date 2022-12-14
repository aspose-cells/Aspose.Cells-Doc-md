---
title: Hantera formler för Excel-filer
linktitle: Formler
type: docs
weight: 122
url: /sv/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells kan helt enkelt hämta, ställa in och beräkna formler för Excel-filer.
---
## **Introduktion**

En av Microsoft Excels övertygande funktioner är dess förmåga att bearbeta data med formler och funktioner. Microsoft Excel tillhandahåller en uppsättning inbyggda funktioner och formler som hjälper användare att snabbt utföra komplexa beräkningar. Aspose.Cells tillhandahåller också en enorm uppsättning inbyggda funktioner och formler som hjälper utvecklare att enkelt beräkna värden. Aspose.Cells stöder även tilläggsfunktioner. Dessutom stöder Aspose.Cells array och R1C1-formler i Aspose.Cells.

## **Använda formler och funktioner**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. Varje föremål i Cells-samlingen representerar ett objekt av[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass.

 Det är möjligt att tillämpa formler på celler med hjälp av egenskaper och metoder som erbjuds av[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass, diskuteras mer i detalj nedan.

- Använder inbyggda funktioner.
- Använda tilläggsfunktioner.
- Arbeta med matrisformler.
- Skapa en R1C1-formel.

## **Använda inbyggda funktioner**

 Inbyggda funktioner eller formler tillhandahålls som färdiga funktioner för att minska utvecklarnas ansträngningar och tid. Ser[en lista över inbyggda funktioner](/cells/sv/net/supported-formula-functions/)stöds av Aspose.Cells. Funktionerna är listade i alfabetisk ordning. Fler funktioner kommer att stödjas i framtiden.

 Aspose.Cells stöder de flesta formler eller funktioner som erbjuds av Microsoft Excel. Utvecklare kan använda dessa formler genom API eller[designerkalkylblad](/cells/sv/net/what-is-a-designer-spreadsheet/). Aspose.Cells stöder en stor uppsättning matematiska formler, strängar, booleska formler, datum/tid, statistik, databas, uppslagsformler och referensformler.

 Använd[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass'[**Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) egenskap för att lägga till en formel i en cell.**Komplexa formler**, till exempel

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, stöds också i Aspose.Cells. När du tillämpar en formel på en cell, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

 I exemplet nedan tillämpas en komplex formel på den första cellen i ett kalkylblad[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling. Formeln använder en inbyggd**OM** funktionen tillhandahålls av Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Använda tilläggsfunktioner**

Vi kan ha några användardefinierade formler som vi vill inkludera som ett excel-tillägg. När du ställer in cell.Formelfunktionen fungerar inbyggda funktioner bra, men det finns ett behov av att ställa in de anpassade funktionerna eller formlerna med hjälp av tilläggsfunktionerna.

 Aspose.Cells tillhandahåller funktioner för att registrera tilläggsfunktioner med hjälp av[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Efteråt när vi ställer in cell.Formula = anyFunctionFromAddIn, innehåller utdata Excel-filen det beräknade värdet från AddIn-funktionen.

Följande XLAM-fil ska laddas ner för registrering av tilläggsfunktionen i exempelkoden nedan. På samma sätt kan utdatafilen "test_udf.xlsx" laddas ner för att kontrollera utdata.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Använda Array Formula**

Matrisformler är formler som tar matriser, istället för enskilda tal, som argument till funktionerna som utgör formeln. När en matrisformel visas är den omgiven av klammerparenteser ({}).

Vissa Microsoft Excel-funktioner returnerar matriser med värden. För att beräkna flera resultat med en matrisformel anger du matrisen i ett cellintervall med samma antal rader och kolumner som matrisargumenten.

 Det är möjligt att tillämpa en matrisformel på en cell genom att anropa[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) metod. De[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) metoden tar följande parametrar:

- **Matrisformel**, matrisformeln.
- **Antal rader**antalet rader som ska fyllas i resultatet av matrisformeln.
- **Antal kolumner**, antalet kolumner som ska fyllas i resultatet av matrisformeln.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Använder R1C1 Formel**

 Lägg till en**R1C1** referera stilformel till en cell med[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klass'[**R1C1Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Förhandsämnen**
- [Prejudikat och beroende](/cells/sv/net/precedents-and-dependents/)
- [Ställ in externa länkar i formler](/cells/sv/net/set-external-links-in-formulas/)
- [Sprid formel i tabell eller listobjekt automatiskt medan du anger data i nya rader](/cells/sv/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Inställningsformel för namngett intervall](/cells/sv/net/setting-formula-for-named-range/)
- [Inställningsformler - Meddelande för icke engelska användare](/cells/sv/net/setting-formulas-notice-for-non-english-users/)
- [Ställa in delad formel](/cells/sv/net/setting-shared-formula/)
- [Ange maximalt antal rader med delad formel](/cells/sv/net/specify-maximum-rows-of-shared-formula/)
- [Excel-funktioner som stöds](/cells/sv/net/supported-formula-functions/)

