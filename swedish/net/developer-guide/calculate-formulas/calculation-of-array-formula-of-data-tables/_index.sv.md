---
title: Beräkning av Data Table Arrayformel
description: Hur man använder Aspose.Cells biblioteket för att beräkna arrayformler för en datatabell i Microsoft Excel. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda metoden som tillhandahålls av Aspose.Cells för att beräkna arrayformeln för datatabellen och få resultatet. Slutligen sparar vi den ändrade Excel filen på disk.
keywords: Aspose.Cells, Excel, datapaket, arrayformler, beräkningar
type: docs
weight: 70
url: /sv/net/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Du kan skapa en datatabell i Microsoft Excel genom att använda Data > Vad om-analys > Datatabell.... Aspose.Cells tillåter nu beräkning av arrayformeln för en datatabell. Använd [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) som normalt för att beräkna vilken typ av formler som helst.

{{% /alert %}}

I följande kodexempel använde vi [källa excel-fil](5115535.xlsx). Om du ändrar värdet i cell B1 till 100 blir värdena i datatabellen som är fyllda med gult färgad till 120, vilket visas i följande bilder. Detta kodexempel genererar [utdata PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Följande kod användes för att generera [utdata PDF](5115538.pdf) från [källa excel-fil](5115535.xlsx). Läs kommentarerna för mer information.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
