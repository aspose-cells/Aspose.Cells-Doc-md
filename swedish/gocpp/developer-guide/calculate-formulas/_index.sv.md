---
title: Kalkylera formler med Golang via C++
linktitle: Beräkna formler
description: Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att beräkna formler i Microsoft Excel med Golang via C++. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoderna som tillhandahålls av Aspose.Cells för att beräkna formeln och få resultatet. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, formler, beräkningar, Direkt Beräkning av Formel, Beräkna formler upprepade gånger, lägga till formler.
type: docs
weight: 125
url: /sv/go-cpp/calculate-formulas/
---

## **Lägga till formler och beräkna resultat**

Aspose.Cells har en inbäddad formelberäkningsmotor. Den kan inte bara omberäkna formler importerade från designermallar utan också stödjer beräkning av resultaten av formler som läggs till vid körning.

Aspose.Cells stödjer de flesta av de formler eller funktioner som ingår i Microsoft Excel (Läs [en lista över de funktioner som stöds av beräkningsmotorn](/cells/sv/cpp/supported-formula-functions/)). Dessa funktioner kan användas via API:erna eller designer kalkylblad. Aspose.Cells stöder ett stort antal matematiska, sträng-, boolean-, datum/tids-, statistiska, databas-, uppslags- och referensformler.

Använd [**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/)-egenskapen eller [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/)-metoderna i [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-klassen för att lägga till en formel till en cell. När du tillämpar en formel, börja alltid strängen med ett likhetstecken (=) som du gör när du skapar en formel i Microsoft Excel, och använd ett komma (,) för att avgränsa funktionsparametrar.

För att beräkna resultaten av formler kan användaren anropa [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) metoden i [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen, som bearbetar alla formler inbäddade i en Excel-fil. Eller, användaren kan anropa [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) metoden i [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen, som bearbetar alla formler inbäddade i ett blad. Alternativt kan användaren också anropa [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) metoden i [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) klassen, som processar formeln för en Cell:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}
### **Viktigt att veta för formler**

{{% alert color="primary" %}}

Egenskapen **GetFormula** och metoderna **SetFormula(...)** i [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) klassen fungerar annorlunda än **Calculate**-metoderna i [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) och [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) klasserna. **GetFormula**-egenskapen och **SetFormula(...)**-metoderna lägger helt enkelt till formeln i en cell men beräknar inte resultatet vid körning. För att få formelresultatet, vänligen använd **Calculate**-metoderna.

{{% /alert %}}

## **Direkt beräkning av formel**

Aspose.Cells har en inbyggd formelberäkningsmotor. Förutom att beräkna formler som importerats från en designfil kan Aspose.Cells också beräkna formelresultat direkt.

Ibland måste du beräkna formelresultat direkt utan att lägga till dem i ett kalkylblad. Värdena för cellerna som används i formeln finns redan i ett kalkylblad, och allt du behöver är att hitta resultatet av dessa värden baserat på någon Microsoft Excel-formel utan att lägga till formeln i ett kalkylblad.

Du kan använda Aspose.Cells formelberäknings-API:er för {0} till {1} för att {2} resultaten av sådana formler utan att lägga till dem i kalkylbladet:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
Ovanstående kod ger följande utmatning:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Hur man räknar ut formler upprepade gånger**

När det finns många formler i arbetsboken och användaren behöver beräkna dem upprepade gånger med att endast modifiera en liten del av dem kan det vara hjälpsamt för prestandan att aktivera formelberäkningskedjan: [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}
### **Viktigt att veta**

{{% alert color="primary" %}}

Som standard är beräkningskedjan inaktiverad. Eftersom skapandet av kedjan också kräver extra tid kan den första gången du beräknar formler ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) ta mer CPU-tid och minnesutrymme jämfört med att beräkna formler utan kedja. Om användaren inte behöver beräkna formler upprepade gånger bör det rekommenderade beteendet vara att beräkna formeln direkt utan att skapa en beräkningskedja.

{{% /alert %}}

## **Avancerade ämnen**
- [Lägg till celler i Microsoft Excel Formelövervakningsfönstret](/cells/sv/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Beräkning av IFNA-funktionen med Aspose.Cells](/cells/sv/cpp/calculating-ifna-function-using-aspose-cells/)
- [Beräkning av Array Formula av Data Tables](/cells/sv/cpp/calculation-of-array-formula-of-data-tables/)
- [Beräkning av Excel 2016 MINIFS och MAXIFS funktioner](/cells/sv/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Minska tiden för beräkning av Cell.Calculate-metoden](/cells/sv/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Direkt beräkning av anpassad funktion utan att skriva den i en kalkylblad](/cells/sv/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implementera anpassad beräkningsmotor för att förlänga standardberäkningsmotorn för Aspose.Cells](/cells/sv/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Returnera en rad med värden med hjälp av AbstractCalculationEngine](/cells/sv/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Inställning av Formelberäkningsläge för Arbetsbok](/cells/sv/cpp/setting-formula-calculation-mode-of-workbook/)
- [Användning av FormulaText-funktionen i Aspose.Cells](/cells/sv/cpp/using-formulatext-function-in-aspose-cells/)
