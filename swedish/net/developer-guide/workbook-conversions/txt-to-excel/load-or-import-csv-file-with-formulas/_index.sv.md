---
title: Ladda eller importera CSV-fil med formler
type: docs
weight: 350
url: /sv/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 CSV-filer innehåller mestadels textdata och de innehåller inga formler. Men ibland händer det att CSV-filer också innehåller formler. Sådana CSV-filer bör laddas genom att ställa in[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) som**Sann** . När den här egenskapen kommer att ställas in**Sann**, Aspose.Cells kommer inte att behandla formeln som enkel text. De kommer att behandlas som formel och Aspose.Cells formelberäkningsmotor kommer att bearbeta dem som vanligt.

{{% /alert %}} 

 Följande kod illustrerar hur du kan ladda och importera en CSV-fil med formler. Du kan använda vilken CSV-fil som helst. I illustrationssyfte använder vi[enkel csv-fil](5115034.csv) som innehåller dessa uppgifter. Som du ser innehåller den en formel.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



 Koden laddar först CSV-filen och importerar den sedan igen i cell D4. Slutligen sparar den arbetsboksobjektet i XSLX-format. De[utgång XLSX-fil](5115052.xlsx) ser ut så här. Som du ser innehåller cell C3 och F4 formeln och dess resultat 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
|:- |

