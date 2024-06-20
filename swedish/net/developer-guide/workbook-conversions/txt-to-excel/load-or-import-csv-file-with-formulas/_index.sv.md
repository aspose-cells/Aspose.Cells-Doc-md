---
title: Ladda eller importera CSV fil med formler
type: docs
weight: 350
url: /sv/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV-filer innehåller huvudsakligen textdata och de innehåller inga formler. Ibland händer det dock att CSV-filer också innehåller formler. Sådana CSV-filer bör laddas genom att ange [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) som **true**. När denna egenskap sätts till **true** kommer inte Aspose.Cells att behandla formel som enkel text. De kommer att behandlas som formel och Aspose.Cells formelberäkning kommer att behandla dem som vanligt.

{{% /alert %}} 

Den följande koden visar hur du kan ladda och importera en CSV-fil med formler. Du kan använda vilken som helst CSV-fil. För illustreringsändamål använder vi [enkel csv-fil](5115034.csv) som innehåller denna data. Som du ser innehåller den en formel.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



Koden laddar först CSV-filen, sedan importerar den igen vid cell D4. Slutligen sparar den arbetsboksobjektet i XSLX-format. [Utgående XLSX-filen](5115052.xlsx) ser ut så här. Som du ser innehåller cell C3 och F4 formeln och dess resultat 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

