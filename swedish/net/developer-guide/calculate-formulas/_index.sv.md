---
title: Beräkna formler
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att beräkna formler i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda de metoder som tillhandahålls av Aspose.Cells för att beräkna formeln och få resultatet. Slutligen sparar vi den modifierade Excel filen på hårddisken.
keywords: Aspose.Cells, Excel, formler, beräkningar, Direkt Beräkning av Formel, Beräkna formler upprepade gånger, lägga till formler.
type: docs
weight: 125
url: /sv/net/calculate-formulas/
---

## **Lägga till formler och beräkna resultat**

Aspose.Cells har en inbyggd formelberäkningsmotor. Inte bara kan den omberäkna formler som importerats från designmallar, men den stöder också att beräkna resultaten av formler som har lagts till vid körning.

Aspose.Cells stöder de flesta formler eller funktioner som ingår i Microsoft Excel (Läs [en lista över de funktioner som stöds av beräkningsmotorn](/cells/sv/net/supported-formula-functions/)). Dessa funktioner kan användas genom API:er eller designkalkylblad. Aspose.Cells stöder en stor uppsättning matematiska, sträng, booleska, datum/tid, statistiska, databaser, uppslag och referens formler.

Använd [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)-egenskapen eller [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2)-metoderna i [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-klassen för att lägga till en formel i en cell. När du tillämpar en formel, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

För att beräkna resultaten av formler kan användaren ringa [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)-metoden i klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som bearbetar alla formler som finns inbäddade i en Excel-fil. Eller så kan användaren ringa [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula)-metoden i klassen [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) som bearbetar alla formler som finns inbäddade i ett ark. Eller så kan användaren också ringa [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate)-metoden i klassen [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) som bearbetar formeln för en cell:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **Viktigt att veta för formler**

{{% alert color="primary" %}}

Egenskapen **Formula** och metoderna **SetFormula(...)** i [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-klassen fungerar annorlunda jämfört med metoderna **Calculate** i klasserna [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) och [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Egenskapen **Formula** och metoderna **SetFormula(...)** lägger helt enkelt till formeln i en cell men beräknar inte resultatet vid körning. För att få resultatet av formler, vänligen anropa metoderna **Calculate**.

{{% /alert %}}

## **Direkt beräkning av formel**

Aspose.Cells har en inbyggd formelberäkningsmotor. Förutom att beräkna formler som importerats från en designfil kan Aspose.Cells också beräkna formelresultat direkt.

Ibland behöver du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad och allt du behöver göra är att hitta resultatet av dessa värden baserat på några Microsoft Excel-formler utan att lägga till formeln i ett kalkylblad.

Du kan använda Aspose.Cells' API:er för formelberäkning från [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) till [**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) resultaten av sådana formler utan att lägga till dem i kalkylbladet:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Ovanstående kod ger följande utmatning:
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Hur man beräknar formler upprepade gånger**

När det finns massor av formler i arbetsboken och användaren behöver beräkna dem upprepade gånger med endast mindre justering av dem kan det vara till hjälp för prestanda att aktivera formelberäkningskedjan: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **Viktigt att veta**

{{% alert color="primary" %}}

Som standard är beräkningskedjan inaktiverad. Eftersom skapandet av kedjan också kräver extra tid kan det första gången för att beräkna formler([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) ta mer CPU-processortid och minne jämfört med att beräkna formler utan kedja. Om användaren inte behöver beräkna formler upprepade gånger bör standardbeteendet(att beräkna formel direkt utan att skapa beräkningskedja) vara det bättre sättet.

{{% /alert %}}


## **Fortsatta ämnen**
- [Lägg till celler i Microsoft Excel Formelövervakningsfönstret](/cells/sv/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Beräkning av IFNA-funktionen med Aspose.Cells](/cells/sv/net/calculating-ifna-function-using-aspose-cells/)
- [Beräkning av Array Formula av Data Tables](/cells/sv/net/calculation-of-array-formula-of-data-tables/)
- [Beräkning av Excel 2016 MINIFS och MAXIFS funktioner](/cells/sv/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Minska tiden för beräkning av Cell.Calculate-metoden](/cells/sv/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Upptäcka cirkulär referens](/cells/sv/net/detecting-circular-reference/)
- [Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad](/cells/sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementera anpassad beräkningsmotor för att förlänga standardberäkningsmotorn för Aspose.Cells](/cells/sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Avbryt eller avbryt formelberäkningen i arbetsbok](/cells/sv/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Returnera en rad med värden med hjälp av AbstractCalculationEngine](/cells/sv/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Returnera ett område av värden med hjälp av ICustomFunction](/cells/sv/net/returning-a-range-of-values-using-icustomfunction/)
- [Inställning av Formelberäkningsläge för Arbetsbok](/cells/sv/net/setting-formula-calculation-mode-of-workbook/)
- [Användning av FormulaText-funktionen i Aspose.Cells](/cells/sv/net/using-formulatext-function-in-aspose-cells/)
- [Använda ICustomFunction-funktionen](/cells/sv/net/using-icustomfunction-feature/)
