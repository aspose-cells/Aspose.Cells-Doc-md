---
title: Beräkning av matrisformel för datatabeller
type: docs
weight: 70
url: /sv/net/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}}

 Du kan skapa datatabell i Microsoft Excel med Data > Vad-om-analys > Datatabell.... Aspose.Cells låter dig nu beräkna matrisformeln för en datatabell. Snälla använd[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) som normalt för att beräkna alla typer av formler.

{{% /alert %}}

I följande exempelkod använde vi[källkod excel-fil](5115535.xlsx) . Om du ändrar värdet på cell B1 till 100 kommer värdena i datatabellen som är fyllda med gul färg att bli 120 som visas i följande bilder. Exempelkoden genererar[mata ut PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

 Här är exempelkoden som används för att generera[mata ut PDF](5115538.pdf) från[källkod excel-fil](5115535.xlsx). Läs kommentarerna för mer information.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
