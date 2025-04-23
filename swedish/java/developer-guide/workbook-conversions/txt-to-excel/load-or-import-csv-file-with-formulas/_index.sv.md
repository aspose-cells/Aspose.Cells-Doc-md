---
title: Ladda eller importera CSV fil med formler
type: docs
weight: 500
url: /sv/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV-filen innehåller mestadels textdata och de innehåller inte några formler. Ibland händer det att CSV-filer också innehåller formler. Sådana CSV-filer bör laddas genom att ställa in [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) till **true**. När den här egenskapen har ställts in till **true**, kommer Aspose.Cells inte behandla formel som enkel text. De kommer att behandlas som en formel och Aspose.Cells formelberäkningsmotor kommer att hantera dem som vanligt.

{{% /alert %}} 
## **Läs in eller importera CSV-fil med formler**
Följande kod illustrerar hur du kan ladda och importera en CSV-fil med formler. Du kan använda vilken CSV-fil som helst. För illustrerande syfte använder vi [enkel csv-fil](5472505.csv) som innehåller denna data. Som du ser innehåller den en formel.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

Koden lastar först in CSV-filen, importerar den sedan igen till cell D4. Slutligen sparar den arbetsboksobjektet i XSLX-formatet. [Utdata XLSX-filen](5472503.xlsx) ser ut så här. Som du ser innehåller cell C3 och F4 en formel och dess resultat 800.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
{{< app/cells/assistant language="java" >}}
