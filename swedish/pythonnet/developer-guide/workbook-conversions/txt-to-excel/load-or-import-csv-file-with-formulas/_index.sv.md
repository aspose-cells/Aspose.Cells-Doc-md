---
title: Ladda eller importera CSV-fil med formler
type: docs
weight: 350
url: /sv/python-net/load-or-import-csv-file-with-formulas/
description: Ladda eller importera CSV-fil med formler genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 CSV-filen innehåller mestadels textdata och de innehåller inga formler. Men ibland händer det att CSV-filer också innehåller formler. Sådana CSV-filer bör laddas genom att ställa in[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) som *sant**. När den här egenskapen har ställts in på *true**, kommer Aspose.Cells inte att behandla formeln som enkel text. De kommer att behandlas som formel och Aspose.Cells formelberäkningsmotor kommer att bearbeta dem som vanligt.

{{% /alert %}} 

 Följande kod illustrerar hur du kan ladda och importera en CSV-fil med formler. Du kan använda vilken CSV-fil som helst. I illustrationssyfte använder vi[enkel csv-fil](5115034.csv)som innehåller dessa uppgifter. Som du ser innehåller den en formel.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



 Koden laddar först filen CSV och importerar den sedan igen i cell D4. Slutligen sparar den arbetsboksobjektet i XSLX-format. De[utgång XLSX fil](5115052.xlsx) ser ut så här. Som du ser innehåller cell C3 och F4 formeln och dess resultat 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

