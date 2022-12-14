---
title: Använda formler eller funktioner för att bearbeta data
type: docs
weight: 5
url: /sv/java/get-and-set-formula/
---
{{% alert color="primary" %}}

En av Microsoft Excels övertygande egenskaper är dess förmåga att bearbeta data med formler och funktioner. Microsoft Excel tillhandahåller en uppsättning inbyggda funktioner och formler som hjälper användare att snabbt utföra komplexa beräkningar. Aspose.Cells tillhandahåller också en enorm uppsättning inbyggda funktioner och formler som hjälper utvecklare att enkelt beräkna värden. Aspose.Cells stöder även tilläggsfunktioner. Dessutom stöder Aspose.Cells array och R1C1-formler i Aspose.Cells.

{{% /alert %}}

## **Använda formler och funktioner**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) samling. Varje objekt i[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) samlingen representerar ett föremål för[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass.

 Det är möjligt att tillämpa formler på celler med hjälp av egenskaper och metoder som erbjuds av[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass, diskuteras mer i detalj nedan.

- [Använder inbyggda funktioner](/cells/sv/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Använda tilläggsfunktioner](/cells/sv/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Arbeta med matrisformler](/cells/sv/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Skapa en R1C1-formel](/cells/sv/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Använda inbyggda funktioner**

 Inbyggda funktioner eller formler tillhandahålls som färdiga funktioner för att minska utvecklarnas ansträngningar och tid. Ser[en lista över inbyggda funktioner](/cells/sv/java/supported-formula-functions/). Funktionerna är listade i alfabetisk ordning. Fler funktioner kommer att stödjas i framtiden.

 Aspose.Cells stöder de flesta formler eller funktioner som erbjuds av Microsoft Excel. Utvecklare kan använda dessa formler genom API eller[designerkalkylblad](/cells/sv/java/what-is-a-designer-spreadsheet/). Aspose.Cells stöder en stor uppsättning matematiska formler, strängar, booleska formler, datum/tid, statistik, databas, uppslagsformler och referensformler.

 Använd[**Formel**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)egendom av[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass för att lägga till en formel i en cell.**Komplexa formler**, till exempel

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, stöds också i Aspose.Cells. När du tillämpar en formel på en cell, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

 I exemplet nedan tillämpas en komplex formel på den första cellen i ett kalkylblad[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) samling. Formeln använder en inbyggd**OM** funktionen tillhandahålls av Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Använda tilläggsfunktioner**

 Vi kan ha några användardefinierade formler som vi vill inkludera som ett excel-tillägg. När du ställer in[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) funktions inbyggda funktioner fungerar bra men det finns ett behov av att ställa in de anpassade funktionerna eller formlerna med hjälp av tilläggsfunktionerna.

 Aspose.Cells tillhandahåller funktioner för att registrera tilläggsfunktioner med hjälp av[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). Efteråt när vi satt[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn, utdata Excel-filen innehåller det beräknade värdet från AddIn-funktionen.

Efter det ska XLAM-filen laddas ner för registrering av tilläggsfunktionen i nedanstående exempelkod. På samma sätt kan utdatafilen "test_udf.xlsx" laddas ner för att kontrollera utdata.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Använda Array Formula**

Matrisformler är formler som fungerar med matriser, istället för enskilda tal, som argument till funktionerna som utgör formeln. När en matrisformel visas är den omgiven av klammerparenteser ({}) som visas nedan.

**Ställa in en matrisformel på cell G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Vissa Microsoft Excel-funktioner returnerar matriser med värden. För att beräkna flera resultat med en matrisformel anger du matrisen i ett cellintervall med samma antal rader och kolumner som matrisargumenten.

 Det är möjligt att tillämpa en matrisformel på en cell genom att anropa[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass'[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int) ) metod. De[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) metod tar följande parametrar:

- **Matrisformel**, matrisformeln.
- **Antal rader**antalet rader som ska fyllas i resultatet av matrisformeln.
- **Antal kolumner**, antalet kolumner som ska fyllas i resultatet av matrisformeln.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Använder R1C1 Formel**

 Applicera en**R1C1** referera stilformel till en cell med[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass'[**setR1C1Formel**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

