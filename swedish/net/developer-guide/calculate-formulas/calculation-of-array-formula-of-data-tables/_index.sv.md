---
title: Beräkning av matrisformel för datatabeller
description: Hur man använder Aspose.Cells-biblioteket för att beräkna matrisformler för en datatabell i Microsoft Excel. Genom att ladda en befintlig Excel-fil eller skapa en ny Excel-fil kan vi använda metoden som tillhandahålls av Aspose.Cells för att beräkna matrisformeln för datatabellen och få resultatet. Slutligen sparar vi den modifierade Excel-filen på disken.
keywords: Aspose.Cells, Excel, data tables, array formulas, calculations
type: docs
weight: 70
url: /sv/net/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}}

Du kan skapa datatabell i Microsoft Excel med Data > Vad-om-analys > Datatabell.... Aspose.Cells låter dig nu beräkna matrisformeln för en datatabell. Snälla använd[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) som normalt för att beräkna alla typer av formler.

{{% /alert %}}

I följande exempelkod använde vi[source excel-fil](5115535.xlsx) . Om du ändrar värdet på cell B1 till 100 kommer värdena i datatabellen som är fyllda med gul färg att bli 120 som visas i följande bilder. Exempelkoden genererar[utgång PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

 Här är exempelkoden som används för att generera[utgång PDF](5115538.pdf) från[source excel-fil](5115535.xlsx). Läs kommentarerna för mer information.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
