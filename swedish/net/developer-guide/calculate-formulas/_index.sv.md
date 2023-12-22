---
title: Beräkna formler
description: Den här artikeln introducerar hur du använder Aspose.Cells-biblioteket för att beräkna formler i Microsoft Excel. Genom att ladda en befintlig Excel-fil eller skapa en ny Excel-fil kan vi använda metoderna som tillhandahålls av Aspose.Cells för att beräkna formeln och få resultatet. Slutligen sparar vi den modifierade Excel-filen på disken.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /sv/net/calculate-formulas/
---
##  **Lägga till formler och beräkna resultat**

Aspose.Cells har en inbäddad formelberäkningsmotor. Det kan inte bara räkna om formler som importerats från designermallar utan det stöder också att beräkna resultaten av formler som läggs till vid körning.

 Aspose.Cells stöder de flesta formler eller funktioner som ingår i Microsoft Excel(Läs[en lista över de funktioner som stöds av beräkningsmotorn](/cells/sv/net/supported-formula-functions/)). Dessa funktioner kan användas via API:er eller designerkalkylblad. Aspose.Cells stöder en stor uppsättning matematiska formler, sträng-, booleska-, datum/tid-, statistiska, databas-, uppslags- och referensformler.

 Använd[**Formel**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) egendom eller[**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) metoder för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass för att lägga till en formel i en cell. När du använder en formel, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel och använd ett kommatecken (,) för att avgränsa funktionsparametrar.

 För att beräkna resultaten av formler kan användaren anropa[**Beräkna Formel**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) metod för[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass som bearbetar alla formler inbäddade i en Excel-fil. Eller så kan användaren ringa till[**Beräkna Formel**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) metod för[**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass som bearbetar alla formler inbäddade i ett ark. Eller så kan användaren också ringa[**Beräkna**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) metod för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass som behandlar formeln för en Cell:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **Viktigt att veta för formler**

{{% alert color="primary" %}}

 De**Formel** egendom och**SetFormula(...)** metoder för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klassarbete annorlunda än**Beräkna** metoder för[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) och[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klasser. De**Formel** egendom och**SetFormula(...)** metoder lägger helt enkelt till formeln i en cell men beräknar inte resultatet vid körning. Ring för att få resultatet av formlerna**Beräkna** metoder.

{{% /alert %}}

##  **Direkt beräkning av formel**

Aspose.Cells har en inbäddad formelberäkningsmotor. Förutom att beräkna formler som importeras från en designerfil kan Aspose.Cells beräkna formelresultat direkt.

Ibland måste du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad och allt du behöver är att hitta resultatet av dessa värden baserat på någon Microsoft Excel-formel utan att lägga till formeln i ett kalkylblad.

 Du kan använda Aspose.Cells' API:er för formelberäkningsmotorer för[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) till[**Beräkna**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) resultaten av sådana formler utan att lägga till dem i kalkylbladet:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

Ovanstående kod ger följande utdata:
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **Hur man beräknar formler upprepade gånger**

När det finns många formler i arbetsboken och användaren behöver beräkna dem upprepade gånger med endast en liten del av dem, kan det vara till hjälp för prestanda att aktivera formelberäkningskedjan:[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **Viktigt att veta**

{{% alert color="primary" %}}

Som standard är beräkningskedjan inaktiverad. Eftersom att skapa kedjan också kräver extra tid, första gången för att beräkna formler([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) kan förbruka mer CPU-behandlingstid och minne när man jämför med beräkningsformler utan kedja. Om användaren inte behöver beräkna formler upprepade gånger, bör standardbeteendet (beräkna formel direkt utan att skapa beräkningskedja) vara det bättre sättet.

{{% /alert %}}


##  **Förhandsämnen**
- [Lägg till Cells till Microsoft Excel Formula Watch Window](/cells/sv/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Beräknar IFNA-funktion med Aspose.Cells](/cells/sv/net/calculating-ifna-function-using-aspose-cells/)
- [Beräkning av matrisformel för datatabeller](/cells/sv/net/calculation-of-array-formula-of-data-tables/)
- [Beräkning av Excel 2016 MINIFS och MAXIFS funktioner](/cells/sv/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Minska beräkningstiden för Cell. Beräkna metod](/cells/sv/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [Detekterar cirkulär referens](/cells/sv/net/detecting-circular-reference/)
- [Direkt beräkning av anpassad funktion utan att skriva det i ett kalkylblad](/cells/sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementera Custom Calculation Engine för att utöka standardberäkningsmotorn för Aspose.Cells](/cells/sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Avbryt eller avbryt formelberäkningen av arbetsboken](/cells/sv/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Returnera ett värdeintervall med AbstractCalculationEngine](/cells/sv/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [Returnera ett värdeintervall med ICustomFunction](/cells/sv/net/returning-a-range-of-values-using-icustomfunction/)
- [Ställa in formelberäkningsläge för arbetsbok](/cells/sv/net/setting-formula-calculation-mode-of-workbook/)
- [Använder FormulaText-funktionen i Aspose.Cells](/cells/sv/net/using-formulatext-function-in-aspose-cells/)
- [Använder ICustomFunction-funktionen](/cells/sv/net/using-icustomfunction-feature/)
