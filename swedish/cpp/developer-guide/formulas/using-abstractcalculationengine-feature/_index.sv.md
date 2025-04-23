---
title: Använda funktionen AbstractCalculationEngine
type: docs
weight: 20
url: /sv/cpp/using-abstractcalculationengine-feature/
---


## **Introduktion**
Den här artikeln ger en förståelse för hur man använder funktionen [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) för att implementera anpassade funktioner med Aspose.Cells API:er.

Gränssnittet AbstractCalculationEngine gör det möjligt att lägga till anpassade formelberäkningsfunktioner för att utöka Aspose.Cells kärnberäkningsmotor för att uppfylla vissa krav. Denna funktion är användbar för att definiera anpassade (användardefinierade) funktioner i en mallfil eller i en kod där den anpassade funktionen kan implementeras och utvärderas med hjälp av Aspose.Cells API:er som vilken annan standard Microsoft Excel funktion som helst.

## **Användning av AbstractCalculationEngine-funktion - 1**

Följande exempelkod implementerar gränssnittet AbstractCalculationEngine som utvärderar och returnerar värdena av de två anpassade funktionerna dvs. MySampleFunc() och YourSampleFunc(). Dessa anpassade funktioner finns inuti cellerna A1 och A2 respektive. Sedan kallar det Workbook.CalculateFormula(const CalculationOptions& options) metoden för att aktivera implementeringen av AbstractCalculationEngine .Calculate(CalculationData& data) metoden. Därefter skrivs värdena A1 och A2 ut på konsolen. Se Konsoloutputen från exempelkoden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine.cpp" >}}


## **Konsoloutput**
{{< highlight java >}}

MySampleFunc-Test called successfully.
YourSampleFunc-Test called successfully.
Value of A1 is : 1
Value of A2 is : 2

{{< /highlight >}}

## **Användning av AbstractCalculationEngine-funktion - 2**

Följande kalkylkod läser en anpassad funktion från en exempel fil och anropar Workbook.CalculateFormula(const CalculationOptions& options)-metoden för att anropa AbstractCalculationEngine .Calculate(CalculationData& data)-metoden för vidare bearbetning.

Exempelfil:[sample-file.xlsx](sample-file.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingAbstractCalculationEngine2.cpp" >}}
