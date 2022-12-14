---
title: Beräkna formler
type: docs
weight: 110
url: /sv/java/calculate-formulas/
---
## **Lägga till formler och beräkna resultat**

Aspose.Cells har en inbäddad formelberäkningsmotor. Det kan inte bara räkna om formler som importerats från designermallar utan det stöder också att beräkna resultaten av formler som läggs till vid körning.

 Aspose.Cells stöder de flesta formler eller funktioner som ingår i Microsoft Excel (Läs[en lista över de funktioner som stöds av beräkningsmotorn](/cells/sv/java/supported-formula-functions/)). Dessa funktioner kan användas via API:er eller designerkalkylblad. Aspose.Cells stöder en stor uppsättning matematiska formler, sträng-, booleska-, datum/tid-, statistiska, databas-, uppslags- och referensformler.

 Använd[**Formel**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) egendom eller[**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object) ) metoder för[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)klass för att lägga till en formel i en cell. När du använder en formel, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

 För att beräkna resultaten av formler kan användaren anropa[**Beräkna Formel**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) metod för[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)klass som bearbetar alla formler inbäddade i en Excel-fil. Eller så kan användaren ringa till[**Beräkna Formel**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) metod för[**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass som bearbetar alla formler inbäddade i ett ark. Eller så kan användaren också ringa[**Beräkna**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) metod för[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)klass som behandlar formeln för en Cell:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Viktigt att veta**

{{% alert color="primary" %}}

 De**Formel** egendom och**SetFormula(...)** metoder för[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)klassarbete annorlunda än**Beräkna** metoder för[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) och[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) klasser. De**Formel** egendom och**SetFormula(...)** metoder lägger helt enkelt till formeln i en cell men beräknar inte resultatet vid körning. Ring för att få resultatet av formlerna**Beräkna** metoder.

{{% /alert %}}

## **Direkt beräkning av formel**

Aspose.Cells har en inbäddad formelberäkningsmotor. Förutom att beräkna formler som importeras från en designerfil kan Aspose.Cells beräkna formelresultat direkt.

Ibland måste du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad och allt du behöver är att hitta resultatet av dessa värden baserat på någon Microsoft Excel-formel utan att lägga till formeln i ett kalkylblad.

 Du kan använda Aspose.Cells' API:er för formelberäkningsmotorer för[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) till[**Beräkna**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) resultaten av sådana formler utan att lägga till dem i kalkylbladet:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Ovanstående kod ger följande utdata:
{{< highlight "java" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Beräknar formler upprepade gånger**

 När det finns många formler i arbetsboken och användaren behöver beräkna dem upprepade gånger med endast en liten del av dem, kan det vara till hjälp för prestanda att aktivera formelberäkningskedjan:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Viktigt att veta**

{{% alert color="primary" %}}

Som standard är beräkningskedjan inaktiverad. Eftersom att skapa kedjan också kräver extra tid, första gången för att beräkna formler([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) kan förbruka mer CPU-bearbetningstid och minne när man jämför med beräkningsformler utan kedja. Om användaren inte behöver beräkna formler upprepade gånger, bör standardbeteendet (beräkna formel direkt utan att skapa beräkningskedja) vara det bättre sättet.

{{% /alert %}}

## **Förhandsämnen**
- [Lägg till Cells i Microsoft Excel Formula Watch Window](/cells/sv/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells Formelberäkningsmotor](/cells/sv/java/aspose-cells-formula-calculation-engine/)
- [Beräknar IFNA-funktion med Aspose.Cells](/cells/sv/java/calculating-ifna-function-using-aspose-cells/)
- [Beräkning av matrisformel för datatabeller](/cells/sv/java/calculation-of-array-formula-of-data-tables/)
- [Beräkning av Excel 2016 MINIFS och MAXIFS funktioner](/cells/sv/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Minska beräkningstiden för Cell. Beräkna metod](/cells/sv/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Detekterar cirkulär referens](/cells/sv/java/detecting-circular-reference/)
- [Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad](/cells/sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementera Custom Calculation Engine för att utöka standardberäkningsmotorn för Aspose.Cells](/cells/sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Avbryt eller avbryt formelberäkningen av arbetsboken](/cells/sv/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Returnera ett värdeintervall med AbstractCalculationEngine](/cells/sv/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Returnera ett värdeintervall med ICustomFunction](/cells/sv/java/returning-a-range-of-values-using-icustomfunction/)
- [Använder ICustomFunction-funktionen](/cells/sv/java/using-icustomfunction-feature/)
