---
title: Sätt att beräkna formler
type: docs
weight: 30
url: /sv/cpp/ways-to-calculate-formulas/
---

## **Introduktion**
Aspose.Cells har en inbyggd formelberäkningsmotor. Den kan inte bara omberäkna formler som importerats från mallar utan stöder också beräkning av resultaten av formler som läggs till vid runtime.
## **Lägga till formler och beräkna resultat**
Aspose.Cells stöder de flesta av formlerna eller funktionerna som är en del av Microsoft Excel. De kan användas via API eller genom att använda designerkalkylblad. Aspose.Cells stöder en stor mängd matematiska, sträng-, booleska, datum-/tid-, statistiska, sök- och referensformler.

Använd Cell.SetFormula-metoden för att lägga till en formel i en cell. När du applicerar en formel på en cell ska du alltid börja strängen med ett likhetstecken (=) precis som när du skapar en formel i Microsoft Excel. Använd ett kommatecken (,) för att avgränsa funktionsparametrarna.

För att beräkna resultaten av formler, anropa Workbook.CalculateFormula() -metoden som bearbetar alla formler som är inbäddade i en Excel-fil. Var god se följande exempelkod som lägger till formeln och beräknar dess resultat. Var god kontrollera den [utdata excel-fil](38109185.xlsx) som genererats med denna kod.

**Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direkt beräkning av formel**
Ibland behöver du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad och allt du behöver göra är att hitta resultatet av dessa värden baserat på några Microsoft Excel-formler utan att lägga till formeln i ett kalkylblad.

Du kan använda metoden Worksheet.CalculateFormula(String formula) för att beräkna resultaten av sådana formler utan att lägga till dem i kalkylbladet.

Koden nedan genererar följande utdata.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
## **Beräkna formler endast en gång**
När Workbook.CalculateFormula() kallas för att beräkna värdena för formler i en arbetsboksmall skapar Aspose.Cells en beräkningskedja. Det ökar prestandan när formler beräknas för andra eller tredje gången.

Men om mallen innehåller många formler kan den första gången formeln beräknas förbruka mycket CPU-processortid och minne.

Aspose.Cells tillåter dig att stänga av skapandet av en beräkningskedja vilket är användbart när du vill beräkna formler endast en gång.

Var god ring Workbook.GetISettings().SetCreateCalcChain() med falskt parameter. Du kan använda den [medföljande Excel-filen](38109186.xlsx) för att testa denna kod.

**Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
