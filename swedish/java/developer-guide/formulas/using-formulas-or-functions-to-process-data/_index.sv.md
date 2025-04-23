---
title: Använda formler eller funktioner för att bearbeta data
type: docs
weight: 5
url: /sv/java/get-and-set-formula/
---

{{% alert color="primary" %}}

En av Microsoft Excels stimulerande funktioner är dess förmåga att bearbeta data med formler och funktioner. Microsoft Excel tillhandahåller en uppsättning inbyggda funktioner och formler som hjälper användare att snabbt utföra komplicerade beräkningar. Aspose.Cells tillhandahåller också en stor uppsättning inbyggda funktioner och formler som hjälper utvecklare att beräkna värden enkelt. Aspose.Cells stöder också tillägg av funktioner. Dessutom stödjer Aspose.Cells array- och R1C1-formler i Aspose.Cells.

{{% /alert %}}

## **Använda formler och funktioner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) samling som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klassen.

Det är möjligt att tillämpa formler på celler med hjälp av egenskaper och metoder som erbjuds av [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen, som diskuteras mer detaljerat nedan.

- [Använda inbyggda funktioner](/cells/sv/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Använda tilläggsfunktioner](/cells/sv/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Arbeta med arrayformler](/cells/sv/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Skapa en R1C1-formel](/cells/sv/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Använda inbyggda funktioner**

Inbyggda funktioner eller formler tillhandahålls som färdiga funktioner för att minska utvecklarnas ansträngningar och tid. Se [en lista över inbyggda funktioner](/cells/sv/java/supported-formula-functions/). Funktionerna listas i alfabetisk ordning. Fler funktioner kommer att stödjas i framtiden.

Aspose.Cells stöder de flesta av de formler eller funktioner som erbjuds av Microsoft Excel. Utvecklare kan använda dessa formler genom API:et eller [designer kalkylbladet](/cells/sv/java/what-is-a-designer-spreadsheet/). Aspose.Cells stödjer en stor uppsättning matematiska, sträng-, booleska, datum/tids-, statistiska, databas-, sök-, och hänvisningsformler.

Använd [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)-egenskapen av klassen [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) för att lägga till en formel i en cell. **Komplexa formler**, till exempel

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, stöds också i Aspose.Cells. När du tillämpar en formel på en cell, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

I exemplet nedan tillämpas en komplex formel på det första cellen i ett arbetsblads [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)-samling. Formeln använder en inbyggd **IF**-funktion som tillhandahålls av Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Använda tilläggsfunktioner**

Vi kan ha några användardefinierade formler som vi vill inkludera som ett Excel-tillägg. När du ställer in [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)-funktionen fungerar inbyggda funktioner bra, men det finns ett behov av att ställa in anpassade funktioner eller formler med hjälp av tilläggsfunktioner.

Aspose.Cells tillhandahåller funktioner för att registrera tillägg av funktioner med hjälp av [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction-java.lang.String-java.lang.String-boolean-). Därefter, när vi ställer in [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn, innehåller den resulterande Excelfilen det beräknade värdet från tilläggsfunktionen.

Efterföljande XLAM-filen ska laddas ner för att registrera tilläggsfunktionen i det nedan angivna exemplet. På samma sätt kan utdatafilen "test_udf.xlsx" laddas ner för att kontrollera resultatet.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Använda arrayformel**

Arrayformler är formler som fungerar med matriser, istället för individuella nummer, som argument till de funktioner som utgör formeln. När en arrayformel visas, omges den av klamrar ({}) som visas nedan.

**Ange en arrayformel på cell G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Vissa Microsoft Excel-funktioner returnerar matriser med värden. För att beräkna flera resultat med en arrayformel, ange matrisen i en cellintervall med samma antal rader och kolumner som matrisargumenten.

Det är möjligt att tillämpa en arrayformel på en cell genom att anropa [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassens [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-)-metod. [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-)-metoden tar följande parametrar:

- **Arrayformel**, arrayformeln.
- **Antal rader**, antalet rader för att fylla resultatet av arrayformeln.
- **Antal kolumner**, antalet kolumner för att fylla resultatet av arrayformeln.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Använda R1C1-formel**

Tillämpa en **R1C1**-hänvisningsstilformel på en cell med [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassens [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)-egenskap.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

{{< app/cells/assistant language="java" >}}
