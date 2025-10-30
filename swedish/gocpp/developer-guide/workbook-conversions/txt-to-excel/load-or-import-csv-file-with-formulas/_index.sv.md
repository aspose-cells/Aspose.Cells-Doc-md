---
title: Ladda eller importera CSV fil med formler med C++
linktitle: Ladda eller importera CSV fil med formler
type: docs
weight: 350
url: /sv/go-cpp/load-or-import-csv-file-with-formulas/
description: Ladda eller importera en CSV fil som innehåller formeln med Aspose.Cells med Golang via C++.
---

{{% alert color="primary" %}} 

 CSV-filer innehåller mestadels textuell data och inkluderar vanligtvis inte några formler. Men det finns fall då CSV-filer kan innehålla formler. Sådana CSV-filer bör laddas genom att ställa in [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) till **true**. När denna egenskap är inställd på **true** behandlar Aspose.Cells inte formler som enkel text. De behandlas som formler, och Aspose.Cells formelberäkningsmotor bearbetar dem som vanligt.

{{% /alert %}} 

Följande kod visar hur du kan ladda och importera en CSV-fil med formler. Du kan använda vilken CSV-fil som helst. För illustrativa syften använder vi [en enkel CSV-fil](5115034.csv) som innehåller denna data. Som du ser, innehåller den en formel.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
Koden laddar först CSV-filen, importer den sedan igen till cell D4. Slutligen sparar den arbetsbokobjektet i XLSX-format. [utdata XLSX-fil](5115052.xlsx) ser ut så här. Som du ser, innehåller cell C3 och F4 formler och deras resultat är 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
