---
title: Beräkna formler
type: docs
weight: 110
url: /sv/java/calculate-formulas/
---

## **Lägga till formler och beräkna resultat**

Aspose.Cells har en inbyggd formelberäkningsmotor. Inte bara kan den omberäkna formler som importerats från designmallar, men den stöder också att beräkna resultaten av formler som har lagts till vid körning.

Aspose.Cells stöder de flesta av de formler eller funktioner som ingår i Microsoft Excel(Läs [en lista över de funktioner som stöds av beräkningsmotorn](/cells/sv/java/supported-formula-functions/)). Dessa funktioner kan användas via API:erna eller designer-kalkylblad. Aspose.Cells stöder en stor uppsättning matematiska, sträng, booleska, datum/tid, statistiska, databas, sök- och referensformler.

Använd [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)-egenskapen eller [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object))-metoderna i [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)-klassen för att lägga till en formel i en cell. När du tillämpar en formel, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

För att beräkna resultaten av formler kan användaren ringa [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))-metoden i klassen [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) som bearbetar alla formler som finns inbäddade i en Excel-fil. Eller så kan användaren ringa [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean))-metoden i klassen [**Worsheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) som bearbetar alla formler som finns inbäddade i ett ark. Eller så kan användaren också ringa [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions))-metoden i klassen [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) som bearbetar formeln för en cell:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **Viktigt att veta**

{{% alert color="primary" %}}

Egenskapen **Formula** och metoderna **SetFormula(...)** i [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)-klassen fungerar annorlunda jämfört med metoderna **Calculate** i klasserna [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) och [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell). Egenskapen **Formula** och metoderna **SetFormula(...)** lägger helt enkelt till formeln i en cell men beräknar inte resultatet vid körning. För att få resultatet av formler, vänligen anropa metoderna **Calculate**.

{{% /alert %}}

## **Direkt beräkning av formel**

Aspose.Cells har en inbyggd formelberäkningsmotor. Förutom att beräkna formler som importerats från en designfil kan Aspose.Cells också beräkna formelresultat direkt.

Ibland behöver du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad och allt du behöver göra är att hitta resultatet av dessa värden baserat på några Microsoft Excel-formler utan att lägga till formeln i ett kalkylblad.

Du kan använda Aspose.Cells' API:er för formelberäkning från [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) till [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions)) resultaten av sådana formler utan att lägga till dem i kalkylbladet:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

Ovanstående kod ger följande utmatning:
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Beräkna formler upprepade gånger**

När det finns massor av formler i arbetsboken och användaren behöver beräkna dem upprepade gånger med endast mindre justering av dem kan det vara till hjälp för prestanda att aktivera formelberäkningskedjan: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **Viktigt att veta**

{{% alert color="primary" %}}

Som standard är beräkningskedjan inaktiverad. Eftersom skapandet av kedjan också kräver extra tid kan det första gången för att beräkna formler([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))) ta mer CPU-processortid och minne jämfört med att beräkna formler utan kedja. Om användaren inte behöver beräkna formler upprepade gånger bör standardbeteendet(att beräkna formel direkt utan att skapa beräkningskedja) vara det bättre sättet.

{{% /alert %}}

## **Fortsatta ämnen**
- [Lägg till celler i Microsoft Excel Formelövervakningsfönstret](/cells/sv/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells formelberäkningmotor](/cells/sv/java/aspose-cells-formula-calculation-engine/)
- [Beräkning av IFNA-funktionen med Aspose.Cells](/cells/sv/java/calculating-ifna-function-using-aspose-cells/)
- [Beräkning av Array Formula av Data Tables](/cells/sv/java/calculation-of-array-formula-of-data-tables/)
- [Beräkning av Excel 2016 MINIFS och MAXIFS funktioner](/cells/sv/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Minska tiden för beräkning av Cell.Calculate-metoden](/cells/sv/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [Upptäcka cirkulär referens](/cells/sv/java/detecting-circular-reference/)
- [Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad](/cells/sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementera anpassad beräkningsmotor för att förlänga standardberäkningsmotorn för Aspose.Cells](/cells/sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Avbryt eller avbryt formelberäkningen i arbetsbok](/cells/sv/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Returnera en rad med värden med hjälp av AbstractCalculationEngine](/cells/sv/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [Returnera ett område av värden med hjälp av ICustomFunction](/cells/sv/java/returning-a-range-of-values-using-icustomfunction/)
- [Använda ICustomFunction-funktionen](/cells/sv/java/using-icustomfunction-feature/)
