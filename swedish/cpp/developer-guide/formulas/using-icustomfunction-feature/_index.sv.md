---
title: Använder ICustomFunction-funktionen
type: docs
weight: 20
url: /sv/cpp/using-icustomfunction-feature/
---
## **Introduktion**
Den här artikeln ger en förståelse för hur du använder ICustomFunction-funktionen för att implementera anpassade funktioner med Aspose.Cells API:er.

ICustomFunction-gränssnittet låter dig lägga till anpassade formelberäkningsfunktioner för att utöka Aspose.Cells kärnberäkningsmotor för att uppfylla vissa krav. Den här funktionen är användbar för att definiera anpassade (användardefinierade) funktioner i en mallfil eller i en kod där den anpassade funktionen kan implementeras och utvärderas med Aspose.Cells API:er som vilken annan standard Microsoft Excel-funktion som helst.
## **Använder ICustomFunction-funktionen**
Följande exempelkod implementerar ICustomFunction-gränssnittet som utvärderar och returnerar värdena för de två anpassade funktionerna, dvs. MySampleFunc() och YourSampleFunc(). Dessa anpassade funktioner finns inuti cellerna A1 respektive A2. Sedan anropar den metoden IWorkbook.CalculateFormula(false, ICustomFunction) för att anropa implementeringen av metoden ICustomFunction.CalculateCustomFunction(). Sedan skriver den ut värdena för A1 och A2 på konsolen som faktiskt är de värden som returneras av ICustomFunction.CalculateCustomFunction(). Se konsolutgången för exempelkoden nedan för mer hjälp.
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **Konsolutgång**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
