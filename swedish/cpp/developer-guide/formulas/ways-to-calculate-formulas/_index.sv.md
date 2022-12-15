---
title: Sätt att beräkna formler
type: docs
weight: 30
url: /sv/cpp/ways-to-calculate-formulas/
---
## **Introduktion**
Aspose.Cells har en inbäddad formelberäkningsmotor. Det kan inte bara räkna om formler som importerats från designermallar utan stöder också beräkning av resultaten av formler som lagts till vid körning.
## **Lägga till formler och beräkna resultat**
Aspose.Cells stöder de flesta formler eller funktioner som ingår i Microsoft Excel. de kan användas via API eller med hjälp av designerkalkylblad. Aspose.Cells stöder en enorm uppsättning matematiska formler, sträng-, booleska-, datum/tid-, statistiska, uppslags- och referensformler.

Använd metoden Cell.Formula för att lägga till en formel i en cell. När du tillämpar en formel på en cell, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel. Använd ett kommatecken (,) för att avgränsa funktionsparametrar.

För att beräkna resultatet av formler, anrop Workbook.CalculateFormula()-metoden som bearbetar alla formler som är inbäddade i en Excel-fil. Se följande exempelkod som lägger till formeln och beräknar dess resultat. Vänligen kontrollera[output excel-fil](38109185.xlsx) genereras med denna kod.

**Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **Direkt beräkning av formel**
Ibland måste du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad och allt du behöver är att hitta resultatet av dessa värden baserat på någon Microsoft Excel-formel utan att lägga till formeln i ett kalkylblad.

Du kan använda metoden Worksheet.CalculateFormula(String formula) för att beräkna resultaten av sådana formler utan att lägga till dem i kalkylbladet.

Koden nedan ger följande utdata.

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **Beräknar formler endast en gång**
När Workbook.CalculateFormula() anropas för att beräkna värdena för formler i en arbetsboksmall, skapar Aspose.Cells en beräkningskedja. Det ökar prestandan när formler beräknas för andra eller tredje gången.

Men om mallen innehåller många formler kan första gången formeln beräknas ta mycket CPU-bearbetningstid och minne.

Aspose.Cells låter dig stänga av att skapa en beräkningskedja, vilket är användbart när du bara vill beräkna formler en gång.

 Vänligen anrop Workbook.GetISettings().SetCreateCalcChain() med false parameter. Du kan använda[tillhandahållit excel-fil](38109186.xlsx) för att testa den här koden.

**Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}
