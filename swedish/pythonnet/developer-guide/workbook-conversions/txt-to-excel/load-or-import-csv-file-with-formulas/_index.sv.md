---
title: Ladda eller importera CSV fil med formler
type: docs
weight: 350
url: /sv/python-net/load-or-import-csv-file-with-formulas/
description: Ladda eller importera CSV fil med formler med Aspose.Cells för Python via .NET API.
keywords: Python Ladda eller importera CSV fil med formler, Konvertera CSV med formler till Excel i Python via NET, Python konvertera CSV med formler till xlsx, Ladda CSV med formler till Excelfil.
---

{{% alert color="primary" %}} 

CSV-filer innehåller främst textdata och de innehåller inte några formler. Men ibland händer det att CSV-filer också innehåller formler. Sådana CSV-filer bör laddas genom att ställa in [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) som **true**. När denna egenskap är inställd på **true**, kommer inte Aspose.Cells att behandla formeln som enkel text. De kommer att behandlas som formel och Aspose.Cells formelberäkning kommer att behandla dem som vanligt.

{{% /alert %}} 

Den följande koden visar hur du kan ladda och importera en CSV-fil med formler. Du kan använda vilken som helst CSV-fil. För illustreringsändamål använder vi [enkel csv-fil](5115034.csv) som innehåller denna data. Som du ser innehåller den en formel.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



Koden laddar först CSV-filen, sedan importerar den igen vid cell D4. Slutligen sparar den arbetsboksobjektet i XSLX-format. [Utgående XLSX-filen](5115052.xlsx) ser ut så här. Som du ser innehåller cell C3 och F4 formeln och dess resultat 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

