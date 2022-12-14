---
title: Anpassa alla kalkylbladskolumner på en enda PDF-sida
type: docs
weight: 70
url: /sv/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 Ibland vill du skapa en PDF-fil som passar alla ett kalkylblads kolumner på en enda sida. De[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) egenskapen tillhandahåller denna funktion på ett mycket lättanvänt sätt. Komplexa beräkningar som höjden och bredden på den utgående PDF-sidan hanteras internt och baseras på data i kalkylbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på en enda PDF-sida**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)ser till att alla kolumner i ett kalkylblad renderas till en enda PDF-sida, även om rader kan utökas till flera sidor beroende på data i kalkylbladet.

{{% alert color="primary" %}}

När ett visst kalkylblad har många kolumner kan den renderade PDF-filen visa innehållet i en mycket liten storlek. Det är fortfarande läsbart när det skalas upp i ett visningsprogram som Acrobat Reader.

{{% /alert %}}

 Exempelkoden nedan visar hur du använder[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)egenskap för att återge ett stort kalkylblad med 100 kolumner.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

 Om ditt kalkylblad innehåller formler är det bäst att ringa[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) -metoden precis innan kalkylarket renderas till PDF-format. Om du gör det säkerställer du att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}
