---
title: Använder FormulaText-funktionen i Aspose.Cells
description: Den här artikeln introducerar hur du använder FormulaText-funktionen i Aspose.Cells-biblioteket för att bearbeta formler i Microsoft Excel. Genom att ladda en befintlig Excel-fil eller skapa en ny Excel-fil kan vi använda metoden som tillhandahålls av Aspose.Cells för att få och ställa in formeltexten för cellen och få resultatet. Slutligen sparar vi den modifierade Excel-filen på disken.
keywords: Aspose.Cells, Excel, FormulaText functions
type: docs
weight: 60
url: /sv/net/using-formulatext-function-in-aspose-cells/
---
{{% alert color="primary" %}} 

FormulaText är en Excel 2013 och senare funktion. Det stöds inte av tidigare versioner som Excel 2010 eller 2007 etc. Som namnet antyder skriver det ut texten i formeln som finns i en given cell. Den här artikeln visar hur du använder den här funktionen med Aspose.Cells.

{{% /alert %}} 

Följande exempelkod visar användningen av FormulaText med Aspose.Cells. Koden skriver först en formel i cell A1 och skriver sedan ut formelns text med FormulaText i cell A2.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
##  **Konsolutgång**
Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

 =SUM(B1:B10)

{{< /highlight >}}
